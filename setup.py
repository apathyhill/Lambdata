import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIRED = [
    "numpy",
    "pandas"
]

setuptools.setup(
    name="lambdata-apathyhill",
    version="0.1.0",
    author="ApathyHill",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/apathyhill/Lambdata",
    packages=setuptools.find_packages(),
    install_requires = REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
