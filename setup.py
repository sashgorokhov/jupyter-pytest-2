from setuptools import setup

setup(
    author='sashgorokhov',
    author_email='sashgorokhov@gmail.com',
    classifiers=[
        'Framework :: Pytest',
        'Framework :: Jupyter',
        'Framework :: IPython',
        'Topic :: Software Development :: Testing',
        'Environment :: Plugins',
    ],
    description='Write and run pytest tests inside a notebook! Why? Because you can!',
    download_url='https://github.com/sashgorokhov/jupyter-pytest-2/archive/master.zip',
    entry_points={'pytest11': ['jupyter_pytest = jupyter_pytest']},
    install_requires=['pytest', 'notebook'],
    keywords=['pytest', 'ipython', 'jupyter', 'testing'],
    license='MIT License',
    name='jupyter-pytest-2',
    py_modules=['jupyter_pytest'],
    url='https://github.com/sashgorokhov/jupyter-pytest-2',
    version='1.0',
)
