from typer.testing import CliRunner

from go_project_cli.main import app

runner = CliRunner()


def test_app():
    result = runner.invoke(app, ["create", "users"])
    assert result.exit_code == 2
