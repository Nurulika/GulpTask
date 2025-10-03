# test_gulptask.py
"""
Tests for GulpTask module.
"""

import unittest
from gulptask import GulpTask

class TestGulpTask(unittest.TestCase):
    """Test cases for GulpTask class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GulpTask()
        self.assertIsInstance(instance, GulpTask)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GulpTask()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
