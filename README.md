## Jogo NIM
>status: Finalizado.

- Este projeto foi a atividade da semana 6 do curso: Introdução à Ciência da Computação com Python I. 
    - https://www.coursera.org/learn/ciencia-computacao-python-conceitos

### Linguagem:
- Python

### Objetivos:
- Visualizar e explorar "múltiplos" cenários;
- Identificar padrões;

- Explicação do Problema:
    - Sejam n o número de peças inicial e m o número máximo de peças que é possível retirar em uma rodada. Para garantir que o computador ganhe sempre, é preciso considerar os dois cenários possíveis para o início do jogo:
      - Se n é múltiplo de (m+1), o computador deve ser "generoso" e convidar o jogador a iniciar a partida com a frase "Você começa!"
      - Caso contrário, o computador toma a inciativa de começar o jogo, declarando "Computador começa!"
    - Uma vez iniciado o jogo, a estratégia do computador para ganhar consiste em deixar sempre um número de peças que seja múltiplo de (m+1) ao jogador. Caso isso não seja possível, deverá tirar o número máximo de peças possíveis. Seu trabalho, então, será implementar o Jogo e fazer com que o computador se utilize da estratégia vencedora.
    
 - Implementação:
     - Uma função computador_escolhe_jogada que recebe, como parâmetros, os números n e m descritos acima e devolve um inteiro correspondente à próxima jogada do computador (ou seja, quantas peças o computador deve retirar do tabuleiro) de acordo com a estratégia vencedora.
     - Uma função usuario_escolhe_jogada que recebe os mesmos parâmetros, solicita que o jogador informe sua jogada e verifica se o valor informado é válido. Se o valor informado for válido, a função deve devolvê-lo; caso contrário, deve solicitar novamente ao usuário que informe uma jogada válida.
     - Uma função partida que não recebe nenhum parâmetro, solicita ao usuário que informe os valores de n e m e inicia o jogo, alternando entre jogadas do computador e do usuário (ou seja, chamadas às duas funções anteriores). A escolha da jogada inicial deve ser feita em função da estratégia vencedora, como dito anteriormente. A cada jogada, deve ser impresso na tela o estado atual do jogo, ou seja, quantas peças foram removidas na última jogada e quantas restam na mesa. Quando a última peça é removida, essa função imprime na tela a mensagem "O computador ganhou!" ou "Você ganhou!" conforme o caso.
