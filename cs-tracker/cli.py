"""
cs-tracker

When training for League of Legends, the ability to see one's progress is a motivating factor to improving.
This provides an easy way to input cs after training sessions
"""

import click

import add
import graph

def main():
    try:
        cli.main(prog_name='cs-tracker')
    except KeyboardInterrupt:
        click.echo('Aborted!')

@click.group()
@click.version_option(version="0.0.1")
def cli():
    pass

cli.add_command(add.add)
cli.add_command(graph.graph)

if __name__ == "__main__":
    main()