from Cleaning import *

def test_remove_clutter():
    assert remove_clutter('1920') == '1920'
    assert remove_clutter('nan') == ''

def test_just_year():
    assert just_year('me no 18/03/08') == '1908'
    assert just_year('1970/1940') == '1940'
    assert just_year('19/01/46 hfhjdjs 10/11/30') == '1930'
    assert just_year('02-aug-1935') == '1935'
    assert just_year('me an sjjdj') == ''

def test_year_format():
    assert year_format('1930') == '1930'
    assert year_format('12') == '1912'
    assert year_format('me') == ''

def test_add_19():
    assert add_19('20') == '1920'
    assert add_19('1940') == '1940'
