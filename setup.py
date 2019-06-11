import setuptools


with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="mx",
    version="0.0.1",
    author="",
    description="Mexico state meta information and other fun stuff",
    long_description=long_description,
    long_description_content_type="text/restructuredtext",
    url="",
    packages=setuptools.find_packages(exclude=('tests', 'docs')),
    install_requires=[],
)
