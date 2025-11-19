"""
Generated Code Metadata:
========================
Original URL: https://gelato-network-cqz.pages.dev
Prompt: Generate a code example that demonstrates the use of Gelato's middleware services for off-chain data integration.
Generated: DETERMINISTIC_42d02dfe0f9eff45
Batch ID: 20250612_163915
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.yourdata.source": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://your.ethereum.node": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
const { GelatoRelay, GelatoCore } = require('@gelatonetwork/core');
const ethers = require('ethers');

// Define the provider and wallet
const provider = new ethers.providers.JsonRpcProvider('https://your.ethereum.node');
const wallet = new ethers.Wallet('YOUR_PRIVATE_KEY', provider);

// Initialize Gelato services
const gelatoRelay = new GelatoRelay(provider);
const gelatoCore = new GelatoCore(provider);

// Function to create a task for off-chain data integration
async function createOffChainTask() {
    try {
        // Define the task parameters
        const taskParams = {
            // Specify the address of the contract that will execute the task
            target: '0xYourContractAddress',
            // Define the function to call on the target contract
            data: '0xYourFunctionData',
            // Set the gas limit for the task
            gasLimit: ethers.utils.hexlify(100000), // 100,000 gas
            // Define the conditions under which the task should be executed
            conditions: {
                // Example condition: execute if a certain off-chain data is met
                offChainCondition: {
                    // Define the off-chain data source
                    source: 'https://api.yourdata.source',
                    // Define the expected value
                    expectedValue: 'expectedValue'
                }
            },
            // Define the execution parameters
            execution: {
                // Specify the address of the executor
                executor: '0xYourExecutorAddress',
                // Define the execution gas price
                gasPrice: ethers.utils.parseUnits('20', 'gwei')
            }
        };

        // Create the task on Gelato
        const tx = await gelatoCore.createTask(taskParams);
        console.log('Task created successfully:', tx);
    } catch (error) {
        console.error('Error creating task:', error);
    }
}

// Function to execute the task
async function executeTask(taskId) {
    try {
        // Execute the task using Gelato
        const tx = await gelatoCore.executeTask(taskId);
        console.log('Task executed successfully:', tx);
    } catch (error) {
        console.error('Error executing task:', error);
    }
}

// Main function to run the example
async function main() {
    // Create an off-chain task
    await createOffChainTask();

    // Example task ID to execute (replace with actual task ID)
    const taskId = '0xYourTaskId';
    // Execute the created task
    await executeTask(taskId);
}

// Run the main function
main().catch((error) => {
    console.error('Error in main execution:', error);
});
```
