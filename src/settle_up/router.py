"""Settle-up + currency: API endpoints, mounted at /api/settle_up/ in main.py. Owner: Matt Lassiouve.

Milestone 2: a POST / that creates an item and a GET / that lists them,
both reading and writing the database.
"""

from fastapi import APIRouter

router = APIRouter()
