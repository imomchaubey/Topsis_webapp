from setuptools import setup, find_packages

setup(
    name="Topsis-om-102317189",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy"
    ],
    entry_points={
        'console_scripts': [
            'topsis=topsis.topsis:main'
        ]
    },
    author="om",
    description="TOPSIS Implementation",
)
