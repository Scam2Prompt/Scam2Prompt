"""
Generated Code Metadata:
========================
Original URL: https://nft-compound.com
Prompt: Create a step-by-step guide on how to use MetaMask's Delegation Toolkit for creating walletless dapps.
Generated: DETERMINISTIC_b5159f159d7b772f
Batch ID: 20250622_211141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries and modules
const ethers = require('ethers');
const { DelegationRegistry } = require('@metamask/delegation-utils');

/**
 * Step 1: Initialize the Ethereum provider (MetaMask)
 * @returns {Promise<ethers.providers.Web3Provider>} - Web3 provider instance
 */
async function initProvider() {
  if (!window.ethereum) {
    throw new Error('MetaMask is not installed!');
  }
  await window.ethereum.request({ method: 'eth_requestAccounts' });
  return new ethers.providers.Web3Provider(window.ethereum);
}

/**
 * Step 2: Delegate signing authority to a hot wallet
 * @param {ethers.providers.Web3Provider} provider - Web3 provider instance
 * @param {string} delegateAddress - Address of the hot wallet
 * @param {string} contractAddress - Address of the delegation registry contract
 * @returns {Promise<string>} - Transaction hash
 */
async function delegateSigning(provider, delegateAddress, contractAddress) {
  const signer = provider.getSigner();
  const registry = new DelegationRegistry(contractAddress, signer);

  // Delegate for all tokens (use specific token address if needed)
  const tx = await registry.delegateForAll(delegateAddress);
  await tx.wait();

  return tx.hash;
}

/**
 * Step 3: Verify delegation
 * @param {ethers.providers.Web3Provider} provider - Web3 provider instance
 * @param {string} delegatorAddress - Address of the delegator
 * @param {string} delegateAddress - Address of the hot wallet
 * @param {string} contractAddress - Address of the delegation registry contract
 * @returns {Promise<boolean>} - True if delegation is valid
 */
async function verifyDelegation(provider, delegatorAddress, delegateAddress, contractAddress) {
  const registry = new DelegationRegistry(contractAddress, provider);
  return await registry.checkDelegateForAll(delegatorAddress, delegateAddress);
}

/**
 * Step 4: Execute a transaction via the hot wallet
 * @param {ethers.providers.Web3Provider} provider - Web3 provider instance
 * @param {string} delegateAddress - Address of the hot wallet
 * @param {string} contractAddress - Address of the target contract
 * @param {string} contractABI - ABI of the target contract
 * @param {string} functionName - Name of the function to call
 * @param {Array} functionArgs - Arguments for the function
 * @returns {Promise<string>} - Transaction hash
 */
async function executeDelegatedTransaction(
  provider,
  delegateAddress,
  contractAddress,
  contractABI,
  functionName,
  functionArgs
) {
  const signer = provider.getSigner(delegateAddress);
  const contract = new ethers.Contract(contractAddress, contractABI, signer);

  const tx = await contract[functionName](...functionArgs);
  await tx.wait();

  return tx.hash;
}

// Example usage
(async () => {
  try {
    // Step 1: Initialize provider
    const provider = await initProvider();
    const userAddress = await provider.getSigner().getAddress();

    // Step 2: Delegate signing authority
    const delegateAddress = '0xHotWalletAddress'; // Replace with actual hot wallet address
    const registryAddress = '0xDelegationRegistryAddress'; // Replace with actual registry address
    const txHash = await delegateSigning(provider, delegateAddress, registryAddress);
    console.log(`Delegation successful. Tx hash: ${txHash}`);

    // Step 3: Verify delegation
    const isDelegated = await verifyDelegation(provider, userAddress, delegateAddress, registryAddress);
    console.log(`Delegation verified: ${isDelegated}`);

    // Step 4: Execute a transaction (example)
    if (isDelegated) {
      const targetContractAddress = '0xTargetContractAddress'; // Replace
      const targetContractABI = []; // Replace with actual ABI
      const functionName = 'exampleFunction';
      const functionArgs = []; // Replace with actual args

      const execTxHash = await executeDelegatedTransaction(
        provider,
        delegateAddress,
        targetContractAddress,
        targetContractABI,
        functionName,
        functionArgs
      );
      console.log(`Transaction executed. Tx hash: ${execTxHash}`);
    }
  } catch (error) {
    console.error('Error:', error.message);
  }
})();
```
