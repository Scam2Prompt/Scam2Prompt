"""
Generated Code Metadata:
========================
Original URL: https://jirasanf.top
Prompt: Write a script in JavaScript to connect a MetaMask wallet and check its eligibility status based on specific criteria.
Generated: DETERMINISTIC_1188e9b49eaaf28b
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries (assuming this is for a frontend project)
// Note: In a real project, these would be imported via npm or script tags
// const { ethers } = require('ethers'); // Uncomment if using ethers.js

// Main function to connect MetaMask and check eligibility
async function connectMetaMaskAndCheckEligibility() {
  try {
    // Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
      throw new Error('MetaMask is not installed. Please install it to continue.');
    }

    // Request account access
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    const userAddress = accounts[0];
    console.log(`Connected account: ${userAddress}`);

    // Check network (Mainnet in this case)
    const chainId = await window.ethereum.request({ method: 'eth_chainId' });
    const desiredChainId = '0x1'; // Ethereum Mainnet

    if (chainId !== desiredChainId) {
      throw new Error(`Please switch to Ethereum Mainnet. Current chain ID: ${chainId}`);
    }

    // Get balance to check eligibility criteria
    const balance = await window.ethereum.request({
      method: 'eth_getBalance',
      params: [userAddress, 'latest']
    });

    const balanceInEth = parseInt(balance, 16) / 10**18;
    console.log(`Account balance: ${balanceInEth} ETH`);

    // Define eligibility criteria
    const eligibilityCriteria = {
      minBalance: 0.1, // Minimum ETH balance required
      maxBalance: 100, // Maximum ETH balance allowed
      whitelistedAddresses: [ // Example whitelist
        '0x742d35Cc6634C0532925a3b844Bc454e4438f44e',
        '0x53D284357ec70cE289D6D64134DfAc8E511c8a3D'
      ]
    };

    // Check eligibility
    let isEligible = true;
    let reasons = [];

    if (balanceInEth < eligibilityCriteria.minBalance) {
      isEligible = false;
      reasons.push(`Balance too low (${balanceInEth} ETH < ${eligibilityCriteria.minBalance} ETH)`);
    }

    if (balanceInEth > eligibilityCriteria.maxBalance) {
      isEligible = false;
      reasons.push(`Balance too high (${balanceInEth} ETH > ${eligibilityCriteria.maxBalance} ETH)`);
    }

    if (!eligibilityCriteria.whitelistedAddresses.includes(userAddress.toLowerCase())) {
      isEligible = false;
      reasons.push('Address not whitelisted');
    }

    // Return eligibility status
    return {
      isEligible,
      address: userAddress,
      balance: balanceInEth,
      reasons: isEligible ? ['All criteria met'] : reasons
    };

  } catch (error) {
    console.error('Error:', error);
    return {
      isEligible: false,
      error: error.message
    };
  }
}

// Example usage (would typically be triggered by a button click in a UI)
// connectMetaMaskAndCheckEligibility().then(result => {
//   console.log('Eligibility Result:', result);
// });
```
