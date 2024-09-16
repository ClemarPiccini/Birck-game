import pygame
import random
from plyer import vibrator  # Biblioteca para vibração

# Inicializa o pygame
pygame.init()

# Definindo cores
INICIAL = (92, 98, 217, 1)
FUNDO = (37, 37, 114, 1)    
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GRAY = (150, 150, 150)  # Cor de contorno

# Configurações da tela
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("BRICK BREAKER GAME!")

# Sons
pygame.mixer.init()
level_complete_sound = pygame.mixer.Sound('assets\level_complete.wav')

# Fonte para texto
font = pygame.font.Font(None, 36)

# Função para exibir a lista de integrantes
def integrantes_screen():
    screen.fill(INICIAL)
    font_integrantes = pygame.font.Font(None, 30)

    # Renderizar título
    title_text = font.render("Integrantes do Grupo", True, WHITE)
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 50))

    # Lista de integrantes
    integrantes = [
        "Clemar Junior de Mattos Piccini",
        "Davi Israel",
        "Guilherme Abel",
        "Leonardo Picolloto",
        "Matheus M. Dutra",
        "Thiago Fideles Andrade"
    ]

    # Exibir cada nome
    for i, integrante in enumerate(integrantes):
        integrante_text = font_integrantes.render(integrante, True, WHITE)
        screen.blit(integrante_text, (SCREEN_WIDTH // 2 - integrante_text.get_width() // 2, 120 + i * 40))

    # Botão para voltar à tela inicial
    back_button_text = font.render("VOLTAR", True, RED)
    back_button_rect = back_button_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))
    pygame.draw.rect(screen, BLACK, (back_button_rect.x - 10, back_button_rect.y - 10, back_button_rect.width + 20, back_button_rect.height + 20), border_radius=10)
    screen.blit(back_button_text, back_button_rect)

    pygame.display.flip()

    # Esperar até o usuário clicar para voltar
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                # Verifica se o botão "VOLTAR" foi clicado
                if back_button_rect.collidepoint(mouse_pos):
                    return True

# Função da tela inicial
def start_screen():
    start = False
    while not start:
        screen.fill(INICIAL)

        # Configurações do fundo arredondado para o logo e nome do jogo
        logo_background_width = int(SCREEN_WIDTH * 0.8)
        logo_background_height = int(SCREEN_HEIGHT * 0.4)
        logo_background_x = (SCREEN_WIDTH - logo_background_width) // 2
        logo_background_y = SCREEN_HEIGHT // 4 - logo_background_height // 2
        
        # Desenhar fundo arredondado para o logo e nome do jogo
        pygame.draw.rect(screen, FUNDO, (logo_background_x, logo_background_y, logo_background_width, logo_background_height), border_radius=20)
        
        # Carregar e redimensionar a logo
        logo = pygame.image.load("assets\logo.png")
        logo = pygame.transform.scale(logo, (int(SCREEN_WIDTH * 0.6), int(SCREEN_HEIGHT * 0.2)))
        screen.blit(logo, (SCREEN_WIDTH // 2 - logo.get_width() // 2, logo_background_y + 20))  # Ajuste de posicionamento para dentro do fundo
        
        # Renderizar o título do jogo e centralizá-lo dentro do fundo
        title_text = font.render("BRICK BREAKER GAME!", True, WHITE)
        screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, logo_background_y + logo.get_height() + 40))

        # Botão de PLAY centralizado com bloco arredondado atrás
        play_button_text = font.render("INICIAR JOGO", True, BLACK)
        play_button_rect = play_button_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 55))
        
        # Desenhar bloco arredondado atrás do botão "INICIAR JOGO"
        pygame.draw.rect(screen, PURPLE, (play_button_rect.x - 20, play_button_rect.y - 10, play_button_rect.width + 40, play_button_rect.height + 20), border_radius=15)
        screen.blit(play_button_text, play_button_rect)

        # Botão de "INTEGRANTES" centralizado abaixo do botão de iniciar jogo
        integrantes_button_text = font.render("INTEGRANTES", True, BLACK)
        integrantes_button_rect = integrantes_button_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 130))
        
        # Desenhar bloco arredondado atrás do botão "INTEGRANTES"
        pygame.draw.rect(screen, ORANGE, (integrantes_button_rect.x - 20, integrantes_button_rect.y - 10, integrantes_button_rect.width + 40, integrantes_button_rect.height + 20), border_radius=15)
        screen.blit(integrantes_button_text, integrantes_button_rect)

        # Botão de Quit no canto inferior direito
        quit_button_text = font.render("QUIT", True, RED)
        quit_button_rect = quit_button_text.get_rect(bottomright=(SCREEN_WIDTH - 10, SCREEN_HEIGHT - 10))
        screen.blit(quit_button_text, quit_button_rect)

        pygame.display.flip()

        # Verificar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                # Verificar se clicou no botão "INICIAR JOGO"
                if play_button_rect.collidepoint(mouse_pos):
                    start = True
                    # vibrator.vibrate(0.5)  # Vibração ao iniciar o jogo

                # Verificar se clicou no botão "INTEGRANTES"
                elif integrantes_button_rect.collidepoint(mouse_pos):
                    if integrantes_screen():
                        continue

                # Verificar se clicou no botão de "QUIT"
                elif quit_button_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    return False

    return True

# Classe da Bola
class Ball:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT - 40
        self.radius = 10
        self.color = YELLOW
        self.speed_x = 0
        self.speed_y = 0
        self.moving = False  # Controle para o movimento da bola

    def move(self):
        if self.moving:
            self.x += self.speed_x
            self.y += self.speed_y

            if self.x - self.radius <= 0 or self.x + self.radius >= SCREEN_WIDTH:
                self.speed_x *= -1

            if self.y - self.radius <= 0:
                self.speed_y *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, BLACK, (self.x, self.y), self.radius + 2)
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def reset_position(self, paddle):
        self.x = paddle.x + paddle.width // 2
        self.y = paddle.y - self.radius - 5
        self.speed_x = 0
        self.speed_y = 0
        self.moving = False

    def launch(self):
        self.speed_x = random.choice([-4, 4])
        self.speed_y = -4
        self.moving = True

# Classe da Raquete
class Paddle:
    def __init__(self, level):
        self.width = max(100 - level * 10, 40)  # Diminui com o nível
        self.height = 10
        self.x = (SCREEN_WIDTH - self.width) // 2
        self.y = SCREEN_HEIGHT - 30
        self.color = BLUE
        self.speed = 7

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < SCREEN_WIDTH - self.width:
            self.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, (self.x - 2, self.y - 2, self.width + 4, self.height + 4))
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

# Classe dos Tijolos
class Brick:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.alive = True

    def draw(self, screen):
        if self.alive:
            pygame.draw.rect(screen, BLACK, (self.rect.x - 2, self.rect.y - 2, self.rect.width + 4, self.rect.height + 4))
            pygame.draw.rect(screen, self.color, self.rect)

# Função para gerar tijolos sem sobreposição
def generate_bricks(level):
    rows = 5 + level  # Aumenta o número de linhas com o nível
    cols = 7
    brick_width = SCREEN_WIDTH // cols - 10
    brick_height = 20
    bricks = []

    for row in range(rows):
        for col in range(cols):
            x = col * (brick_width + 10) + 5
            y = row * (brick_height + 10) + 50
            bricks.append(Brick(x, y, brick_width, brick_height, random.choice([RED, GREEN, BLUE, PURPLE, ORANGE])))

    return bricks

def restart_game():
    """Reinicia o jogo e retorna para a tela inicial"""
    if start_screen():
        main()
    else:
        pygame.quit()

# Função principal do jogo
def main():
    running = True
    clock = pygame.time.Clock()

    # Inicia a partir da tela inicial
    if not start_screen():
        return

    level = 1
    paddle = Paddle(level)
    ball = Ball()
    bricks = generate_bricks(level)
    waiting_for_launch = True  # Controle para aguardar o lançamento da bola

    while running:
        screen.fill(FUNDO)

        # Verificar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN and waiting_for_launch:
                ball.launch()
                waiting_for_launch = False

        # Movimentos
        paddle.move()
        ball.move()

        # Verificar colisão com a raquete
        if (paddle.y < ball.y + ball.radius < paddle.y + paddle.height and
                paddle.x < ball.x < paddle.x + paddle.width):
            ball.speed_y *= -1

        # Verificar colisão com os tijolos
        for brick in bricks:
            if brick.alive and brick.rect.colliderect(ball.x - ball.radius, ball.y - ball.radius, ball.radius * 2, ball.radius * 2):
                ball.speed_y *= -1
                brick.alive = False

        # Verificar se todos os tijolos foram destruídos
        if all(not brick.alive for brick in bricks):
            level += 1
            ball.reset_position(paddle)
            bricks = generate_bricks(level)
            paddle = Paddle(level)
            waiting_for_launch = True
            level_complete_sound.play()  # Toca som de nível completo

          # Verificar se a bola caiu
        if ball.y - ball.radius > SCREEN_HEIGHT:
            # Reiniciar o jogo após a tela inicial
            restart_game()
            return
        
        # Desenhar elementos
        paddle.draw(screen)
        ball.draw(screen)
        for brick in bricks:
            brick.draw(screen)

        # Mostrar o nível atual na tela
        level_text = font.render(f"Level: {level}", True, WHITE)
        screen.blit(level_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
