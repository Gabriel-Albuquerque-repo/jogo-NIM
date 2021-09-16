def computador_escolhe_jogada(x,y):
    z = x

    if z % (y + 1) != 0:
        while z  % (y + 1) != 0: 
            z = z - 1

        g = x - z

        print("\nO computador tirou", g, "peça(s) no tabuleiro.\n")
    
        return g 

    else:

        print("\nO computador tirou", y, "peça(s) no tabuleiro.\n")
        return y

def usuario_escolhe_jogada(x,y):
    
    if x < y or x < 1 or y < 1: 
        
        return "esses parâmetros não são admitidos"

    else:
        w = int(input("Quantas peças você vai tirar? "))

        while w < 1 or w > y or w > x:
            print("\nOops! Jogada inválida! Tente de novo.\n")
            w = int(input("Quantas peças você vai tirar? "))
    
        print("\nVocê tirou", w, "peça(s).")
        
        return w 
        
def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    while m > n or n < 1 or m < 1:
        n = int(input("Escolha inválida, diga um novo n: "))
        m = int(input("Limite de peças por jogada? "))
        
    if n % (m + 1) == 0:
        print("\nVoce começa!\n")
         
        while n != 0: 
            a = usuario_escolhe_jogada(n,m)
            n = n - a
            z = computador_escolhe_jogada(n,m)
            n = n - z  
            
    else:
        print("\nComputador começa!")

        while n != 0: 
            a = computador_escolhe_jogada(n,m)
            n = n - a
            if n == 0:
                break
            
            z = usuario_escolhe_jogada(n,m)
            n = n - z
            
    print("Fim do jogo! O computador ganhou!")
    
def campeonato():
    print("**** Rodada 1 ****\n")
    partida()
    print("\n**** Rodada 2 ****\n")    
    partida()
    print("\n**** Rodada 3 ****\n")
    partida()



print("Bem-vindo ao jogo do NIM! Escolha:\n") 
print("1 - para jogar uma partida isolada")     
print("2 - para jogar um campeonato")           
g = int(input())                                

while g != 1 and g != 2:                      
    g = int(input("Você precisa selecionar a opção 1 ou 2\n"))
            
if g == 1: 
    print("Voce escolheu uma partida isolada!\n")
    partida()
    print("\nPlacar: Você 0 x 1 Computador")
    
else:
    print("Voce escolheu um campeonato!\n")
    campeonato()
    print("\n**** Final do campeonato! ****")
    print("\nPlacar: Voce 0 x 3 Computador")

    
