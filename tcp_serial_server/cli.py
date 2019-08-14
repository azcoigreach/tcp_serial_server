#!/usr/bin/env python
import os
import sys
import click
import logging
import coloredlogs
import socket
import time

'''
Project: TCP Socket Serial Server
Author: azcoigreach@gmail.com
Description: TCP socket server to serialize data from TCP port and encapsulate in pickle to be read by another program.
'''

coloredlogs.install(level='DEBUG')
logger = logging.getLogger(__name__)

class Context(object):
    def __init__(self):
        self.logging_level = logger

pass_context = click.make_pass_decorator(Context, ensure=True)

@click.command()
def cli():
    pass

