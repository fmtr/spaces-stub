import sys
from os import getenv

import importlib
import logging
import subprocess


def install_package(name):
    try:
        result = subprocess.run([sys.executable, '-m', 'pip', 'install', name, '--no-input'])
        stdout = result.stdout.decode('utf-8')
        stderr = result.stderr.decode('utf-8')
        return stdout, stderr
    except Exception as e:
        return None, str(e)


def run():
    FMTR_LOG_LEVEL = getenv('FMTR_LOG_LEVEL', 'INFO')
    logging.getLogger().setLevel(FMTR_LOG_LEVEL)

    MODULE_NAME = getenv('PACKAGE_NAME')
    if not MODULE_NAME:
        raise KeyError('No MODULE_NAME set.')

    print(f'Starting {MODULE_NAME}...')

    subprocess.run([sys.executable, '-m', 'pip', 'install', MODULE_NAME])

    # logging.debug(f"Pip Output:\n{stdout}")
    # logging.debug(f"Pip Error:\n{stderr}")
    # logging.debug(f"Pip Freeze:\n{Path('/tmp/freeze.txt').read_text()}")

    interface = importlib.import_module(f'{MODULE_NAME}.interface')
    interface.run()
