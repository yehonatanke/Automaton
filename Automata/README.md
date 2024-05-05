
# Automaton Visualizer

Automaton Visualizer is a Python application that allows you to define an automaton and generate its visual representation. It provides a user-friendly interface to input the automaton definition and generates a graphical representation of the automaton using the Graphviz library.

## Features

- Define an automaton by specifying its states, alphabet, start state, final states, and transition function.
- Option to use default automaton values or provide custom input.
- Generate a visual representation of the automaton as a graph.
- Display the generated automaton graph.

## Prerequisites

Before running the application, ensure that you have the following prerequisites installed:

- Python 3.x
- Graphviz (https://graphviz.org/download/)


## Usage

To run the application, execute the following command:

```bash
python main.py
```

You will be prompted to either use default values for the automaton definition or provide custom input.

If you choose to use default values, the application will generate and visualize a predefined automaton.

If you choose to provide custom input, you will be prompted to enter the following information:

- States (comma-separated)
- Alphabet (comma-separated)
- Start state
- Final states (comma-separated)
- Transition function (in the format: `state, input -> next_state`)

After providing the automaton definition, the application will generate and display the visual representation of the automaton.

## Project Structure

```
automaton-visualizer/
├── main.py
├── automaton_definition.py
├── automaton_generator.py
├── automaton_visualizer.py
└── README.md
```

- `main.py`: Entry point of the application.
- `automaton_definition.py`: Contains functions to prompt the user for the automaton definition.
- `automaton_generator.py`: Generates the automaton based on the provided definition.
- `automaton_visualizer.py`: Visualizes the automaton using the Graphviz library.
- `README.md`: This file, containing project information and usage instructions.

## License

This project is licensed under the [MIT License](LICENSE).


