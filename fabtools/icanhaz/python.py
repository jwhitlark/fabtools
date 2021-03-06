"""
Idempotent API for managing python packages
"""
from fabtools.python import *


def package(pkg_name, virtualenv=None, use_sudo=False):
    """
    I can haz python package
    """
    if not is_installed(pkg_name):
        install(pkg_name, virtualenv, use_sudo)


def packages(pkg_list, virtualenv=None, use_sudo=False):
    """
    I can haz python packages
    """
    pkg_list = [pkg for pkg in pkg_list if not is_installed(pkg)]
    if pkg_list:
        install(pkg_list, virtualenv, use_sudo)
