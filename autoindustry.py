import pygame
import sys
from industries import auto_industry, auto_indautomate, auto_indhuman

# Initialize Pygame
pygame.init()

# Define colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Set up the display
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Job Simulation')

# Convert percentage values to float
auto_indautomate_values = [float(value) for value in auto_indautomate]
auto_indhuman_values = [float(value) for value in auto_indhuman]

# Abbreviations for industries
industry_abbreviations = ["EM", "WA", "DRV", "SLS", "CNS"]

# Calculate initial positions for automation and human dots
dot_spacing = 50
middle_vertical = height // 2 - dot_spacing * (len(auto_industry) - 1) / 2

# Calculate time to reach target percentage
max_time = 100  # Set the maximum time for dots to reach the side
human_times = [percent * max_time / 100 for percent in auto_indhuman_values]
auto_times = [percent * max_time / 100 for percent in auto_indautomate_values]

human_dots = [{'color': BLUE, 'position': (width // 2, middle_vertical + i * dot_spacing), 'speed': 1 / human_times[i], 'label': industry_abbreviations[i]} for i in range(len(auto_industry))]
auto_dots = [{'color': RED, 'position': (width // 2, middle_vertical + i * dot_spacing), 'speed': -1 / auto_times[i], 'label': industry_abbreviations[i]} for i in range(len(auto_industry))]

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update job dots based on time
    for dot in human_dots + auto_dots:
        # Update position based on speed (move horizontally)
        dot['position'] = (dot['position'][0] + dot['speed'], dot['position'][1])

        # Stop at the target_x position (percentage)
        if (dot['speed'] > 0 and dot['position'][0] >= width // 2 + max_time) or (dot['speed'] < 0 and dot['position'][0] <= width // 2 - max_time):
            dot['position'] = (width // 2 + max_time * dot['speed'], dot['position'][1])

    # Draw the environment
    screen.fill((255, 255, 255))  # White background

    # Draw job dots with labels
    for dot in human_dots + auto_dots:
        pygame.draw.circle(screen, dot['color'], (int(dot['position'][0]), int(dot['position'][1])), 5)  # Small dots
        font = pygame.font.Font(None, 20)
        text = font.render(dot['label'], True, (0, 0, 0))
        screen.blit(text, (dot['position'][0] + 10, dot['position'][1]))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)  # 60 frames per second
