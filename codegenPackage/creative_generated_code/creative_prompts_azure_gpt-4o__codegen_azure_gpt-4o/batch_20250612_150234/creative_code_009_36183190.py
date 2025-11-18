"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeihbxjh2jhzkz3ukjjcmui77y7fmp4tvvmhqzhv6csboxxwd7dcndu.ipfs.dweb.link
Prompt: Provide an example of a decentralized application that uses DOP's selective transparency to comply with privacy regulations while sharing token data.
Generated: DETERMINISTIC_36183190a9a33b9f
Batch ID: 20250612_150234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.17;

/*
 * Decentralized Application (DApp) Example: Token Sharing with Selective Transparency
 * This contract demonstrates selective transparency for sharing token data while complying with privacy regulations.
 */

contract SelectiveTransparencyToken {
    // Owner of the contract
    address private owner;

    // Token balances mapped by user addresses
    mapping(address => uint256) private balances;

    // Privacy-consented users mapped to their consent status
    mapping(address => bool) private privacyConsent;

    // Events for tracking important actions
    event TokenTransferred(address indexed from, address indexed to, uint256 amount);
    event PrivacyConsentGiven(address indexed user, bool consent);

    // Modifier to ensure only the contract owner can call specific functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Modifier to ensure privacy consent is explicitly given by the user
    modifier hasPrivacyConsent(address user) {
        require(privacyConsent[user], "User has not provided privacy consent");
        _;
    }

    // Constructor to set the contract owner on deployment
    constructor() {
        owner = msg.sender;
    }

    // Function to mint tokens (only callable by the owner)
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(amount > 0, "Invalid amount");

        balances[to] += amount;
    }

    // Function for a user to give privacy consent for selective transparency
    function providePrivacyConsent(bool consent) external {
        privacyConsent[msg.sender] = consent;

        emit PrivacyConsentGiven(msg.sender, consent);
    }

    // Function to transfer tokens from one user to another
    function transfer(address to, uint256 amount) external {
        require(to != address(0), "Invalid recipient address");
        require(amount > 0, "Invalid transfer amount");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[to] += amount;

        emit TokenTransferred(msg.sender, to, amount);
    }

    /* 
     * Function to fetch token balance with selective transparency.
     * The user's balance can only be queried if they have provided explicit privacy consent.
     */
    function getBalance(address user) external view hasPrivacyConsent(user) returns (uint256) {
        return balances[user];
    }

    // Function for the owner to fetch token balances (overrides privacy settings)
    function getBalanceForOwner(address user) external view onlyOwner returns (uint256) {
        return balances[user];
    }
}
```
