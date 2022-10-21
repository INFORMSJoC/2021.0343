import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='RECASOpt',
    version='0.0.1',
    author='Wenyu Wang',
    author_email='wenyu_wang@u.nus.edu',
    description='An surrogate-assisted optimizer for expensive many-objective optimization problems',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/WY-Wang/2021.0343/src/RECASOpt',
    license='MIT',
    packages=setuptools.find_packages(),
)
