"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portal-coln.pages.dev
Prompt: Write a Solidity contract example for an airdrop system where tokens are automatically distributed to wallet addresses after the airdrop ends, similar to the $PORTAL token distribution process.
Generated: DETERMINISTIC_daf7b77a469bc007
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title AirdropContract
 * @dev A contract for automating token distribution after an airdrop event.
 */
contract AirdropContract {
    // Address of the ERC20 token being distributed
    address public tokenAddress;

    // Address of the contract owner
    address public owner;

    // Airdrop end timestamp
    uint256 public airdropEnd;

    // Mapping to track eligible participants and their token allocations
    mapping(address => uint256) public allocations;

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Modifier to ensure the airdrop has ended before executing certain functions
    modifier afterAirdropEnd() {
        require(block.timestamp >= airdropEnd, "Airdrop is still ongoing");
        _;
    }

    // Event to log token distributions
    event TokensDistributed(address indexed recipient, uint256 amount);

    /**
     * @dev Constructor to initialize the contract.
     * @param _tokenAddress Address of the ERC20 token being distributed.
     * @param _airdropEnd Timestamp when the airdrop ends.
     */
    constructor(address _tokenAddress, uint256 _airdropEnd) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_airdropEnd > block.timestamp, "Airdrop end must be in the future");

        tokenAddress = _tokenAddress;
        owner = msg.sender;
        airdropEnd = _airdropEnd;
    }

    /**
     * @dev Function to set token allocations for participants.
     * @param recipients Array of recipient addresses.
     * @param amounts Array of token amounts assigned to each recipient.
     */
    function setAllocations(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Arrays must be of equal length");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Invalid recipient address");
            allocations[recipients[i]] = amounts[i];
        }
    }

    /**
     * @dev Function to distribute tokens after the airdrop ends.
     * Iterates over the participants and transfers tokens to each.
     * @param recipients Array of recipient addresses to distribute tokens.
     */
    function distributeTokens(address[] calldata recipients) external afterAirdropEnd onlyOwner {
        for (uint256 i = 0; i < recipients.length; i++) {
            address recipient = recipients[i];
            uint256 amount = allocations[recipient];

            require(amount > 0, "No tokens allocated to this recipient");

            allocations[recipient] = 0; // Reset allocation to prevent re-distribution
            require(ERC20(tokenAddress).transfer(recipient, amount), "Token transfer failed");

            emit TokensDistributed(recipient, amount);
        }
    }

    /**
     * @dev Emergency function to withdraw tokens from the contract.
     * Can only be called by the owner.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(ERC20(tokenAddress).transfer(owner, amount), "Token transfer failed");
    }
}

/**
 * @dev Minimal ERC20 interface for interacting with the token contract.
 */
interface ERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
