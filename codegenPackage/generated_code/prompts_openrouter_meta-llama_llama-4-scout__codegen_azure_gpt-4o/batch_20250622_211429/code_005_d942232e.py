"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2783--docusaurus-2.netlify.app
Prompt: Write a script that automates the deployment of a Docusaurus site to GitHub Pages using a CI/CD pipeline.
Generated: DETERMINISTIC_d942232e383770ca
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```yaml
# .github/workflows/deploy-docusaurus.yml
# GitHub Actions workflow to automate the deployment of a Docusaurus site to GitHub Pages.

name: Deploy Docusaurus to GitHub Pages

on:
  # Trigger the workflow on push to the main branch or manual dispatch.
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  deploy:
    name: Deploy Docusaurus Site
    runs-on: ubuntu-latest

    steps:
      # Step 1: Check out the repository.
      - name: Checkout repository
        uses: actions/checkout@v3

      # Step 2: Set up Node.js environment.
      - name: Set up Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '16' # Use the Node.js version compatible with Docusaurus.

      # Step 3: Install dependencies.
      - name: Install dependencies
        run: npm install

      # Step 4: Build the Docusaurus site.
      - name: Build Docusaurus site
        run: npm run build

      # Step 5: Deploy to GitHub Pages.
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }} # Use GitHub's built-in token for authentication.
          publish_dir: build # The directory containing the built Docusaurus site.

      # Optional: Notify success.
      - name: Notify deployment success
        run: echo "Docusaurus site successfully deployed to GitHub Pages!"
```
