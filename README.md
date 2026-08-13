# Vehicle Dynamics

Python backend for passenger vehicle dynamics with DEM soft-soil (loose ground) support. Frontend deferred.

## Run

```powershell
python main.py
```

## Layout

| Path | Purpose |
|------|---------|
| `main.py` | Entry point |
| `src/` | Backend packages |
| `tests/` | Pytest suite |
| `documentation/` | IEEE LaTeX (SRS, SDD, testing, milestones) |
| `out/` | Simulation outputs (from M3+) |

## Milestones

Each milestone mirrors Phase 1: **structure → docs → runnable `main.py`**.

| ID | Name | Focus | Status |
|----|------|-------|--------|
| M1 | Scaffold | Dirs, IEEE docs, `main.py` stub, CI | Done |
| M2 | Backend package | `src/vehicle_dynamics`, config, wired entry | Planned |
| M3 | Vehicle core | Dual-track model, scenario, CSV export | Planned |
| M4 | DEM soil (small N) | CPU particle step, unit tests | Planned |
| M5 | Coupling | Wheel–soil forces, integration tests | Planned |
| M6 | GPU scale path | Warp (default), large-N mode | Planned |
| M7 | Front end | UI / visualization | Deferred |

Full write-up: [documentation/milestones.tex](documentation/milestones.tex).

## CI

GitHub Actions under `.github/workflows/`:

| Workflow | Role |
|----------|------|
| `python-package-conda.yml` | Conda env, flake8, `main.py` smoke, pytest |
| `pylint.yml` | Pylint on tracked `*.py` |
| `codeql.yml` | CodeQL for Python + Actions |
| `sonarqube.yml` | SonarQube (`SONAR_TOKEN`, `SONAR_HOST_URL` secrets) |

Supporting files: `environment.yml`, `requirements.txt`, `sonar-project.properties`.

## Documentation

IEEE conference format (`IEEEtran`). Requires a TeX install with the IEEE class (TeX Live / MiKTeX).

- [documentation/srs.tex](documentation/srs.tex) — Software Requirements Specification
- [documentation/sdd.tex](documentation/sdd.tex) — Software Design Description
- [documentation/testing.tex](documentation/testing.tex) — Testing document
- [documentation/milestones.tex](documentation/milestones.tex) — Milestone plan

```powershell
cd documentation
pdflatex srs.tex
pdflatex sdd.tex
pdflatex testing.tex
pdflatex milestones.tex
```
