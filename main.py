from email.policy import default

from fastapi import FastAPI, Body,  HTTPException, Path, Query
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class Course(BaseModel):
    id: int
    title: str
    trainer: str
    description: str
    duration_weeks: int

COURSES = [
    Course(
        id=1,
        title='Mathematics',
        trainer='John Smith',
        description='Fundamentals of math',
        duration_weeks=4
    ),
    Course(
        id=2,
        title='Computer Science',
        trainer='Marry Poppins',
        description='Fundamentals of computer science',
        duration_weeks=8
    ),
    Course(
        id=3,
        title='Java Backend',
        trainer='Martin Morgan',
        description='OOP, variables and loops',
        duration_weeks=3
    ),
    Course(
        id=4,
        title='Python',
        trainer='Andrew Louder',
        description='Python & Python Pro',
        duration_weeks=5
    ),
    Course(
        id=5,
        title='Databases',
        trainer='Mark Michigan',
        description='Lorem ipsum description',
        duration_weeks=5
    )
]

class CourseRequest(BaseModel):
    id: int
    title: str
    trainer: str
    description: str
    duration_weeks: int

@app.get("/")
def greet():
    hour = datetime.now().hour

    if 5 <= hour < 12:
        message = "Bună dimineața!"
    elif 12 <= hour < 18:
        message = "Bună ziua!"
    elif 18 <= hour < 23:
        message = "Bună seara!"
    else:
        message = "Noapte bună!"

    return {"message": message}


@app.get("/")
def home():
    return {"message": "BUNA ZIUA!"}

@app.get('/courses')
async def read_all_courses():
    return COURSES

@app.get('/courses/{course_id}')
def get_course_by_id(course_id: int = Path(..., ge=1)):
    for course in COURSES:
        if course.id == course_id:
            return course
    raise HTTPException(status_code=404, detail="Course not found")

