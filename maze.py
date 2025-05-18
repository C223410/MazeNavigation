import numpy as np
import random

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = np.ones((height, width), dtype=int)  # 1 represents walls
        self.generate_maze()

    def generate_maze(self):
        # Start with all walls
        # Create a maze using recursive backtracking
        start_x, start_y = 1, 1
        self.maze[start_y, start_x] = 0
        stack = [(start_x, start_y)]
        
        while stack:
            current_x, current_y = stack[-1]
            # Get all adjacent cells
            directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
            random.shuffle(directions)
            
            found_path = False
            for dx, dy in directions:
                new_x, new_y = current_x + dx, current_y + dy
                
                if (0 <= new_x < self.width and 
                    0 <= new_y < self.height and 
                    self.maze[new_y, new_x] == 1):
                    
                    # Create a path by removing walls
                    self.maze[new_y, new_x] = 0
                    self.maze[current_y + dy//2, current_x + dx//2] = 0
                    
                    stack.append((new_x, new_y))
                    found_path = True
                    break
            
            if not found_path:
                stack.pop()

        # Set start and goal positions
        self.start = (1, 1)
        self.goal = (self.width - 2, self.height - 2)
        self.maze[self.start[1], self.start[0]] = 0
        self.maze[self.goal[1], self.goal[0]] = 0

    def is_valid_move(self, x, y):
        return (0 <= x < self.width and 
                0 <= y < self.height and 
                self.maze[y, x] == 0)

    def get_neighbors(self, x, y):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbors = []
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if self.is_valid_move(new_x, new_y):
                neighbors.append((new_x, new_y))
        
        return neighbors 