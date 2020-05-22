import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session

engine = create_engine("postgresql+psycopg2://postgres:admin@localhost:5432/dvdrental")
db=scoped_session(sessionmaker(bind=engine))

def main():
    actors =db.execute("SELECT * FROM actor ")
    print("Helosasd")
    for actor in actors:
        print(f"{actor.first_name} and {actor.last_name}")


if __name__ == "__main__":
    main()