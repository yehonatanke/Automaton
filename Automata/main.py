from automaton import get_automaton_definition
from automaton_generator import generate_automaton
from automaton_visualizer import visualize_automaton


def main():
    # Get the automaton definition from the user
    automaton_definition = get_automaton_definition()

    # Generate the automaton based on the definition
    automaton = generate_automaton(automaton_definition)

    # Visualize the automaton
    visualize_automaton(automaton)


if __name__ == "__main__":
    main()
