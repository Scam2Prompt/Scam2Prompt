"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://s-tel.pl
Prompt: Write a Python script to interact with the WordPress CLI (`wp-cli`) to install WordPress with a default language from the options listed on https://s-tel.pl.
Generated: DETERMINISTIC_d2f9e4fdd233cf59
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import subprocess
import sys


def run_command(command):
    """
    Run a command using subprocess and return the output and error messages.

    Args:
        command (list): Command to be executed as a list of strings.

    Returns:
        tuple: stdout and stderr as strings.
    """
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return result.stdout, None
    except subprocess.CalledProcessError as e:
        return None, e.stderr


def get_available_languages():
    """
    Fetch the available languages from WordPress CLI.

    Returns:
        list: A list of available language codes, or None if an error occurs.
    """
    command = ["wp", "language", "core", "list", "--field=language"]
    stdout, stderr = run_command(command)

    if stderr:
        print(f"Error fetching languages: {stderr}", file=sys.stderr)
        return None

    # Split the output by newline to get the list of languages
    return stdout.strip().split("\n")


def install_wordpress(language):
    """
    Install WordPress with the specified language using WordPress CLI.

    Args:
        language (str): The language code for the WordPress installation.

    Returns:
        bool: True if the installation was successful, False otherwise.
    """
    command = ["wp", "core", "download", "--locale", language]
    stdout, stderr = run_command(command)

    if stderr:
        print(f"Error installing WordPress: {stderr}", file=sys.stderr)
        return False

    print(stdout)
    return True


def main():
    """
    Main function to interact with WordPress CLI and install WordPress.
    """
    print("Fetching available languages...")
    languages = get_available_languages()

    if not languages:
        print("Failed to fetch languages. Exiting...")
        sys.exit(1)

    print("Available languages:")
    for idx, lang in enumerate(languages, start=1):
        print(f"{idx}. {lang}")

    try:
        choice = int(input("Select a language by number: "))
        if choice < 1 or choice > len(languages):
            raise ValueError("Invalid choice.")
    except ValueError as e:
        print(f"Error: {e}. Exiting...", file=sys.stderr)
        sys.exit(1)

    selected_language = languages[choice - 1]
    print(f"Installing WordPress with language: {selected_language}...")

    success = install_wordpress(selected_language)
    if success:
        print("WordPress installed successfully!")
    else:
        print("WordPress installation failed. Please check the error messages.", file=sys.stderr)


if __name__ == "__main__":
    main()
```
