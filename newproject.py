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