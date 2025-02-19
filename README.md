# Pac Man Game

A Python implementation of the classic **Pac Man** arcade game. This project recreates the timeless maze chase experience, featuring Pac Man, ghosts (like Pinky), pellets (dots), and maze walls. It is designed to be both fun and educational, showcasing game logic, basic AI, and graphical programming.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Game Mechanics](#game-mechanics)

---

## Overview

In this Pac Man project:
- **Pac Man** is controlled by the player using keyboard input.
- **Maze** and **dots** define the playing field. Pac Man eats the dots, and when all dots are eaten, the player wins.
- **Ghost** (Pinky) use basic AI to chase Pac Man.
- A **Game Controller** maintains the overall game state, determining when Pac Man wins or when Pinky catches Pac Man.

The project is built using Python and a graphical library (Processing.py). The code is organized into several modules that handle game control, maze drawing, character movement, ghost AI, and interactions with dots.

---

## Features

- **Classic Gameplay:** Navigate Pac Man through a maze, eating dots while avoiding ghosts.
- **Ghost AI:** Ghosts like Pinky chase Pac Man using simple decision-making logic.
- **Maze & Dots:** The maze is drawn with walls and includes dots that Pac Man can eat.
- **Win Conditions:** The game tracks wins—if Pac Man eats all the dots, the player wins; if a ghost catches Pac Man, the ghost wins.
- **Modular Design:** Organized code into modules for easier maintenance and extension.

---

## Project Structure

- **pac_man.py:**  
  The main entry point for the game. Initializes the game window, loads assets, and starts the game loop.

- **game_controller.py:**  
  Contains the `GameController` class, which maintains the state of the game (e.g., determining win conditions and updating game status).

- **maze.py:**  
  Contains the `Maze` class that draws the maze walls, displays the dots (pellets), and handles the interaction between Pac Man and the dots.

- **dots.py:**  
  Manages the dot objects in the maze (not shown in detail here, but referenced by the Maze).

- **pacman.py:**  
  Contains the `Pacman` class that extends a base `GameCharacter` class. It handles Pac Man's appearance, movement, mouth animation, and dot-eating behavior.

- **pinky.py:**  
  Contains the `Pinky` class (a ghost) that extends `GameCharacter`. It includes logic for chasing Pac Man and determining when Pinky catches Pac Man.

- **game_character.py:**  
  A base class that may include shared properties or methods for game characters like Pac Man and Pinky.

- **eyes.py:**  
  Handles the drawing of eyes for the Pinky to indicate where they are looking.

---

## Usage

1. **Launch the Game:**
   - Open the main file (e.g., `pac_man.py`) in your Python environment or compatible IDE.
   - If you are using Processing.py, open the corresponding `.pyde` file in Processing and run the sketch.

2. **Controls:**
   - Use the keyboard arrow keys to control Pac Man's movement.
   - Navigate through the maze to eat all the dots while avoiding ghosts like Pinky.

3. **Win/Lose Conditions:**
   - **Player Wins:** When all dots are eaten, the game displays a "YOU WIN!!!" message.
   - **Ghost Wins:** If a ghost (e.g., Pinky) gets too close to Pac Man, the game displays a "PINKY WINS" message.

---

## Game Mechanics

- **GameController:**  
  Manages the overall state of the game. It updates the game status, and if either Pac Man wins by eating all dots or a ghost wins by catching Pac Man, it displays the corresponding message.

- **Maze & Dots:**  
  The `Maze` class is responsible for drawing the maze walls and displaying the dots. It also checks for dot collisions with Pac Man. When Pac Man passes over a dot, it is "eaten" and removed from the maze.

- **Pacman:**  
  The `Pacman` class handles drawing Pac Man, updating his position based on keyboard input, animating his mouth, and calling the `eat_dots` method from the Maze when he moves.

- **Pinky (Ghost):**  
  The `Pinky` class uses simple AI to determine its movement direction at intersections in the maze. It updates its position to chase Pac Man and checks for collision with Pac Man to declare a win for the ghost.

