import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hamilton",
    version="0.1.0",
    author="khuxkm",
    author_email="khuxkm+hamilton@tilde.team",
    description="Maintaining AutoSite Legacy and improving it",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dotcomboom/AutoSite",
    packages=setuptools.find_packages(),
    install_requires=[
        'pathlib',
        'bs4',
        'commonmark',
        'argparse',
        'dirsync'
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "License :: Public Domain",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Markup :: HTML"
    ],
    entry_points={
          'console_scripts': ['hamilton=hamilton.__init__:main'],
    },
)
