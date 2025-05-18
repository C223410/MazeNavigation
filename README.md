# Maze Solving AI Agent

This project implements a simple AI agent that can navigate through a maze using various pathfinding algorithms.

## Project Structure
- `maze.py`: Contains the Maze class for creating and managing the maze environment
- `agent.py`: Implements the AI agent with pathfinding capabilities
- `main.py`: Main script to run the maze-solving simulation
- `utils.py`: Utility functions for visualization and helper methods

## Setup
1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Project
```bash
python main.py
```

## Features
- Random maze generation
- A* pathfinding algorithm
- Visual representation using Pygame
- Configurable maze size and complexity 