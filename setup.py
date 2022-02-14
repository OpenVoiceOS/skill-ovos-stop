#!/usr/bin/env python3
from setuptools import setup

# NOTE: if you want compatibility with mycroft-core you CAN NOT move __init__.py
# skills installed from source are git cloned and depend on a rigid structure

# skill_id=package_name:SkillClass
PLUGIN_ENTRY_POINT = 'mycroft-stop.mycroftai=ovos_plugin_skill_stop:StopSkill'
# in this case the skill_id is defined to purposefully replace the mycroft version of the skill,
# or rather to be replaced by it in case it is present. all skill directories take precedence over plugin skills

setup(
    # this is the package name that goes on pip
    name='ovos-plugin-skill-stop',
    version='0.0.1',  # don't forget to follow proper versioning and increment on each release!
    description='OVOS stop skill plugin',
    url='https://github.com/OpenVoiceOS/skill-ovos-stop',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',

    # empty str define the package as the root
    # note the usage of _ instead of - for the imports
    package_dir={"ovos_plugin_skill_stop": ""},
    packages=['ovos_plugin_skill_stop'],
    package_data={'ovos_plugin_skill_stop': ['locale/*', 'vocab/*', "dialog/*"]},
    include_package_data=True,
    keywords='ovos mycroft skill plugin',
    entry_points={'ovos.plugin.skill': PLUGIN_ENTRY_POINT}
)
