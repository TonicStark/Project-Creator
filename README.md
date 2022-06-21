# Project Creator
Project Creator is a free CLI, for automatically creating Projects. It creates the local one and then connects it to the before-created Github Remote Repo

## Set Up
Download the ZIP Folder, or Clone the Repository with:
```
git clone https://github.com/TonicStark/Project-Creator.git
```

Then install the dependencies in a virtualenv, you can create one via `python -m venv <name of the virtualenv>`, with:
```
pip install -r requirements.txt
```

## Personalization
### Projects Path
You have to specify, which is the path on your machine, where you _usually_ store all your projects:
```python
PROJECTS_PATH = "D:\\GitHub"
```
### Environment Variables
In the `.env` file, there are 2 variables: USERNAME and TOKEN. In the username, you have to insert your Github Username; in the Token your Github Acces Token.

For creating a Token, [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) is the Official Github Docs.

**Note**: Set **No Expiration** for better User Experience, use it **ONLY** for this automation, and give **ONLY the simplest privileges**: only for **creating** and **updating** repository.

# Start the Script
Now that you have configured all the options, try this thing out. If you have VS Code, it will also automatically open the editor in the JIT-created Project Folder! **Happy Automation!**