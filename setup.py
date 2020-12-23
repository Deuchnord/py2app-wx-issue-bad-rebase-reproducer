#!/usr/bin/env python3

from setuptools import setup
from datetime import date

from kosmorrolib.version import VERSION


APP_DARWIN_IDENTIFIER = 'fr.deuchnord.testapp'
EXECUTABLE_NAME = 'app'
APP_NAME = 'Test App'
APP_COPYRIGHT = 'Jérôme Deuchnord © 2020 - WTF License'

APP = ['app.py']
DATA_FILES = []
OPTIONS = {
    'plist': {
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'CFBundleExecutable': EXECUTABLE_NAME,
        'CFBundleIdentifier': APP_DARWIN_IDENTIFIER,
        'CFBundleShortVersionString': VERSION,
        'NSHumanReadableCopyright': APP_COPYRIGHT
    },
    'packages': ','.join(['wx'])
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
