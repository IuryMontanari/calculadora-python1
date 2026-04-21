# Calculadora em Python

## Descrição

Este projeto consiste em uma calculadora desenvolvida em Python, capaz de realizar operações matemáticas básicas como soma, subtração, multiplicação e divisão.

O programa permite a interação com o usuário através do terminal, tornando sua utilização simples e intuitiva.

---

## Como executar o arquivo `.sh`

Para executar o programa no Linux, siga os passos abaixo:

### 1. Clonar o repositório

```bash
git clone https://github.com/IuryMontanari/calculadora-python1.git
```

### 2. Acessar a pasta do projeto

```bash
cd calculadora-python1
```

### 3. Dar permissão de execução ao arquivo

```bash
chmod +x iniciar.sh
```

### 4. Executar o script

```bash
./iniciar.sh
```

---

## Explicação do código em Python

O código da calculadora foi desenvolvido utilizando a linguagem Python e possui uma estrutura simples e organizada.

O funcionamento do programa ocorre da seguinte forma:

Primeiramente, é apresentado um menu ao usuário com as opções de operações matemáticas disponíveis: soma, subtração, multiplicação e divisão.

O usuário escolhe a operação desejada digitando um número correspondente. Em seguida, o programa solicita a entrada de dois valores numéricos, que são convertidos para o tipo `float`, permitindo trabalhar com números decimais.

De acordo com a escolha do usuário, o programa utiliza estruturas condicionais (`if`, `elif` e `else`) para executar a operação correspondente.

No caso da divisão, foi implementada uma verificação para evitar divisão por zero, garantindo que o programa não apresente erro durante a execução.

Após realizar o cálculo, o resultado é exibido na tela para o usuário.

---

## Conclusão

Este projeto demonstra a criação de um programa em Python com interação via terminal, o uso de estruturas condicionais e tratamento de erros, além da execução do programa em ambiente Linux por meio de um script `.sh`.
