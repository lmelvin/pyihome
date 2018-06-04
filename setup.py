import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyihome",
    version="0.0.1",
    author="lmelvin",
    author_email="luke@lucasmelvin.com",
    description="Python library to interface with iHome API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lmelvin/pyihome",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    )
)
