import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="xml_to_df",
    version="0.0.5",
    author="Praveen Kumar B",
    author_email="bpraveenkumar21@gmail.com",
    description="Package to convert xml to Pandas dataframe (flattens each and every xml element to dataframe column)",
    keywords = ['XML to Pandas Dataframe', 'XML to CSV', 'Flatten XML to DF', 'XML to Pandas DF'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PraveenKumar-21/xml_to_df",
    packages=setuptools.find_packages(),
    install_requires=[
        'pandas',
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)