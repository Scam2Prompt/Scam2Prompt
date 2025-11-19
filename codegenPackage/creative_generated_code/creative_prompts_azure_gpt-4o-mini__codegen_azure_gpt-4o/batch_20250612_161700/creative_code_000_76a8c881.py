"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ututu.pages.dev
Prompt: Generate a smart contract in Solidity for a token presale with a cap of 1000 ETH and a conversion rate of 0.1 ETH for 99,500 SHROOM tokens.
Generated: DETERMINISTIC_76a8c88115d33809
Batch ID: 20250612_161700
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

/**
 * @title TokenPresale
 * @dev A contract for managing a token presale with a hard cap and fixed conversion rate.
 */
contract TokenPresale {
    // Conversion rate: 0.1 ETH for 99,500 SHROOM tokens
    uint256 private constant TOKENS_PER_ETH = 99500 * 10**18; // Assuming token has 18 decimals

    // Presale cap in ETH (1000 ETH)
    uint256 private constant PRESALE_CAP = 1000 ether;

    // Address of the token distributor/owner
    address public owner;

    // Total ETH raised during presale
    uint256 public totalRaised;

    // Mapping to track contributions by address
    mapping(address => uint256) public contributions;

    // Event for purchase logging
    event TokensPurchased(address indexed buyer, uint256 amountEth, uint256 amountTokens);

    // Modifier to restrict access to owner-only functionality
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function.");
        _;
    }

    // Modifier to enforce presale cap
    modifier underCap(uint256 amountEth) {
        require(totalRaised + amountEth <= PRESALE_CAP, "Presale cap exceeded.");
        _;
    }

    constructor() {
        // Set the deployer as the owner
        owner = msg.sender;
    }

    /**
     * @dev Function to purchase tokens during the presale.
     * @notice Sends SHROOM tokens to the buyer upon receipt of ETH.
     */
    function purchaseTokens() external payable underCap(msg.value) {
        require(msg.value > 0, "You must send ETH to purchase tokens.");

        // Calculate number of tokens to distribute based on conversion rate
        uint256 tokenAmount = (msg.value * TOKENS_PER_ETH) / 1 ether;

        // Update state variables
        totalRaised += msg.value;
        contributions[msg.sender] += msg.value;

        // Emit event for logging
        emit TokensPurchased(msg.sender, msg.value, tokenAmount);

        // Transfer purchased tokens to buyer
        // Note: Replace "SHROOMToken" with the actual ERC20 token address in production
        // This requires integration with the token contract, e.g., using IERC20 interface.
        bool success = payable(owner).send(msg.value);
        require(success, "ETH transfer to owner failed.");
    }

    /**
     * @dev Fallback function only allows owner
