import unittest
from unittest.mock import Mock

from src.model.CalculadoraConsole import CalculadoraConsole


class TestCalculadoraAbstrata(unittest.TestCase):
    def test_write_console_25(self):
        mock_print = Mock()
        mock_print.print.return_value = None
        calculadoraConsole = CalculadoraConsole("5 vezes 5", mock_print.print)
        calculadoraConsole.parse()
        
        mock_print.print.assert_called_once_with("O RESULTADO É 25")

if __name__ == '__main__':
    unittest.main()