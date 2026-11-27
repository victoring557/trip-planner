# Trip planner

Group project for Software Management & Development (IE), Team 5.

A small app for planning trips with friends: the trip, who is going, bookings, shared costs, the budget, and who owes whom at the end.

## Team

| Member | GitHub |
|---|---|
| Carlos Parra | @carlosparra11 |
| Jorge Plaza | @jorgeplza |
| Victor Boros | @victoring557 |
| Diana Rubaga | @dianarubaga |
| Paul George | @paulhgeorge-creator |
| Matt Lassiouve | @mattlasscode |

## Modules

| Module | Owner | Main entity | Calculated result |
|---|---|---|---|
| Trips | Carlos Parra | trip (name, dates, destination) | trip length in days |
| Travellers | Jorge Plaza | traveller on a trip | cost per person |
| Bookings | Victor Boros | booking (flight, hotel, activity, price) | total booked per trip |
| Shared costs | Diana Rubaga | expense paid by a traveller | total paid per person |
| Budget | Paul George | budget per category | amount left per category |
| Settle-up + currency | Matt Lassiouve | settlement | who owes whom, in one currency |

## Shared jobs

| Job | Owner |
|---|---|
| Continuous integration (GitHub Actions: Ruff and tests on every PR) | Victor Boros |
| Containers and configuration (Dockerfile, Docker Compose, .env.example) | Jorge Plaza |
| Cloud deployment (Azure resources, deployment and cost) | Diana Rubaga |
| Frontend shell and dashboard | Carlos Parra |
| Database (shared setup, common base, sample data) | Matt Lassiouve |
| Code review (review rules, every PR reviewed) | Matt Lassiouve |
| Documentation and board (README, architecture diagram, issues) | Paul George, together with Diana Rubaga |

## Project structure

```
trip-planner/
├── pyproject.toml            # uv project: dependencies and tools
├── src/
│   ├── main.py               # the one FastAPI app; every module's router is included here
│   ├── database.py           # shared database setup (Matt)
│   ├── trips/                # Carlos
│   ├── travellers/           # Jorge
│   ├── bookings/             # Victor
│   ├── shared_costs/         # Diana
│   ├── budget/               # Paul
│   └── settle_up/            # Matt
├── tests/<module>/           # each module's tests
├── frontend/                 # shell and dashboard (Carlos), pages/<module>/ for each module's page
├── data/                     # sample data (Matt)
├── docs/                     # architecture diagram (Paul and Diana)
└── .github/workflows/        # CI (Victor)
```

Each module folder has the same four files:

- `models.py`: the database tables
- `schemas.py`: what the API receives and returns
- `service.py`: the business logic and the calculated result
- `router.py`: the endpoints, under `/api/<module>/`

Work only in your own module folder. The routers are already included in `main.py`, so you don't need to edit it.

## Running the API

```bash
uv sync
uv run uvicorn src.main:app --reload
```

Then open http://127.0.0.1:8000/docs.

## How we work

- Every change goes through a pull request, approved by another member, merged with a merge commit.
- Tasks are GitHub issues on the project board, assigned to their owner.
- Conventions (stack, package names, API routes, money and dates) will be added here for Milestone 2.
