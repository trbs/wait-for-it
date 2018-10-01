import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wait-for-it",
    version="0.0.1",
    author="Travis Clarke",
    author_email="travis.m.clarke@gmail.com",
    description="Wait for service(s) to be available before executing a command.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/clarketm/wait-for-it",
    packages=setuptools.find_packages(),
    py_modules=["wait_for_it"],
    install_requires=["click"],
    entry_points={
        'console_scripts': ['wait-for-it=wait_for_it:cli'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
