from setuptools import setup

package_name = 'alan_py'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/alan_py']),
        ('share/alan_py', ['package.xml']),
    ],
    install_requires=['setuptools'],
    maintainer='gulsum135',
    maintainer_email='gulsum135@users.noreply.github.com',
    description='Dikdortgen alani sunucusu ve istemcisi',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'server = alan_py.server:main',
            'client = alan_py.client:main',
        ],
    },
)
