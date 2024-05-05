def get_automaton_definition():
    """
    Prompt the user to input the definition of the automaton.
    Return the automaton definition as a dictionary.
    """
    use_default = input("Do you want to use default values? (y/n): ").lower() == "y"

    if use_default:
        states = ["q0", "q1", "q2"]
        alphabet = ["a", "b"]
        start_state = "q0"
        final_states = ["q2"]
        transition_function = {
            ("q0", "a"): "q1",
            ("q1", "a"): "q1",
            ("q1", "b"): "q2",
            ("q2", "a"): "q2",
            ("q2", "b"): "q2"
        }
    else:
        states = input("Enter the states (comma-separated): ").split(",")
        alphabet = input("Enter the alphabet (comma-separated): ").split(",")
        start_state = input("Enter the start state: ")
        final_states = input("Enter the final states (comma-separated): ").split(",")

        transition_function = {}
        print("Enter the transition function (state, input -> next_state):")
        while True:
            transition = input()
            if not transition:
                break
            state, input_symbol, next_state = transition.split("->")
            transition_function[(state.strip(), input_symbol.strip())] = next_state.strip()

    automaton_definition = {
        "states": states,
        "alphabet": alphabet,
        "start_state": start_state,
        "final_states": final_states,
        "transition_function": transition_function
    }

    return automaton_definition
