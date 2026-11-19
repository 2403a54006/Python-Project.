from pathlib import Path


def test_workflow_exists():
    """The repository must contain the Python Actions workflow."""
    workflow = Path(".github/workflows/python-app.yml")
    assert workflow.is_file()


def test_workflow_uses_supported_python():
    """The workflow should pin a supported Python version."""
    workflow = Path(".github/workflows/python-app.yml").read_text()
    assert 'python-version: "3.10"' in workflow


def test_workflow_runs_pytest():
    """The CI workflow must invoke pytest."""
    workflow = Path(".github/workflows/python-app.yml").read_text()
    assert "pytest" in workflow
