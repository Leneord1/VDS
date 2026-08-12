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

## Documentation

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
