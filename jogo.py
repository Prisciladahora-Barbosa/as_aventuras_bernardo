import time 
import sys

def digitar(texto):
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print()

def mostrar_status(vida, inventario):
    print("\n" + "="*30)
    print(f"❤️ VIDA: {vida} | 🎒 ITENS: {', '.join(inventario) if inventario else 'Vazio'}")
    print("="*30 + "\n")

def fim_de_jogo(mensagem):
    digitar(f"\n💀 {mensagem}")
    digitar("FIM DE JOGO. Tente novamente!")
    sys.exit()

def inicio():
    print("""
    #######################################
    #        AS AVENTURAS DE BERNARDO     #
    #              ( ^_^)／               #
    #######################################
    """)

    digitar("Bernardo acorda em uma floresta densa. Ele não se lembra de como chegou aqui.")
    digitar("Ao seu lado, há uma mochila velha e dois caminhos à frente.")
    
    vida = 100
    inventario = ["Mapa Antigo"]
    
    primeira_escolha(vida, inventario)

def primeira_escolha(vida, inventario):
    mostrar_status(vida, inventario)
    print("1. Seguir pela trilha de pedras (Parece levar a uma montanha)")
    print("2. Seguir pelo caminho das flores (Cheiro de mel, mas silencioso demais)")
    
    escolha = input("> ")
    
    if escolha == "1":
        caverna_montanha(vida, inventario)
    elif escolha == "2":
        digitar("Bernardo caminha e encontra um enxame de abelhas gigantes!")
        vida -= 30
        digitar(f"Ele foi picado! Perdeu 30 de vida.")
        inventario.append("Mel Curativo")
        digitar("Mas ele conseguiu escapar com um pouco de 'Mel Curativo'.")
        caverna_montanha(vida, inventario)
    else:
        print("Escolha inválida.")
        primeira_escolha(vida, inventario)

def caverna_montanha(vida, inventario):
    mostrar_status(vida, inventario)
    digitar("Bernardo chega à entrada de uma caverna escura.")
    digitar("Um Guardião de Pedra bloqueia o caminho.")
    print("""
          _______
       /|        |
      | |  [@@]  |
      | |   __   |
      | |________|
      /_|________|_\\
     /              \\
    """)
    print("1. Tentar lutar com o Guardião")
    print("2. Mostrar o Mapa Antigo")
    if "Mel Curativo" in inventario:
        print("3. Oferecer o Mel Curativo")

    escolha = input("> ")

    if escolha == "1":
        fim_de_jogo("O Guardião era forte demais. Bernardo virou estátua.")
    elif escolha == "2":
        digitar("O Guardião reconhece o símbolo no mapa e se afasta solenemente.")
        boss_final(vida, inventario)
    elif escolha == "3" and "Mel Curativo" in inventario:
        digitar("O Guardião adora o doce e deixa Bernardo passar com um sorriso de pedra.")
        vida = 100 # Recupera vida
        boss_final(vida, inventario)
    else:
        print("Escolha inválida.")
        caverna_montanha(vida, inventario)
 

def boss_final(vida, inventario):
    digitar("No fundo da caverna, Bernardo encontra o Portal de Cristal.")
    digitar("Um dragão de sombras surge das paredes!")
    
    print("""
             ___====-_  _-====___
       _--^^^#####//      \\#####^^^--_
    _-^##########// (    ) \\##########^-_
   -############//  |\^^/|  \\############-
  _/############//   (@::@)   \\############\_
 /#############((     \\//     ))#############\
""")
    # ----------------------------------
    print("1. Atravessar o portal correndo")
    print("2. Usar o brilho do Mapa Antigo para afastar as sombras")

    escolha = input("> ")

    if escolha == "1":
        if vida > 80:
            digitar("Bernardo é rápido e, apesar de alguns arranhões, atravessa o portal!")
            vitoria()
        else:
            fim_de_jogo("Bernardo estava fraco demais para correr e as sombras o pegaram.")
    elif escolha == "2":
        digitar("O mapa brilha intensamente, dissipando o dragão. O caminho está livre!")
        vitoria()
    else:
        boss_final(vida, inventario)

def vitoria():
    print("""
       ___________
      '._==_==_=_.'
      .-\\:      /-.
     | (|:.     |) |
      '-|:.     |-'
        \\\\::.    /
         '::. .'
           ) (
         _.' '._
        '-------'
    """)
    print("\n" + "✨"*20)
    digitar("PARABÉNS, BERNARDO!")
    digitar("Você atravessou o portal e voltou para casa como um verdadeiro herói.")
    print("✨"*20)
    sys.exit()

# Iniciar o jogo
if __name__ == "__main__":
    inicio()