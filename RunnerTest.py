import tests_12_1
import unittest

from tests_12_1 import Runner


class runner_tests(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner = Runner("TestRunner")
        # Вызываем метод walk у объекта 10 раз
        for _ in range(10):
            runner.walk()

        # Сравниваем distance объекта со значением 50
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner = Runner("TestRunner1")
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1 = Runner("TestRunnerOne")
        runner2 = Runner("TestRunnerTwo")
        # Вызываем метод run у первого объекта 10 раз
        for _ in range(10):
            runner1.run()

        # Вызываем метод walk у второго объекта 10 раз
        for _ in range(10):
            runner2.walk()

        # Убеждаемся, что дистанции не равны
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
     unittest.main()