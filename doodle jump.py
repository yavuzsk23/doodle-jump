import pygame
import random

# --- SETTINGS ---
WIDTH = 400
HEIGHT = 600
FPS = 60
GRAVITY = 0.35
JUMP_STRENGTH = -10
PLATFORM_COUNT = 10

# --- Platform spacing 
MIN_PLATFORM_GAP = 40
MAX_PLATFORM_GAP = 110

# Colors
BACKGROUND = (248, 248, 216)  # Paper-like color
PLAYER_COLOR = (161, 204, 59)
PLATFORM_COLOR = (60, 179, 113)
TEXT_COLOR = (50, 50, 50)


class Player:
    def __init__(self):
        self.width = 30
        self.height = 30
        self.x = WIDTH // 2
        self.y = HEIGHT - 100
        self.vel_y = 0
        self.vel_x = 7

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.vel_x
        if keys[pygame.K_RIGHT]:
            self.x += self.vel_x

        # Wrap around screen (teleport)
        if self.x > WIDTH:
            self.x = -self.width
        elif self.x < -self.width:
            self.x = WIDTH

        # Gravity and vertical movement
        self.vel_y += GRAVITY
        self.y += self.vel_y

    def draw(self, screen):
        pygame.draw.rect(screen, PLAYER_COLOR, [self.x, self.y, self.width, self.height], 0, 5)
        # Eyes
        pygame.draw.circle(screen, (0, 0, 0), (int(self.x + 10), int(self.y + 10)), 3)
        pygame.draw.circle(screen, (0, 0, 0), (int(self.x + 20), int(self.y + 10)), 3)


class Platform:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 60
        self.height = 12

    def draw(self, screen):
        pygame.draw.rect(screen, PLATFORM_COLOR, [self.x, self.y, self.width, self.height], 0, 3)


def create_initial_platforms():
    """
    Creates the starting platforms from top to bottom with controlled gaps,
    ensuring the player can always reach them (not random/independent).
    """
    platforms = [Platform(WIDTH // 2 - 30, HEIGHT - 50)]
    current_y = HEIGHT - 50
    for _ in range(PLATFORM_COUNT):
        current_y -= random.randint(MIN_PLATFORM_GAP, MAX_PLATFORM_GAP)
        platforms.append(Platform(random.randint(0, WIDTH - 60), current_y))
    return platforms


def spawn_platform_above(platforms):
    """Generates a new platform above the current top one, within reachable distance."""
    top_y = min(p.y for p in platforms)
    new_y = top_y - random.randint(MIN_PLATFORM_GAP, MAX_PLATFORM_GAP)
    return Platform(random.randint(0, WIDTH - 60), new_y)


def main_loop():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Doodle Jump")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 24, bold=True)

    player = Player()
    platforms = create_initial_platforms()

    score = 0
    high_score = 0
    game_over = False

    while True:
        screen.fill(BACKGROUND)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_over:
                    # Reset (high_score is preserved, only game state resets)
                    player = Player()
                    platforms = create_initial_platforms()
                    score = 0
                    game_over = False

        if not game_over:
            player.move()

            # Platform collision (only when falling down)
            if player.vel_y > 0:
                for p in platforms:
                    if (player.x + player.width > p.x and
                            player.x < p.x + p.width and
                            player.y + player.height > p.y and
                            player.y + player.height < p.y + p.height + player.vel_y):
                        player.vel_y = JUMP_STRENGTH
                        break

            # Screen scrolling
            if player.y < 200:
                scroll_amount = abs(player.vel_y)
                player.y += scroll_amount
                score += int(scroll_amount // 10)
                for p in platforms:
                    p.y += scroll_amount

            
                # collect platforms to remove separately first.
                platforms_to_remove = [p for p in platforms if p.y > HEIGHT]
                for p in platforms_to_remove:
                    platforms.remove(p)
                    platforms.append(spawn_platform_above(platforms))

            # Death check
            if player.y > HEIGHT:
                game_over = True
                if score > high_score:
                    high_score = score

        # Draw everything
        for p in platforms:
            p.draw(screen)
        player.draw(screen)

        # UI
        score_text = font.render(f"SCORE: {score}", True, TEXT_COLOR)
        high_score_text = font.render(f"BEST: {high_score}", True, TEXT_COLOR)
        screen.blit(score_text, (10, 10))
        screen.blit(high_score_text, (10, 38))

        if game_over:
            over_text = font.render("GAME OVER!", True, (200, 0, 0))
            retry_text = font.render("Retry: SPACE", True, TEXT_COLOR)
            screen.blit(over_text, (WIDTH // 2 - 70, HEIGHT // 2 - 20))
            screen.blit(retry_text, (WIDTH // 2 - 80, HEIGHT // 2 + 20))

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main_loop()
