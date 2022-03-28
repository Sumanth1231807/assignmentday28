import prism
import pytest

def test_surface_area_prism():
    l=2
    b=3
    h=4
    result=prism.surface_area_prism(l,b,h)
    assert result == 2*((l*b) + (l*h) + (b*h))

def test_volume_prism():
    l = 2
    b = 3
    h = 4
    result = prism.volume_prism(l, b, h)
    assert result == l*b*h

def test_diagonol_prism():
    l = 2
    b = 3
    h = 4
    diagonal = ((l * l) + (b * b )+ (h * h))
    result = prism.diagonol_prism(l, b, h)
    assert result == diagonal ** 0.5