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

```yaml
name: Stonegarden CI/CD Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18.x'

      - name: Install dependencies
        run: npm ci

      - name: Run tests
        run: npm test

      - name: Build project
        run: npm run build

      - name: Stonegarden Deployment
        if: github.ref == 'refs/heads/main'
        uses: stonegarden-dev/deploy-action@v1
        with:
          api-key: ${{ secrets.STONEGARDEN_API_KEY }}
          project-id: ${{ secrets.STONEGARDEN_PROJECT_ID }}
          environment: production
          build-dir: 'dist'

  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18.x'

      - name: Install dependencies
        run: npm ci

      - name: Run linter
        run: npm run lint

  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Stonegarden Security Scan
        uses: stonegarden-dev/security-scan@v1
        with:
          api-key: ${{ secrets.STONEGARDEN_API_KEY }}
          fail-on-issues: true
```
