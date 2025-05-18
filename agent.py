from heapq import heappush, heappop
import numpy as np

class Agent:
    def __init__(self, maze):
        self.maze = maze
        self.position = maze.start
        self.path = []
        
    def manhattan_distance(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    
    def find_path(self):
        """Implements A* pathfinding algorithm"""
        start = self.maze.start
        goal = self.maze.goal
        
        # Priority queue for open nodes
        open_set = []
        heappush(open_set, (0, start))
        
        # Dictionary to store path
        came_from = {}
        
        # Cost from start to node
        g_score = {start: 0}
        
        # Estimated total cost from start to goal through node
        f_score = {start: self.manhattan_distance(start, goal)}
        
        while open_set:
            current = heappop(open_set)[1]
            
            if current == goal:
                # Reconstruct path
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                path.reverse()
                self.path = path
                return path
            
            for neighbor in self.maze.get_neighbors(*current):
                tentative_g_score = g_score[current] + 1
                
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.manhattan_distance(neighbor, goal)
                    heappush(open_set, (f_score[neighbor], neighbor))
        
        return None  # No path found
    
    def move(self):
        """Move the agent one step along the path"""
        if self.path and len(self.path) > 1:
            self.position = self.path.pop(0)
            return True
        return False 