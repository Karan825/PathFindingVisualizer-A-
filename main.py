import pygame
import Helper_func as help
from Helper_func import make_grid
import Constants as c

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Pathfinding Algorithm")

def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)

    start, end = None, None
    run, started = True, False

    while run:
        win.fill(c.BACKGROUND)
        help.draw(win, grid, ROWS, width)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if started:
                continue

            if pygame.mouse.get_pressed()[0]:  # Left Click
                pos = pygame.mouse.get_pos()
                row, col = help.get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]

                if not start and spot != end:
                    start = spot
                    start.make_start()
                elif not end and spot != start:
                    end = spot
                    end.make_end()
                elif spot != start and spot != end:
                    spot.make_barrier()

            elif pygame.mouse.get_pressed()[2]:  # Right Click
                pos = pygame.mouse.get_pos()
                row, col = help.get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()

                if spot == start:
                    start = None
                elif spot == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbours(grid)

                    help.algorithm(lambda: help.draw(win, grid, ROWS, width), grid, start, end)

                if event.key == pygame.K_c:
                    start, end = None, None
                    grid = make_grid(ROWS, width)

    pygame.quit()

if __name__ == "__main__":
    main(WIN, WIDTH)