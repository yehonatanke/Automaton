class Automaton:
    def __init__(self, states, alphabet, start_state, final_states, transition_function):
        self.states = states
        self.alphabet = alphabet
        self.start_state = start_state
        self.final_states = final_states
        self.transition_function = transition_function


def generate_automaton(automaton_definition):
    """
    Generate the automaton based on the provided definition.
    Return the automaton as a suitable data structure.
    """
    states = automaton_definition["states"]
    alphabet = automaton_definition["alphabet"]
    start_state = automaton_definition["start_state"]
    final_states = automaton_definition["final_states"]
    transition_function = automaton_definition["transition_function"]

    return Automaton(states, alphabet, start_state, final_states, transition_function)
