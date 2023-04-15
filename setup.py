import setuptools

setuptools.setup(
    name="streamlit-mermaid-component",
    version="0.0.5",
    author="Alexandre da Silva",
    author_email="phytter@hotmail.com",
    description="A component that implements mermaid",
    long_description="",
    long_description_content_type="text/plain",
    url="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
)
