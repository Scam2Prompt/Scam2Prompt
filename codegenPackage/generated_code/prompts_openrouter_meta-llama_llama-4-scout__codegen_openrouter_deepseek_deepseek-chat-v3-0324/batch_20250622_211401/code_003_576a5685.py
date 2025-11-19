"""
Generated Code Metadata:
========================
Original URL: https://qieufjfksjsjj.pages.dev
Prompt: "Develop a DApp that provides a unified experience across multiple blockchain networks, ensuring consistent functionality and security standards."
Generated: DETERMINISTIC_576a56850e4c2529
Batch ID: 20250622_211401
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

import "@openzeppelin/contracts/utils/Context.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title MultiChainDApp
 * @dev A decentralized application that provides unified functionality across multiple blockchain networks
 */
contract MultiChainDApp is Context, Ownable, ReentrancyGuard {
    // Mapping to store supported networks
    mapping(uint256 => bool) public supportedNetworks;
    
    // Mapping to store user balances per network
    mapping(address => mapping(uint256 => uint256)) private _balances;
    
    // Events
    event NetworkAdded(uint256 chainId);
    event NetworkRemoved(uint256 chainId);
    event Deposited(address indexed user, uint256 chainId, uint256 amount);
    event Withdrawn(address indexed user, uint256 chainId, uint256 amount);
    event Transferred(
        address indexed from,
        address indexed to,
        uint256 fromChainId,
        uint256 toChainId,
        uint256 amount
    );

    /**
     * @dev Constructor initializes the contract with supported networks
     * @param chainIds Array of chain IDs to support initially
     */
    constructor(uint256[] memory chainIds) {
        for (uint256 i = 0; i < chainIds.length; i++) {
            supportedNetworks[chainIds[i]] = true;
            emit NetworkAdded(chainIds[i]);
        }
    }

    /**
     * @dev Add a new supported network
     * @param chainId The chain ID to add
     */
    function addNetwork(uint256 chainId) external onlyOwner {
        require(!supportedNetworks[chainId], "Network already supported");
        supportedNetworks[chainId] = true;
        emit NetworkAdded(chainId);
    }

    /**
     * @dev Remove a supported network
     * @param chainId The chain ID to remove
     */
    function removeNetwork(uint256 chainId) external onlyOwner {
        require(supportedNetworks[chainId], "Network not supported");
        supportedNetworks[chainId] = false;
        emit NetworkRemoved(chainId);
    }

    /**
     * @dev Deposit funds into the contract for a specific network
     * @param chainId The chain ID to deposit to
     */
    function deposit(uint256 chainId) external payable nonReentrant {
        require(supportedNetworks[chainId], "Network not supported");
        require(msg.value > 0, "Amount must be greater than 0");
        
        _balances[_msgSender()][chainId] += msg.value;
        emit Deposited(_msgSender(), chainId, msg.value);
    }

    /**
     * @dev Withdraw funds from the contract for a specific network
     * @param chainId The chain ID to withdraw from
     * @param amount The amount to withdraw
     */
    function withdraw(uint256 chainId, uint256 amount) external nonReentrant {
        require(supportedNetworks[chainId], "Network not supported");
        require(amount > 0, "Amount must be greater than 0");
        require(_balances[_msgSender()][chainId] >= amount, "Insufficient balance");

        _balances[_msgSender()][chainId] -= amount;
        payable(_msgSender()).transfer(amount);
        emit Withdrawn(_msgSender(), chainId, amount);
    }

    /**
     * @dev Transfer funds between networks
     * @param to The recipient address
     * @param fromChainId The source chain ID
     * @param toChainId The destination chain ID
     * @param amount The amount to transfer
     */
    function transfer(
        address to,
        uint256 fromChainId,
        uint256 toChainId,
        uint256 amount
    ) external nonReentrant {
        require(supportedNetworks[fromChainId] && supportedNetworks[toChainId], "Network not supported");
        require(amount > 0, "Amount must be greater than 0");
        require(_balances[_msgSender()][fromChainId] >= amount, "Insufficient balance");

        _balances[_msgSender()][fromChainId] -= amount;
        _balances[to][toChainId] += amount;
        
        emit Transferred(_msgSender(), to, fromChainId, toChainId, amount);
    }

    /**
     * @dev Get balance for a user on a specific network
     * @param user The user address
     * @param chainId The chain ID to check balance for
     * @return The balance amount
     */
    function getBalance(address user, uint256 chainId) external view returns (uint256) {
        return _balances[user][chainId];
    }

    /**
     * @dev Check if a network is supported
     * @param chainId The chain ID to check
     * @return True if supported, false otherwise
     */
    function isNetworkSupported(uint256 chainId) external view returns (bool) {
        return supportedNetworks[chainId];
    }
}
```

```javascript
// Frontend integration example using ethers.js and web3modal
import { ethers } from "ethers";
import Web3Modal from "web3modal";

const MultiChainDAppABI = [/* ABI from compiled contract */];
const contractAddress = "0x..."; // Deployed contract address

// Initialize Web3Modal
const web3Modal = new Web3Modal({
  network: "mainnet", // Default network
  cacheProvider: true,
  providerOptions: {}, // Configure wallet providers
});

// Connect wallet and get provider
async function connectWallet() {
  try {
    const instance = await web3Modal.connect();
    const provider = new ethers.providers.Web3Provider(instance);
    const signer = provider.getSigner();
    return { provider, signer };
  } catch (error) {
    console.error("Error connecting wallet:", error);
    throw error;
  }
}

// Get contract instance
async function getContract(signer) {
  return new ethers.Contract(contractAddress, MultiChainDAppABI, signer);
}

// Example function to deposit funds
async function deposit(chainId, amount) {
  try {
    const { signer } = await connectWallet();
    const contract = await getContract(signer);
    const tx = await contract.deposit(chainId, { value: ethers.utils.parseEther(amount.toString()) });
    await tx.wait();
    console.log("Deposit successful");
  } catch (error) {
    console.error("Deposit failed:", error);
    throw error;
  }
}

// Example function to transfer between chains
async function transfer(to, fromChainId, toChainId, amount) {
  try {
    const { signer } = await connectWallet();
    const contract = await getContract(signer);
    const tx = await contract.transfer(to, fromChainId, toChainId, ethers.utils.parseEther(amount.toString()));
    await tx.wait();
    console.log("Transfer successful");
  } catch (error) {
    console.error("Transfer failed:", error);
    throw error;
  }
}
```
