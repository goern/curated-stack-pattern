"""Setup file for thoth.curated_stack_pattern python package."""


from setuptools import setup
import os

_HERE = os.path.dirname(os.path.abspath(__file__))


def get_version():
    """Get version of."""
    with open(os.path.join(_HERE, "version.py")) as f:
        content = f.readlines()

    for line in content:
        if line.startswith("__version__ ="):
            return line.split(" = ")[1][1:-2]

    raise ValueError("No version identifier found")


setup(
    name="curated_stack_pattern",
    version=get_version(),
    description="...",
    keywords=[],
    url="https://github.com/thoth-station/",
    download_url="https://pypi.org/project/",
    long_description=open(os.path.join(_HERE, "README.md")).read(),
    long_description_content_type="text/markdown",
    author="",
    author_email="",
    license="LGPLv3+",
    py_modules=["curated_stack_pattern"],
    install_requires=["pip>=9"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
    ],
    extras_require={
        "toml": ["toml"],
    },
)