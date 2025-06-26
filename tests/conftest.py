import pytest

from stuff.accum import Accumulator


@pytest.fixture
def accum(scope="function"):
    yield Accumulator()


@pytest.fixture
def accum2():
    return Accumulator()
