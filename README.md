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
