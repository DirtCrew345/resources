from sqlmodel import Field , SQLModel

class Employee(SQLModel, table=True):
    empid: int | None = Field(default=None, primary_key=True)
    name: str
    dept: str
    age: int | None = None

class department(SQLModel, table=True):
    empid: int | None = Field(default=None, primary_key=True)
    name: str
    dept: str
    age: int | None = None

class Student(SQLModel):
    empid: int | None = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    email: str
    age: int

students = []

class Course(SQLModel):
    empid: int | None = Field(default=None, primary_key=True)
    course_code: str
    course_name: str
    description: str
    units: int


courses = []


class Teacher(SQLModel):
    empid: int | None = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    email: str
    department: str


teachers = []

