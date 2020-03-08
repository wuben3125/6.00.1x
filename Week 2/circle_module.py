# -*- coding: utf-8 -*-
"""
This is a test module for a circle
"""

pi = 3.1415928008

def area(r):
    return r**2*pi


def perimeter(r):
    return 2*r*pi


def area_perimeter_sum(r):
    return area(r) + perimeter(r)