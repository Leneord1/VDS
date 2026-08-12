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
| `src/` | Backend packages (later) |
| `documentation/` | SRS, SDD, testing (LaTeX) |

## CI

GitHub Actions under `.github/workflows/`:

| Workflow | Role |
|----------|------|
| `python-package-conda.yml` | Conda env, flake8, `main.py` smoke, pytest |
| `pylint.yml` | Pylint on tracked `*.py` |
| `codeql.yml` | CodeQL for Python + Actions |
| `sonarqube.yml` | SonarQube (`SONAR_TOKEN`, `SONAR_HOST_URL` secrets) |

Supporting files: `environment.yml`, `requirements.txt`, `sonar-project.properties`.


IEEE conference format (`IEEEtran`). Requires a TeX install with the IEEE class (TeX Live / MiKTeX).

- [documentation/srs.tex](documentation/srs.tex) — Software Requirements Specification
- [documentation/sdd.tex](documentation/sdd.tex) — Software Design Description
- [documentation/testing.tex](documentation/testing.tex) — Testing document

```powershell
cd documentation
pdflatex srs.tex
pdflatex sdd.tex
pdflatex testing.tex
```
