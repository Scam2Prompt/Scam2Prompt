"""
Generated Code Metadata:
========================
Original URL: https://zksync-starter.vercel.app
Prompt: "Generate a Turborepo configuration for a zkSync project with shared dependencies and tasks for a React app and smart contracts."
Generated: DETERMINISTIC_8148e29414928c21
Batch ID: 20250622_205156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// turborepo.config.js
/**
 * Turborepo configuration for zkSync project.
 * 
 * This configuration defines shared dependencies and tasks for a React app and smart contracts.
 */

module.exports = {
  // Define the root of the monorepo
  root: './',

  // Define the pipeline
  pipeline: {
    // Build task for React app
    'build:react': {
      // Depends on install task
      dependsOn: ['^install'],
      // Cache the build output
      outputs: ['dist/**'],
    },

    // Build task for smart contracts
    'build:contracts': {
      // Depends on install task
      dependsOn: ['^install'],
      // Cache the build output
      outputs: ['contracts/dist/**'],
    },

    // Install task for shared dependencies
    install: {
      // Run in parallel
      parallel: true,
    },
  },

  // Define shared dependencies
  remoteCache: {
    // Enable remote caching
    enabled: true,
    // Use a global cache
    globalCache: true,
  },

  // Define task dependencies
  tasks: {
    // React app build task
    'build:react': {
      // Command to build React app
      command: 'npm run build --workspace=react-app',
    },

    // Smart contracts build task
    'build:contracts': {
      // Command to build smart contracts
      command: 'npm run build --workspace=contracts',
    },

    // Install shared dependencies task
    install: {
      // Command to install shared dependencies
      command: 'npm install',
    },
  },
};
```

```json
// package.json
{
  "name": "zkSync-project",
  "version": "1.0.0",
  "workspaces": [
    "react-app",
    "contracts"
  ],
  "scripts": {
    "build:react": "turbo run build:react",
    "build:contracts": "turbo run build:contracts",
    "install": "turbo run install"
  }
}
```

```json
// react-app/package.json
{
  "name": "react-app",
  "version": "1.0.0",
  "scripts": {
    "build": "react-scripts build"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-scripts": "5.0.1"
  }
}
```

```json
// contracts/package.json
{
  "name": "contracts",
  "version": "1.0.0",
  "scripts": {
    "build": "npx hardhat compile"
  },
  "dependencies": {
    "@nomiclabs/hardhat": "^2.13.0",
    "@nomiclabs/hardhat-ethers": "^2.4.0"
  }
}
```
