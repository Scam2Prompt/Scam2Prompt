"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xipon.pages.dev
Prompt: Create a smart contract example for managing rewards distribution in the Xion DeFi ecosystem, ensuring compatibility with the BonusBlock protocol.
Generated: DETERMINISTIC_3c88ee3e2a81413c
Batch ID: 20250612_151947
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
 * @title RewardsDistribution
 * @dev A smart contract to manage rewards distribution in the Xion DeFi ecosystem
 *      with compatibility for the BonusBlock protocol.
 */
contract RewardsDistribution {
    // Address of the owner (admin) of the contract
    address public owner;

    // Mapping to store user balances
    mapping(address => uint256) public userRewards;

    // Total rewards available in the contract
    uint256 public totalRewards;

    // Event to notify reward distribution
    event RewardDistributed(address indexed user, uint256 amount);

    // Event to notify fund deposit
    event FundsDeposited(address indexed from, uint256 amount);

    // Event to notify ownership transfer
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to deposit funds into the contract. Only the owner can call this.
     * @param amount Amount to be deposited (in wei).
     */
    function depositFunds(uint256 amount) external payable onlyOwner {
        require(msg.value == amount, "Incorrect deposit value");
        totalRewards += amount;
        emit FundsDeposited(msg.sender, amount);
    }

    /**
     * @dev Function to distribute rewards to a specific user.
     * @param user Address of the user.
     * @param amount Amount of rewards to distribute (in wei).
     */
    function distributeReward(address user, uint256 amount) external onlyOwner {
        require(totalRewards >= amount, "Insufficient rewards in the contract");
        require(user != address(0), "Invalid user address");

        // Update state variables
        userRewards[user] += amount;
        totalRewards -= amount;

        emit RewardDistributed(user, amount);
    }

    /**
     * @dev Function for users to claim their rewards.
     */
    function claimReward() external {
        uint256 reward = userRewards[msg.sender];
        require(reward > 0, "No rewards available to claim");

        userRewards[msg.sender] = 0; // Reset reward balance before transfer
        payable(msg.sender).transfer(reward); // Transfer the reward

        emit RewardDistributed(msg.sender, reward);
    }

    /**
     * @dev Function to transfer ownership to a new owner. Only the current owner can call this.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Fallback function to receive Ether. Ensures the contract can handle direct transfers.
     */
    receive() external payable {
        totalRewards += msg.value;
        emit FundsDeposited(msg.sender, msg.value);
    }

    /**
     * @dev Function to retrieve the current balance of the contract.
     * @return Contract balance in wei.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }

    /**
     * @dev Function to retrieve the reward balance of a specific user.
     * @param user Address of the user.
     * @return Reward balance of the user in wei.
     */
    function getUserReward(address user) external view returns (uint256) {
        return userRewards[user];
    }
}
```
