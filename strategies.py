"""Estrategias concretas para os canais de envio (Strategy)."""
from abc import ABC, abstractmethod
from .models import Notificacao


class CanalEnvio(ABC):
    """Contrato comum para qualquer canal de notificacao."""
    @abstractmethod
    def enviar(self, notificacao: Notificacao) -> str:
        """Executa o envio e devolve uma descricao do resultado."""
        raise NotImplementedError


class EnvioEmail(CanalEnvio):
    def enviar(self, notificacao: Notificacao) -> str:
        return (f"[E-MAIL] Para: {notificacao.destinatario} | "
                f"Mensagem: {notificacao.mensagem}")


class EnvioSMS(CanalEnvio):
    def enviar(self, notificacao: Notificacao) -> str:
        return (f"[SMS] Para: {notificacao.destinatario} | "
                f"Mensagem: {notificacao.mensagem}")


class EnvioPush(CanalEnvio):
    def enviar(self, notificacao: Notificacao) -> str:
        return (f"[PUSH] Dispositivo: {notificacao.destinatario} | "
                f"Mensagem: {notificacao.mensagem}")
