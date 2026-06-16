# HR Productivity App

A full-stack productivity tool for HR professionals to manage their weekly **availability** and **meetings**, with secure per-user authentication and full CRUD on both resources.

## Description

This app provides the functionality to allow HR users to log in, display weekly availablity, and create/track tasks with the status of "working on", "completed", or "post-poned". This helps alleviate the stress of working with various departments who often wonder about the status of their cases HR is working on, provides better tracking, and improved communications for all involved. All data is private to the logged-in user.

## Technologies Used

- **Backend:** Flask, Flask-SQLAlchemy, Flask-Migrate, Flask-JWT-Extended, Flask-Cors
- **Database:** PostgreSQL
- **Frontend:** React (Vite), React Router v6
- **Auth:** JWT (JSON Web Tokens)
- **Other:** python-dotenv for environment variables

## Setup & Run Instructions

### Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

cp .env.example .env

export FLASK_APP=app.py
flask db init
flask db migrate -m "initial tables"
flask db upgrade

python app.py
```

### Frontend

```bash
cd frontend
npm install
cp .env.example .env 
npm run dev    
```

## Core Functionality

- **Auth:** Sign up, log in, log out (JWT-based). Protected routes redirect to login if not authenticated.
- **Availability (CRUD):** Each user creates weekly availability blocks (day, start time, end time). List is paginated (`/api/availability?page=1&per_page=5`).
- **Meetings (CRUD):** Each user creates meetings with title, description, start/end time, status, and attendees. List is paginated and filterable by status (`/api/meetings?status=scheduled&page=1&per_page=5`).
- **Ownership:** Every availability block and meeting belongs to the user who created it. The API enforces that users can only read, update, or delete their own records.

## Deployment

- Backend: deploy to Render (Web Service, build command `pip install -r requirements.txt`, start command `gunicorn app:create_app()`)
- Frontend: deploy to Vercel/Netlify (set `VITE_API_URL` to the deployed backend URL)

## Pitch vs. Built Scope

My original pitch would have gathered regulations and wage data from three external APIs, along with providing Claude AI advice layer. However, because I fell behind project timelines I had to make the decision to seed the regulation data myself rather than depend on three live third-party APIs.

I had to trade reliability over breadth: the free tiers for Symmetry and DOL's APIv4 either require account approval or have undocumented rate limits, which made them a risk for a hard deadline. If one went down (or rate-limited during grading) it would make a working app look broken. A self-seeded dataset is fully under my control and demos consistently every time.

The Claude API integration from the original pitch is unchanged and still the centerpiece AI feature: it takes the seeded regulation data as context and generates plain-English HR compliance guidance, fulfilling the "AI-powered feature" requirement.

**Future Enhancements**
- Replace seeded data with live calls to DOL, Symmetry, and/or Stanford Wage Theft APIs once accounts/rate limits are sorted out
- Expand seeded regulation coverage from a handful of states to all 50