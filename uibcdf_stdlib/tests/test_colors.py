import pytest
import numpy as np
from uibcdf_stdlib import colors

rgbcolor=[0.0, 0.5019607843137255, 0.5019607843137255]
hexcolor='#008080'

def test_1():
    argument = hexcolor
    output = colors.is_hex(argument)
    assert output == True

def test_2():
    argument = hexcolor
    output = colors.is_rgb(argument)
    assert output == False

def test_3():
    argument = rgbcolor
    output = colors.is_hex(argument)
    assert output == False

def test_4():
    argument = rgbcolor
    output = colors.is_rgb(argument)
    assert output == True

def test_5():
    argument = rgbcolor
    output = colors.rgb2hex(argument)
    assert output == hexcolor

def test_6():
    argument = hexcolor
    output = colors.hex2rgb(argument)
    assert np.allclose(output, rgbcolor)

def test_7():
    argument = hexcolor
    output = colors.convert(argument, to_form='hex')
    assert output == hexcolor

def test_8():
    argument = rgbcolor
    output = colors.convert(argument, to_form='rgb')
    assert np.allclose(output, rgbcolor)

def test_9():
    argument = rgbcolor
    output = colors.convert(argument, to_form='hex')
    assert output == hexcolor

def test_10():
    argument = hexcolor
    output = colors.convert(argument, to_form='rgb')
    assert np.allclose(output, rgbcolor)





