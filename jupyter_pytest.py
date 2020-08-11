from types import ModuleType

import IPython
import pytest
from _pytest import runner
from _pytest.runner import runtestprotocol


class IPythonNamespaceCollector(pytest.Module):
    def _getobj(self):
        mod = ModuleType('notebook_tests')
        shell = IPython.get_ipython()
        for key, value in shell.ns_table['user_global'].items():
            setattr(mod, key, value)
        return mod


@pytest.hookimpl(tryfirst=True)
def pytest_make_collect_report(collector):
    m = IPythonNamespaceCollector.from_parent(parent=collector, fspath=collector.fspath)
    return runner.pytest_make_collect_report(m)


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_protocol(item, nextitem):
    """Copypasted original pytest implementation, except that reports from runtestprotocol are assigned to test item for further access"""
    item.ihook.pytest_runtest_logstart(nodeid=item.nodeid, location=item.location)
    reports = runtestprotocol(item, nextitem=nextitem)
    item.reports = reports
    item.ihook.pytest_runtest_logfinish(nodeid=item.nodeid, location=item.location)
    return True
