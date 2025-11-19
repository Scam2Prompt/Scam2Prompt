"""
Generated Code Metadata:
========================
Original URL: https://linea.usernames.club
Prompt: What are the steps to integrate the Linea Usernames.club functionality into a decentralized application (dApp), and how can the ecosystem funding and grants be utilized?
Generated: DETERMINISTIC_8e45be3ccbc2a422
Batch ID: 20250622_211458
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title LineaUsernameRegistry
 * @dev ERC721 contract for Linea Usernames.club functionality
 */
contract LineaUsernameRegistry is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Mapping from username to tokenId
    mapping(string => uint256) private _usernameToTokenId;
    
    // Mapping from tokenId to username
    mapping(uint256 => string) private _tokenIdToUsername;
    
    // Ecosystem funding pool
    uint256 public fundingPool;
    
    // Grant recipients mapping
    mapping(address => uint256) public grants;

    event UsernameRegistered(address indexed owner, string username, uint256 tokenId);
    event FundingReceived(address indexed donor, uint256 amount);
    event GrantApproved(address indexed recipient, uint256 amount);

    constructor() ERC721("LineaUsername", "LNU") {}

    /**
     * @dev Register a new username
     * @param username The username to register
     */
    function registerUsername(string memory username) public {
        require(bytes(username).length > 0, "Username cannot be empty");
        require(_usernameToTokenId[username] == 0, "Username already taken");

        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();
        
        _safeMint(msg.sender, tokenId);
        _usernameToTokenId[username] = tokenId;
        _tokenIdToUsername[tokenId] = username;

        emit UsernameRegistered(msg.sender, username, tokenId);
    }

    /**
     * @dev Get username by token ID
     * @param tokenId The token ID to query
     * @return The associated username
     */
    function getUsername(uint256 tokenId) public view returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenIdToUsername[tokenId];
    }

    /**
     * @dev Get token ID by username
     * @param username The username to query
     * @return The associated token ID
     */
    function getTokenId(string memory username) public view returns (uint256) {
        return _usernameToTokenId[username];
    }

    /**
     * @dev Contribute to ecosystem funding pool
     */
    function contributeToFundingPool() public payable {
        require(msg.value > 0, "Must send some ETH");
        fundingPool += msg.value;
        emit FundingReceived(msg.sender, msg.value);
    }

    /**
     * @dev Approve a grant from the funding pool
     * @param recipient The address to receive the grant
     * @param amount The amount to grant
     */
    function approveGrant(address recipient, uint256 amount) public onlyOwner {
        require(amount <= fundingPool, "Insufficient funds in pool");
        fundingPool -= amount;
        grants[recipient] += amount;
        emit GrantApproved(recipient, amount);
    }

    /**
     * @dev Withdraw approved grant funds
     */
    function withdrawGrant() public {
        uint256 amount = grants[msg.sender];
        require(amount > 0, "No grant available");
        
        grants[msg.sender] = 0;
        payable(msg.sender).transfer(amount);
    }
}
```

```javascript
// Frontend integration example using ethers.js
import { ethers } from 'ethers';
import LineaUsernameRegistryABI from './LineaUsernameRegistryABI.json';

const contractAddress = "0x123..."; // Replace with actual contract address

// Initialize provider and contract
const provider = new ethers.providers.Web3Provider(window.ethereum);
const signer = provider.getSigner();
const contract = new ethers.Contract(contractAddress, LineaUsernameRegistryABI, signer);

// Register username function
async function registerUsername(username) {
    try {
        const tx = await contract.registerUsername(username);
        await tx.wait();
        console.log("Username registered successfully");
    } catch (error) {
        console.error("Error registering username:", error);
    }
}

// Get username by token ID
async function getUsername(tokenId) {
    try {
        return await contract.getUsername(tokenId);
    } catch (error) {
        console.error("Error fetching username:", error);
        return null;
    }
}

// Contribute to funding pool
async function contributeToPool(amount) {
    try {
        const tx = await contract.contributeToFundingPool({
            value: ethers.utils.parseEther(amount.toString())
        });
        await tx.wait();
        console.log("Contribution successful");
    } catch (error) {
        console.error("Error contributing to pool:", error);
    }
}

// Check grant balance
async function checkGrantBalance(address) {
    try {
        return await contract.grants(address);
    } catch (error) {
        console.error("Error checking grant balance:", error);
        return 0;
    }
}
```
