# Stack-Based Expression Evaluation

## Overview
This Python program evaluates mathematical expressions from an input text file using a **stack-based approach** and writes the results to an output file.

## Files
- `stack_evaluator.py`: Main program file.
- `input.txt`: Sample input file with expressions.
- `output.txt`: Generated results.
- `README.md`: Instructions on running the program.

## Usage
1. Place all files in the same directory.
2. Run the program in VS Code or terminal:
   ```bash
   python stack_evaluator.py
   ```
3. The evaluated results will appear in `output.txt`.

## Example
**Input (input.txt):**
```
3 + 5 * 2
-----
(8 / 4) + 7 * 2
-----
10 - (2 + 3) * 4
```
3+4*2
---
(3+4)*2
---
10/2
---
8-3+2
---
5*(2+3)
---
10/3
---
2+3*4-6/2
**Output (output.txt):**
```
13
-----
17
-----
-10
```
11
---
14
---
5
---
7
---
25
---
3.33
---
11
