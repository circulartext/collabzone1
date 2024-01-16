import pygame
import sys
import colorsys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Job Simulation')

# Define colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Define job dots
job_dots = [{'color': BLUE, 'position': (50, 200), 'speed': 2, 'color_transition': 0.0}]  # Example: Blue dot at (50, 200) with speed 2

# Define arena sides
left_side = pygame.Rect(0, 0, width // 2, height)
right_side = pygame.Rect(width // 2, 0, width // 2, height)

# Font setup
font = pygame.font.SysFont(None, 30)

# Main game loop
clock = pygame.time.Clock()
current_year = 1

while current_year <= 5:  # Simulation for 5 years
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update job dots based on time
    for dot in job_dots:
        dot['position'] = (dot['position'][0] + dot['speed'], dot['position'][1])

        # Change color after a certain time
        if pygame.time.get_ticks() % 2000 == 0:  # Change color every 2 seconds (adjust as needed)
            dot['color_transition'] += 0.2  # Increase this value for faster color transition
            dot['color_transition'] = min(1.0, dot['color_transition'])  # Clamp to 1.0
            dot['color'] = [int(c * 255) for c in colorsys.hsv_to_rgb(dot['color_transition'], 1.0, 1.0)]

    # Draw the environment
    screen.fill((255, 255, 255))  # White background

    # Draw arena sides
    pygame.draw.rect(screen, BLACK, left_side)
    pygame.draw.rect(screen, BLACK, right_side)

    # Draw labels
    left_label = font.render('Human Working', True, BLACK)
    right_label = font.render('Automation', True, BLACK)
    screen.blit(left_label, (width // 4 - left_label.get_width() // 2, height - 30))
    screen.blit(right_label, (3 * width // 4 - right_label.get_width() // 2, height - 30))

    # Draw job dots
    for dot in job_dots:
        pygame.draw.circle(screen, dot['color'], (int(dot['position'][0]), int(dot['position'][1])), 5)  # Small dots

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)  # 60 frames per second

    # Increment the year every 2 seconds
    if pygame.time.get_ticks() % 2000 == 0:
        current_year += 1
        print(f'Year: {current_year}')

# Wait for a key press before closing the window
pygame.event.wait()
pygame.quit()
sys.exit()
