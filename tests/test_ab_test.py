import pytest
from src.ab_test import compare_conversion

def test_compare_conversion_significant_difference():
    pvalue = compare_conversion(50, 500, 100, 500)
    assert pvalue < 0.05

def test_compare_conversion_no_significant_difference():
    pvalue = compare_conversion(50, 500, 52, 500)
    assert pvalue > 0.05