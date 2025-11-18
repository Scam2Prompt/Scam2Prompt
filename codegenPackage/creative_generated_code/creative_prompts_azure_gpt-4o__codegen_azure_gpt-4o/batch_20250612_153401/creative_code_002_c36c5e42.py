"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-apedinbase.pages.dev
Prompt: Using Solidity, write a smart contract function that enforces the contribution limits (min: 0.1 ETH, max: 0.5 ETH) for the $APED presale as described on the webpage.
Generated: DETERMINISTIC_c36c5e428fbec9ef
Batch ID: 20250612_153401
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
 * @title APEDPresale
 * @dev Smart contract to manage the APED token presale with contribution limits.
 */
contract APEDPresale {
    // State variables
    address public owner; // Owner of the presale contract
    uint256 public constant MIN_CONTRIBUTION = 0.1 ether; // Minimum contribution limit
    uint256 public constant MAX_CONTRIBUTION = 0.5 ether; // Maximum contribution limit
    mapping(address => uint256) public contributions; // Tracks contributions of each participant

    /**
     * @dev Modifier to restrict function access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    /**
     * @dev Constructor sets the owner of the contract.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows participants to contribute ETH to the presale within defined limits.
     * Emits an event for successful contributions.
     */
    function contribute() external payable {
        // Validate contribution amount
        require(msg.value >= MIN_CONTRIBUTION, "Contribution must be at least 0.1 ETH");
        require(msg.value <= MAX_CONTRIBUTION, "Contribution must not exceed 0.5 ETH");

        // Update contributions
        contributions[msg.sender] += msg.value;

        // Emit event for successful contribution
        emit ContributionReceived(msg.sender, msg.value);
    }

    /**
     * @dev Allows the owner to withdraw all collected ETH.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available for withdrawal");

        // Transfer all ETH to the owner
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Failed to transfer funds to the owner");
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("Direct transfers are not allowed. Use the contribute function.");
    }

    /**
     * @dev Receive function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct transfers are not allowed. Use the contribute function.");
    }

    /**
     * @dev Event emitted when a participant successfully contributes to the presale.
     * @param contributor Address of the contributor.
     * @param amount Amount of ETH contributed.
     */
    event ContributionReceived(address indexed contributor, uint256 amount);
}
```
