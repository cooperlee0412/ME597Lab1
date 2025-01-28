# from setuptools import find_packages, setup

# package_name = 'task_1'

# setup(
#     name=package_name,
#     version='0.0.0',
#     packages=find_packages(exclude=['test']),
#     data_files=[
#         ('share/ament_index/resource_index/packages',
#             ['resource/' + package_name]),
#         ('share/' + package_name, ['package.xml']),
#     ],
#     install_requires=['setuptools'],
#     zip_safe=True,
#     maintainer='li5313',
#     maintainer_email='li5313@purdue.edu',
#     description='TODO: Package description',
#     license='TODO: License declaration',
#     tests_require=['pytest'],
#     entry_points={
#          'console_scripts': [
#         'publisher = task_1.publisher_member_function:main',
#         'subscriber = task_1.subscriber_member_function:main',
#         'basic_publisher = task_1.basic_publisher:main',
#         'timed_publisher = task_1.timed_publisher:main',
#     ],
# },
# )

from setuptools import find_packages, setup

package_name = 'task_1'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='li5313',
    maintainer_email='li5313@purdue.edu',
    description='ROS 2 package with custom publisher and subscriber',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = task_1.my_publisher:main',  
            'listener = task_1.my_subscriber:main',  
        ],
    },
)
