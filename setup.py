from setuptools import find_packages, setup

setup(
    name='spaces_stub',
    version=f'0.0.1',
    url='https://github.com/fmtr/spaces-stub',
    license='Copyright © 2022 Frontmatter. All rights reserved.',
    author='Frontmatter',
    author_email='ed@frontmatter.ai',
    description='Stub for hosting on Spaces',
    packages=find_packages(),
    package_data={},
    install_requires=[],
    extras_require={
        'numerics': [
            'fmtr.tools[logging,profiling,parallel]',

            'dask[bag,distributed]',
            'datasets',
            'emoji-country-flag',
            'faker',
            'forex_python',
            'gradio',
            'loguru',
            'names-generator',
            'num2words',
            'openpyxl',
            'pandas',
            'pycountry',
            'sre_yield',
            'torch',
            'transformers[torch]',
            'wandb',

            'bokeh',
            'contexttimer',
            'xyzservices',
        ]
        ,

    },
)
