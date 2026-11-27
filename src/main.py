"""The one FastAPI application of the team.

Every module's router is already included below, under /api/<module>.
You don't need to edit this file to add endpoints: add them in your own
src/<module>/router.py.

Start it with:  uv run uvicorn src.main:app --reload
"""

from fastapi import FastAPI

from src.trips.router import router as trips_router
from src.travellers.router import router as travellers_router
from src.bookings.router import router as bookings_router
from src.shared_costs.router import router as shared_costs_router
from src.budget.router import router as budget_router
from src.settle_up.router import router as settle_up_router

app = FastAPI(title="Trip planner")

app.include_router(trips_router, prefix="/api/trips", tags=["Trips"])
app.include_router(travellers_router, prefix="/api/travellers", tags=["Travellers"])
app.include_router(bookings_router, prefix="/api/bookings", tags=["Bookings"])
app.include_router(shared_costs_router, prefix="/api/shared_costs", tags=["Shared costs"])
app.include_router(budget_router, prefix="/api/budget", tags=["Budget"])
app.include_router(settle_up_router, prefix="/api/settle_up", tags=["Settle-up + currency"])


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
