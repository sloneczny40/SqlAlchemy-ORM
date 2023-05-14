from sqlalchemy import Integer, Column, String, create_engine
from sqlalchemy.ext import declarative
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    "mysql+pymysql://root:password@localhost:3306/company"
)
Base = declarative_base(bind=engine)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)

    def __repr__(self):
        return f"User {self.first_name}  {self.last_name}>"


Base.metadata.create_all()