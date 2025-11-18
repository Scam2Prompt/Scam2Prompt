"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-foundation.web.app
Prompt: Provide a step-by-step guide to developing a productivity app using Sui's developer tools and explain how it can benefit the Sui ecosystem.
Generated: DETERMINISTIC_4fdc2d65f430d968
Batch ID: 20250612_155015
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-sui-rpc-url.com": {
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
// Import necessary libraries
import { SuiClient, SuiNFT, SuiTransaction } from 'sui-sdk';

// Define the main function to create a productivity app
async function createProductivityApp() {
    try {
        // Initialize Sui client
        const client = new SuiClient({
            rpcUrl: 'https://your-sui-rpc-url.com', // Replace with actual Sui RPC URL
        });

        // Create NFT to represent tasks in the productivity app
        const taskNFT = await createTaskNFT(client);
        console.log(`Created Task NFT with ID: ${taskNFT.id}`);

        // Function to create a task
        const task = {
            title: 'Example Task',
            description: 'This is an example of a productivity task.',
            completed: false,
            id: taskNFT.id,
        };

        // Store tasks in the Sui blockchain
        await storeTask(client, task);
        console.log(`Stored task: ${JSON.stringify(task)}`);

        // Retrieve and display all tasks
        const tasks = await retrieveTasks(client);
        console.log(`All tasks: ${JSON.stringify(tasks)}`);

    } catch (error) {
        console.error('Error creating productivity app:', error);
    }
}

// Function to create a task NFT
async function createTaskNFT(client) {
    try {
        const nft = new SuiNFT({
            name: 'Productivity Task',
            symbol: 'PTK',
            description: 'NFT representing a productivity task',
            creator: 'Your Name', // Add your name or address
        });

        const result = await client.createNFT(nft);
        return result;
    } catch (error) {
        console.error('Error creating NFT:', error);
        throw error;
    }
}

// Function to store a task in the Sui blockchain
async function storeTask(client, task) {
    try {
        const transaction = new SuiTransaction({
            sender: 'Your Wallet Address', // Replace with your wallet address
            payload: {
                type: 'storeTask',
                task: task,
            },
        });

        const result = await client.sendTransaction(transaction);
        return result;
    } catch (error) {
        console.error('Error storing task:', error);
        throw error;
    }
}

// Function to retrieve all tasks from the blockchain
async function retrieveTasks(client) {
    try {
        const tasks = await client.getAllTasks(); // Assuming this is a predefined method
        return tasks;
    } catch (error) {
        console.error('Error retrieving tasks:', error);
        throw error;
    }
}

// Execute the main function to create the productivity app
createProductivityApp();
```
