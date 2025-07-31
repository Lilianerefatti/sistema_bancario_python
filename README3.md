# 💳 Sistema Bancário em Python

Este repositório acompanha minha evolução na linguagem Python, através da construção e refatoração de um **sistema bancário**. O projeto começou com uma abordagem procedural e foi gradualmente transformado em um código **orientado a objetos (POO)**, aplicando boas práticas de encapsulamento, herança, composição e polimorfismo.

---

## 🧠 Objetivo do Projeto

Desenvolver um sistema de banco simples que permita:
- Criar usuários e contas
- Realizar depósitos e saques com regras
- Exibir extratos com histórico de transações
- Listar contas registradas

Com isso, pude comparar os paradigmas procedural e orientado a objetos, praticando os conceitos de POO com exemplos reais e didáticos.

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
📋 Funcionalidades do Menu
Opção	Ação
d	Depositar
s	Sacar
e	Exibir extrato
nu	Criar novo usuário
nc	Criar nova conta para usuário
lc	Listar todas as contas
q	Sair do sistema

🧪 Regras de Negócio
- Saques possuem limite de valor e de quantidade por dia
- Contas associadas ao CPF do cliente
- Transações armazenadas com data/hora e tipo
- Apenas uma conta por cliente (na versão atual)

💡 Aprendizados
- Refatoração de código real para POO 
- Uso de @property, herança e métodos de classe 
- Organização modular e princípios do SOLID
- Aplicação prática de classes abstratas com abc.ABC

📌 Desafio Original
Refatorar o código bancário procedural para um sistema orientado a objetos, criando uma hierarquia de classes baseada em um diagrama UML fornecido, garantindo o encapsulamento da lógica bancária.

🚀 Futuras Melhorias
- Persistência com arquivos (JSON ou SQLite)
- Interface gráfica (Tkinter ou PyQt)
- Criação de múltiplas contas por cliente
- Testes unitários com pytest
