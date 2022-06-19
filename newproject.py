# Importing Libraries
from rich.console import Console
from github import Github
from dotenv import load_dotenv
import sys
import os

# Initialization
# Loading the ENV Variables
load_dotenv()

# Creating a Global Console Object
CONSOLE = Console()

# Method for Taking Project Name


def get_project_name() -> str:

    # Creating a Scoped Project Name variable
    PRJ_NAME = ""

    # Trying to take the Project Name from the Command Line
    try:

        # Saving the Project Name
        PRJ_NAME = sys.argv[1]

    # If the Command ARgument isn't given, trhow an Error
    except IndexError:

        # Print an Error Message
        CONSOLE.print("❌ [red]Error:[reset] No Project Name Given!")

        # Exit the Program
        sys.exit(1)

    # Return the Project Name
    return PRJ_NAME


# Saving some Informations
USERNAME = os.getenv("USERNAME")
PROJECTS_PATH = "D:\\GitHub"

# Method for Creating the Github Repository


def create_github_repo(prj_name: str) -> str:

    # Adding Animations
    with CONSOLE.status("🔧 [green]Creating the Remote Repo...[reset]"):

        # Trying to Operate
        try:

            # Access Token
            ACCESS_TOKEN = os.getenv("TOKEN")

            # Loging into Github
            USER = Github(ACCESS_TOKEN).get_user()

            # Modifing the Project Name
            N_PRJ_NAME = prj_name.replace(" ", "-")

            # Creating the Remote Repository
            USER.create_repo(N_PRJ_NAME)

        except Exception:

            # Print an Error Message
            CONSOLE.print(
                "❌ [red]Error:[reset] Couldn't Create the Remote Repository!")

            # Exit the Program
            sys.exit(1)

    # Success Message
    CONSOLE.print("✅ [green]Success:[reset] Remote Repo Created!")

    # Returning the Repo Remote URL
    return f"https://github.com/{USERNAME}/{N_PRJ_NAME}.git"

# Method for Creating the Project Folder


def create_local_project(prj_name: str, remote_link: str) -> None:

    # Adding Animations
    with CONSOLE.status("🔧 [green]Creating the Local Project..[reset]"):

        # Creating the Project's Folder
        PROJECT_PATH = f"{PROJECTS_PATH}\\{prj_name}"
        os.mkdir(PROJECT_PATH)

        # Changing the Working Directory to the Project's Folder
        os.chdir(PROJECT_PATH)

        # Creating the README.md File
        with open(f"{PROJECT_PATH}\\README.md", "w") as f:

            # Writing the Content
            f.write(f"# {prj_name}")

    # Creating a Commands List to Perform
    COMMANDS = ["git init .",
                "git branch -M main",
                f"git remote add origin {remote_link}",
                "git add README.md",
                'git commit -m "Initial Commit"',
                "git push -u origin main"]

    # Executing the Commands
    for COMMAND in COMMANDS:

        os.system(COMMAND)

    # Success Message
    CONSOLE.print(
        "✅ [green]Success:[reset] Local Project Created and Connected to the Remote Repo!")
    CONSOLE.print("🔥 [green]You are Ready to Go![reset]")

    # Opening the Project in VS Code
    os.system(f"code {PROJECT_PATH}")


# Main Program
if __name__ == "__main__":

    # Getting the Project Name
    PRJ_NAME = get_project_name()

    # Creating the Remote Repository
    REMOTE_LINK = create_github_repo(PRJ_NAME)

    # Creating the Local Project
    create_local_project(PRJ_NAME, REMOTE_LINK)
