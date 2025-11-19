"""
Generated Code Metadata:
========================
Original URL: https://clean-4dq.pages.dev
Prompt: Write a smart contract that demonstrates the issuance of assets on SatoshiVM, utilizing its compatibility with the Ethereum ecosystem and native BTC gas.
Generated: DETERMINISTIC_49b4436a30851ed2
Batch ID: 20250612_152326
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

/**
 * @title AssetIssuer
 * @dev A smart contract for issuing and managing assets on SatoshiVM
 * with Ethereum compatibility and BTC gas support.
 */
contract AssetIssuer {
    // Owner of the contract
    address public owner;
    
    // Mapping to track issued assets
    mapping(address => uint256) public issuedAssets;
    
    // Mapping to track authorized issuers
    mapping(address => bool) public authorizedIssuers;
    
    // Event emitted when new assets are issued
    event AssetIssued(address indexed recipient, uint256 amount);
    
    // Event emitted when an issuer is authorized/revoked
    event IssuerAuthorization(address indexed issuer, bool authorized);
    
    // Modifier to restrict functions to owner only
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }
    
    // Modifier to restrict functions to authorized issuers only
    modifier onlyAuthorized() {
        require(authorizedIssuers[msg.sender] || msg.sender == owner, "Not authorized");
        _;
    }
    
    /**
     * @dev Constructor sets the deployer as the initial owner
     */
    constructor() {
        owner = msg.sender;
        authorizedIssuers[msg.sender] = true;
    }
    
    /**
     * @dev Issue new assets to a recipient
     * @param recipient Address to receive the assets
     * @param amount Amount of assets to issue
     */
    function issueAssets(address recipient, uint256 amount) external onlyAuthorized {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");
        
        issuedAssets[recipient] += amount;
        emit AssetIssued(recipient, amount);
    }
    
    /**
     * @dev Authorize or revoke an issuer
     * @param issuer Address of the issuer to modify
     * @param authorized Whether to authorize or revoke
     */
    function setIssuerAuthorization(address issuer, bool authorized) external onlyOwner {
        require(issuer != address(0), "Invalid issuer address");
        authorizedIssuers[issuer] = authorized;
        emit IssuerAuthorization(issuer, authorized);
    }
    
    /**
     * @dev Transfer ownership of the contract
     * @param newOwner Address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        owner = newOwner;
    }
    
    /**
     * @dev Get the balance of assets for an address
     * @param account Address to query
     * @return The balance of assets
     */
    function balanceOf(address account) external view returns (uint256) {
        return issuedAssets[account];
    }
    
    /**
     * @dev Check if an address is an authorized issuer
     * @param issuer Address to check
     * @return Whether the address is authorized
     */
    function isAuthorizedIssuer(address issuer) external view returns (bool) {
        return authorizedIssuers[issuer];
    }
}
```
