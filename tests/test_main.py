from typer.testing import CliRunner
import shutil

from go_project_cli.main import app

runner = CliRunner()


def test_app():
    result = runner.invoke(app, ["new", "test_users"])
    assert result.exit_code == 0
    shutil.rmtree('test_users')
