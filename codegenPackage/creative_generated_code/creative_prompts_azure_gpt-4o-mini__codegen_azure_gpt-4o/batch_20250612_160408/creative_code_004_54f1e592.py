"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zoracoin.io
Prompt: Provide an example of a Solidity contract that allows users to buy ZORA tokens during the presale phase with a bonus incentive.
Generated: DETERMINISTIC_54f1e59230072517
Batch ID: 20250612_160408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title ZoraPresale
 * @dev A smart contract to handle the presale of ZORA tokens with a bonus incentive.
 */
contract ZoraPresale {
    // Address of the owner (contract deployer).
    address public owner;

    // Token price in wei (1 ZORA token = tokenPrice wei).
    uint256 public tokenPrice;

    // Bonus percentage for presale (e.g., 10% bonus => bonusPercentage = 10).
    uint256 public bonusPercentage;

    // Total ZORA tokens available for presale.
    uint256 public presaleSupply;

    // Mapping to track user token purchases.
    mapping(address => uint256) public balances;

    // Flag to indicate if presale is active.
    bool public presaleActive;

    // Event emitted when tokens are bought during presale.
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 bonusAmount);

    // Modifier to restrict access to owner-only functions.
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Modifier to ensure presale is active.
    modifier presaleIsActive() {
        require(presaleActive, "Presale is not active");
        _;
    }

    /**
     * @dev Constructor to initialize the presale contract.
     * @param _tokenPrice Price of one ZORA token in wei.
     * @param _bonusPercentage Bonus percentage during presale.
     * @param _presaleSupply Total tokens available for presale.
     */
    constructor(uint256 _tokenPrice, uint256 _bonusPercentage, uint256 _presaleSupply) {
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(_bonusPercentage >= 0 && _bonusPercentage <= 100, "Invalid bonus percentage");
        require(_presaleSupply > 0, "Presale supply must be greater than zero");

        owner = msg.sender;
        tokenPrice = _tokenPrice;
        bonusPercentage = _bonusPercentage;
        presaleSupply = _presaleSupply;
        presaleActive = true;
    }

    /**
     * @dev Function to buy tokens during the presale.
     */
    function buyTokens() external payable presaleIsActive {
        require(msg.value > 0, "You must send some Ether to buy tokens");

        // Calculate the number of tokens based on the amount sent.
        uint256 tokens = msg.value / tokenPrice;
        require(tokens > 0, "Insufficient Ether sent to buy tokens");
        require(tokens <= presaleSupply, "Not enough tokens available for presale");

        // Calculate bonus tokens.
        uint256 bonusTokens = (tokens * bonusPercentage) / 100;

        // Update state variables.
        balances[msg.sender] += tokens + bonusTokens;
        presaleSupply -= tokens;

        // Emit event for token purchase.
        emit TokensPurchased(msg.sender, tokens, bonusTokens);
    }

    /**
     * @dev Function for the owner to end the presale.
     */
    function endPresale() external onlyOwner {
        require(presaleActive, "Presale is already ended");
        presaleActive = false;
    }

    /**
     * @dev Function for the owner to withdraw Ether collected during presale.
     */
    function withdrawFunds() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds to withdraw");
        payable(owner).transfer(contractBalance);
    }

    /**
     * @dev Function to check the total balance of the contract (presale funds received).
     */
    function contractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
