#!/usr/bin/env python
from setuptools import (
    setup,
    find_packages,
)


extras_require = {
    'test': [
        'cryptography',
        'pytest-cov',
        'pytest-django',
        'pytest-xdist',
        'pytest',
        'tox',
    ],
    'lint': [
        'flake8',
        'pep8',
        'isort',
    ],
    'doc': [
        'Sphinx>=1.6.5,<2',
        'sphinx_rtd_theme>=0.1.9',
    ],
    'dev': [
        'bumpversion>=0.5.3,<1',
        'pytest-watch',
        'wheel',
        'twine',
        'ipython',
    ],
    'python-jose': [
        'python-jose==3.0.0',
    ],
}

extras_require['dev'] = (
    extras_require['dev'] +  # noqa: W504
    extras_require['test'] +  # noqa: W504
    extras_require['lint'] +  # noqa: W504
    extras_require['doc'] +  # noqa: W504
    extras_require['python-jose']
)


setup(
    name='djangorestframework_simplejwt_captcha',
    version='1.1.6',
    url='https://github.com/SimpleJWT/django-rest-framework-simplejwt',
    license='MIT',
    description='A minimal JSON Web Token',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    author='juks9527',
    author_email='15507925675xiao@gmail.com',
    install_requires=[
        'Django',
        'captcha',
        'djangorestframework',
        'pyjwt',
        'Pillow'

    ],

    long_description_content_type='text/markdown',
    python_requires='>=3.6',
    extras_require=extras_require,
    packages=find_packages(exclude=['tests', 'tests.*', 'licenses', 'requirements']),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
