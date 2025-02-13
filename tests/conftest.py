"""Common functions and fixtures for pysqueezebox tests."""

import pytest


def pytest_addoption(parser: pytest.Parser) -> None:
    """Add the commandline options"""
    parser.addoption(
        "--host",
        type=str,
        default=None,
        action="store",
        dest="HOST",
        help="the host for the squeezebox server to be used for the integration tests",
    )

    parser.addoption(
        "--port",
        type=int,
        default=9000,
        action="store",
        dest="PORT",
        help="the port for the squeezebox server to be used for the integration tests",
    )

    parser.addoption(
        "--https",
        type=bool,
        default=False,
        action="store",
        dest="HTTPS",
        help="whether to use https to connect",
    )

    parser.addoption(
        "--prefer-player",
        type=str,
        default=None,
        action="append",
        dest="PREFER",
        help="prefer this player in tests",
    )

    parser.addoption(
        "--exclude-player",
        type=str,
        default=None,
        action="append",
        dest="EXCLUDE",
        help="exclude this player from being used in tests",
    )


def pytest_runtest_setup(item: pytest.Item) -> None:
    """Skip tests marked 'integration' unless an ip address is given."""
    if "integration" in item.keywords and not item.config.getoption("--host"):
        pytest.skip(
            "use --host and a hostname or an ip address to run integration tests."
        )
