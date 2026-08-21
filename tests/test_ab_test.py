import pytest
from src.ab_test import compare_conversion, conversion_diff_ci

def test_compare_conversion_significant_difference():
    pvalue = compare_conversion(50, 500, 100, 500)
    assert pvalue < 0.05

def test_compare_conversion_no_significant_difference():
    pvalue = compare_conversion(50, 500, 52, 500)
    assert pvalue > 0.05


def test_conversion_diff_ci_significant():
    low, high = conversion_diff_ci(50, 500, 100, 500)
    assert not(high >= 0 and low <= 0)

def test_conversion_diff_ci_no_significant():
    low, high = conversion_diff_ci(50, 500, 52, 500)
    assert (high >= 0 and low <= 0)