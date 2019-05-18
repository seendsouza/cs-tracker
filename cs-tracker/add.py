"""
add timestamped entries with cs count at 5 minutes for training type
add new training type
add new session of entries
"""

import click

@click.group(help='')
def add():
    pass

@add.command(help='entry')
def entry():
    pass

@add.command(help='training type')
def training():
    pass

@add.command(help='session')
def session():
    pass