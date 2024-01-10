# Mathematical Expression Evaluators Comparator

Version traduite en français disponible [ici](./LISEZMOI.md)

## Description
This project implements and compares various mathematical expression evaluators in Python, created for a project at the High School Computer Club. The aim is to compare the efficiency of various methods (iterative, recursive, and Python's built-in `eval` function) in terms of performance and accuracy.

## Project Structure
- `evaluate_recursive.py`: Contains the recursive implementation of the expression evaluator.
- `evaluate_iterative.py`: Contains the iterative implementation of the expression evaluator.
- `testcases/`: Directory containing test files with mathematical expressions.
- `performances.py`: The main script that runs the evaluators on test cases and compares their performance.

## Operation
The main script (`performances.py`) reads mathematical expressions from files in the `testcases` directory. It then executes each expression through the three evaluators (iterative, recursive, and built-in) and measures the time required for each evaluation. The results and execution times are displayed for comparison.

## Usage
To use this project, follow these steps:
1. Place your test mathematical expressions in separate files in the `testcases` directory.
2. Run the main script with Python:
```bash
python performances.py
```
3. Review the results displayed on the console to compare the performance of the different evaluators.
