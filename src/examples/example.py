#!/usr/bin/env python3  # noqa: CPY001

"""Examples of using the zero-spinner with Click."""

import time

try:
    import click
except ImportError:
    print('Please install click: uv install --group test')

from yeeti.zero_spinner import spinner


@click.group()
def cli():
    """Example CLI application with spinners."""
    pass


@cli.command()
def basic():
    """Basic spinner usage."""
    spin = spinner('Loading unicorns').start()
    time.sleep(2)
    spin.succeed('Unicorns loaded!')


@cli.command()
def changing():
    """Change spinner text and color during execution."""
    spin = spinner('Loading unicorns').start()
    time.sleep(1.5)

    spin.text = 'Loading rainbows'
    spin.color = 'yellow'
    time.sleep(1.5)

    spin.text = 'Loading butterflies'
    spin.color = 'magenta'
    time.sleep(1.5)

    spin.succeed('All loaded!')


@cli.command()
def states():
    """Demonstrate different completion states."""
    # Success
    spin = spinner('Processing step 1', color='cyan').start()
    time.sleep(1.5)
    spin.succeed('Step 1 complete')

    # Warning
    spin = spinner('Processing step 2', color='yellow').start()
    time.sleep(1.5)
    spin.warn('Step 2 completed with warnings')

    # Info
    spin = spinner('Processing step 3', color='blue').start()
    time.sleep(1.5)
    spin.info('Step 3 information')

    # Failure
    spin = spinner('Processing step 4', color='red').start()
    time.sleep(1.5)
    spin.fail('Step 4 failed')

    # End
    spin = spinner('Processing step 5', color='magenta').start()
    time.sleep(1.5)
    spin.end('>.<', text='Step 5 complete')


@cli.command()
def context():
    """Use spinner as a context manager."""
    click.echo('Starting tasks...')

    with spinner('Installing dependencies', color='green'):
        time.sleep(2)

    with spinner('Building project', color='cyan'):
        time.sleep(2)

    click.echo('All tasks completed!')


@cli.command()
@click.argument('filename')
def process(filename):
    """Process a file with spinner feedback."""
    spin = spinner(f'Reading {filename}', color='cyan').start()
    time.sleep(1)

    spin.text = f'Processing {filename}'
    time.sleep(2)

    spin.text = f'Writing results for {filename}'
    time.sleep(1)

    spin.succeed(f'Successfully processed {filename}')


@cli.command()
def colors():
    """Demonstrate different spinner colors."""
    spinner_colors = [
        'black',
        'red',
        'green',
        'yellow',
        'blue',
        'magenta',
        'cyan',
        'white',
        'bright_black',
        'bright_red',
        'bright_green',
        'bright_yellow',
        'bright_blue',
        'bright_magenta',
        'bright_cyan',
        'bright_white',
        'random',
        'rainbow',
        'rainbow_bright',
        'rainbow_rgb',
        'rgb(255,0,0)',
        'rgb(0,255,0)',
        'rgb(0,0,255)',
        'rgb(255,165,0)',
    ]

    for color in spinner_colors:
        spin = spinner(f'Color: {color}', color=color).start()
        time.sleep(2)
        spin.succeed(f'{color} spinner')


@cli.command()
@click.option('--text', default='Processing', help='Text to display in the spinner.')
@click.option('--prefix-text', default='', help='Prefix text for the spinner.')
@click.option('--suffix-text', default='', help='Suffix text for the spinner.')
@click.option('--color', default='cyan', help='Color of the spinner.')
@click.option('--hide-cursor', default=True, type=bool, help='Hide the cursor during spinning.')
@click.option('--indent', default=0, type=int, help='Indentation level of the spinner.')
@click.option('--sleep', default=2.0, type=float, help='Time to sleep while spinning.')
@click.option('--final-text', default='Done!', help='Text to show upon completion.')
def custom(
    text,
    prefix_text,
    suffix_text,
    color,
    hide_cursor,
    indent,
    sleep,
    final_text,
):
    """Run a custom spinner with configurable options."""
    spin = spinner(
        text=text,
        prefix_text=prefix_text,
        suffix_text=suffix_text,
        color=color,
        hide_cursor=hide_cursor,
        indent=indent,
    ).start()
    time.sleep(sleep)
    spin.succeed(final_text)


@cli.command()
def error_handling():
    """Demonstrate error handling with context manager.

    Raises:
        Exception: For demonstration purposes
    """
    try:
        with spinner('Attempting risky operation', color='yellow'):
            time.sleep(1)
            raise Exception('Oops! Something went wrong')
    except Exception as e:
        click.echo(f'Error: {e}')


if __name__ == '__main__':
    cli()
