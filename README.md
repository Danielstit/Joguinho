# Jogo da Descoberta de Palavras

Este projeto é um jogo interativo em Python onde o usuário precisa adivinhar uma palavra com base em dicas e tentativas limitadas. O jogador pode tentar adivinhar a palavra, letra por letra, até acertar ou atingir o limite de tentativas.

## Funcionalidades

- **Entrada de palavra e dica**: O jogador insere o nome de um objeto, pessoa ou animal e fornece uma dica para ajudar na adivinhação.
- **Número de tentativas**: O jogador pode tentar adivinhar a palavra com um número limitado de tentativas, definidas pelo próprio usuário.
- **Adivinhação letra por letra**: O jogador insere uma letra de cada vez. O sistema verifica se a letra está na palavra e revela as letras acertadas.
- **Validação de entrada**: O jogo garante que o jogador insira apenas uma letra por vez. Se uma entrada inválida for dada, o sistema avisa e continua.
- **Feedback constante**: O jogador é informado sobre quantas tentativas restam e quais letras já foram tentadas.

## Como jogar

1. **Requisitos**:
   - Python 3.x instalado no seu sistema.

2. **Passos para rodar**:
   1. Baixe ou clone este repositório.
   2. Abra o terminal/linha de comando.
   3. Navegue até a pasta onde o arquivo Python está localizado.
   4. Execute o arquivo:
      ```bash
      python jogo_palavra.py
      ```
   5. O programa solicitará que você insira:
      - Um nome a ser adivinhado (ex: objeto, pessoa, animal).
      - Uma dica para ajudar a adivinhar a palavra.
      - A quantidade de tentativas que o jogador terá.
      - Uma letra de cada vez para tentar adivinhar a palavra.
      
   6. O jogo continuará até que o jogador adivinhe a palavra corretamente ou atinja o número máximo de tentativas.

## Exemplo de Execução

```bash
INFORME O NOME A SER DESCOBERTO(EX: OBJETO, PESSOAS, ANIMAIS...): 
cachorro

DÊ UMA DICA: 
É um animal

INFORME A QUANTIDADE DE TENTATIVAS QUE O USUARIO TERÁ PARA ENCONTRAR AS PALAVRA: 
5

DICA: É um animal
DIGITE UMA LETRA:
c

QUANTIDADE DE TENTATIVAS: 1

---------------------------------------------
TENTATIVAS RESTANTES: 4

TODAS AS LETRAS INSERIDAS:[c]

LETRAS QUE POSSUEM NO NOME 
|c| 

---------------------------------------------
DIGITE UMA LETRA:
a

QUANTIDADE DE TENTATIVAS: 2

---------------------------------------------
TENTATIVAS RESTANTES: 3

TODAS AS LETRAS INSERIDAS:[ca]

LETRAS QUE POSSUEM NO NOME 
|ca| 

---------------------------------------------
DIGITE UMA LETRA:
h

QUANTIDADE DE TENTATIVAS: 3

---------------------------------------------
TENTATIVAS RESTANTES: 2

TODAS AS LETRAS INSERIDAS:[cah]

LETRAS QUE POSSUEM NO NOME 
|cah| 

---------------------------------------------
DIGITE UMA LETRA:
o

QUANTIDADE DE TENTATIVAS: 4

---------------------------------------------
TENTATIVAS RESTANTES: 1

TODAS AS LETRAS INSERIDAS:[caho]

LETRAS QUE POSSUEM NO NOME 
|caho| 

---------------------------------------------
DIGITE UMA LETRA:
r

QUANTIDADE DE TENTATIVAS: 5

---------------------------------------------
TENTATIVAS RESTANTES: 0

TODAS AS LETRAS INSERIDAS:[cahor]

LETRAS QUE POSSUEM NO NOME 
|cahor| 

---------------------------------------------
PARABÉNS!! VOCÊ ACERTOU A PALAVRA [cachorro]
