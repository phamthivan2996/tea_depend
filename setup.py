from setuptools import setup, find_packages

setup(
    name="tea_depend",
    version='0.0.1',
    author="phamthivan2996",
    author_email="kagum2996@gmail.com",
    description='Private bot for interacting with socials and profiles from tea_depend',
    packages=find_packages(),
    url='https://github.com/phamthivan2996/tea_depend',
    install_requires=[
        'g4f', 'capmonstercloudclient', 'commonstrings',
        'aiogram', 'aiofiles', 'aioimaplib', 'tweepy-self', 'better_proxy', 'aiohttp_proxy',
        'python-dotenv', 'loguru'
    ],
    project_urls={
        "GitHub": "https://github.com/phamthivan2996/tea_depend",
        "Source": "https://github.com/phamthivan2996/tea_depend"
    },
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ]
)
