# CodeOrbit Tech — Python Programming Internship Tasks

This repository contains four beginner-friendly Python projects for the internship task list.

## Projects

1. **Simple Calculator** (`task1_simple_calculator.py`)
   - Addition, subtraction, multiplication, and division
   - Handles invalid numeric input, invalid operators, and division by zero

2. **To-Do List CLI App** (`task2_todo_list_cli.py`)
   - Add, view, and remove tasks
   - Saves tasks in `tasks.txt` and loads them on the next run

3. **Number Guessing Game** (`task3_number_guessing_game.py`)
   - Random number from 1 to 100
   - Gives “too high” / “too low” hints
   - Tracks attempts and supports multiple rounds

4. **File Handling Mini Project — Contacts Manager** (`task4_file_handling_contacts.py`)
   - Adds, views, and searches contact records
   - Stores data in `contacts.csv`
   - Handles missing files and basic file errors

## Technologies Used

- Python 3
- Python standard library: `random`, `csv`, and `pathlib`
- Text and CSV file handling

## Requirements

Install Python 3. No third-party packages are required.

Check the installation:

```bash
python --version
```

On some systems, use:

```bash
python3 --version
```

## How to Run

Open a terminal in this folder and run one project at a time:

```bash
python task1_simple_calculator.py
python task2_todo_list_cli.py
python task3_number_guessing_game.py
python task4_file_handling_contacts.py
```

If your computer uses `python3`, replace `python` with `python3`.

## Sample Input / Output

### Calculator

```text
Enter the first number: 10
Enter an operation (+, -, *, /): +
Enter the second number: 5
Result: 15
```

### Number Guessing Game

```text
I'm thinking of a number from 1 to 100.
Your guess: 40
Too low! Try again.
```

(The secret number is random, so the exact output varies.)

### Contacts Manager

```text
Choose an option (1-4): 1
Name: Ravi
Phone: 9876543210
Email: ravi@example.com
Contact saved.
```

Use fictional/sample contact details while testing.

## GitHub Submission Checklist

- [ ] Run and test each Python script on your computer.
- [ ] Understand the code and be ready to explain it.
- [ ] Upload all four `.py` files and this `README.md` to your GitHub repository.
- [ ] Record a 2–5 minute demo showing at least one completed project.
- [ ] Publish a LinkedIn post with `#CodeOrbitTech` and `#Internship`.
- [ ] Submit your GitHub repository link and LinkedIn post link using the official submission form.

**Important:** Confirm the minimum task count and submission instructions with the internship team. Keep your own copies of your work.
