from setuptools import setup, find_packages

base_packages = [
    'pandas',
    'numpy',
    'scikit-learn',
    'pytest',
    'openpyxl'
]

util_packages = [
    "jupyterlab",
]

docs_packages = [
    "sphinx==3.5.4",
    "nbsphinx",
    'sphinx_rtd_theme'
]

dev_packages = base_packages + util_packages + docs_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='PyMinHash',
      version='0.1.1',
      author="Frits Hermans",
      description="Efficient MinHashing",
      long_description=long_description,
      long_description_content_type="text/markdown",
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      url="https://github.com/fritshermans/pyminhash",
      packages=find_packages(exclude=['notebooks']),
      package_data={"pyminhash": ["data/*.xlsx", "data/*.csv"]},
      install_requires=base_packages,
      extras_require={
          "base": base_packages,
          "dev": dev_packages,
          "docs": docs_packages,
      },
      python_requires=">=3.6.9",
      )
