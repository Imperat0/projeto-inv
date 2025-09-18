from setuptools import setup, find_packages

setup(
    name="meu_investimento",
    version="0.4",
    packages=find_packages(),
    install_requires=[],
    author="Daniel Imperato",
    author_email="imperato06@gmail.com",
    description="Uma biblioteca para cálculos de investimentos.",
    url="https://github.com/Imperat0/meu-investimento",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
