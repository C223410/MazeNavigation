import pygame

class MazeVisualizer:
    def __init__(self, maze, cell_size=30):
        self.maze = maze
        self.cell_size = cell_size
        self.width = maze.width * cell_size
        self.height = maze.height * cell_size
        
        # Initialize Pygame
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Maze Solving AI")
        
        # Colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        
    def draw(self, agent):
        self.screen.fill(self.WHITE)
        
        # Draw maze
        for y in range(self.maze.height):
            for x in range(self.maze.width):
                rect = pygame.Rect(
                    x * self.cell_size,
                    y * self.cell_size,
                    self.cell_size,
                    self.cell_size
                )
                
                if self.maze.maze[y, x] == 1:  # Wall
                    pygame.draw.rect(self.screen, self.BLACK, rect)
                else:  # Path
                    pygame.draw.rect(self.screen, self.WHITE, rect)
                    pygame.draw.rect(self.screen, self.BLACK, rect, 1)
        
        # Draw start and goal
        start_rect = pygame.Rect(
            self.maze.start[0] * self.cell_size,
            self.maze.start[1] * self.cell_size,
            self.cell_size,
            self.cell_size
        )
        pygame.draw.rect(self.screen, self.GREEN, start_rect)
        
        goal_rect = pygame.Rect(
            self.maze.goal[0] * self.cell_size,
            self.maze.goal[1] * self.cell_size,
            self.cell_size,
            self.cell_size
        )
        pygame.draw.rect(self.screen, self.RED, goal_rect)
        
        # Draw agent
        agent_rect = pygame.Rect(
            agent.position[0] * self.cell_size,
            agent.position[1] * self.cell_size,
            self.cell_size,
            self.cell_size
        )
        pygame.draw.rect(self.screen, self.BLUE, agent_rect)
        
        pygame.display.flip()
        
    def quit(self):
        pygame.quit() 