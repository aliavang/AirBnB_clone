#!/usr/bin/python3
"""Test cases for Review class."""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """A TestCase for Review class."""
    def test_inherits_BaseModel(self):
        """Tests if Review inherits from BaseModel."""
        instance = Review()
        self.assertIsInstance(instance, BaseModel)

    def test_place_id_exists(self):
        """Tests the default place_id value."""
        self.assertEqual(hasattr(Review, "place_id"), True)
        self.assertIs(type(Review.place_id), str)
        self.assertEqual(Review.place_id, "")

    def test_user_id_exists(self):
        """Tests the default user_id value."""
        self.assertEqual(hasattr(Review, "user_id"), True)
        self.assertIs(type(Review.user_id), str)
        self.assertEqual(Review.user_id, "")

    def test_text_exists(self):
        """Tests the default text value."""
        self.assertEqual(hasattr(Review, "text"), True)
        self.assertIs(type(Review.text), str)
        self.assertEqual(Review.text, "")
