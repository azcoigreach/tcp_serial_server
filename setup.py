from setuptools import setup

setup(
    author="azcoigreach",
    author_email="azcoigreach@gmail.com",
    name = 'TCP Socket Serial Server',
    version = '0.0.1',
    packages=['tcp_serial_server'],
    include_package_data=True,
    install_requires = [
        'click',
        'coloredlogs',
    ],
    entry_points = '''
        [console_scripts]
        tcp_serial_server=tcp_serial_server.cli:cli
    ''',
)