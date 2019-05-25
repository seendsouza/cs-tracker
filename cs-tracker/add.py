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
@click.option('-v', '--verbose', is_flag = True, help='print a message for each created training type')
@click.option('-d', '--directory', help='specify the session to put the training type in')
@click.argument('filename')
def training(verbose, directory, filename):
    """Creates a new training type

    Creates a new training type by creating a file in cs-tracker/<session_name> with the user's custom training type name

    Args:
        directory: name of the directory the session will be stored in
        filename: name of the directory the session will be stored in
        verbose: boolean of whether to print Directory Created

    Raises:
        FileNotFoundError: 
        FileExistsError: Cannot create a file when that file already exists
        PermissionError:
    """
    try:
        path = os.path.relpath('../data/{}'.format(directory))
        if os.path.exists(path) == False or directory == "":
            raise FileNotFoundError
        path += "\{}.csv".format(filename)
        abs_path = os.path.abspath(path)
        if os.path.exists(abs_path):
            raise FileExistsError
        open(abs_path,'w').close()
        if verbose:
            click.echo("Training Type " + filename + " Created")

    except FileNotFoundError:
        click.echo("Cannot create a training type when the session does not exist: '{}'".format(directory))
    except FileExistsError:
        click.echo("Cannot create a training type when that training type already exists: '{}'".format(filename))
    except PermissionError:
        click.echo("Cannot create a training type when the user does not have the permsissions to write to the directory: '{}'".format(abs_path))

@add.command(help='create a new session to store training data')
@click.option('-v', '--verbose', is_flag = True, help='print a message for each created directory')
@click.argument('directory')
def session(verbose, directory):
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