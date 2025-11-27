# Copyright (C) 2025 Yeeti

"""Example of cli entrypoint."""

import click


@click.group()
def cli():
    """Yeeti cli group."""
    pass


@cli.command()
@click.argument('name')
def hello(name):
    """Command that outputs Hello followed by the given name.

    Args:
       name (str): The name to greet.
    """
    click.echo(f'Hello {name}!')


if __name__ == '__main__':
    cli()
