# Flask + Django Web App with Docker Compose

## About the Project

This project contains a simple Flask app and a Django app, containerized with Docker Compose.

## Part 1: Flask Application

A simple Flask web application with the following features:

- **Homepage** (`/`) displays a `"Hello, World!"` message.
- **User Form Route** (`/form`) accepts a user's **name** and **age**, then returns a personalized greeting. 
- Implements **basic error handling** for invalid inputs. 

---

## Part 2: Django Application

A basic Django project with:

- **Homepage** that displays a list of items (e.g., books, tasks, or products) from a database.
- **Admin panel** for adding and modifying items. 
- A **form on the homepage** to add new items to the list. 

---

## Part 3: Docker Compose Setup (30 Marks)

Containerization using Docker:

- Separate `Dockerfile` for both **Flask** and **Django** applications. 
- A `docker-compose.yml` file to manage both services. 
- Applications are accessible on different local **ports**:
  - Flask: `http://localhost:5000`
  - Django: `http://localhost:8000` 

---

## How to Run

### Step 1: Clone the repo
```bash
git clone https://github.com/SRCEM-AIM-Class-A/A27_AtharvaKulkarni_FinalAssignment.git
```

### Step 2: Start the containers
```bash
docker-compose up --build
```
### Step 3: Open in browser
```bash
- Flask App: http://localhost:5000

- Django App: http://localhost:8000
```
### Requirements
- Python 3.8+

- Docker & Docker Compose

- pip (Python package installer)