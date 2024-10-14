import random
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Lista de palavras predefinidas
lista_palavras = ['floresta', 'mesa', 'telemovel', 'arvore', 'computador', 'python', 'jogo', 'carro']

# Escolhe uma palavra aleatória da lista
words = random.choice(lista_palavras)

word_display = ['_' for _ in words]  
attempts = 8  
limpar_tela()

print("BEM-VINDO!\n\nVamos começar!")

while attempts > 0 and '_' in word_display:
    print("\n" + ' '.join(word_display))
    guess = input("Escolhe uma letra: ").lower()

    if guess in words:
        for index, letter in enumerate(words):
            if letter == guess:
                word_display[index] = guess  
    else:
        print("A palavra não tem essa letra. Tente outra!")
        attempts -= 1
        print('Tentativas restantes: ' + str(attempts))  # Converte o número para string

if '_' not in word_display:
    print("\nParabéns! Acertaste a palavra!")
    print(' '.join(word_display))
    print("Bem jogado!")
else:
    print("\nGastaste todas as tentativas :(\nA palavra era: " + words)
    print("PERDESTE")

# Mantém o programa aberto até que o usuário pressione Enter para sair
input("\nPressiona Enter para sair...")
