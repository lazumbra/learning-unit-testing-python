from unittest import TestCase
from app.fila import Fila


class TestFila(TestCase):

    # O setUpClass roda apenas uma vez antes de tudo
    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    # O tearDownClass é executado apenas uma vez no final do teste.
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    # Antes de cada teste ele executa o setUp
    def setUp(self):
        self.fila = Fila()
        print('SetUp')

    # Depois de cada teste ele executa o tearDown
    def tearDown(self):
        print('tearDown')

    def test_quando_5_entrar_na_fila_5_deve_estar_no_final_fila(self):
        entrada = 5
        saida_esperada = 5

        self.fila.entrar(entrada)

        self.assertEqual(saida_esperada, self.fila[-1])

    def test_quando_10_entrar_na_fila_10_deve_estar_no_final_fila(self):
        entrada = 10
        saida_esperada = 10

        self.fila.entrar(entrada)

        self.assertEqual(saida_esperada, self.fila[-1])

    def test_quando_10_entrar_na_fila_seguido_de_5_10_deve_estar_no_comeco_da_fila(self):
        entrada1 = 10
        entrada2 = 5

        saida_esperada = 10

        self.fila.entrar(entrada1)
        self.fila.entrar(entrada2)

        self.assertEqual(saida_esperada, self.fila[0])
