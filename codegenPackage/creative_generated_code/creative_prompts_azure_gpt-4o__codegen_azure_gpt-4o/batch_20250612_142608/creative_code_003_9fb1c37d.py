"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarket.gitbook.io
Prompt: Create a step-by-step guide in code to automate the creation of a GitBook site using the Polymarket starter template and its "Getting Started" features.
Generated: DETERMINISTIC_9fb1c37d41c0f9f0
Batch ID: 20250612_142608
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:4000": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/Polymarket/gitbook-starter-template.git": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import sys

# Function to run shell commands and handle errors
def run_command(command, cwd=None):
    try:
        # Run the command
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error while running command: {command}")
        print(e.stderr)
        sys.exit(1)

# Step 1: Check if Node.js and Git are installed
def check_prerequisites():
    print("Checking prerequisites...")
    run_command("node -v")  # Check Node.js version
    run_command("npm -v")   # Check npm version
    run_command("git --version")  # Check Git version
    print("All prerequisites are met.")

# Step 2: Clone the Polymarket starter GitBook template
def clone_template():
    print("Cloning Polymarket GitBook starter template...")
    run_command("git clone https://github.com/Polymarket/gitbook-starter-template.git")
    print("Template cloned successfully.")

# Step 3: Navigate into the project directory
def navigate_to_project_directory():
    project_dir = "gitbook-starter-template"
    if not os.path.exists(project_dir):
        print(f"Error: Directory '{project_dir}' does not exist.")
        sys.exit(1)
    os.chdir(project_dir)
    print(f"Navigated to project directory: {project_dir}")

# Step 4: Install dependencies
def install_dependencies():
    print("Installing dependencies using npm...")
    run_command("npm install")
    print("Dependencies installed successfully.")

# Step 5: Start the GitBook
def start_gitbook():
    print("Starting GitBook development server...")
    run_command("npm start")
    print("GitBook server is running. Visit http://localhost:4000 in your browser.")

# Main function to orchestrate the steps
def main():
    print("Automating the creation of a GitBook site using the Polymarket starter template...")
    check_prerequisites()
    clone_template()
    navigate_to_project_directory()
    install_dependencies()
    start_gitbook()
    print("GitBook setup completed successfully.")

if __name__ == "__main__":
    main()
```
