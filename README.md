# Genetic Optimization with GUI and Visualization

## Project Overview

This project implements a genetic algorithm for optimizing continuous functions with a user-friendly graphical interface built using Tkinter. It includes:

- Input screen for function expression and algorithm parameters.
- Live logging of algorithm iterations.
- Real-time plotting of the optimization progress using matplotlib and enhanced with seaborn styles.
- Threaded execution allowing GUI responsiveness during computation.
- Controls to start, force stop the algorithm, and return to the input screen anytime without restarting the app.

---

## Features

- **Function Input:** User can input any mathematical function of x as a string.
- **Algorithm Parameters:** Set population size, number of iterations, mutation rate, deviance, and alpha.
- **Real-time Progress:** Logs iteration results and updates a large progress graph dynamically.
- **Threaded Execution:** Runs genetic algorithm in a separate thread for smooth GUI operations.
- **Force Stop:** Allows aborting the optimization while keeping current results.
- **Return to Input Screen:** Restart parameter input screen anytime for a new experiment.
- **Beautiful UI:** Modern styled buttons, clear layout, and seaborn-enhanced plots.
  
---

## Requirements

- Python 3.8+
- Packages:
  - numpy
  - matplotlib
  - seaborn

Install required packages with:

```
pip install numpy matplotlib seaborn
```

---

## Usage Instructions

1. Run the main Python script.
2. Enter the function expression and parameters on the first input screen.
3. Press "RUN GENETIC ALGORITHM" to start optimization.
4. The next window shows logs, parameter summary, and a large real-time updating progress graph.
5. Use the **START** button to begin optimization.
6. Use **FORCE STOP** button to abort optimization and keep current progress.
7. Use **Return to Input Screen** button to go back and change parameters for a new run.
8. Close any window to exit the application.

---

## Code Structure Outline

- `show_input_window()`: Displays the input screen for parameters.
- Genetic algorithm functions: selection, crossover, mutation, elitism, fitness evaluation.
- Main window with logs, status, and matplotlib graph embedded in tkinter.
- Threading implementation for running the genetic algorithm concurrently.
- GUI controls with style and user interaction management.

---

## Notes

- The algorithm uses Python `eval()` for function evaluation; be cautious with untrusted input.
- The application is single-user desktop focused.
- GUI styling uses Tkinter widgets customized with colors/fonts and hover effects.
- Seaborn styling improves matplotlib plot appearance.

---

## Screenshots

Screenshots can be found in the repository or run the app to experience the modern GUI and live plotting.

---

## License

[Specify license if needed]

---

For any questions or issues, please open an issue or contact the author.

---

This project is ideal for learning genetic algorithms with practical visualization and GUI interaction.
