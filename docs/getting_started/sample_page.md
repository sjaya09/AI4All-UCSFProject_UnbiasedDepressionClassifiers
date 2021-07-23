---
layout: default
title: Sample Page
parent: Getting Started
nav_order: 2
description: "Sample Page"
has_children: false
permalink: /getting_started/sample_page/
has_toc: false
---

# Setup Environment
Next, you'll need to setup a virtual environment. In command line, we'll create a new virtual environment called *env*:
```
pip install --upgrade pip
pip install virtualenv
python -m venv env
```

Now you should see a directory called *env* in your project directory, and now we can activate the environment:
```
. env/bin/activate
```

Each time you're done working on the project, you can deactivate the virtual environment by using the `deaactivate` command.

We'll now install the Python libraries we need into *env*. A list of the once we need are located in *requirements.txt*, and we'll use that information for the installation:
```
pip install -r requirements.txt --upgrade
```


![](images/brain.jpg)
[link to image](https://pixabay.com/illustrations/brain-mind-psychology-idea-drawing-2062057/)
