from staticjinja import Site
import json

class Project:
  _id = 0
  def __init__(self, path: str) -> None:
    self.id = Project._id
    Project._id += 1
    self.path = path
    with open(f'{path}/info.json') as json_file:
      data = json.load(json_file)
      self.name = data['name']
      self.description = data['description']
      self.tags = [tag.upper() for tag in data['tags']]
      self.repo = data.get('repo', None)
      self.large = data.get('large', False)

def load_projects() -> list[Project]:
  projects : list[Project] = []
  with open('projects/content.json') as json_file:
      data = json.load(json_file)
      for project in data:
        projects.append(Project(f'projects/{project}'))
  return projects


class Paper:
  _id = 0
  def __init__(self, data: dict) -> None:
    self.id = Paper._id
    Paper._id += 1
    self.title: str = data["title"]
    self.authors: str = data["authors"]
    self.conf: str = data["conf"]
    self.year: int = data["year"]
    self.pdf: str = data["pdf"]
    self.img: str = data["img"]
    
def load_papers() -> list[Paper]:
  papers : list[Paper] = []
  with open('papers.json') as json_file:
      data = json.load(json_file)
      for paper in data:
        papers.append(Paper(paper))
  return papers




if __name__ == "__main__":
  
  home_context = {
    "title": "Home",
    "selected": "Home",
    "show_header": False
  }
  project_context = {
    "title": "Personal Projects",
    "selected": "Projects",
    "projects": load_projects(),
    "show_header": True
    }
  research_context = {
    "title": "Research Activities",
    "selected": "Research",
    "papers": sorted(load_papers(), key=lambda p: p.year, reverse=True),
    "show_header": True
  }
  resume_context = {
    "title": "Education and Experience",
    "selected": "CV",
    "show_header": True
  }
  site = Site.make_site(contexts=[
    ('home.html', home_context),
    ('projects.html', project_context),
    ('research.html', research_context),
    ('resume.html', resume_context)
    ])
  
  # for development
  # site.render(use_reloader=True)

  # render once and exit
  site.render(use_reloader=False) 