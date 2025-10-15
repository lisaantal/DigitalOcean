# test_digitalocean.py
"""
Tests for DigitalOcean module.
"""

import unittest
from digitalocean import DigitalOcean

class TestDigitalOcean(unittest.TestCase):
    """Test cases for DigitalOcean class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DigitalOcean()
        self.assertIsInstance(instance, DigitalOcean)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DigitalOcean()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
