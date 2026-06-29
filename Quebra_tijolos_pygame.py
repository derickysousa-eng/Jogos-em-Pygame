import pygame
tamanho_tela = (800,800)
pygame.init()
janela = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Teste Pygame")

branco = (255,255,255)
preto = (0,0,0)
amarelo = (255,255,0)
azul = (0,0,255)
verde = (0,255,0)

tamanho_da_bola = 15
tamanho_do_jogador = 100
bola = pygame.Rect(100,500, tamanho_da_bola,tamanho_da_bola)
jogador = pygame.Rect(0,750,tamanho_do_jogador, 15)


qtde_bloco_linha = 8
qtde_linha_blocos = 10
qtde_total_blocos = qtde_bloco_linha * qtde_linha_blocos
def criar_blocos(qtde_linha_blocos, qtde_bloco_linha):
  altura_tela = tamanho_tela[1]
  largura_tela = tamanho_tela[0]
  largura_bloco = (largura_tela / 8) - 5
  altura_bloco = 15
  distancia_entre_linhas = altura_bloco + 10

  blocos = []
  for j in range (qtde_linha_blocos):
    for i in range(qtde_bloco_linha):
      bloco = pygame.Rect(i * (largura_bloco + 5),j * distancia_entre_linhas,largura_bloco,altura_bloco)
      blocos.append(bloco)

  return blocos

fim_jogo = False
pontuacao = 0
movimento_bola = [1 , -1]
def desenhar_inicio_jogo():
  janela.fill(preto)
  pygame.draw.rect(janela, azul,jogador)
  pygame.draw.rect(janela, branco,bola)

def desenhar_blocos(blocos):
  for bloco in blocos:
    pygame.draw.rect(janela, verde, bloco)

def movimentar_jogador(evento):
  if evento.type == pygame.KEYDOWN: # Evento.type serve para criar açao, pygame.KEYDOWN pra pegar o movimento do teclado
     if evento.key == pygame.K_RIGHT: # evento key é a maneira de chamar o KETDOWN, K_('a tecla que vai ser usada')
       if (jogador.x + tamanho_do_jogador) < tamanho_tela[0]: # logica para limitar o obj ao tamanho da tela sem q ele saia
          jogador.x = jogador.x + 3 # Positivo se for pra direita no eixo x
     if evento.key == pygame.K_LEFT:
        if jogador.x > 0:
          jogador.x = jogador.x - 3 # Negativo se for pra esquerda no eixo x

def movimentar_bola(bola):
  movimento = movimento_bola
  bola.x = bola.x + movimento[0]
  bola.y = bola.y + movimento[1]
  if bola.x <= 0: 
    movimento[0] = - movimento[0]
  if bola.y <= 0:
    movimento[1] = 0 - movimento[1]
  if bola.x + tamanho_da_bola >= tamanho_tela [0]:
    movimento[0] = 0 - movimento[0]
  if bola.y + tamanho_da_bola >= tamanho_tela [1]:
        movimento = None
  if jogador.collidepoint(bola.x, bola.y):
    movimento[1] = - movimento[1]
  for bloco in blocos:
    if bloco.collidepoint(bola.x, bola.y):
     blocos.remove(bloco)
     movimento[1] = - movimento[1]
  return movimento
def atualizar_pontuacao(pontuacao):
  fonte = pygame.font.Font(None, 30)
  texto = fonte.render(f'Pontuação: {pontuacao}', 1, amarelo)
  janela.blit(texto,(0,700))
  if pontuacao >= qtde_total_blocos:
    return True
  else:
    return False




blocos = criar_blocos(qtde_bloco_linha,qtde_linha_blocos)
 
while not fim_jogo:
 desenhar_inicio_jogo()
 desenhar_blocos(blocos)
 fim_jogo = atualizar_pontuacao(qtde_total_blocos - len(blocos))
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
    fim_jogo = True
 movimentar_jogador(event)
 if not movimentar_bola:
   fim_jogo = True

 movimento_bola = movimentar_bola(bola)
 pygame.time.wait(1) #comando para fazer a tela ficar atualizando a cada milessimo. Extrema importancia conter em qualquer codigo de jogo no pygame
 pygame.display.flip() # atualiza a tela do jogo, fundamental para constar as mudanças na tela

pygame.quit()


