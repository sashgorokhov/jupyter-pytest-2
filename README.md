jupyter-pytest-2
================

This small pytest plugin allows it to discover and run tests written inside ipython notebook cells. It works by examining notebook global scope, putting it into a module object and passing it to pytest for futher processing. No temporary files or bytecode hacks. This allows you to share objects, dataframes, and references between your notebook, pytest fixtures and tests.

There may be memory leaks, but i did not bother testing it.

> You can not run pytest itself and give it a notebook, like 
> 
> ```shell
> pytest example.ipynb
> ```
> This will not work.

##### But why??!!1

I wrote this plugin to write data quality tests in databricks platform.

Installation
------------

```shell
pip install jupyter-pytest-2
```

Example notebook
----------------
https://github.com/sashgorokhov/jupyter-pytest-2/blob/master/example.ipynb

Usage
-------

Install the plugin, copypaste this into the notebook cell and run:

```python
import pytest


def test_foo():
    assert True

pytest.main()
```

You can separate this by different cells, write fixtures, parametrized or not, use different fixture scopes - you can use everything you love pytest for.

```python
import pytest

some_out_of_test_object = 'Hello, world!'

# Cell

@pytest.fixture(params=[1,2,3])
def foo(request):
  return request.param
  
# Cell

def test_foo(foo):
  assert some_out_of_test_object == 'Hello, world!'
  assert isinstance(foo, int)
  
# Cell

pytest.main(args=['-sv'])

```

### Usage notes

1. Plugin will discover only tests, fixtures and data in cells which were run in the current kernel scope. If you restart kernel, or load a notebook, you need to re-run cells with test related stuff.

2. If you write some tests, execute a cell, and then remove or rename that test, this test will remain in global scope and will be found & executed by plugin. This can lead to an unexpected things, even harming ones. When renaming or removing test or fixture, also restart the kernel.

Enjoy!
