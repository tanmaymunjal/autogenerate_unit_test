import click
import os
from unit_test_generator import UnitTestGenerator

unit_test_generator = UnitTestGenerator()


@click.command()
@click.argument("inputs", nargs=-1, required=True)
def process_inputs(inputs):
    """
    CLI that processes either a list of files or a single directory.

    If a list of files is provided, each file will be processed individually.
    If a directory is provided, all files within the directory will be processed.
    """
    # Check if the first argument is a directory
    if len(inputs) == 1 and os.path.isdir(inputs[0]):
        directory = inputs[0]
        files = [os.path.join(directory, file) for file in os.listdir(directory)]
        click.echo(f"Processing directory: {directory}")
        for file in files:
            click.echo(f"Processing file: {file}")
            unit_test_generator.generate_tests(file)
    else:
        click.echo("Processing individual files:")
        for file in inputs:
            if os.path.isfile(file):
                click.echo(f"Processing file: {file}")
                unit_test_generator.generate_tests(file)
            else:
                click.echo(f"Error: {file} is not a valid file.")


if __name__ == "__main__":
    process_inputs()
