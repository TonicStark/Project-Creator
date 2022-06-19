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