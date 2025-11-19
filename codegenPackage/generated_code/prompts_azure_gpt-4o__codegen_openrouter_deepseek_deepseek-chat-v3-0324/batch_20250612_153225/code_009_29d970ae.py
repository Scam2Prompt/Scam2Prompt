"""
Generated Code Metadata:
========================
Original URL: https://giitechcodes.com.ng
Prompt: Create a software solution for automating a process using Docker and Git, as described in GII Tech Codes' IoT and software engineering services.
Generated: DETERMINISTIC_29d970ae0b306b88
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Docker and Git Automation Script for GII Tech Codes' IoT and Software Engineering Services.

This script automates the process of setting up a Docker environment,
cloning a Git repository, building Docker images, and managing containers.
"""

import os
import subprocess
import sys
import argparse
from typing import Optional, List, Dict


class DockerGitAutomation:
    """Main class for Docker and Git automation."""

    def __init__(self, repo_url: str, dockerfile_path: str = "Dockerfile", 
                 image_name: str = "giitech-image", container_name: str = "giitech-container"):
        """
        Initialize the automation tool with repository and Docker configuration.
        
        Args:
            repo_url: URL of the Git repository to clone
            dockerfile_path: Path to Dockerfile (default: "Dockerfile")
            image_name: Name for the Docker image (default: "giitech-image")
            container_name: Name for the Docker container (default: "giitech-container")
        """
        self.repo_url = repo_url
        self.dockerfile_path = dockerfile_path
        self.image_name = image_name
        self.container_name = container_name
        self.repo_dir = os.path.basename(repo_url).replace('.git', '')

    def check_docker_installed(self) -> bool:
        """Check if Docker is installed and running."""
        try:
            subprocess.run(["docker", "--version"], check=True, 
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False

    def check_git_installed(self) -> bool:
        """Check if Git is installed."""
        try:
            subprocess.run(["git", "--version"], check=True, 
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False

    def clone_repository(self) -> bool:
        """Clone the Git repository."""
        try:
            if os.path.exists(self.repo_dir):
                print(f"Directory {self.repo_dir} already exists. Pulling latest changes...")
                os.chdir(self.repo_dir)
                subprocess.run(["git", "pull"], check=True)
                os.chdir("..")
            else:
                subprocess.run(["git", "clone", self.repo_url], check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error cloning repository: {e}")
            return False

    def build_docker_image(self) -> bool:
        """Build Docker image from Dockerfile."""
        try:
            subprocess.run(
                ["docker", "build", "-t", self.image_name, "-f", 
                 os.path.join(self.repo_dir, self.dockerfile_path), "."],
                check=True
            )
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error building Docker image: {e}")
            return False

    def run_docker_container(self, ports: Optional[Dict[str, str]] = None, 
                            env_vars: Optional[Dict[str, str]] = None) -> bool:
        """
        Run Docker container from the built image.
        
        Args:
            ports: Dictionary of port mappings (host:container)
            env_vars: Dictionary of environment variables
        """
        cmd = ["docker", "run", "-d", "--name", self.container_name]
        
        if ports:
            for host_port, container_port in ports.items():
                cmd.extend(["-p", f"{host_port}:{container_port}"])
        
        if env_vars:
            for key, value in env_vars.items():
                cmd.extend(["-e", f"{key}={value}"])
        
        cmd.append(self.image_name)
        
        try:
            subprocess.run(cmd, check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error running Docker container: {e}")
            return False

    def stop_container(self) -> bool:
        """Stop the running container."""
        try:
            subprocess.run(["docker", "stop", self.container_name], check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error stopping container: {e}")
            return False

    def remove_container(self) -> bool:
        """Remove the container."""
        try:
            subprocess.run(["docker", "rm", self.container_name], check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error removing container: {e}")
            return False

    def remove_image(self) -> bool:
        """Remove the Docker image."""
        try:
            subprocess.run(["docker", "rmi", self.image_name], check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error removing image: {e}")
            return False

    def cleanup(self) -> bool:
        """Clean up Docker resources and repository."""
        success = True
        if not self.stop_container():
            success = False
        if not self.remove_container():
            success = False
        if not self.remove_image():
            success = False
        
        try:
            subprocess.run(["rm", "-rf", self.repo_dir], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error removing repository directory: {e}")
            success = False
        
        return success


def main():
    """Main function to handle command-line arguments and execute automation."""
    parser = argparse.ArgumentParser(
        description="Docker and Git Automation for GII Tech Codes' IoT Services"
    )
    parser.add_argument("repo_url", help="Git repository URL to clone")
    parser.add_argument("--dockerfile", default="Dockerfile", 
                        help="Path to Dockerfile (relative to repo root)")
    parser.add_argument("--image", default="giitech-image", 
                        help="Name for the Docker image")
    parser.add_argument("--container", default="giitech-container", 
                        help="Name for the Docker container")
    parser.add_argument("--ports", nargs="+", 
                        help="Port mappings (format: host:container)")
    parser.add_argument("--env", nargs="+", 
                        help="Environment variables (format: KEY=VALUE)")
    parser.add_argument("--cleanup", action="store_true", 
                        help="Clean up all resources after running")

    args = parser.parse_args()

    # Parse ports and environment variables
    ports = {}
    if args.ports:
        for port_mapping in args.ports:
            host, container = port_mapping.split(":")
            ports[host] = container

    env_vars = {}
    if args.env:
        for env_pair in args.env:
            key, value = env_pair.split("=")
            env_vars[key] = value

    # Initialize automation
    automation = DockerGitAutomation(
        repo_url=args.repo_url,
        dockerfile_path=args.dockerfile,
        image_name=args.image,
        container_name=args.container
    )

    # Check prerequisites
    if not automation.check_docker_installed():
        print("Error: Docker is not installed or not running.")
        sys.exit(1)
    if not automation.check_git_installed():
        print("Error: Git is not installed.")
        sys.exit(1)

    # Execute workflow
    if not automation.clone_repository():
        sys.exit(1)
    if not automation.build_docker_image():
        sys.exit(1)
    if not automation.run_docker_container(ports=ports, env_vars=env_vars):
        sys.exit(1)

    print("Successfully deployed container from Git repository!")

    if args.cleanup:
        if not automation.cleanup():
            print("Warning: Some cleanup operations failed")
        else:
            print("Successfully cleaned up all resources")


if __name__ == "__main__":
    main()
```
