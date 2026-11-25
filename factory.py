"""Criadores concretos e Factory Method para selecionar o canal."""
from abc import ABC, abstractmethod
from .models import Notificacao
from .strategies import CanalEnvio, EnvioEmail, EnvioSMS, EnvioPush


class CriadorNotificador(ABC):
    """Define o Factory Method e o fluxo geral de notificacao."""
    @abstractmethod
    def criar_canal(self) -> CanalEnvio:
        """Retorna a estrategia concreta de envio."""
        raise NotImplementedError

    def notificar(self, destinatario: str, mensagem: str) -> str:
        notificacao = Notificacao.criar(destinatario, mensagem)
        canal = self.criar_canal()
        return canal.enviar(notificacao)


class CriadorEmail(CriadorNotificador):
    def criar_canal(self) -> CanalEnvio:
        return EnvioEmail()


class CriadorSMS(CriadorNotificador):
    def criar_canal(self) -> CanalEnvio:
        return EnvioSMS()


class CriadorPush(CriadorNotificador):
    def criar_canal(self) -> CanalEnvio:
        return EnvioPush()
