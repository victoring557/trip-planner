"""Bookings: API endpoints, mounted at /api/bookings/ in main.py. Owner: Victor Boros.

Milestone 2: a POST / that creates an item and a GET / that lists them,
both reading and writing the database.
"""

from fastapi import APIRouter

router = APIRouter()
