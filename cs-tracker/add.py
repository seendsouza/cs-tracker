"""
add timestamped entries with cs count at 5 minutes for training type
add new training type
add new session of entries
"""
import os

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

@add.command(help='create a new session to store training data')
@click.option('-v', '--verbose', is_flag = True, help='print a message for each created directory')
@click.argument('directory')
def session(directory, verbose):
    """Creates a new session

    Creates a new session by creating a folder in cs-tracker/data with the user's custom directory name

    Args:
        directory: name of the directory the session will be stored in
        verbose: boolean of whether to print Directory Created
    
    Raises:
        FileExistsError: Cannot create a file when that file already exists
    """
    try:
        path = os.path.relpath('../data/{}'.format(directory))
        os.mkdir(path)
        if verbose:
            click.echo("Directory " + directory + " Created")
    except FileExistsError:
        click.echo("Cannot create a session when that session already exists: '{}'".format(directory))