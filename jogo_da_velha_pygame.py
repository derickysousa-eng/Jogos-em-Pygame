import pygame

pygame.init()

LARGURA, ALTURA = 800, 800 
janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Velha")

preto = (0, 0, 0)
branco = (255, 255, 255)
verde = (0, 255, 0)
azul = (0, 0, 255)
azul_escuro = (0,0,128)
vermelho_escuro = (139,0,0)
vermelho = (255,0,0)

tabuleiro = [["" for _ in range(3)] for _ in range(3)]
jogador = "x"
venceu = False
empate = False  
vencedor = None
linha_vencedora = None
botao_reiniciar = pygame.Rect(280, 700, 240, 60)



# -------------------- FUNÇÕES --------------------
def desenhar_tabuleiro():
    for i in range(1, 3):
        pygame.draw.line(janela, azul_escuro,
                         (150, 100 + i * 180),
                         (690, 100 + i * 180), 5)

        pygame.draw.line(janela, vermelho_escuro,
                         (150 + i * 180, 100),
                         (150 + i * 180, 640), 5)
def desenhar_botao():
    pygame.draw.rect(janela, azul_escuro, botao_reiniciar, border_radius=10)

    texto = fonte.render("Reset", True, branco)
    janela.blit(texto, texto.get_rect(center = botao_reiniciar.center))

def desenhar_jogadas():
    for l in range(3):
        for c in range(3):
            x = 150 + c * 180
            y = 100 + l * 180

            if tabuleiro[l][c] == "x":
                pygame.draw.line(janela, vermelho, (x+40, y+40), (x+140, y+140), 5)
                pygame.draw.line(janela, vermelho, (x+140, y+40), (x+40, y+140), 5)

            elif tabuleiro[l][c] == "o":
                pygame.draw.circle(janela, azul, (x+90, y+90),55, 5)



def verificar_vitoria(j):
    combinacoes = [
        [(0,0),(0,1),(0,2)],
        [(1,0),(1,1),(1,2)],
        [(2,0),(2,1),(2,2)],

        [(0,0),(1,0),(2,0)],
        [(0,1),(1,1),(2,1)],
        [(0,2),(1,2),(2,2)],

        [(0,0),(1,1),(2,2)],
        [(0,2),(1,1),(2,0)]
    ]

    for c in combinacoes:
        if (tabuleiro[c[0][0]][c[0][1]] ==
            tabuleiro[c[1][0]][c[1][1]] ==
            tabuleiro[c[2][0]][c[2][1]] ==
            j):
            return c

    return None


def desenhar_linha_vitoria(linha):
    if not linha:
        return

    x1 = 150 + linha[0][1] * 180 + 90
    y1 = 100 + linha[0][0] * 180 + 90

    x2 = 150 + linha[2][1] * 180 + 90
    y2 = 100 + linha[2][0] * 180 + 90

    pygame.draw.line(janela, verde, (x1, y1), (x2, y2), 5)


def reiniciar():
    global tabuleiro, jogador, venceu, vencedor, linha_vencedora, empate
    tabuleiro = [["" for _ in range(3)] for _ in range(3)]
    jogador = "x"
    venceu = False
    vencedor = None
    empate = False
    linha_vencedora = None
    




def clicar(pos):
    global jogador, venceu, vencedor, linha_vencedora, empate, botao_reiniciar
    x, y = pos

    if botao_reiniciar.collidepoint(pos):
      reiniciar()
      return

    if venceu or empate:
        return

    if not (150 <= x <= 690 and 100 <= y <= 640):
     return

    col = (x - 150) // 180
    lin = (y - 100) // 180
    

    if tabuleiro[lin][col] == "":
        tabuleiro[lin][col] = jogador

        linha_vencedora = verificar_vitoria(jogador)
        if linha_vencedora:
            venceu = True
            vencedor = jogador
        elif verificar_empate():
            empate = True

        else:
            jogador = "o" if jogador == "x" else "x"
  


def verificar_empate():
    for l in tabuleiro:
        for c in l:
            if c == "":
                return False
    return True


# -------------------- LOOP --------------------
rodando = True
fonte = pygame.font.SysFont(None, 60)

while rodando:

    janela.fill(preto)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            clicar(event.pos)
        

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reiniciar()

    desenhar_tabuleiro()
    desenhar_jogadas()
    desenhar_botao()

    if linha_vencedora:
        desenhar_linha_vitoria(linha_vencedora)

    if venceu and vencedor:
        texto = fonte.render(f"{vencedor.upper()} venceu!", True, verde)
        janela.blit(texto, (250, 20))

    elif empate:
        texto = fonte.render("Empate!", True, verde)
        janela.blit(texto, (320, 20))
    pygame.display.update()

pygame.quit()
