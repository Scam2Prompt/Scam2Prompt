"""
Generated Code Metadata:
========================
Original URL: https://stonegarden.dev
Prompt: Generate code that integrates Stonegarden.dev tools with GitHub Actions for CI/CD workflows.
Generated: DETERMINISTIC_af6b93d684741545
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```yml
# .github/workflows/stonegarden-ci-cd.yml

name: Stonegarden CI/CD Workflow

on:
  push:
    branches:
      - main

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Login to Stonegarden
        uses: stonegarden/action-login@v1
        with:
          api-key: ${{ secrets.STONEGARDEN_API_KEY }}
          api-secret: ${{ secrets.STONEGARDEN_API_SECRET }}

      - name: Build and deploy
        run: |
          # Stonegarden CLI commands to build and deploy
          stonegarden build
          stonegarden deploy

      - name: Run automated tests
        run: |
          # Run automated tests using Stonegarden CLI
          stonegarden test

      - name: Notify on failure
        if: ${{ failure() }}
        uses: actions/upload-artifact@v3
        with:
          name: build-logs
          path: stonegarden.log
          if-no-files-found: error

      - name: Notify on success
        if: ${{ success() }}
        run: |
          # Send notification on successful deployment
          stonegarden notify --success

```

```python
# stonegarden_integrations.py

import os
import logging
from stonegarden import Stonegarden

def login_to_stonegarden(api_key, api_secret):
    """
    Logs in to Stonegarden using provided API credentials.

    Args:
        api_key (str): Stonegarden API key.
        api_secret (str): Stonegarden API secret.

    Returns:
        Stonegarden: Logged-in Stonegarden client.
    """
    try:
        sg = Stonegarden(api_key=api_key, api_secret=api_secret)
        sg.login()
        return sg
    except Exception as e:
        logging.error(f"Failed to login to Stonegarden: {str(e)}")
        return None

def build_and_deploy(sg):
    """
    Builds and deploys using Stonegarden CLI.

    Args:
        sg (Stonegarden): Logged-in Stonegarden client.
    """
    try:
        sg.build()
        sg.deploy()
    except Exception as e:
        logging.error(f"Failed to build and deploy: {str(e)}")

def run_automated_tests(sg):
    """
    Runs automated tests using Stonegarden CLI.

    Args:
        sg (Stonegarden): Logged-in Stonegarden client.
    """
    try:
        sg.test()
    except Exception as e:
        logging.error(f"Failed to run automated tests: {str(e)}")

if __name__ == "__main__":
    api_key = os.environ.get("STONEGARDEN_API_KEY")
    api_secret = os.environ.get("STONEGARDEN_API_SECRET")

    sg = login_to_stonegarden(api_key, api_secret)
    if sg:
        build_and_deploy(sg)
        run_automated_tests(sg)
```

```python
# stonegarden_notify.py

import os
import logging
from stonegarden import Stonegarden

def send_notification(sg, status):
    """
    Sends notification using Stonegarden CLI.

    Args:
        sg (Stonegarden): Logged-in Stonegarden client.
        status (str): Notification status (success/failure).
    """
    try:
        sg.notify(status=status)
    except Exception as e:
        logging.error(f"Failed to send notification: {str(e)}")

if __name__ == "__main__":
    api_key = os.environ.get("STONEGARDEN_API_KEY")
    api_secret = os.environ.get("STONEGARDEN_API_SECRET")

    sg = Stonegarden(api_key=api_key, api_secret=api_secret)
    sg.login()

    status = os.environ.get("NOTIFICATION_STATUS")
    send_notification(sg, status)
```
