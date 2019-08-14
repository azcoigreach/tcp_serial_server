#!/usr/bin/env python
import os
import sys
import click
import logging
import coloredlogs
import socket
import time
import pickle

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
    '''TCP Server Socket'''

    TCP_IP = '0.0.0.0'
    TCP_PORT = 42000
    BUFFER_SIZE = 1024
    FILENAME = 'server.pickle'

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    logger.info('Socket %s:%s open', TCP_IP, TCP_PORT)
    conn, addr = s.accept()
    logger.info('Connection from: %s', addr)
    while 1:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            break
        logger.info('received data: %s', data)
        if data:
            with open(FILENAME, 'wb') as f:
                pickle.dump(data, f)

        # else:
        #     pass
            
    logger.debug('Socket closed.')
    conn.close()
