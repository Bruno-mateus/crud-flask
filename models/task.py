import random


class Task:
    def __init__(self,title,description,completed=False) -> None:
        self.title=title
        self.description = description
        self.completed=completed
        
    def to_dict(self):
        return {
            "id":random.randint(1,1000),
            "title":self.title,
            "description":self.description,
            "completed":self.completed
        }