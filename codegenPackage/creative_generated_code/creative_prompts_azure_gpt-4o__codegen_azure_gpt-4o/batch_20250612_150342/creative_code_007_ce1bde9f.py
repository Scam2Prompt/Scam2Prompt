"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zksync-starter.vercel.app
Prompt: Explain how to configure Turborepo to manage tasks and dependencies for a project combining a zkSync-based Next.js frontend and a Hardhat backend.
Generated: DETERMINISTIC_ce1bde9fc7df5947
Batch ID: 20250612_150342
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://turbo.build/schema.json": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// turborepo.json
{
  // Turborepo configuration file
  "$schema": "https://turbo.build/schema.json",
  "pipeline": {
    // Define tasks for the frontend (Next.js)
    "build:frontend": {
      "outputs": [".next/**"], // Cache the .next directory for faster rebuilds
      "dependsOn": ["^build:frontend"] // Depend on parent-level frontend builds
    },
    "lint:frontend": {
      "outputs": [], // Linting doesn't produce build artifacts
      "dependsOn": [] // Run independently
    },
    "dev:frontend": {
      "cache": false, // Don't cache dev mode tasks
      "persistent": true // Keep dev server running
    },
    // Define tasks for the backend (Hardhat)
    "build:backend": {
      "outputs": ["artifacts/**", "cache/**"], // Cache Hardhat artifacts and cache
      "dependsOn": ["^build:backend"] // Depend on parent-level backend builds
    },
    "test:backend": {
      "outputs": [], // Tests don't produce build artifacts
      "dependsOn": ["build:backend"] // Ensure the backend is built before testing
    },
    "lint:backend": {
      "outputs": [], // Linting doesn't produce build artifacts
      "dependsOn": [] // Run independently
    },
    // Set up the shared "clean" task for all packages
    "clean": {
      "cache": false, // Don't cache cleaning tasks
      "outputs": [] // Cleaning tasks don't produce outputs
    }
  }
}
```

```bash
# package.json
{
  "name": "zksync-nextjs-hardhat-monorepo",
  "version": "1.0.0",
  "private": true,
  "workspaces": [
    "frontend", // Next.js frontend workspace
    "backend"   // Hardhat backend workspace
  ],
  "scripts": {
    "build": "turbo run build",  // Run all build tasks (frontend and backend)
    "dev": "turbo run dev",      // Run dev tasks (frontend and backend dev servers)
    "lint": "turbo run lint",    // Lint both frontend and backend
    "test": "turbo run test",    // Run backend tests
    "clean": "turbo run clean"   // Clean up all outputs
  },
  "devDependencies": {
    "turbo": "^1.10.0" // Install the latest turborepo CLI
  }
}
```

```bash
# frontend/package.json
{
  "name": "frontend",
  "version": "1.0.0",
  "scripts": {
    "build": "next build", // Build Next.js frontend
    "dev": "next dev",     // Run Next.js development server
    "lint": "next lint"    // Lint Next.js code
  },
  "dependencies": {
    "next": "^13.0.0",
    "react": "^18.0.0",
    "react-dom": "^18.0.0",
    "@zksync/ethers": "^0.10.1", // zkSync-related dependency for the frontend
    "ethers": "^5.7.0"           // Ethereum library for interacting with smart contracts
  },
  "devDependencies": {
    "eslint": "^8.0.0" // Dependency for linting
  }
}
```

```bash
# backend/package.json
{
  "name": "backend",
  "version": "1.0.0",
  "scripts": {
    "build": "hardhat compile", // Compile smart contracts using Hardhat
    "test": "hardhat test",     // Run Hardhat tests
    "lint": "eslint . --ext .js,.ts" // Lint backend code
  },
  "dependencies": {
    "@nomiclabs/hardhat-ethers": "^2.1.0", // Hardhat plugin for ethers.js
    "ethers": "^5.7.0",                    // Ethereum library
    "@nomiclabs/hardhat-waffle": "^2.0.0", // Hardhat plugin for Waffle (testing)
    "chai": "^4.3.0"                       // Assertion library for testing
  },
  "devDependencies": {
    "hardhat": "^2.12.0", // Hardhat framework for Ethereum development
    "eslint": "^8.0.0"    // Dependency for linting
  }
}
```

```bash
# .gitignore
# Ignore generated files and build artifacts
node_modules/
**/node_modules/
**/.next/
**/artifacts/
**/cache/
```

```bash
# Run the following command to bootstrap the project structure
# Initialize Turborepo and create the workspaces
mkdir frontend backend
npm install
```

```bash
# Example usage for running tasks
# Build both frontend and backend:
npm run build

# Start the frontend development server:
npm run dev --filter=frontend

# Clean all build artifacts across the monorepo:
npm run clean
```
