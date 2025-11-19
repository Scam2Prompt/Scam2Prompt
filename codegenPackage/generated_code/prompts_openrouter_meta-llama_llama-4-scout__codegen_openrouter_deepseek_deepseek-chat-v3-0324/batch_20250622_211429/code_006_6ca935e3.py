"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-2614--docusaurus-2.netlify.app
Prompt: Write a Docusaurus API documentation page that describes how to use the `docusaurus` command-line tool to build and deploy a site.
Generated: DETERMINISTIC_6ca935e331019a48
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```markdown
---
title: Docusaurus CLI Reference
sidebar_label: CLI Reference
description: Documentation for the Docusaurus command-line tool to build and deploy sites.
---

# Docusaurus CLI

The `docusaurus` command-line tool provides various commands to help you develop, build, and deploy your Docusaurus site.

## Installation

The CLI is automatically installed when you create a Docusaurus project:

```bash
npx create-docusaurus@latest my-website classic
```

Alternatively, you can install it globally:

```bash
npm install --global docusaurus
```

## Commands

### `docusaurus start`

Starts a local development server with hot-reloading.

**Usage:**

```bash
docusaurus start [options]
```

**Options:**

- `--port`: Specify the port to run the development server (default: `3000`)
- `--host`: Specify the host to run the development server (default: `localhost`)
- `--hot-only`: Enable hot module replacement without page refresh
- `--no-open`: Do not automatically open the browser

**Example:**

```bash
docusaurus start --port 4000
```

### `docusaurus build`

Builds your site for production.

**Usage:**

```bash
docusaurus build [options]
```

**Options:**

- `--bundle-analyzer`: Analyze the production bundle size
- `--out-dir`: Specify the output directory (default: `build`)
- `--minify`: Minify the output (enabled by default in production)

**Example:**

```bash
docusaurus build --out-dir ./dist
```

### `docusaurus deploy`

Deploys your built site to a hosting provider.

**Usage:**

```bash
docusaurus deploy [options]
```

**Options:**

- `--out-dir`: Specify the directory containing the built files (default: `build`)
- `--skip-build`: Skip the build step and deploy existing build

**Example:**

```bash
docusaurus deploy --out-dir ./dist
```

### `docusaurus clear`

Clears the build artifacts and cached files.

**Usage:**

```bash
docusaurus clear
```

### `docusaurus serve`

Serves the built site locally for testing.

**Usage:**

```bash
docusaurus serve [options]
```

**Options:**

- `--port`: Specify the port to run the server (default: `3000`)
- `--host`: Specify the host to run the server (default: `localhost`)
- `--dir`: Specify the directory to serve (default: `build`)

**Example:**

```bash
docusaurus serve --port 5000
```

## Common Errors

1. **Port already in use**:
   ```bash
   Error: listen EADDRINUSE: address already in use 127.0.0.1:3000
   ```
   Solution: Specify a different port with `--port`

2. **Build directory not found**:
   ```bash
   Error: ENOENT: no such file or directory, stat '/path/to/build'
   ```
   Solution: Run `docusaurus build` first or specify correct `--out-dir`

## Best Practices

1. Always test your site locally with `docusaurus serve` before deploying
2. Use `--bundle-analyzer` periodically to optimize bundle size
3. Automate deployments with CI/CD pipelines using the CLI commands

## Version Information

To check your Docusaurus version:

```bash
docusaurus --version
```

To update Docusaurus:

```bash
npm update @docusaurus/core@latest @docusaurus/preset-classic@latest
```
```
