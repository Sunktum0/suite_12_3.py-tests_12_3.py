import unittest
import tests_12_2
import RunnerTest


test_one = unittest.TestSuite()
test_one.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest.runner_tests))
test_one.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_one)
