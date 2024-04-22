import os
from setuptools import find_packages, setup

raise ValueError(f'{os.environ=}')

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
    extras_require={},
)
