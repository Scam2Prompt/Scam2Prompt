"""
Generated Code Metadata:
========================
Original URL: https://synthesizations.netlify.app
Prompt: What are some best practices for building a decentralized dapp that interacts with various wallets and blockchain networks, and how can I implement a whitelist feature for trusted payment sources?
Generated: DETERMINISTIC_42a11efb9fb9d595
Batch ID: 20250622_205529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Address.sol";

/**
 * @title WhitelistedPaymentContract
 * @dev Implements whitelist functionality for trusted payment sources
 */
contract WhitelistedPaymentContract is Ownable {
    using Address for address;

    mapping(address => bool) private _whitelistedAddresses;
    address[] private _whitelist;

    event AddressWhitelisted(address indexed account);
    event AddressRemovedFromWhitelist(address indexed account);

    /**
     * @dev Modifier to check if sender is whitelisted
     */
    modifier onlyWhitelisted() {
        require(_whitelistedAddresses[msg.sender], "Sender not whitelisted");
        _;
    }

    /**
     * @dev Add address to whitelist
     * @param _address Address to be added to whitelist
     */
    function addToWhitelist(address _address) external onlyOwner {
        require(!_whitelistedAddresses[_address], "Address already whitelisted");
        require(_address != address(0), "Invalid address");
        
        _whitelistedAddresses[_address] = true;
        _whitelist.push(_address);
        emit AddressWhitelisted(_address);
    }

    /**
     * @dev Remove address from whitelist
     * @param _address Address to be removed from whitelist
     */
    function removeFromWhitelist(address _address) external onlyOwner {
        require(_whitelistedAddresses[_address], "Address not whitelisted");
        
        _whitelistedAddresses[_address] = false;
        
        // Remove from array
        for (uint256 i = 0; i < _whitelist.length; i++) {
            if (_whitelist[i] == _address) {
                _whitelist[i] = _whitelist[_whitelist.length - 1];
                _whitelist.pop();
                break;
            }
        }
        
        emit AddressRemovedFromWhitelist(_address);
    }

    /**
     * @dev Check if address is whitelisted
     * @param _address Address to check
     * @return bool True if whitelisted
     */
    function isWhitelisted(address _address) public view returns (bool) {
        return _whitelistedAddresses[_address];
    }

    /**
     * @dev Get all whitelisted addresses
     * @return address[] Array of whitelisted addresses
     */
    function getWhitelist() public view returns (address[] memory) {
        return _whitelist;
    }

    /**
     * @dev Example payable function that only accepts whitelisted addresses
     */
    function processPayment() external payable onlyWhitelisted {
        // Payment processing logic here
        require(msg.value > 0, "Payment amount must be greater than 0");
    }
}
```

```javascript
// Frontend implementation using ethers.js and web3modal
import { ethers } from 'ethers';
import Web3Modal from 'web3modal';

// Configuration for multiple wallet providers
const providerOptions = {
  walletconnect: {
    package: WalletConnectProvider,
    options: {
      infuraId: "YOUR_INFURA_ID"
    }
  },
  metamask: {
    package: true
  },
  // Add other wallet providers as needed
};

const web3Modal = new Web3Modal({
  network: "mainnet", // Optional - change to desired network
  cacheProvider: true, // Optional
  providerOptions // Required
});

// Connect wallet function
async function connectWallet() {
  try {
    const instance = await web3Modal.connect();
    const provider = new ethers.providers.Web3Provider(instance);
    const signer = provider.getSigner();
    const address = await signer.getAddress();
    
    return {
      provider,
      signer,
      address
    };
  } catch (error) {
    console.error("Error connecting wallet:", error);
    throw error;
  }
}

// Check if address is whitelisted
async function checkWhitelist(contractAddress, abi, userAddress) {
  try {
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const contract = new ethers.Contract(contractAddress, abi, provider);
    const isWhitelisted = await contract.isWhitelisted(userAddress);
    return isWhitelisted;
  } catch (error) {
    console.error("Error checking whitelist:", error);
    throw error;
  }
}

// Process payment function
async function processPayment(contractAddress, abi, signer, amount) {
  try {
    const contract = new ethers.Contract(contractAddress, abi, signer);
    const tx = await contract.processPayment({ value: ethers.utils.parseEther(amount) });
    await tx.wait();
    return tx.hash;
  } catch (error) {
    console.error("Payment processing failed:", error);
    throw error;
  }
}
```
