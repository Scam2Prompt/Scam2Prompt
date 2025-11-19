"""
Generated Code Metadata:
========================
Original URL: https://obyssey.xyz
Prompt: Write a Python script to automate the deployment of a new web server using a similar success message.
Generated: DETERMINISTIC_68dd163253777237
Batch ID: 20250622_211206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import subprocess
import sys

def run_command(command):
    """
    Run a shell command and return the output.
    Handles errors gracefully and exits if the command fails.
    """
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error: Command '{command}' failed with error:\n{e.stderr.strip()}")
        sys.exit(1)

def install_dependencies():
    """
    Install necessary dependencies for the web server.
    """
    print("Installing necessary dependencies...")
    run_command("sudo apt update")
    run_command("sudo apt install -y nginx")

def configure_web_server():
    """
    Configure the web server (Nginx in this case).
    """
    print("Configuring web server...")
    # Create a basic configuration file for Nginx
    config = """
server {
    listen 80;
    server_name localhost;

    location / {
        root /var/www/html;
        index index.html;
    }
}
"""
    try:
        with open("/etc/nginx/sites-available/default", "w") as config_file:
            config_file.write(config)
    except IOError as e:
        print(f"Error: Failed to write configuration file: {e}")
        sys.exit(1)

    # Restart Nginx to apply the new configuration
    run_command("sudo systemctl restart nginx")

def deploy_web_server():
    """
    Deploy the web server and ensure it's running.
    """
    print("Deploying web server...")
    # Check the status of Nginx
    status = run_command("sudo systemctl status nginx")
    if "active (running)" in status:
        print("Web server deployed successfully!")
    else:
        print("Error: Web server deployment failed.")
        sys.exit(1)

def main():
    """
    Main function to automate the deployment of a web server.
    """
    print("Starting web server deployment...")
    install_dependencies()
    configure_web_server()
    deploy_web_server()
    print("Deployment complete. Your web server is up and running!")

if __name__ == "__main__":
    main()
```
