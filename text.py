from azure_rest import access_token, cost_rep

tenantId='ce0576f1-a4d1-40a5-895e-39f37c308e24'
client_id='2c85eb60-87a2-4574-91c2-b6ebfc180844'
client_secret='lR.8Q~nRQ391aaI-ejUCWtMFzd563DC5PaElKapU'

token = access_token(tenantId, client_id, client_secret)

scope = 'subscriptions/7bef0f67-54c5-4b3d-b872-750dee392d65'
granularity = 'Monthly'
filter_name = 'ResourceId'
filter_value = ['/subscriptions/7bef0f67-54c5-4b3d-b872-750dee392d65/resourcegroups/tech_demo_res_group/providers/microsoft.storage/storageaccounts/anirudhastorageaccount']

print(cost_rep(token, scope, granularity, filter_name, filter_value))


###########################################################################

from setuptools import find_packages, setup

setup(
    name="azure_rest",
    version="0.0.1",
    description="This package hepls you to generate metrics cost and resource usage on Microsoft Azure",
    package_dir={"": "azure_rest"},
    packages=find_packages(where="azure_rest"),
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
    install_requires=["bson >= 0.5.10", "requests>=2.30.0"],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.8",
)