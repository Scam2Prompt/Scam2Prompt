"""
Generated Code Metadata:
========================
Original URL: https://stonegarden.dev
Prompt: Generate a code snippet for integrating GitLab CI/CD with a project hosted on GitHub as described on Stonegarden.dev.
Generated: DETERMINISTIC_ba93042b05bee5b8
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import yaml
from github import Github
from gitlab import Gitlab

# Configuration
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
GITLAB_TOKEN = os.environ.get('GITLAB_TOKEN')
GITHUB_REPO = os.environ.get('GITHUB_REPO')
GITLAB_PROJECT_ID = os.environ.get('GITLAB_PROJECT_ID')

# Initialize GitHub and GitLab clients
def init_clients():
    try:
        github_client = Github(GITHUB_TOKEN)
        gitlab_client = Gitlab(private_token=GITLAB_TOKEN)
        return github_client, gitlab_client
    except Exception as e:
        print(f"Failed to initialize clients: {e}")
        return None, None

# Get GitHub repository and GitLab project
def get_repo_project(github_client, gitlab_client):
    try:
        github_repo = github_client.get_repo(GITHUB_REPO)
        gitlab_project = gitlab_client.projects.get(GITLAB_PROJECT_ID)
        return github_repo, gitlab_project
    except Exception as e:
        print(f"Failed to get repository or project: {e}")
        return None, None

# Create GitLab CI/CD configuration
def create_gitlab_ci(github_repo, gitlab_project):
    try:
        # Load .gitlab-ci.yml template
        with open('.gitlab-ci.yml.template', 'r') as f:
            gitlab_ci_config = yaml.safe_load(f)

        # Update GitLab CI/CD configuration with GitHub repository information
        gitlab_ci_config['variables']['GITHUB_REPO'] = GITHUB_REPO
        gitlab_ci_config['variables']['GITHUB_TOKEN'] = GITHUB_TOKEN

        # Create or update GitLab CI/CD configuration
        existing_config = gitlab_project.files.get(file_path='.gitlab-ci.yml', ref='main')
        if existing_config:
            gitlab_project.files.update(
                file_path='.gitlab-ci.yml',
                branch='main',
                content=yaml.dump(gitlab_ci_config),
                commit_message='Update GitLab CI/CD configuration'
            )
        else:
            gitlab_project.files.create(
                file_path='.gitlab-ci.yml',
                branch='main',
                content=yaml.dump(gitlab_ci_config),
                commit_message='Create GitLab CI/CD configuration'
            )
    except Exception as e:
        print(f"Failed to create or update GitLab CI/CD configuration: {e}")

# Main function
def main():
    github_client, gitlab_client = init_clients()
    if github_client and gitlab_client:
        github_repo, gitlab_project = get_repo_project(github_client, gitlab_client)
        if github_repo and gitlab_project:
            create_gitlab_ci(github_repo, gitlab_project)

if __name__ == '__main__':
    main()
```

```yml
# .gitlab-ci.yml.template
stages:
  - build

variables:
  GITHUB_REPO: $GITHUB_REPO
  GITHUB_TOKEN: $GITHUB_TOKEN

build:
  stage: build
  script:
    - echo "Building $GITHUB_REPO with $GITHUB_TOKEN"
  only:
    - main
```
