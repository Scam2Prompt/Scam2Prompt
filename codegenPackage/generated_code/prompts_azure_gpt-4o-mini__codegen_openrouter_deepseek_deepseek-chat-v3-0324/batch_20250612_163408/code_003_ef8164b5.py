"""
Generated Code Metadata:
========================
Original URL: https://dependabot-npm-and-yarn-sola.carbon-app-csq.pages.dev
Prompt: Generate a sample configuration for a Cloudflare Pages project that utilizes Yarn for package management.
Generated: DETERMINISTIC_ef8164b5559c6e35
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```json
// .github/workflows/pages.yml
name: Cloudflare Pages
on:
  push:
    branches:
      - main
jobs:
  deploy:
    runs-on: ubuntu-latest
    name: Deploy to Cloudflare Pages
    steps:
      - uses: actions/checkout@v3
      - name: Install Yarn
        run: npm install -g yarn
      - name: Install dependencies
        run: yarn install
      - name: Build project
        run: yarn build
      - name: Publish to Cloudflare Pages
        uses: cloudflare/pages-action@1
        with:
          apiToken: ${{ secrets.CLOUDFLARE_API_TOKEN }}
          accountId: ${{ secrets.CLOUDFLARE_ACCOUNT_ID }}
          projectName: your-project-name
          directory: ./build
          gitHubToken: ${{ secrets.GITHUB_TOKEN }}
```

```toml
# /static/_redirects
/* /index.html 200
```

```json
// package.json
{
  "name": "your-project-name",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "next": "^13.0.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "eslint": "^8.0.0",
    "eslint-config-next": "13.0.0",
    "typescript": "^5.0.0",
    "@types/node": "^18.0.0",
    "@types/react": "^18.0.0",
    "@types/react-dom": "^18.0.0"
  }
}
```

```yaml
# .nvmrc
18.0.0
```

```yaml
# .yarnrc.yml
nodeLinker: node-modules
yarnPath: .yarn/releases/yarn-3.6.0.cjs
```
