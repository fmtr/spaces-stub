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
    pip.main(['install', URL])

    interface = importlib.import_module(f'{MODULE_NAME}.interface')
    interface.run()
