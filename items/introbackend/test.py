from fastapi import FastAPI
from sqlmodel import Session , select
from contextlib import asynccontextmanager
from database import create_db_and_tables, engine

from models import Employee 

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)



@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/students/{id}")
async def read_students(id):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        emp = session.get(Student, id)
        return {"message": emp}
    

@app.post("/students")
async def root(Student : Student):
    with Session(engine) as session:
        session.add(Student)
        session.commit()
        session.refresh(Student)

        return {"message": 'created'}

@app.get("/courses/{id}")
async def read_courses(id):
    with Session(engine) as session:
         print(id,'--------------------------------------------------------------')
         emp = session.get(courses, id)
         return {"message": emp}


@app.post("/courses")
async def root(Course: Course):
        session.add(Course)
        session.commit()
        session.refresh(Course)
        return {"message": 'created'}

@app.get("/teachers/{id}")
async def read_teachers(id):
    with Session(engine) as session:
             print(id,'--------------------------------------------------------------')
             emp = session.get(courses, id)
             return {"message": emp}
    
@app.post("/teachers")
async def root(Teacher: Teacher):
        session.add(Teacher)
        session.commit()
        session.refresh(Teacher)
        return {"message": 'created'}