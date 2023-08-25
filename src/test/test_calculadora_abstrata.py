import unittest

from src.model.CalculadoraAbstrata import CalculadoraAbstrata


class TestCalculadoraAbstrata(unittest.TestCase):
    def test_add_1_1_result_2(self):
        calculadoraAbstrata = CalculadoraAbstrata("1 mais 1")
        result = calculadoraAbstrata.parse()
        self.assertEqual(result, 2)

    def test_subtract_2_1_result_1(self):
        calculadoraAbstrata = CalculadoraAbstrata("2 menos 1")
        result = calculadoraAbstrata.parse()
        self.assertEqual(result, 1)

    def test_divide_4_2_result_2(self):
        calculadoraAbstrata = CalculadoraAbstrata("4 dividido por 2")
        result = calculadoraAbstrata.parse()
        self.assertEqual(result, 2)

    def test_multiply_3_3_result_9(self):
        calculadoraAbstrata = CalculadoraAbstrata("3 vezes 3")
        result = calculadoraAbstrata.parse()
        self.assertEqual(result, 9)

    def test_power_4_2_result_16(self):
        calculadoraAbstrata = CalculadoraAbstrata("4 elevado a 2")
        result = calculadoraAbstrata.parse()
        self.assertEqual(result, 16)

    def test_try_to_power_0_by_any_number(self):
        calculadoraAbstrata = CalculadoraAbstrata("0 elevado a -10")
        with self.assertRaises(ValueError) as e:
            calculadoraAbstrata.parse()
        self.assertEqual(str(e.exception), "Não pode elevar 0 por um número igual ou menor que 0!")

    def test_force_brute_minus_100_100_all(self):
        for key in CalculadoraAbstrata.operations.keys():
            for x in range(-100, 101):
                for y in range(-100, 101):
                    operation = CalculadoraAbstrata.operations.get(key)
                    try:
                        result = CalculadoraAbstrata(f'{x} {operation} {y}').parse()
                        self.assertIsNotNone(result)
                    except: 
                        continue
                


if __name__ == '__main__':
    unittest.main()