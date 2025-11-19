"""
Generated Code Metadata:
========================
Original URL: https://biconomyprofum.com
Prompt: Generate code to implement a basic dapp using blockchain technology, focusing on enabling/disabling functionality based on user settings, like JavaScript enablement.
Generated: DETERMINISTIC_72b883d1ed696ea8
Batch ID: 20250622_212534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title FeatureToggle
 * @dev A smart contract that allows users to enable/disable features
 */
contract FeatureToggle {
    address public owner;
    mapping(address => mapping(string => bool)) private userFeatures;

    event FeatureToggled(address indexed user, string feature, bool enabled);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Toggle a feature for the caller
     * @param feature The name of the feature to toggle
     * @param enabled Whether to enable or disable the feature
     */
    function toggleFeature(string memory feature, bool enabled) public {
        userFeatures[msg.sender][feature] = enabled;
        emit FeatureToggled(msg.sender, feature, enabled);
    }

    /**
     * @dev Check if a feature is enabled for a user
     * @param user The address of the user to check
     * @param feature The name of the feature to check
     * @return bool Whether the feature is enabled
     */
    function isFeatureEnabled(address user, string memory feature) public view returns (bool) {
        return userFeatures[user][feature];
    }

    /**
     * @dev Transfer ownership of the contract
     * @param newOwner The address of the new owner
     */
    function transferOwnership(address newOwner) public onlyOwner {
        require(newOwner != address(0), "New owner cannot be zero address");
        owner = newOwner;
    }
}
```

```javascript
// Frontend JavaScript for interacting with the FeatureToggle contract
import Web3 from 'web3';
import FeatureToggleABI from './FeatureToggleABI.json';

const CONTRACT_ADDRESS = '0x123...'; // Replace with actual contract address

class FeatureToggleDapp {
  constructor() {
    this.web3 = null;
    this.contract = null;
    this.userAddress = null;
    this.initialize();
  }

  async initialize() {
    try {
      // Check if Web3 is injected (e.g., MetaMask)
      if (window.ethereum) {
        this.web3 = new Web3(window.ethereum);
        await window.ethereum.enable();
        this.userAddress = (await this.web3.eth.getAccounts())[0];
        
        // Initialize contract
        this.contract = new this.web3.eth.Contract(
          FeatureToggleABI,
          CONTRACT_ADDRESS
        );
        
        console.log('DApp initialized successfully');
      } else {
        throw new Error('No Ethereum provider detected');
      }
    } catch (error) {
      console.error('Initialization error:', error);
    }
  }

  async toggleFeature(feature, enabled) {
    try {
      if (!this.contract) throw new Error('Contract not initialized');
      
      await this.contract.methods
        .toggleFeature(feature, enabled)
        .send({ from: this.userAddress });
      
      console.log(`Feature "${feature}" ${enabled ? 'enabled' : 'disabled'}`);
    } catch (error) {
      console.error('Error toggling feature:', error);
    }
  }

  async checkFeature(feature) {
    try {
      if (!this.contract) throw new Error('Contract not initialized');
      
      const enabled = await this.contract.methods
        .isFeatureEnabled(this.userAddress, feature)
        .call();
      
      return enabled;
    } catch (error) {
      console.error('Error checking feature:', error);
      return false;
    }
  }
}

// Example usage
// const dapp = new FeatureToggleDapp();
// dapp.toggleFeature('javascript', true);
// const isEnabled = await dapp.checkFeature('javascript');
```
