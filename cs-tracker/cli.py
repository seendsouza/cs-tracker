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
        ctx_obj = dict()
        entry_point.main(prog_name='cs-tracker',obj=ctx_obj)
    except KeyboardInterrupt:
        click.echo('Aborted!')

@click.group()
@click.version_option(version="0.0.1")
def entry_point():
    pass

entry_point.add_command(add.add)
entry_point.add_command(graph.graph)

if __name__ == "__main__":
    main()