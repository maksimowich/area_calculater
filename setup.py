from setuptools import setup, find_packages

setup(
    name='area_calculater',
    version="0.0.1",
    packages=find_packages(),
    extras_require={
        'dev': ['pytest'],
    },
    include_package_data=True,
    author='Alexander Maksimovich',
    python_requires=">=3.6.0",
    author_email='maximowwwich@gmail.com',
    description='Calculate area of different figures.',
)
