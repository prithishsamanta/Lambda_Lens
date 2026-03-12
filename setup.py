from setuptools import setup, find_packages

setup(
    name='lambda-debug',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'boto3',
        'python-dotenv',
        'rich',
        'fastapi',
        'uvicorn',
        'jinja2',
        'click'
    ],
    entry_points={
        'console_scripts': [
            'lambda-debug=cli.main:debug',
        ],
    },
    description='AI-Powered Lambda Debugger',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/lambda-debug',
    author='Prithish Samanta',
    author_email='prithishsamanta@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
    ],
)