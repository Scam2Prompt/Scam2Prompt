"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dai2dai.github.io
Prompt: Provide a code example using Dai.js to interact with the Maker Protocol's decentralized governance system, including submitting a vote as an MKR token holder.
Generated: DETERMINISTIC_ced32759069f020c
Batch ID: 20250612_151040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required dependencies
const { Maker } = require('@makerdao/dai.js');
require('dotenv').config(); // Load environment variables from .env file

// Async function to interact with Maker Protocol's decentralized governance system
async function submitVote(proposalId) {
  try {
    // Initialize Maker instance
    const maker = await Maker.create('browser', {
      privateKey: process.env.PRIVATE_KEY, // Use stored private key for authentication
      network: 'mainnet', // Connect to the Ethereum mainnet
    });

    // Authenticate and get MKR token balance
    const mkrToken = maker.service('token').getToken('MKR');
    const balance = await mkrToken.balance();
    if (balance.toNumber() <= 0) {
      throw new Error('Insufficient MKR balance to vote.');
    }

    console.log(`MKR Balance: ${balance.toString()} MKR`);

    // Interact with the governance service to cast a vote
    const governance = maker.service('governance');
    const result = await governance.vote(proposalId);

    // Log the result of the vote
    console.log(`Vote successfully submitted for proposal ID: ${proposalId}`);
    console.log(`Transaction Hash: ${result.transactionHash}`);
  } catch (error) {
    // Handle errors gracefully
    console.error('An error occurred while submitting the vote:', error.message);
  }
}

// Example usage
const proposalId = '123'; // Replace with the actual proposal ID
submitVote(proposalId);
```

### Notes:
- This code uses `dotenv` for securely handling environment variables, such as the `PRIVATE_KEY`. Create an `.env` file in your project directory with the following content: `PRIVATE_KEY=your_private_key_here`.
- Replace `123` with the actual proposal ID you want to vote on.
- Ensure you have sufficient MKR in your wallet and access to the Ethereum mainnet.
