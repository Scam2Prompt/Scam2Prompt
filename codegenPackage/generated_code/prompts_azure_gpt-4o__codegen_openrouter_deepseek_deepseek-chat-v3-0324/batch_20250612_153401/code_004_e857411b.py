"""
Generated Code Metadata:
========================
Original URL: https://atlasnft.pages.dev
Prompt: Write a JavaScript module to integrate NAVI token staking and vesting functionality with a connected wallet, as described on the Atlas Navi website.
Generated: DETERMINISTIC_e857411b1c48f2ff
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * NAVI Token Staking and Vesting Module
 * Integrates with wallet providers to handle staking and vesting operations
 */

const NaviStakingVesting = (() => {
  // Constants
  const CONTRACT_ADDRESS = '0x...'; // Replace with actual contract address
  const ABI = [/* Insert ABI here */];
  const NETWORK_ID = 1; // Mainnet by default
  
  // State variables
  let web3;
  let contract;
  let account;
  let provider;
  
  /**
   * Initialize the module with a web3 provider
   * @param {Object} provider - Web3 provider (e.g., from MetaMask)
   * @returns {Promise<boolean>} - True if initialized successfully
   */
  const init = async (walletProvider) => {
    try {
      if (!walletProvider) {
        throw new Error('Wallet provider is required');
      }
      
      provider = walletProvider;
      web3 = new Web3(provider);
      
      // Check network
      const chainId = await web3.eth.getChainId();
      if (chainId !== NETWORK_ID) {
        throw new Error(`Please connect to network with ID: ${NETWORK_ID}`);
      }
      
      // Initialize contract
      contract = new web3.eth.Contract(ABI, CONTRACT_ADDRESS);
      
      // Get accounts
      const accounts = await web3.eth.getAccounts();
      if (accounts.length === 0) {
        throw new Error('No accounts found');
      }
      account = accounts[0];
      
      return true;
    } catch (error) {
      console.error('Initialization error:', error);
      throw error;
    }
  };
  
  /**
   * Stake NAVI tokens
   * @param {string} amount - Amount to stake in wei
   * @param {number} lockPeriod - Lock period in days
   * @returns {Promise<Object>} - Transaction receipt
   */
  const stakeTokens = async (amount, lockPeriod) => {
    try {
      if (!web3 || !contract) {
        throw new Error('Module not initialized');
      }
      
      if (!amount || amount <= 0) {
        throw new Error('Invalid stake amount');
      }
      
      if (!lockPeriod || lockPeriod <= 0) {
        throw new Error('Invalid lock period');
      }
      
      const tx = await contract.methods.stake(amount, lockPeriod)
        .send({ from: account });
      
      return tx;
    } catch (error) {
      console.error('Staking error:', error);
      throw error;
    }
  };
  
  /**
   * Withdraw staked tokens after vesting period
   * @param {string} stakeId - ID of the stake to withdraw
   * @returns {Promise<Object>} - Transaction receipt
   */
  const withdrawStake = async (stakeId) => {
    try {
      if (!web3 || !contract) {
        throw new Error('Module not initialized');
      }
      
      if (!stakeId) {
        throw new Error('Stake ID is required');
      }
      
      const tx = await contract.methods.withdraw(stakeId)
        .send({ from: account });
      
      return tx;
    } catch (error) {
      console.error('Withdrawal error:', error);
      throw error;
    }
  };
  
  /**
   * Claim vested tokens
   * @param {string} vestingId - ID of the vesting schedule
   * @returns {Promise<Object>} - Transaction receipt
   */
  const claimVestedTokens = async (vestingId) => {
    try {
      if (!web3 || !contract) {
        throw new Error('Module not initialized');
      }
      
      if (!vestingId) {
        throw new Error('Vesting ID is required');
      }
      
      const tx = await contract.methods.claim(vestingId)
        .send({ from: account });
      
      return tx;
    } catch (error) {
      console.error('Claim error:', error);
      throw error;
    }
  };
  
  /**
   * Get user's active stakes
   * @returns {Promise<Array>} - Array of stake objects
   */
  const getActiveStakes = async () => {
    try {
      if (!web3 || !contract) {
        throw new Error('Module not initialized');
      }
      
      const stakes = await contract.methods.getUserStakes(account).call();
      return stakes;
    } catch (error) {
      console.error('Error fetching stakes:', error);
      throw error;
    }
  };
  
  /**
   * Get user's vesting schedules
   * @returns {Promise<Array>} - Array of vesting schedule objects
   */
  const getVestingSchedules = async () => {
    try {
      if (!web3 || !contract) {
        throw new Error('Module not initialized');
      }
      
      const vestings = await contract.methods.getUserVestings(account).call();
      return vestings;
    } catch (error) {
      console.error('Error fetching vestings:', error);
      throw error;
    }
  };
  
  /**
   * Get available rewards for a stake
   * @param {string} stakeId - ID of the stake
   * @returns {Promise<string>} - Reward amount in wei
   */
  const getPendingRewards = async (stakeId) => {
    try {
      if (!web3 || !contract) {
        throw new Error('Module not initialized');
      }
      
      if (!stakeId) {
        throw new Error('Stake ID is required');
      }
      
      const rewards = await contract.methods.pendingRewards(stakeId).call();
      return rewards;
    } catch (error) {
      console.error('Error fetching rewards:', error);
      throw error;
    }
  };
  
  /**
   * Get current wallet address
   * @returns {string} - Connected wallet address
   */
  const getWalletAddress = () => {
    return account;
  };
  
  return {
    init,
    stakeTokens,
    withdrawStake,
    claimVestedTokens,
    getActiveStakes,
    getVestingSchedules,
    getPendingRewards,
    getWalletAddress
  };
})();

// Export for ES modules
export default NaviStakingVesting;

// For CommonJS environments
if (typeof module !== 'undefined' && module.exports) {
  module.exports = NaviStakingVesting;
}
```
