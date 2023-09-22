# Visual Pathfinder with Pygame

## Introduction

This Python program utilizes the Pygame library to create an interactive visual pathfinder. With this application, you can set up a grid, designate start and end points, and find a path between them. Additionally, you have the option to visualize or hide the path as you see fit.

## Installation

Before running the program, ensure you have the Pygame library installed. You can install it using pip:

```bash
pip install pygame
```

# Usage
Follow these steps to use the Visual Pathfinder:

1. Run the program.
2. Set up your pathfinding scenario on the grid:
    * Left-click to establish the starting point (displayed in blue).
    * Right-click to set the ending point (displayed in red).
    * Middle-click to add or remove obstacles (displayed in purple).
3. To find the path, click the "Start (Space)" button or press the spacebar.
4. For a fresh start, click "Reset (R)" to clear the grid.
5. Toggle the path visualization on or off by clicking "Hide the Path."
6. To save a screenshot of the grid, click "Save as PNG."

#   Code Structure
The code is organized as follows:

* Initialization of Pygame and setting up the display window.
* Functions for drawing grid squares, buttons, and managing user interactions.
* Pathfinding and path visualization functions.
* The main game loop, responsible for event handling and display updates.

You can customize the fonts and colors to match your preferences. Make sure to handle exceptions when attempting to start pathfinding without defining both start and end points to prevent crashes.

# Notes
* Ensure that you have Python and the Pygame library installed on your system.
* Feel free to extend or customize the code to add more features or enhance the user interface according to your requirements.
