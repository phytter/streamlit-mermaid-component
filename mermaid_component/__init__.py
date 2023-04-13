import os
import streamlit.components.v1 as components

_RELEASE = True

if not _RELEASE:
    _mermaid_component = components.declare_component(
        "mermaid_component",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _mermaid_component = components.declare_component("mermaid_component", path=build_dir)


def mermaid_component(source: str ='', style: dict=None, key: str | int=None):
    """
        Function Description:
            The `mermaid_component` function takes in three parameters: 
            1. `source`: A string which represents the Mermaid graph code.
            2. `style`: Optional parameter of type dictionary which represents the styles to be applied on the graph.
            3. `key`: Optional parameter of type string which represents a unique key for the component.

            The function then calls the `_mermaid_component` function with the provided parameters, and assigns the result
            to the `component_value` variable. Finally, it returns the value of `component_value`.

        Parameters:
            source : str
                A string that represents the Mermaid graph code.

            style : dict, optional
                A dictionary representing the styles to be applied on the graph.

            key : str, optional
                An optional parameter representing a unique key for the component.

        Returns:
            Any
                The result of the `_mermaid_component` function call. This could be a HTML string or None.
    """
    component_value = _mermaid_component(source=source, key=key, style=style, default=None)

    return component_value


if not _RELEASE:
    import streamlit as st

    st.subheader("Mermeid development!!")

    mermaid_component("""
        graph TD 
            A[Client] --> B[Load Balancer] 
            B --> C[Server01] 
            B --> D[Server02]
    """, key='1')

    mermaid_component("""
        graph TD 
            A[Client] --> B[Load Balancer] 
            B --> C[Server01] 
            B --> D[Server02]
    """, key='2')

    st.markdown("---")
