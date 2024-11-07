from setuptools import find_packages, setup

package_name = 'University_Blvd'

data_files = []
data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))
data_files.append(('share/' + package_name + '/launch', ['launch/University_Blvd.py']))

data_files.append(('share/' + package_name + '/worlds', [
    'worlds/University_Blvd.wbt', 
]))
data_files.append(('share/' + package_name, ['package.xml']))
data_files.append(('share/' + package_name + '/resource', [
    'resource/University_Blvd.urdf',
    'resource/ros2control.yml',
]))

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=data_files,
    install_requires=['setuptools', 'launch'],
    zip_safe=True,
    maintainer='Mohammad Ghanatian',
    maintainer_email='mghanatian@crimson.ua.edu',
    description='Simulated environment for University Boulevard',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'launch.frontend.launch_extension': ['launch_ros = launch_ros'],    
        'console_scripts': ['University_Blvd = University_Blvd.University_Blvd:main']
    },

)
