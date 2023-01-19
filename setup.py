from setuptools import setup, find_packages



VERSION = '0.0.1'
DESCRIPTION = 'Türkçe sözlükten bir kelimenin anlamını almak için bir paket'
LONG_DESCRIPTION = 'Türkçe sözlükten bir kelimenin anlamını almak için bir paket'
AUTHOR = 'Hüseyin Averbek'

# Setting up
setup(
    name="kelimepy",
    version=VERSION,
    author=AUTHOR,
    author_email="<huseyinaverbek@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests'], # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'
    keywords=['python', 'kelime', 'anlam', 'sözlük', 'türkçe'],
    classifiers= [
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)