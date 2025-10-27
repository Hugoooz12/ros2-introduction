from setuptools import find_packages, setup

package_name = 'patate'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='student',
    maintainer_email='hugobastien12@gmail.com',
    description='A patate Package',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'talker = patate.publisher_member_function:main',
            'listener = patate.subscriber_member_function:main',
            'mytho = patate.mytho_subcriber_member_function:main',
            'service = patate.service_member_function:main',
            'client = patate.client_member_function:main',
        ],
    },
)
