from unittest import TestCase
from com.kuma.operacoes import Operacoes

class TestOperacoes(TestCase):
    
    def setUp(self):
        self.operacoes = Operacoes()
    
    def test_div(self):
        self.assertEqual(self.operacoes.div(10,10),1,'should be 1')
    