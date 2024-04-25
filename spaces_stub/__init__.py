import importlib
import logging
import pip
import subprocess
import sys
from os import getenv


def install_package(url):
    try:
        result = subprocess.run([sys.executable, '-m', 'pip', 'install', url], stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
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

    GITHUB_TOKEN = getenv('GITHUB_TOKEN')
    if not GITHUB_TOKEN:
        raise KeyError('No GITHUB_TOKEN set.')

    print(f'Starting {MODULE_NAME}...')

    URL = f'git+https://{GITHUB_TOKEN}@github.com/fmtr/{MODULE_NAME}.git'

    stdout, stderr = install_package(URL)

    GITHUB_TOKEN_MASK = '****'
    stdout = (stdout or '').replace(GITHUB_TOKEN, GITHUB_TOKEN_MASK)
    stderr = stderr.replace(GITHUB_TOKEN, GITHUB_TOKEN_MASK)

    logging.debug(f"Pip Output:\n{stdout}")
    logging.debug(f"Pip Error:\n{stderr}")

    interface = importlib.import_module(f'{MODULE_NAME}.interface')
    interface.run()
