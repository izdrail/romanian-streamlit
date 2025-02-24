
# romanian-streamlit: Romanian spacy nlp building blocks for Streamlit apps

This package contains utilities for visualizing [spaCy](https://spacy.io) models
and building interactive spaCy-powered apps with
[Streamlit](https://streamlit.io). 

It includes various building blocks you can
use in your own Streamlit app, like visualizers for **syntactic dependencies**,
**named entities**, **text classification**, **semantic similarity** via word
vectors, token attributes, and more.

[![Current Release Version](https://img.shields.io/github/release/explosion/spacy-streamlit.svg?style=flat-square&logo=github&include_prereleases)](https://github.com/explosion/spacy-streamlit/releases)
[![pypi Version](https://img.shields.io/pypi/v/spacy-streamlit.svg?style=flat-square&logo=pypi&logoColor=white)](https://pypi.org/project/romanian-streamlit/)

<img width="50%" align="right" src="https://user-images.githubusercontent.com/13643239/85388081-f2da8700-b545-11ea-9bd4-e303d3c5763c.png">

## 🚀 Quickstart

You can install `romanian-streamlit` from pip:

```bash
pip install romanian-streamlit
```

The package includes **building blocks** that call into Streamlit and set up all
the required elements for you. You can either use the individual components
directly and combine them with other elements in your app, or call the
`visualize` function to embed the whole visualizer.

Download the English model from spaCy to get started.

```bash
python -m spacy download ro_core_web_sm
```

Then put the following example code in a file.

```python
# streamlit_app.py
import spacy_streamlit

models = ["en_core_web_sm", "en_core_web_md"]
default_text = "Sundar Pichai is the CEO of Google."
spacy_streamlit.visualize(models, default_text)
```

You can then run your app with `streamlit run streamlit_app.py`. The app should
pop up in your web browser. 😀
