# Flask Students CRUD API

## Features
- Flask backend
- In-memory storage (array)
- CRUD APIs for students
- Tested with Postman
- Ready for Render deployment

## Setup

```bash
pip install -r requirements.txt
python app.py
```

## API Endpoints

### Create Student
POST /students

Body:
```json
{
  "name": "John",
  "age": 20,
  "course": "CSE"
}
```

### Get All Students
GET /students

### Get Student by ID
GET /students/<id>

### Update Student
PUT /students/<id>

### Delete Student
DELETE /students/<id>

## Postman Testing
1. Open Postman
2. Use the endpoints above
3. Set Body → raw → JSON

## Deploy on Render

1. Push code to GitHub
2. Go to https://render.com
3. New → Web Service
4. Build Command:
```
pip install -r requirements.txt
```
5. Start Command:
```
python app.py
```
