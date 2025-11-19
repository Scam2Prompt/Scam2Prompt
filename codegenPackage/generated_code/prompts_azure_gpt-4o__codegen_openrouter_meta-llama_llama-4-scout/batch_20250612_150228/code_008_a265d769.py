"""
Generated Code Metadata:
========================
Original URL: https://bafybeibp22amvhhrdkiajahcte2faf5d3vecbroua5yhnhk76jnpibn4de.ipfs.dweb.link
Prompt: Write code to implement chain abstraction using Particle Network's modular L1 infrastructure for seamless multi-chain user experience.
Generated: DETERMINISTIC_a265d7692d181440
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { ParticleNetwork, ParticleProvider, Ethers } = require('@particle-network/particle-ethers');
const { ethers } = require('ethers');

// Define a class for Chain Abstraction
class ChainAbstraction {
  /**
   * Initialize the ChainAbstraction instance
   * @param {string} projectId - Particle Network project ID
   * @param {string} clientKey - Particle Network client key
   * @param {string} appId - Particle Network app ID
   */
  constructor(projectId, clientKey, appId) {
    this.projectId = projectId;
    this.clientKey = clientKey;
    this.appId = appId;
    this.particleNetwork = new ParticleNetwork(projectId, clientKey, appId);
  }

  /**
   * Initialize the Ethers provider
   * @returns {Promise<ParticleProvider>}
   */
  async initEthersProvider() {
    try {
      const provider = new ParticleProvider(this.particleNetwork);
      return provider;
    } catch (error) {
      console.error('Error initializing Ethers provider:', error);
      throw error;
    }
  }

  /**
   * Get the current chain ID
   * @param {ParticleProvider} provider - Ethers provider instance
   * @returns {Promise<number>}
   */
  async getChainId(provider) {
    try {
      const chainId = await provider.getChainId();
      return chainId;
    } catch (error) {
      console.error('Error getting chain ID:', error);
      throw error;
    }
  }

  /**
   * Switch to a different chain
   * @param {ParticleProvider} provider - Ethers provider instance
   * @param {number} chainId - Target chain ID
   * @returns {Promise<void>}
   */
  async switchChain(provider, chainId) {
    try {
      await provider.switchChain(chainId);
    } catch (error) {
      console.error('Error switching chain:', error);
      throw error;
    }
  }

  /**
   * Send a transaction
   * @param {ParticleProvider} provider - Ethers provider instance
   * @param {string} to - Recipient address
   * @param {ethers.BigNumber} amount - Transaction amount
   * @returns {Promise<ethers.Transaction>}
   */
  async sendTransaction(provider, to, amount) {
    try {
      const signer = await provider.getSigner();
      const transaction = await signer.sendTransaction({
        to,
        value: amount,
      });
      return transaction;
    } catch (error) {
      console.error('Error sending transaction:', error);
      throw error;
    }
  }
}

// Example usage
async function main() {
  const projectId = 'YOUR_PROJECT_ID';
  const clientKey = 'YOUR_CLIENT_KEY';
  const appId = 'YOUR_APP_ID';

  const chainAbstraction = new ChainAbstraction(projectId, clientKey, appId);
  const provider = await chainAbstraction.initEthersProvider();
  const chainId = await chainAbstraction.getChainId(provider);
  console.log(`Current chain ID: ${chainId}`);

  const targetChainId = 5; // Ethereum Goerli testnet
  await chainAbstraction.switchChain(provider, targetChainId);
  const newChainId = await chainAbstraction.getChainId(provider);
  console.log(`Switched to chain ID: ${newChainId}`);

  const to = '0x... recipient address ...';
  const amount = ethers.utils.parseEther('1.0');
  const transaction = await chainAbstraction.sendTransaction(provider, to, amount);
  console.log(`Transaction hash: ${transaction.hash}`);
}

main().catch((error) => {
  console.error('Error:', error);
});
```
