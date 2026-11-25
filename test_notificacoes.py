"""Testes automatizados basicos da prova de conceito."""
import unittest
from src.factory import CriadorEmail, CriadorSMS, CriadorPush
from src.models import Notificacao


class TestSistemaNotificacoes(unittest.TestCase):
    def test_envio_email(self):
        saida = CriadorEmail().notificar("aluno@exemplo.com", "Aviso")
        self.assertIn("[E-MAIL]", saida)
        self.assertIn("aluno@exemplo.com", saida)

    def test_envio_sms(self):
        saida = CriadorSMS().notificar("+5588999990000", "Codigo")
        self.assertIn("[SMS]", saida)

    def test_envio_push(self):
        saida = CriadorPush().notificar("celular-01", "Atualizacao")
        self.assertIn("[PUSH]", saida)

    def test_destinatario_vazio(self):
        with self.assertRaises(ValueError):
            Notificacao.criar("   ", "Mensagem")

    def test_mensagem_vazia(self):
        with self.assertRaises(ValueError):
            Notificacao.criar("destino", "   ")


if __name__ == "__main__":
    unittest.main()
