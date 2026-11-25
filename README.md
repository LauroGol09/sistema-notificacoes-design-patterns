# Sistema de Notificacoes — UML e Design Patterns

Prova de conceito academica em Python com dois padroes de projeto:

- **Factory Method (criacional):** concentra a criacao do canal concreto em criadores especializados.
- **Strategy (comportamental):** encapsula cada forma de envio por meio do contrato `CanalEnvio`.

## Requisitos
- Python 3.9 ou superior.
- Nenhuma biblioteca externa para executar o sistema.

## Executar
Abra o terminal na pasta do projeto e execute:

```bash
python main.py
```

## Executar testes

```bash
python -m unittest discover -s tests -v
```

## Estrutura

```text
sistema_notificacoes/
|-- main.py
|-- src/
|   |-- __init__.py
|   |-- models.py
|   |-- strategies.py
|   `-- factory.py
|-- tests/
|   `-- test_notificacoes.py
`-- docs/
    |-- diagrama_classes.png
    `-- diagrama_sequencia.png
```

## Limites da prova de conceito
O programa simula o envio e imprime a mensagem no console. Ele **nao** realiza entrega real por SMTP, operadora de SMS ou servico de notificacoes Push. Para uso real, seria necessario integrar provedores, credenciais, tratamento de falhas e politicas de seguranca.

## Publicar no GitHub
1. Crie um repositorio vazio com o nome `sistema-notificacoes-design-patterns`.
2. No terminal, dentro desta pasta, execute os comandos abaixo, substituindo `SEU-USUARIO` pelo seu usuario real do GitHub:

```bash
git init
git add .
git commit -m "Projeto Sistema de Notificacoes"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/sistema-notificacoes-design-patterns.git
git push -u origin main
```
3. Copie a URL real do repositorio e substitua o campo indicado na ultima secao do PDF.
