# Copyright (C) 2025 Yeeti
"""Example of tests."""

import pytest

from yeeti.test_module.example import capital_case


def test_succeed():
    """Example of successful test."""

    assert capital_case('semaphore') == 'Semaphore'


def test_raises_exception():
    """Example of exception test."""

    with pytest.raises(AttributeError):
        capital_case(9)
