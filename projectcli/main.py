import typer
import utils

app = typer.Typer()


@app.command()
def new(package_name: str):
    utils.new_package(package_name)


@app.command()
def generate(semantic: str, package_name: str):
    utils.generate_file(semantic, package_name)


if __name__ == "__main__":
    app()
