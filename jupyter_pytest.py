from types import ModuleType

import IPython
import pytest
from _pytest import runner


class IPythonNamespaceCollector(pytest.Module):
    """
    Custom pytest collector that pretends to be a module.

    It collects all user-defined objects from notebook global scope and assigns them to a module object,
    which is then processed by pytest routines.
    """
    def _getobj(self):
        mod = ModuleType('notebook_tests')
        shell = IPython.get_ipython()
        for key, value in shell.ns_table['user_global'].items():
            setattr(mod, key, value)
        return mod


@pytest.hookimpl(tryfirst=True)
def pytest_make_collect_report(collector):
    # noop if in non-IPython environment
    if not IPython.get_ipython():
        return None
    m = IPythonNamespaceCollector.from_parent(parent=collector, fspath=collector.fspath)
    return runner.pytest_make_collect_report(m)
