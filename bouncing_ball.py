import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Bouncing Ball')

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BALL_COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Ball properties
ball_radius = 20
ball_x = random.randint(ball_radius, screen_width - ball_radius)
ball_y = random.randint(ball_radius, screen_height - ball_radius)
ball_speed_x = random.choice([-5, 5])
ball_speed_y = random.choice([-5, 5])

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Change direction and speed on mouse click
            ball_speed_x = random.choice([-10, -7, -5, 5, 7, 10])
            ball_speed_y = random.choice([-10, -7, -5, 5, 7, 10])

    # Update ball position
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball bouncing logic
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= screen_width:
        ball_speed_x = -ball_speed_x
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= screen_height:
        ball_speed_y = -ball_speed_y

    # Drawing
    screen.fill(BLACK)  # Fill the screen with black
    pygame.draw.circle(screen, BALL_COLOR, (ball_x, ball_y), ball_radius)  # Draw the ball

    pygame.display.flip()  # Update the screen
    clock.tick(60)  # Frame rate (60 FPS)

# Quit Pygame
pygame.quit()
