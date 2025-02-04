from setuptools import find_packages, setup

setup(
    name="bitcart",
    packages=find_packages(),
    version="1.10.1.0",
    license="LGPLv3+",
    description="BitcartCC coins support library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="MrNaif2018",
    author_email="chuff184@gmail.com",
    url="https://github.com/bitcartcc/bitcart-sdk",
    keywords=["electrum", "daemon", "bitcart", "bitcartcc"],
    install_requires=["jsonrpcclient", "aiohttp<4.0.0", "universalasync"],
    extras_require={"proxy": ["aiohttp_socks"]},
    package_data={"bitcart": ["py.typed"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
)
