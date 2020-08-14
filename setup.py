from setuptools import setup

try:
    with open('README.md', 'r') as f:
        long_description = f.read()
except:
    long_description = 'Error reading README.md'


setup(
    author='sashgorokhov',
    author_email='sashgorokhov@gmail.com',
    classifiers=[
        'Framework :: Pytest',
        'Framework :: Jupyter',
        'Framework :: IPython',
        'Environment :: Plugins',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Testing',
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description='Write and run pytest tests inside a notebook! Why? Because you can!',
    download_url='https://github.com/sashgorokhov/jupyter-pytest-2/archive/master.zip',
    entry_points={'pytest11': ['jupyter_pytest = jupyter_pytest']},
    install_requires=['pytest >= 5.0', 'notebook >= 6.0'],
    keywords=['pytest', 'ipython', 'jupyter', 'testing'],
    license='MIT License',
    long_description=long_description,
    long_description_content_type="text/markdown",
    name='jupyter-pytest-2',
    py_modules=['jupyter_pytest'],
    url='https://github.com/sashgorokhov/jupyter-pytest-2',
    version='1.0.1',
)
