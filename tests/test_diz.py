import unittest
from diz.diz import Diz

class TestDiz(unittest.TestCase):
    """Test the Diz class
    """
    
    # TODO add real unittests
    
    def setUp(self):
        self.diz = Diz()

    def test_sample(self):
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()