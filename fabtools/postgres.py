"""
Fabric tools for managing PostgreSQL users and databases
"""
from fabric.api import *


def user_exists(name):
    """
    Check if a PostgreSQL user exists
    """
    with settings(hide('running', 'stdout', 'stderr', 'warnings'), warn_only=True):
        res = sudo('''psql -t -A -c "SELECT COUNT(*) FROM pg_user WHERE usename = '%(name)s';"''' % locals(), user='postgres')
    return (res == "1")


def create_user(name, passwd):
    """
    Create a PostgreSQL user
    """
    sudo('''psql -c "CREATE USER %(name)s WITH PASSWORD '%(passwd)s';"''' % locals(), user='postgres')


def database_exists(name):
    """
    Check if a PostgreSQL database exists
    """
    with settings(hide('running', 'stdout', 'stderr', 'warnings'), warn_only=True):
        return sudo('''psql -d %(name)s -c ""''' % locals(), user='postgres').succeeded


def create_database(name, owner):
    """
    Create a PostgreSQL database
    """
    sudo('''createdb --owner %(owner)s --template template0 --encoding=UTF8 %(name)s''' % locals(), user='postgres')
