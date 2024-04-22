import subprocess
import sys


def install_package(url):
    try:
        # Redirect stdout and stderr to PIPE
        result = subprocess.run([sys.executable, '-m', 'pip', 'install', url], stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        # Capture stdout and stderr
        stdout = result.stdout.decode('utf-8')
        stderr = result.stderr.decode('utf-8')
        # Return the captured output
        return stdout, stderr
    except Exception as e:
        return None, str(e)


def run():
    import importlib
    from os import getenv
    import pip

    MODULE_NAME = getenv('PACKAGE_NAME')
    if not MODULE_NAME:
        raise KeyError('No MODULE_NAME set.')

    GITHUB_TOKEN = getenv('GITHUB_TOKEN')
    if not GITHUB_TOKEN:
        raise KeyError('No GITHUB_TOKEN set.')

    URL = f'git+https://{GITHUB_TOKEN}@github.com/fmtr/{MODULE_NAME}.git'

    stdout, stderr = install_package(URL)

    GITHUB_TOKEN_MASK = '<GITHUB_TOKEN>'
    stdout = stdout.replace(GITHUB_TOKEN, GITHUB_TOKEN_MASK)
    stderr = stderr.replace(GITHUB_TOKEN, GITHUB_TOKEN_MASK)
    print("Pip Output:", stdout)
    print("Pip Error:", stderr)

    interface = importlib.import_module(f'{MODULE_NAME}.interface')
    interface.run()
