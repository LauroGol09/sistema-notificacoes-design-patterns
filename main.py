"""Ponto de entrada da prova de conceito. Execute: python main.py"""
from src.factory import CriadorEmail, CriadorSMS, CriadorPush


def executar_demo() -> None:
    exemplos = [
        (CriadorEmail(), "usuario@exemplo.com", "Seu cadastro foi confirmado."),
        (CriadorSMS(), "+55 88 99999-0000", "Seu codigo de acesso e 123456."),
        (CriadorPush(), "dispositivo-001", "Voce tem uma nova atualizacao."),
    ]

    print("=== SISTEMA DE NOTIFICACOES ===")
    for criador, destinatario, mensagem in exemplos:
        resultado = criador.notificar(destinatario, mensagem)
        print(resultado)


if __name__ == "__main__":
    executar_demo()
