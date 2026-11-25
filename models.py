"""Entidades e validacoes do dominio."""
from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Notificacao:
    """Representa uma mensagem destinada a um usuario ou dispositivo."""
    destinatario: str
    mensagem: str
    criado_em: datetime

    @classmethod
    def criar(cls, destinatario: str, mensagem: str) -> "Notificacao":
        destinatario = destinatario.strip()
        mensagem = mensagem.strip()
        if not destinatario:
            raise ValueError("O destinatario nao pode ficar vazio.")
        if not mensagem:
            raise ValueError("A mensagem nao pode ficar vazia.")
        return cls(destinatario, mensagem, datetime.now())
