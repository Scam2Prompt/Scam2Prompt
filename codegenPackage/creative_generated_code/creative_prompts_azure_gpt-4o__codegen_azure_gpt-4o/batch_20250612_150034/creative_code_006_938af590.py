"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xai327k.com
Prompt: Write a smart contract in Solidity for managing xAI327K token presale contributions and distributing bonuses.
Generated: DETERMINISTIC_938af590b3f08c40
Batch ID: 20250612_150034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

/**
 * @title xAI327K Token Presale Contract
 * @dev This contract manages presale contributions and bonus distributions
 */
contract xAI327KPresale {
    // Token presale configuration
    address public owner; // Owner of the contract
    uint256 public constant TOKEN_PRICE = 0.001 ether; // Token price in wei
    uint256 public constant BONUS_THRESHOLD = 3 ether; // Contribution threshold for bonus eligibility
    uint256 public constant BONUS_PERCENTAGE = 10; // Bonus percentage (10%)

    // Track contributions
    mapping(address => uint256) public contributions;
    mapping(address => uint256) public bonuses;

    // Events
    event ContributionReceived(address indexed contributor, uint256 amount, uint256 tokensIssued);
    event BonusDistributed(address indexed contributor, uint256 bonusTokens);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows a user to contribute ether and receive tokens
     */
    function contribute() external payable {
        require(msg.value > 0, "Contribution must be greater than zero");

        uint256 tokenAmount = msg.value / TOKEN_PRICE; // Calculate token amount
        contributions[msg.sender] += tokenAmount; // Update contributor's balance

        // Check for bonus eligibility
        if (msg.value >= BONUS_THRESHOLD) {
            uint256 bonusTokens = (tokenAmount * BONUS_PERCENTAGE) / 100; // Calculate bonus tokens
            bonuses[msg.sender] += bonusTokens; // Update bonus balance
            emit BonusDistributed(msg.sender, bonusTokens);
        }

        emit ContributionReceived(msg.sender, msg.value, tokenAmount);
    }

    /**
     * @dev Allows the owner to withdraw all ether from the contract
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Returns the contributor's total token balance including bonuses
     * @param contributor The address of the contributor
     */
    function getTotalBalance(address contributor) external view returns (uint256) {
        return contributions[contributor] + bonuses[contributor];
    }

    /**
     * @dev Fallback function to prevent accidental ether transfers
     */
    fallback() external payable {
        revert("Ether cannot be sent directly to the contract");
    }

    /**
     * @dev Receive function for handling direct ether transfers
     */
    receive() external payable {
        revert("Ether cannot be received directly");
    }
}
```
