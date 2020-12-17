"""
Tests for the molecule module.
"""

import molecool
import pytest
import numpy as np

def test_molecular_mass():
    symbols = ['C', 'H', 'H', 'H', 'H']

    calculated_mass = molecool.calculate_molecular_mass(symbols)

    actual_mass = 16.04

    assert pytest.approx(actual_mass, abs=1e-2) == calculated_mass

def test_calculate_angle():
    rA = np.array([0,0,-1])
    rB = np.array([0,0,0])
    rC = np.array([1,0,0])

    expected_angle = 90

    calculated_angle = molecool.calculate_angle(rA, rB, rC, degrees=True)

    assert pytest.approx(expected_angle) == calculated_angle

@pytest.mark.parametrize("p1, p2, p3, expected_angle",[
    (np.array([np.sqrt(2)/2, np.sqrt(2)/2, 0]), np.array([0,0,0]), np.array([1,0,0]), 45),
    (np.array([0,0,-1]), np.array([0,1,0]), np.array([1,0,0]), 60)
])
def test_calculate_angle_many(p1, p2, p3, expected_angle):
    calculated_angle = molecool.calculate_angle(p1, p2, p3, degrees=True)

    assert pytest.approx(expected_angle) == calculated_angle
