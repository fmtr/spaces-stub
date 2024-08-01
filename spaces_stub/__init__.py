import sys
from os import getenv, path

import importlib
import logging
import subprocess
from pathlib import Path


def run():
    FMTR_LOG_LEVEL = getenv('FMTR_LOG_LEVEL', 'INFO')
    logging.getLogger().setLevel(FMTR_LOG_LEVEL)

    home_directory = Path(path.expanduser("~")).absolute()



    MODULE_NAME = getenv('PACKAGE_NAME')
    if not MODULE_NAME:
        raise KeyError('No MODULE_NAME set.')

    PIP_INDEX_URL = getenv('PIP_INDEX_URL')
    if not PIP_INDEX_URL:
        raise KeyError('No PIP_INDEX_URL set.')

    PIP_USERNAME = getenv('PIP_USERNAME')
    if not PIP_USERNAME:
        raise KeyError('No PIP_USERNAME set.')

    PIP_PASSWORD = getenv('PIP_PASSWORD')
    if not PIP_PASSWORD:
        raise KeyError('No PIP_PASSWORD set.')

    lines_nrc = [
        f'machine {PIP_INDEX_URL}',
        f'login {PIP_USERNAME}',
        f'password {PIP_PASSWORD}'
    ]

    (home_directory / '.netrc').write_text('\n'.join(lines_nrc))

    print(f'Starting {MODULE_NAME}...')

    subprocess.run(
        [sys.executable, '-m', 'pip', 'install', MODULE_NAME, '--no-input', f'--index-url http://{PIP_INDEX_URL}'])

    # logging.debug(f"Pip Output:\n{stdout}")
    # logging.debug(f"Pip Error:\n{stderr}")
    # logging.debug(f"Pip Freeze:\n{Path('/tmp/freeze.txt').read_text()}")

    interface = importlib.import_module(f'{MODULE_NAME}.interface')
    interface.run()
