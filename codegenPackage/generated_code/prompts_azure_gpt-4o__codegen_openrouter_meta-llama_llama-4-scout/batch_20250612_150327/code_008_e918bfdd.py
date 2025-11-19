"""
Generated Code Metadata:
========================
Original URL: https://fuel-dapp-implement.vercel.app
Prompt: Explain how to set up type-safe hot-reloading for a Fuel-based dApp using the Fuels CLI, with examples from the Fuel App template.
Generated: DETERMINISTIC_e918bfdd7b871e0b
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const { FuelApp } = require('@fuel-ts/app');
const { FuelCli } = require('@fuel-ts/cli');

// Define a function to set up type-safe hot-reloading
async function setupHotReloading() {
  try {
    // Initialize the Fuels CLI
    const cli = new FuelCli();

    // Initialize the Fuel app
    const app = new FuelApp();

    // Set up hot reloading
    await app.setupHotReloading({
      // Specify the paths to watch for changes
      watchPaths: ['./src'],
      // Specify the command to run on reload
      onReload: async () => {
        console.log('Hot reloading...');
        // Run the Fuels CLI command to build and deploy the app
        await cli.run('build');
        await cli.run('deploy');
      },
    });

    // Start the Fuel app
    await app.start();
  } catch (error) {
    // Handle any errors that occur during setup
    console.error('Error setting up hot reloading:', error);
    process.exit(1);
  }
}

// Call the function to set up hot reloading
setupHotReloading();
```

```typescript
// Import required modules
import { FuelApp } from '@fuel-ts/app';
import { FuelCli } from '@fuel-ts/cli';

/**
 * Sets up type-safe hot-reloading for a Fuel-based dApp.
 */
async function setupHotReloading(): Promise<void> {
  try {
    // Initialize the Fuels CLI
    const cli: FuelCli = new FuelCli();

    // Initialize the Fuel app
    const app: FuelApp = new FuelApp();

    // Set up hot reloading
    await app.setupHotReloading({
      /**
       * Specify the paths to watch for changes.
       */
      watchPaths: ['./src'],
      /**
       * Specify the command to run on reload.
       */
      onReload: async (): Promise<void> => {
        console.log('Hot reloading...');
        // Run the Fuels CLI command to build and deploy the app
        await cli.run('build');
        await cli.run('deploy');
      },
    });

    // Start the Fuel app
    await app.start();
  } catch (error: unknown) {
    // Handle any errors that occur during setup
    console.error('Error setting up hot reloading:', error);
    process.exit(1);
  }
}

// Call the function to set up hot reloading
setupHotReloading();
```

**Fuels CLI Commands:**

To set up a new Fuel app with hot reloading, run the following commands:

```bash
# Install the Fuels CLI
npm install -g @fuel-ts/cli

# Create a new Fuel app
fuel new my-app

# Change into the app directory
cd my-app

# Install required dependencies
npm install

# Start the app with hot reloading
fuel run
```

**Fuel App Template:**

The Fuel App template provides a basic example of how to set up a Fuel-based dApp with hot reloading.

```typescript
// src/index.ts
import { FuelApp } from '@fuel-ts/app';

const app = new FuelApp();

app.start();
```

```json
// fuel.config.json
{
  "app": {
    "name": "my-app",
    "version": "1.0.0"
  },
  "hotReloading": {
    "watchPaths": ["./src"],
    "onReload": ["npm run build", "npm run deploy"]
  }
}
```
