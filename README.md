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
| Continuous integration (GitHub Actions: Ruff and tests on every PR) | Paul George |
| Containers and configuration (Dockerfile, Docker Compose, .env.example) | Jorge Plaza |
| Cloud deployment (Azure resources, deployment and cost) | Diana Rubaga |
| Frontend shell and dashboard | Carlos Parra |
| Database (shared setup, common base, sample data) | Matt Lassiouve |
| Code review (review rules, every PR reviewed) | Matt Lassiouve |
| Documentation and board (README, architecture diagram, issues) | Victor Boros |

## How we work

- Every change goes through a pull request, approved by another member, merged with a merge commit.
- Tasks are GitHub issues on the project board, assigned to their owner.
- Conventions (stack, package names, API routes, money and dates) will be added here for Milestone 2.
