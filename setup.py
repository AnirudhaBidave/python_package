from setuptools import find_packages, setup

setup(
    name="azurerm",
    version="0.0.1",
    description="This package hepls you to generate metrics cost and resource usage on Microsoft Azure",
    package_dir={"": "azurerm"},
    packages=find_packages(where="azurerm"),
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    # url="https://github.com/ArjanCodes/2023-package",
    author="AnirudhaBidave",
    author_email="bidaveanirudha@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=["bson >= 0.5.10"],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2", "requests>=2.30.0"],
    },
    python_requires=">=3.10",
)