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

```bash
# Step 1: Install Turborepo globally
npm install -g turbo

# Step 2: Create a new Turborepo
npx create-turbo@latest my-turborepo

# Change into the newly created directory
cd my-turborepo

# Step 3: Create Next.js frontend and Hardhat backend directories
mkdir apps
mkdir packages

# Create Next.js frontend
npx create-next-app@latest apps/frontend --typescript

# Create Hardhat backend
mkdir apps/backend
cd apps/backend
npm init -y
npm install --save-dev hardhat

# Initialize Hardhat
npx hardhat

# Go back to the root directory
cd ../../

# Step 4: Configure the Turborepo in the `turbo.json` file
cat <<EOL > turbo.json
{
  "$schema": "https://turbo.build/schema.json",
  "pipeline": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**"]
    },
    "dev": {
      "cache": false
    },
    "lint": {
      "dependsOn": ["^lint"]
    }
  }
}
EOL

# Step 5: Set up package dependencies for frontend and backend
# Create a package.json in the root directory for shared dependencies
cat <<EOL > package.json
{
  "private": true,
  "workspaces": [
    "apps/*",
    "packages/*"
  ]
}
EOL

# Step 6: Install common dependencies (if needed)
npm install --workspace=apps/frontend ethers hardhat
npm install --workspace=apps/backend @nomiclabs/hardhat-ethers

# Step 7: Configure the Hardhat project
# Add necessary settings to `hardhat.config.js`
cat <<EOL > apps/backend/hardhat.config.js
require("@nomiclabs/hardhat-ethers");

module.exports = {
  solidity: "0.8.0",
  networks: {
    // Configure networks here
  },
};
EOL

# Step 8: Ensure scripts are properly defined in both package.json files

# Frontend package.json
cat <<EOL > apps/frontend/package.json
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  }
}
EOL

# Backend package.json
cat <<EOL > apps/backend/package.json
{
  "scripts": {
    "test": "hardhat test",
    "compile": "hardhat compile"
  }
}
EOL

# Step 9: Run the Turborepo tasks to test everything is configured correctly
npx turbo run build
npx turbo run dev --filter=frontend
```

This script sets up a Turborepo with a Next.js frontend and a Hardhat backend, complete with basic configurations and package management. Be sure to tailor the configuration settings, dependencies, and scripts according to your specific project needs.
