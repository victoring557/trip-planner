"""Budget: API endpoints, mounted at /api/budget/ in main.py. Owner: Paul George.

Milestone 2: a POST / that creates an item and a GET / that lists them,
both reading and writing the database.
"""

from fastapi import APIRouter

router = APIRouter()
