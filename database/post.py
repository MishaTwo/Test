from sqlalchemy import Column, Integer, String, Float
from base import Base

class Posts():
    __tablename__='posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False, unique=True)
    content = Column(String(100), nullable=False)

    def post(self, title, content):
        self.title = title
        self.content = content