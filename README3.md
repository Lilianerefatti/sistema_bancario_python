# 💳 Sistema Bancário em Python

Este projeto simula um **sistema bancário em Python orientado a objetos**, implementando os principais conceitos de POO: **herança, encapsulamento, polimorfismo e abstração**.

> 🔁 Este é o terceiro desafio do repositório [`sistema_bancario_python`](https://github.com/Lilianerefatti/sistema_bancario_python), desenvolvido com foco educacional.

---

## 🧠 Objetivo do Projeto

Desenvolver um sistema de banco simples que permita:
- Criar usuários e contas
- Realizar depósitos e saques com regras
- Exibir extratos com histórico de transações
- Listar contas registradas

Com isso, pude comparar os paradigmas procedural e orientado a objetos, praticando os conceitos de POO com exemplos reais e didáticos.

---
## 📂 Estrutura do Projeto

- `Cliente`: classe base para clientes, com herança em `PessoaFisica`
- `Conta`: classe base para contas, com herança em `ContaCorrente`
- `Transacao`: classe abstrata com implementações para `Deposito` e `Saque`
- `Historico`: armazena todas as transações realizadas
- `main()`: interface de menu com opções para realizar operações bancárias

---

## 🚀 Funcionalidades

- Criar usuários (Pessoa Física)
- Criar contas correntes com limite e controle de saques
- Realizar depósitos e saques
- Gerar extrato com saldo e histórico de transações
- Listar todas as contas criadas

---
## 📖 Conceitos aplicados
- Refatoração de código real para Programação Orientada a Objetos (POO)
- Uso de @property, herança e métodos de classe 
- Métodos abstratos (com uso do abc)
- Encapsulamento com propriedades privadas
- Registro e histórico de transações

---

## 🧱 Evolução do Projeto

### ✅ Versão Inicial (Procedural)
- Estrutura baseada em funções e dicionários
- Controle de usuários, contas, depósitos, saques e extrato
- Lógica embutida em uma única função `main()`

### ✅ Versão Final (POO)
- Refatoração completa com classes e métodos
- Abstrações como `Cliente`, `Conta`, `Transacao`, `Historico`
- Aplicação de herança (`PessoaFisica`, `ContaCorrente`)
- Uso de classes abstratas (`Transacao`) para obrigar implementação de métodos

---

## 🗂️ Principais Classes

| Classe          | Função                                                                 |
|----------------|------------------------------------------------------------------------|
| `Cliente`       | Representa um cliente genérico                                         |
| `PessoaFisica`  | Herda de Cliente com atributos específicos (nome, CPF, etc.)          |
| `Conta`         | Modelo base para contas (saldo, saque, depósito, extrato)             |
| `ContaCorrente` | Especializa `Conta` com limites e contagem de saques                  |
| `Transacao`     | Abstração para movimentações (subclasses: `Saque`, `Deposito`)        |
| `Historico`     | Guarda o extrato com timestamp de todas as transações                 |

---
## 📋 Funcionalidades do Menu
|Opção	|Ação                          |
|-------|------------------------------|
|d	    |Depositar                     |
|s	    |Sacar                         |
|e	    |Exibir extrato                |
|nu	    |Criar novo usuário            |
|nc	    |Criar nova conta para usuário |
|lc	    |Listar todas as contas        |
|q	    |Sair do sistema               |

---

## 📌 Regras de Negócio
- Limite de **R$ 500,00 por saque**
- Máximo de **3 saques diários**
- Depósitos e saques precisam ser **positivos**
- CPF único para cada usuário
- Contas associadas ao CPF do cliente
- Transações armazenadas com data/hora e tipo

---

## 📌 Desafio Original
Refatorar o código bancário procedural para um sistema orientado a objetos, criando uma hierarquia de classes baseada em um diagrama UML fornecido, garantindo o encapsulamento da lógica bancária.

---

🚀 Futuras Melhorias
- Persistência com arquivos (JSON ou SQLite)
- Interface gráfica (Tkinter ou PyQt)
- Criação de múltiplas contas por cliente
- Testes unitários com pytest

---
## 👩‍💻 Desenvolvido por
Liliane Refatti
🔗 linkedin.com/in/lilianerefatti

---
## 🗂️ Outros desafios no repositório
banco1.py: versão procedural
banco2.py: transição com modularização
banco3.py: versão orientada a objetos com boas práticas
