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


def mermaid_component(name, style=None, key=None):
    component_value = _mermaid_component(source=name, key=key, style=style, default=None)

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
