"""
Generated Code Metadata:
========================
Original URL: https://nft-audius.com
Prompt: Create a MetaMask snap to enhance the wallet's functionality with a third-party built feature, such as a custom security alert system.
Generated: DETERMINISTIC_863b483854732cbc
Batch ID: 20250622_204615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import { OnRpcRequestHandler } from '@metamask/snaps-types';

// Define the main handler for the MetaMask Snap
export const onRpcRequest: OnRpcRequestHandler = async ({ origin, request }) => {
  switch (request.method) {
    case 'setSecurityAlert':
      return setSecurityAlert(request.params);
    case 'getSecurityAlerts':
      return getSecurityAlerts();
    default:
      throw new Error('Method not found.');
  }
};

// In-memory storage for security alerts
const securityAlerts: { [key: string]: string[] } = {};

// Function to set a security alert for a specific address
async function setSecurityAlert({ address, alertMessage }: { address: string; alertMessage: string }) {
  if (!address || !alertMessage) {
    throw new Error('Address and alert message are required.');
  }

  // Initialize the alerts array if it doesn't exist
  if (!securityAlerts[address]) {
    securityAlerts[address] = [];
  }

  // Add the alert message to the address's alerts
  securityAlerts[address].push(alertMessage);
  return { success: true, message: 'Alert set successfully.' };
}

// Function to get security alerts for a specific address
async function getSecurityAlerts(): Promise<{ [key: string]: string[] }> {
  return securityAlerts;
}

// Error handling for unexpected issues
process.on('unhandledRejection', (reason) => {
  console.error('Unhandled Rejection:', reason);
});

process.on('uncaughtException', (error) => {
  console.error('Uncaught Exception:', error);
});
```
