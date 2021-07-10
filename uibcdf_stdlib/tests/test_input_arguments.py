import pytest
import numpy as np
from uibcdf_stdlib.input_arguments import check_input_argument
import pyunitwizard as puw
puw.configure.load_library('pint')

def test_1():
    argument = 5.0
    output = check_input_argument(argument, float)
    assert output == True

def test_2():
    argument = 5.0
    output = check_input_argument(argument, str)
    assert output == False

def test_3():
    argument = np.zeros([3,4])
    output = check_input_argument(argument, np.ndarray, shape=(3,4))
    assert output == True

def test_4():
    argument = puw.quantity(10, 'nm')
    output = check_input_argument(argument, 'quantity', dimensionality={'[L]':1}, value_type=int)
    assert output == True

def test_5():
    argument = puw.quantity(5.0, 'ps')
    output = check_input_argument(argument, 'quantity', dimensionality={'[L]':1}, value_type=float)
    assert output == False

def test_6():
    argument = puw.quantity([0,0,0], 'nm/ps')
    output = check_input_argument(argument, 'quantity', dimensionality={'[L]':1, '[T]':-1},
                                  value_type=np.ndarray, shape=(3,))
    assert output == True

def test_7():
    argument = puw.quantity(np.array([0,0,0]), 'ps')
    output = check_input_argument(argument, 'quantity', value_type=np.ndarray, shape=(3,), unit='ps')
    assert output == True

def test_8():
    argument = puw.quantity(np.array([0,0,0]), 'ps')
    output = check_input_argument(argument, 'quantity', shape=(3), unit='ns')
    assert output == False

def test_9():
    argument = puw.quantity([0,0,0], 'nm')
    output = check_input_argument(argument, 'quantity', value_type=[list, tuple, np.ndarray])
    assert output == True

