import pygame
import time
from maze import Maze
from agent import Agent
from utils import MazeVisualizer

def main():
    # Initialize maze
    maze_width = 15
    maze_height = 15
    maze = Maze(maze_width, maze_height)
    
    # Initialize agent
    agent = Agent(maze)
    
    # Initialize visualizer
    visualizer = MazeVisualizer(maze)
    
    # Find path
    path = agent.find_path()
    if not path:
        print("No path found!")
        return
    
    # Main game loop
    running = True
    clock = pygame.time.Clock()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Move agent
        if not agent.move():
            time.sleep(1)  # Pause at the end
            running = False
        
        # Update display
        visualizer.draw(agent)
        clock.tick(5)  # Control animation speed
    
    visualizer.quit()

if __name__ == "__main__":
    main() 