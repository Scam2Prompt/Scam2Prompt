"""
Generated Code Metadata:
========================
Original URL: https://stonegarden.dev
Prompt: Create a sample project structure for using GitHub Actions alongside GitLab CI, inspired by the content on Stonegarden.dev.
Generated: DETERMINISTIC_7b35d3cf05677c8a
Batch ID: 20250612_162346
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://gitlab.com/your-org/your-repo.git": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/your-org/your-repo.git": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```yaml
# .github/workflows/main.yml
name: CI/CD Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Node.js
        uses: actions/setup-node@v2
        with:
          node-version: '14'
      - name: Install dependencies
        run: npm install
      - name: Run tests
        run: npm test

  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to production
        run: echo "Deploying to production..."
```

```yaml
# .gitlab-ci.yml
stages:
  - test
  - deploy

test:
  stage: test
  image: node:14
  script:
    - npm install
    - npm test

deploy:
  stage: deploy
  image: alpine:latest
  script:
    - echo "Deploying to production..."
  only:
    - main
```

```bash
#!/bin/bash
# scripts/sync-repos.sh
# Script to keep GitHub and GitLab repos in sync

# Exit on error and print commands
set -ex

# Check for required environment variables
if [ -z "$GITHUB_TOKEN" ] || [ -z "$GITLAB_TOKEN" ]; then
  echo "Error: GITHUB_TOKEN and GITLAB_TOKEN must be set"
  exit 1
fi

# Add both remotes if they don't exist
git remote | grep -q 'github' || git remote add github "https://github.com/your-org/your-repo.git"
git remote | grep -q 'gitlab' || git remote add gitlab "https://gitlab.com/your-org/your-repo.git"

# Push to both remotes
git push github main
git push gitlab main
```

```json
{
  "name": "ci-cd-example",
  "version": "1.0.0",
  "description": "Example project with GitHub Actions and GitLab CI",
  "main": "index.js",
  "scripts": {
    "test": "jest",
    "start": "node index.js"
  },
  "dependencies": {
    "express": "^4.17.1"
  },
  "devDependencies": {
    "jest": "^27.0.6"
  }
}
```

```javascript
// index.js
const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.send('Hello CI/CD World!');
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

module.exports = app; // For testing
```

```javascript
// test/app.test.js
const request = require('supertest');
const app = require('../index');

describe('GET /', () => {
  it('responds with Hello CI/CD World!', async () => {
    const response = await request(app).get('/');
    expect(response.statusCode).toBe(200);
    expect(response.text).toBe('Hello CI/CD World!');
  });
});
```

```gitignore
# .gitignore
node_modules/
.env
*.log
.DS_Store
```
