"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbitcoins-io.web.app
Prompt: Write a Solidity contract to manage community rewards distribution for $GBTC holders, allocating 5% of the tokenomics as described in the Green Bitcoin documentation.
Generated: DETERMINISTIC_ac96416e3923b15c
Batch ID: 20250612_145213
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
 * @title CommunityRewards
 * @dev This contract manages the distribution of community rewards
 *      for $GBTC holders, allocating 5% of the tokenomics as per
 *      the Green Bitcoin documentation.
 */
contract CommunityRewards {
    address public owner;

    // Mapping to track rewards for each address
    mapping(address => uint256) public rewards;

    // Total rewards pool (set as 5% of tokenomics, to be funded externally)
    uint256 public totalRewardsPool;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed recipient, uint256 amount);

    // Event emitted when the rewards pool is funded
    event RewardsPoolFunded(uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Constructor to initialize the contract
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to fund the rewards pool.
     * @param amount The amount of ether to add to the rewards pool.
     */
    function fundRewardsPool() external payable onlyOwner {
        require(msg.value > 0, "Funding amount must be greater than zero");
        totalRewardsPool += msg.value;

        emit RewardsPoolFunded(msg.value);
    }

    /**
     * @dev Function to distribute rewards to a specific address.
     * @param recipient The address of the reward recipient.
     * @param amount The reward amount to distribute.
     */
    function distributeReward(address payable recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");
        require(amount <= totalRewardsPool, "Insufficient rewards pool");

        // Deduct the reward from the rewards pool
        totalRewardsPool -= amount;

        // Track rewards for the recipient
        rewards[recipient] += amount;

        // Transfer the reward to the recipient
        (bool success, ) = recipient.call{value: amount}("");
        require(success, "Reward transfer failed");

        emit RewardsDistributed(recipient, amount);
    }

    /**
     * @dev Function to check the balance of the contract.
     * @return The current balance of the contract in wei.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }

    /**
     * @dev Fallback function to accept ETH.
     */
    receive() external payable {
        // Accept ETH sent directly to the contract but does not add it to the rewards pool
    }
}
```
