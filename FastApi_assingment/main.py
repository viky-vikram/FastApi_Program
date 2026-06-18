from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Hello, FastAPI"
    }


@app.get("/greet/{name}")
def greet_user(name: str):
    return {
        "message": f"Hello, {name}",
        "name": name
    }


@app.get("/student/{student_name}/marks/{mark}")
def student_grade(student_name: str, mark: int):
    if mark >= 90:
        grade = "A"
    elif mark >= 80:
        grade = "B"
    elif mark >= 70:
        grade = "C"
    elif mark >= 60:
        grade = "D"
    else:
        grade = "E"

    return {
        "student_name": student_name,
        "mark": mark,
        "grade": grade
    }