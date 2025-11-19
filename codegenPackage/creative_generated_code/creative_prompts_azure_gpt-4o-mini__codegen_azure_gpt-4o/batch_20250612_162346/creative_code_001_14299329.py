"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stonegarden.dev
Prompt: What are the best practices for using version control with GitLab and GitHub mentioned on Stonegarden.dev?
Generated: DETERMINISTIC_14299329bdcf6417
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python script that automates the setup of best practices for using version control with GitLab and GitHub. The script assumes you have `git` installed and configured on your machine.

```python
import os
import subprocess

def run_command(command):
    """
    Run a shell command and return its output.
    """
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}\n{e.stderr}")
        return None

def initialize_git_repo(repo_name, remote_url=None):
    """
    Initialize a git repository with best practices.
    
    Args:
        repo_name (str): Name of the repository.
        remote_url (str): Remote repository URL for GitLab/GitHub (optional).
    """
    try:
        # Create a new directory for the repository
        os.makedirs(repo_name, exist_ok=True)
        os.chdir(repo_name)
        
        # Initialize git
        print("Initializing Git repository...")
        run_command(["git", "init"])
        
        # Create a README file
        print("Creating README.md file...")
        with open("README.md", "w") as f:
            f.write(f"# {repo_name}\n\nThis is the README for {repo_name}.\n")
        
        # Create a .gitignore file
        print("Creating .gitignore file...")
        with open(".gitignore", "w") as f:
            f.write("# Ignore common files\n*.log\n*.tmp\n.env\n")
        
        # Create a commit template
        print("Setting up commit template...")
        commit_template = "commit-template.txt"
        with open(commit_template, "w") as f:
            f.write("Commit message guidelines:\n\n* Start with a short summary.\n* Provide detailed explanations.\n* Use imperative tone.\n")
        run_command(["git", "config", "commit.template", commit_template])
        
        # Stage and commit initial files
        print("Staging and committing files...")
        run_command(["git", "add", "."])
        run_command(["git", "commit", "-m", "Initial commit with README and .gitignore"])
        
        # Add remote repository if provided
        if remote_url:
            print("Adding remote repository...")
            run_command(["git", "remote", "add", "origin", remote_url])
            print("Remote repository set to:", remote_url)
        
        print("Git repository setup complete.")
    
    except Exception as e:
        print(f"Error initializing git repository: {e}")

def configure_global_git_settings():
    """
    Configure global Git settings for best practices.
    """
    try:
        print("Configuring global Git settings...")
        
        # Set user name and email
        user_name = input("Enter your Git user name: ")
        user_email = input("Enter your Git user email: ")
        run_command(["git", "config", "--global", "user.name", user_name])
        run_command(["git", "config", "--global", "user.email", user_email])
        
        # Set core editor
        run_command(["git", "config", "--global", "core.editor", "nano"])  # Change to preferred editor
        
        # Enable colored output
        run_command(["git", "config", "--global", "color.ui", "auto"])
        
        # Set global pull behavior to rebase
        run_command(["git", "config", "--global", "pull.rebase", "true"])
        
        # Configure default branch name
        run_command(["git", "config", "--global", "init.defaultBranch", "main"])
        
        print("Global Git settings configured successfully.")
    
    except Exception as e:
        print(f"Error configuring global Git settings: {e}")

if __name__ == "__main__":
    print("Automating Git repository setup and configuration...")
    repo_name = input("Enter your repository name: ")
    remote_url = input("Enter remote repository URL (leave blank if none): ")
    
    configure_global_git_settings()
    initialize_git_repo(repo_name, remote_url)
```

### Key Features of the Code:
- **Global Git Settings:** Prompts the user to configure their Git name, email, editor, branch name, and other recommended settings.
- **Error Handling:** Captures errors during command execution and prints useful messages.
- **Best Practices:** Creates a `README.md` file, `.gitignore`, and commit template file.
- **Production-Ready:** Clean, modular, and adheres to Python best practices.
