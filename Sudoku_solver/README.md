# SudokuSolver.py

I asked ChatGPT to teach me how to write this program. Most of this was written myself. However, I did ask for hints where I got stuck to try help me solve the . Below is the prompt I used to get started:

```Act as an expert programming teacher. You’re teaching a relative novice. They understand some of the basic concepts of python but also how to approach a problems programmatically. Don’t jump straight to the answer. Only provide one step at a time, allowing the student to ask questions. We are building a program that can solve sudoku puzzles.```

Granted, this is not the most well written prompt, but it did the job.

Here is an example of the output it provided me:

#### **Next Step: Checking if a Move is Valid**

Now, let’s **write a function** that checks whether a given number can be placed at a specific position (row, col) in the Sudoku grid **without breaking the rules.**

**Step 1: Check Row and Column**

- Loop through the entire row to see if the number already exists.
- Loop through the entire column to check the same.

**Step 2: Check the 3x3 Box**

- Each (row, col) belongs to a 3x3 subgrid (e.g., top-left, center, bottom-right, etc.).
- Then, loop through the 3x3 section to check if the number already exists.

## Challenges
- nested range() loops – it took me a while to realise I need to loop through each row and each column separately and looping through range(9) for each 3x3 cube was not going to work. 
- I struggled a lot with the solver function. I was on the right track with my range and for loop, however I missed the part where I needed to store the empty cell in the function `empty = empty_cell(board)`

## Reflections

I thought this was a valuable way to learn how to create programs. Maybe this particular problem was above my skill level. I spent approximately 7 hours working on this challenge, and while I did require some help from ChatGPT, I feel that I have better understanding of range loops in particular but also watching out for missing inputs within a function. I will attempt this challenge again in a few weeks without ChatGPT to see how I go.

For fun, I asked Cursor.AI and Claude 3.5-sonnet to write the same program. I've included that version in this folder. It's a slightly simpler program that combines the empty cell check and solver into one function. My version displays the results in a clearer way.