# Contributors

- Albert Lee (albert.lee8@ucsf.edu)
- Srinidhi Jayaprakash (srinidhijay10@gmail.com)
- Helen Liu (helenliu583@gmail.com)
- Isabelle Gunawan (gunawanisabelle@gmail.com)
- Michael Gallup
- Loren Hung (kai5107031882@gmail.com)

# Setup Instructions
- Clone Repo from GitHub
- Setup Virtual Environment
- Run Data Pipeline


## Clone Repo from GitHub
Make sure you set up your username and email in git:
```
git config --global user.name "FIRST_NAME LAST_NAME"
git config --global user.email "MY_NAME@example.com"
```

Using command line (terminal), Navigate to where you would like to store the repository locally using the `cd` command, and enter the following command:
```
git clone https://github.com/albemlee/ai4all_nhanes.git
```

Once you have cloned the repo, you can enter it using `cd `.


## Setup Virtual Environment
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

Each time you're done working on the project, you can deactivate the virtual environment by using the `deactivate` command.

We'll now install the Python libraries we need into *env*. A list of the once we need are located in *requirements.txt*, and we'll use that information for the installation:
```
pip install -r requirements.txt --upgrade
```


## Run Data Pipeline
This repository uses [DVC](https://dvc.org/) to manage data pipelines. To run the most up-to-date pipeline into your local repository, run:
```
dvc repro
```
