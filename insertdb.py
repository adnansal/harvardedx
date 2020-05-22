import os
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session

engine = create_engine("postgresql+psycopg2://postgres:admin@localhost:5432/dvdrental")
db=scoped_session(sessionmaker(bind=engine))

def main():
    f=open('actors.csv')
    rea=csv.reader(f)
    for fn, ln in rea: 
         actors =db.execute("INSERT INTO actor (first_name,last_name,last_update) VALUES (:first_name,:last_name,NOW())",
         {"first_name":fn,"last_name":ln})
         print(f"Inserted {fn} {ln}")
    db.commit()


if __name__ == "__main__":
    main()