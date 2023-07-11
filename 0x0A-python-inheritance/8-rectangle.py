#!/usr/bin/python3
"""
Contains the class BaseGeometry aand subclass Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A representation of a recctangle"""
    def __init__(self, width, height):
        """instantiation of thee rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height