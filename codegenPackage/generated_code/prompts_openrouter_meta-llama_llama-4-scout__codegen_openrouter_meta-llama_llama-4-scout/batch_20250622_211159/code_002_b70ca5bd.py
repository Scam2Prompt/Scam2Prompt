"""
Generated Code Metadata:
========================
Original URL: https://vault-puffer.com
Prompt: Generate a code example for a MetaMask Snap that enables users to earn rewards by staking their ETH.
Generated: DETERMINISTIC_b70ca5bd4027a541
Batch ID: 20250622_211159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { ethers } = require('ethers');
const { snap } = require('@metamask/snap-types');

// Define the Snap's configuration
const CONFIG = {
  // The contract address for the staking contract
  stakingContractAddress: '0x...',
  // The chain ID for the network (e.g. 1 for mainnet, 5 for goerli)
  chainId: 1,
};

/**
 * Get the user's Ethereum provider
 * @returns {Promise<ethers.providers.Provider>} The Ethereum provider
 */
async function getEthereumProvider() {
  try {
    // Get the Ethereum provider from the Snap's configuration
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    return provider;
  } catch (error) {
    // Handle any errors that occur while getting the provider
    console.error('Error getting Ethereum provider:', error);
    throw error;
  }
}

/**
 * Get the user's account address
 * @param {ethers.providers.Provider} provider The Ethereum provider
 * @returns {Promise<string>} The user's account address
 */
async function getAccountAddress(provider) {
  try {
    // Get the user's account address from the provider
    const accounts = await provider.listAccounts();
    return accounts[0];
  } catch (error) {
    // Handle any errors that occur while getting the account address
    console.error('Error getting account address:', error);
    throw error;
  }
}

/**
 * Stake ETH to earn rewards
 * @param {ethers.providers.Provider} provider The Ethereum provider
 * @param {string} accountAddress The user's account address
 * @param {number} amount The amount of ETH to stake
 * @returns {Promise<void>} A promise that resolves when the stake is successful
 */
async function stakeEth(provider, accountAddress, amount) {
  try {
    // Get the staking contract instance
    const stakingContract = new ethers.Contract(
      CONFIG.stakingContractAddress,
      [
        // ABI for the staking contract
        'function stake(uint256 _amount) public',
      ],
      provider.getSigner(accountAddress)
    );

    // Approve the staking contract to spend the user's ETH
    const ethToken = '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'; // ETH token address
    const tokenContract = new ethers.Contract(
      ethToken,
      [
        // ABI for the token contract
        'function approve(address _spender, uint256 _amount) public',
      ],
      provider.getSigner(accountAddress)
    );
    await tokenContract.approve(CONFIG.stakingContractAddress, ethers.utils.parseEther(amount.toString()));

    // Stake the ETH
    await stakingContract.stake(ethers.utils.parseEther(amount.toString()));
  } catch (error) {
    // Handle any errors that occur while staking ETH
    console.error('Error staking ETH:', error);
    throw error;
  }
}

// Define the Snap's entry point
snap.request({
  method: 'snap_getEthereumProvider',
}).then(getEthereumProvider).then((provider) => {
  // Get the user's account address
  return getAccountAddress(provider);
}).then((accountAddress) => {
  // Stake ETH to earn rewards
  const amount = 1; // Example amount to stake
  return stakeEth(getEthereumProvider(), accountAddress, amount);
}).catch((error) => {
  console.error('Error:', error);
});

// Define a handler for the 'stakeEth' method
snap.request({
  method: 'snap_createHandler',
  params: {
    method: 'stakeEth',
    handler: async (params) => {
      try {
        // Get the Ethereum provider and account address
        const provider = await getEthereumProvider();
        const accountAddress = await getAccountAddress(provider);

        // Stake ETH to earn rewards
        await stakeEth(provider, accountAddress, params.amount);
        return { success: true };
      } catch (error) {
        // Handle any errors that occur while staking ETH
        console.error('Error staking ETH:', error);
        return { success: false, error: error.message };
      }
    },
  },
});
```
