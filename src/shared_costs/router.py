"""Shared costs: API endpoints, mounted at /api/shared_costs/ in main.py. Owner: Diana Rubaga.

Milestone 2: a POST / that creates an item and a GET / that lists them,
both reading and writing the database.
"""

from fastapi import APIRouter

router = APIRouter()
