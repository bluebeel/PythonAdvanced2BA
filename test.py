# test.py
# author: Sébastien Combéfis
# version: February 1, 2016

import sys
import unittest

sys.path.append('CodeExamples')
from lib import test_mathutil

suite = unittest.TestLoader().loadTestsFromTestCase(test_mathutil.TestMathUtil)
runner = unittest.TextTestRunner()
exit(not runner.run(suite).wasSuccessful())