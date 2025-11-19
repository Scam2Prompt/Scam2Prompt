"""
Generated Code Metadata:
========================
Original URL: https://flow-blockchain.com
Prompt: Explain how to use Flow Blockchain's emulator for local development and provide a code example for setting it up.
Generated: DETERMINISTIC_e60209be969d542d
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const { emulator, init } = require('@onflow/flow-js-testing');
const path = require('path');

// Configuration for the emulator
const emulatorConfig = {
  logging: false, // Disable verbose logging
  adminPort: 3569, // Admin port for the emulator
  restPort: 8888, // REST API port
  grpcPort: 3569, // gRPC port
  dbPath: path.join(__dirname, 'flowdb'), // Path to store the emulator's database
  tokenSupply: '1000000000.0', // Initial token supply
  transactionExpiry: 10, // Transaction expiry in blocks
  storageLimit: true, // Enable storage limits
  servicePrivateKey: '5f9d7a1e3e6b8c2d5e4f1a7b3c8d9e0f2b4a6d7c8e9f0a1b2c3d4e5f6a7b8', // Service account private key
  serviceSigAlgorithm: 'ECDSA_P256', // Service account signature algorithm
  serviceHashAlgorithm: 'SHA3_256', // Service account hash algorithm
  servicePublicKey: 'a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1', // Service account public key
};

// Initialize and start the emulator
async function setupEmulator() {
  try {
    // Initialize the testing framework
    await init(path.resolve(__dirname));

    // Start the emulator with the specified configuration
    await emulator.start(emulatorConfig);

    console.log('Flow Emulator started successfully');
    
    // Example: Deploy a contract
    const deployContract = async () => {
      const [deployResult, error] = await deployContractByName({
        name: 'HelloWorld',
        to: '0x01', // Address to deploy to
      });

      if (error) throw error;
      console.log('Contract deployed:', deployResult);
    };

    await deployContract();

  } catch (error) {
    console.error('Error setting up emulator:', error);
    process.exit(1);
  }
}

// Stop the emulator
async function stopEmulator() {
  try {
    await emulator.stop();
    console.log('Flow Emulator stopped successfully');
  } catch (error) {
    console.error('Error stopping emulator:', error);
  }
}

// Handle process termination
process.on('SIGINT', async () => {
  await stopEmulator();
  process.exit();
});

// Run the setup
setupEmulator();
```
