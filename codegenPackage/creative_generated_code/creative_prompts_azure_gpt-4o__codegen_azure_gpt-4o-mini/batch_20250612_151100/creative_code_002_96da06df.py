"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ta-orch-api.agoric-sdk.pages.dev
Prompt: Provide a detailed example of creating and installing a Zoe contract facet bundle using the Agoric SDK, ensuring the `yarn build` step is included to generate the contract facet bundle.
Generated: DETERMINISTIC_96da06df7e0f8683
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from the Agoric SDK
import { E } from '@endo/eventual-send';
import { makeZoe } from '@agoric/zoe';
import { AmountMath } from '@agoric/ertp';
import { makeIssuerKit } from '@agoric/ertp';

// Create a contract facet bundle for Zoe
const createContractFacetBundle = async () => {
  // Create an issuer for a digital asset (e.g., a token)
  const { issuer, mint, amountMath } = makeIssuerKit('token');

  // Make a Zoe instance for contract deployment
  const zoe = makeZoe();

  // Define the contract installation function
  const installContract = async (contractBundle) => {
    try {
      const installation = await E(zoe).install(contractBundle);

      // Return the installation details
      return installation;
    } catch (error) {
      console.error('Error during contract installation:', error);
      throw new Error('Failed to install contract.');
    }
  };

  // Define the contract code to be bundled
  const contractCode = async (zoeInstance) => {
    // Define your contract logic here
    const start = async (instanceHandle, terms) => {
      // Add contract start logic
    };

    return { start };
  };

  // Create the contract bundle
  const contractBundle = {
    source: contractCode.toString(),
    // Add other necessary fields for the contract bundle
  };

  // Run the installation process and return the installation object
  return await installContract(contractBundle);
};

// Function to build the contract facet bundle
const buildAndInstallBundle = async () => {
  try {
    // Build the contract using the yarn build command
    const result = await exec('yarn build');
    console.log('Build result:', result);

    // Create and install the contract facet bundle
    const installation = await createContractFacetBundle();
    console.log('Contract installed:', installation);
  } catch (error) {
    console.error('Error during build and installation:', error);
    throw new Error('Failed to build and install the contract facet bundle.');
  }
};

// Execute the build and installation process
buildAndInstallBundle().catch((error) => {
  console.error('An error occurred:', error);
});

// Helper function to execute shell commands
const exec = (command) => {
  return new Promise((resolve, reject) => {
    require('child_process').exec(command, (error, stdout, stderr) => {
      if (error) {
        reject(`Error: ${stderr}`);
      } else {
        resolve(stdout);
      }
    });
  });
};
```
