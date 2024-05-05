import graphviz


def visualize_automaton(automaton):
    """
    Visualize the automaton using Graphviz.
    """
    dot = graphviz.Digraph()
    dot.attr("node", shape="circle")

    # Add nodes
    for state in automaton.states:
        if state == automaton.start_state:
            dot.node(state, label="", root="true")
        elif state in automaton.final_states:
            dot.node(state, label="", shape="doublecircle")
        else:
            dot.node(state)

    # Add edges
    for (state, input_symbol), next_state in automaton.transition_function.items():
        dot.edge(state, next_state, label=input_symbol)

    # Render the graph
    dot.render("automaton", view=True)
