from properties import Properties
from config import *
import pygame

def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Physics Simulator")
    font = pygame.font.SysFont(None, 30)
    fps = 120

    circle = Properties(GROUND, X, Y, MASS, ACCELERATION, VELOCITY, DELTA_TIME, APPLY_FORCE, GROUND_ABSORPTION, WIND_RESISTANCE)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                circle.apply_upward_force()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                circle.apply_downward_force()

        circle.advance()

        win.fill((219, 252, 255))
        pygame.draw.circle(win, (255, 100, 100), (int(circle.x), int(circle.y)), 50)
        pygame.draw.line(win, (100, 100, 100), (0, GROUND + 50), (WIDTH, GROUND + 50), 10)

        altitude = font.render(f"Altitude: {round(abs(circle.y - GROUND))} px", True, (255, 255, 255), (0, 0, 0))
        win.blit(altitude, (10, 10))

        vel_text = font.render(f"Velocity: {round(abs(circle.velocity))} px/s", True, (255, 255, 255), (0, 0, 0))
        win.blit(vel_text, (10, 35))

        pygame.display.flip()
        pygame.time.Clock().tick(fps)

    pygame.quit()

if __name__ == "__main__":
    main()