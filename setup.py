#!/usr/bin/env python3
from setuptools import setup
import os


BASEDIR = os.path.abspath(os.path.dirname(__file__))


def get_version():
    """ Find the version of the package"""
    version = None
    version_file = os.path.join(BASEDIR, 'version.py')
    major, minor, build, alpha = (None, None, None, None)
    with open(version_file) as f:
        for line in f:
            if 'VERSION_MAJOR' in line:
                major = line.split('=')[1].strip()
            elif 'VERSION_MINOR' in line:
                minor = line.split('=')[1].strip()
            elif 'VERSION_BUILD' in line:
                build = line.split('=')[1].strip()
            elif 'VERSION_ALPHA' in line:
                alpha = line.split('=')[1].strip()

            if ((major and minor and build and alpha) or
                    '# END_VERSION_BLOCK' in line):
                break
    version = f"{major}.{minor}.{build}"
    if alpha and int(alpha) > 0:
        version += f"a{alpha}"
    return version


def required(requirements_file):
    """ Read requirements file and remove comments and empty lines. """
    with open(os.path.join(BASEDIR, requirements_file), 'r') as f:
        requirements = f.read().splitlines()
        if 'MYCROFT_LOOSE_REQUIREMENTS' in os.environ:
            print('USING LOOSE REQUIREMENTS!')
            requirements = [r.replace('==', '>=').replace('~=', '>=') for r in requirements]
        return [pkg for pkg in requirements
                if pkg.strip() and not pkg.startswith("#")]

# NOTE: if you want compatibility with mycroft-core you CAN NOT move __init__.py
# skills installed from source are git cloned and depend on a rigid structure

# skill_id=package_name:SkillClass
PLUGIN_ENTRY_POINT = 'ovos-skill-stop.OpenVoiceOS=ovos_skill_stop:StopSkill'

setup(
    # this is the package name that goes on pip
    name='ovos-skill-stop',
    version=get_version(),
    description='OVOS stop skill plugin',
    url='https://github.com/OpenVoiceOS/skill-ovos-stop',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',

    # empty str define the package as the root
    # note the usage of _ instead of - for the imports
    package_dir={"ovos_skill_stop": ""},
    packages=['ovos_skill_stop'],
    package_data={'ovos_skill_stop': ['locale/*', 'vocab/*', "dialog/*"]},
    include_package_data=True,
    keywords='ovos mycroft skill plugin',
    entry_points={'ovos.plugin.skill': PLUGIN_ENTRY_POINT}
)
