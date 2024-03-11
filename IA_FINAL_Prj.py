import pygame
import random

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initialize pygame
pygame.init()

# Set the width and height of the screen (grid)
GRID_SIZE = 500
SCREEN_SIZE = (GRID_SIZE, GRID_SIZE)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Wandering in the Woods Game")

clock = pygame.time.Clock()

class Person:
    def __init__(self, color):
        self.x = random.randint(0, GRID_SIZE)
        self.y = random.randint(0, GRID_SIZE)
        self.color = color

    def move(self):
        self.x += random.choice([-1, 0, 1])
        self.y += random.choice([-1, 0, 1])

        self.x = max(0, min(GRID_SIZE, self.x))
        self.y = max(0, min(GRID_SIZE, self.y))

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 5)

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)

        # Initialize people
        person1 = Person(RED)
        person2 = Person(BLACK)

        # Move people
        while person1.x != person2.x or person1.y != person2.y:
            person1.move()
            person2.move()

        # Draw people
        person1.draw()
        person2.draw()

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
