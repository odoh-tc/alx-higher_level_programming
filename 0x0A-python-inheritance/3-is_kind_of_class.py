#!/usr/bin/python3
"""
Contains thee is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """True if obj is an instance or iinherited from a_class, else False"""
    return (isinstance(obj, a_class))
