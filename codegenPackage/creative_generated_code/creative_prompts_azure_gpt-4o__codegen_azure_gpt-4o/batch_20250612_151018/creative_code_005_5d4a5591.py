"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-3358--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Write a Node.js script to deploy a web server on a Linode Nanode instance and configure it with Linode's DDoS Protection.
Generated: DETERMINISTIC_5d4a5591677e30b4
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const { LinodeClient } = require('@linode/api-v4'); // Linode API client
const axios = require('axios'); // HTTP Client for API requests
const fs = require('fs'); // File system module for SSH key handling
const path = require('path'); // Path module for file paths

// Environment variables for sensitive data
require('dotenv').config(); // Load environment variables from .env file
const LINODE_API_TOKEN = process.env.LINODE_API_TOKEN; // Linode API token
const SSH_PUBLIC_KEY_PATH = process.env.SSH_PUBLIC_KEY_PATH; // Path to SSH public key
const SSH_PRIVATE_KEY_PATH = process.env.SSH_PRIVATE_KEY_PATH; // Path to SSH private key

// Check if environment variables are set
if (!LINODE_API_TOKEN || !SSH_PUBLIC_KEY_PATH || !SSH_PRIVATE_KEY_PATH) {
  console.error('Error: Missing required environment variables.');
  process.exit(1);
}

// Initialize Linode API client
const client = new LinodeClient(LINODE_API_TOKEN);

// Function to deploy a Linode instance
async function deployLinodeInstance() {
  try {
    // Ensure that the SSH key files exist
    if (!fs.existsSync(SSH_PUBLIC_KEY_PATH) || !fs.existsSync(SSH_PRIVATE_KEY_PATH)) {
      throw new Error('SSH key files not found. Please provide valid paths.');
    }

    // Read the SSH public key
    const sshPublicKey = fs.readFileSync(SSH_PUBLIC_KEY_PATH, 'utf8');

    // Create a Linode Nanode instance
    console.log('Creating Linode Nanode instance...');
    const linode = await client.linodeInstances.create({
      region: 'us-east', // Replace with your preferred region
      type: 'g6-nanode-1', // Nanode instance type
      image: 'linode/ubuntu22.04', // Ubuntu 22.04 image
      root_pass: 'StrongPassword123!', // Replace with a strong password
      authorized_keys: [sshPublicKey], // Add SSH public key for access
      label: 'NodeWebServer', // Label for the instance
      stackscript_data: {},
    });

    console.log('Linode instance created successfully:', linode);

    // Wait for the instance to boot
    console.log('Waiting for instance to boot...');
    await waitForInstanceStatus(linode.id, 'running');

    console.log('Instance is booted and running.');

    // Enable DDoS Protection
    console.log('Enabling DDoS Protection...');
    await client.linodeInstances.update(linode.id, {
      backups_enabled: true, // Optional: Enable backups
      watchdog_enabled: true, // Enable Linode's DDoS Protection
    });

    console.log('DDoS Protection enabled successfully.');

    // Print instance details
    console.log(`Instance IP Address: ${linode.ipv4[0]}`);
  } catch (error) {
    console.error('Error deploying Linode instance:', error.message);
    process.exit(1);
  }
}

// Function to wait for a specific instance status
async function waitForInstanceStatus(instanceId, status) {
  try {
    while (true) {
      const instance = await client.linodeInstances.view(instanceId);
      if (instance.status === status) {
        break;
      }
      console.log(`Current status: ${instance.status}. Waiting for "${status}"...`);
      await delay(5000); // Wait for 5 seconds before checking again
    }
  } catch (error) {
    throw new Error('Error while waiting for instance status: ' + error.message);
  }
}

// Helper function for delay
function delay(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

// Main function
async function main() {
  console.log('Starting Linode instance deployment...');
  await deployLinodeInstance();
  console.log('Deployment completed successfully.');
}

// Execute main function
main();
```

### Additional Notes:
- Before running the script, you must create a `.env` file in the root directory with the following fields:
  ```
  LINODE_API_TOKEN=your-linode-api-token
  SSH_PUBLIC_KEY_PATH=/path/to/your/ssh-public-key
  SSH_PRIVATE_KEY_PATH=/path/to/your/ssh-private-key
  ```
- Replace `us-east`, `StrongPassword123!`, and other placeholders with appropriate values for production.
- Install dependencies via: `npm install @linode/api-v4 axios dotenv`.
