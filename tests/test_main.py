# Smoke tests for Phase 1 entry point.

from main import main


def test_main_runs(capsys):
    main()
    captured = capsys.readouterr()
    assert "Vehicle Dynamics" in captured.out
