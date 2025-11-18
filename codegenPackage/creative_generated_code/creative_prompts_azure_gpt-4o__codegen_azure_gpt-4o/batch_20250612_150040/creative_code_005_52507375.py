"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://faint-potato-small.on-fleek.app
Prompt: Write a smart contract to manage reward distribution for the BNB Chain Airdrop Alliance Program, ensuring compatibility with BSC and opBNB.
Generated: DETERMINISTIC_52507375c82ba072
Batch ID: 20250612_150040
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
 * @title RewardDistribution
 * @dev A smart contract to manage reward distribution for the BNB Chain Airdrop Alliance Program.
 * Compatible with BSC and opBNB.
 */
contract RewardDistribution {
    // Address of the contract owner
    address public owner;

    // Mapping to track airdrop recipients and their rewards
    mapping(address => uint256) public rewards;

    // Event to notify reward distribution
    event RewardDistributed(address indexed recipient, uint256 amount);

    // Event for ownership transfer
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to transfer ownership of the contract.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Function to set rewards for a list of recipients.
     * @param recipients Array of recipient addresses.
     * @param amounts Array of reward amounts corresponding to each recipient.
     */
    function setRewards(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Recipients and amounts arrays must have the same length");

        for (uint256 i = 0; i < recipients.length; i++) {
            rewards[recipients[i]] = amounts[i];
        }
    }

    /**
     * @dev Function to claim rewards by recipients.
     * Transfers the reward to the caller if eligible.
     */
    function claimReward() external {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards available to claim");

        rewards[msg.sender] = 0;

        (bool success, ) = msg.sender.call{value: reward}("");
        require(success, "Reward transfer failed");

        emit RewardDistributed(msg.sender, reward);
    }

    /**
     * @dev Function to deposit BNB to the contract for reward distribution.
     * Allows the owner to deposit BNB.
     */
    function deposit() external payable onlyOwner {
        require(msg.value > 0, "Deposit amount must be greater than zero");
    }

    /**
     * @dev Function to withdraw leftover BNB from the contract.
     * @param amount Amount of BNB to withdraw.
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient contract balance");

        (bool success, ) = owner.call{value: amount}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Fallback function to accept BNB deposits directly into the contract.
     */
    receive() external payable {}
}
```

Note: Ensure to test the contract thoroughly before deploying it in a production environment. Proper audits are also recommended for security reasons.
