# 1330GP
This is a Python game created by group L2-3 in ENGG1330. The game is consist of 2 parts: ***Klotski*** and ***Maze***. Both of them provides user with different difficulty levels and random events.
## Team members
_Fan Richard Xu_,
_Ding Yitian_,
_Li Shangheng_,
_Ling Kwok Chun_,
_Yang Haotian_
## Game instruction
### KLOTSKI
#### Objective
Move the piece with number “0” on it into the correct positions so that it meet the bottom row of the matrix which shows “==”.

#### Rules
1. Start the Game
The game randomly generates an initial matrix layout.
Your goal is to move the numbers to arrange them correctly.

2. Movement Commands
Input format: “number direction”, e.g., “3 s” means move the piece with number 3 down.
Directions include:
 “w”: move up
“s”: move down
“a”: move left
“d”: move right

3.Input Guidelines
Valid inputs include numbers (0-9) and direction commands (w, s, a, d).
Invalid inputs will prompt an error message and the the program will give player another chance to input again. 	 

4. Help Function
If stuck after 5 moves, type “help”to request assistance.
The system will display the steps to solve the current matrix layout.


### MAZE

#### Objective
Navigate through the maze from the starting point (`S`) to the end point (`E`) and win the game.

#### Game Modes
1. easy: 5x5 maze.
2. medium: 10x10 maze.
3. hard: 20x20 maze.
4. selfdesign: Customize the length and width of the maze.

#### Controls
- Use the keyboard to enter `w`, `a`, `s`, `d` to move your position.
  - `w`: Move up
  - `a`: Move left
  - `s`: Move down
  - `d`: Move right

- After each move, the current state of the maze will be displayed, with your position marked as `C`, the start position marked as `S`, and the end position marked as `E`.
When you reach the end position, the message "You win!" will be displayed, and the game will end.

#### Game Steps
1. Choose a mode: Enter `easy`, `medium`, `hard`, or `selfdesign` to select the maze difficulty.
2. Generate the maze: The program will generate a random maze and display the initial state.
3. Start moving: Follow the prompts and enter `w`, `a`, `s`, `d` to navigate through the maze.
4. Win the game: Reach the end position to win the game.

