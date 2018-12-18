from setuptools import setup

APP = ['app.py']
DATA_FILES = ['images']
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True,
    },
    'packages': ['rumps'],
    'iconfile':'images/app_icon.icns',
}

setup(
    app=APP,
    name='OV Door',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)