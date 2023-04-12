# streamlit-mermaid-component

## Steps to start development:


Open a new terminal and navigate to the mermaid_component/frontend directory and install the dependencies

```
npm install
```

Start the application

```
npm start
```

Open a new terminal in root project folder

Setup a virtual python environment

install the streamlit 
```
pip install streamlit
```
start server

```
streamlit run mermaid_component/__init__.py
```
[Streamlit reference](https://docs.streamlit.io/library/components/components-api#create-a-bi-directional-component)

---

## Steps to build and publish:


Build react project

```
cd mermaid_component/frontend
npm run build
```

build a python wheel

```
python setup.py sdist bdist_wheel
```

publish to PyPi
```
python3 -m twine upload --repository testpypi dist/*
```

install this package on other project

```
python -m pip install --index-url https://test.pypi.org/simple/ --no-deps streamlit-mermaid-component
```

[Streamlit reference](https://docs.streamlit.io/library/components/publish)