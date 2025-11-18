"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hashai.pages.dev
Prompt: Create a Solidity contract that enables Hash & Node rental services, ensuring fair distribution of rewards to renters, as part of Hash AI's service expansion.
Generated: DETERMINISTIC_83631100dadc9024
Batch ID: 20250612_153517
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
 * @title HashNodeRental
 * @dev Contract for renting Hash & Nodes with fair rewards distribution.
 */
contract HashNodeRental {
    // Struct to hold renter details
    struct Renter {
        uint256 hashPower; // Representing rented hash power
        uint256 rewards;   // Rewards accumulated
    }

    address public owner; // Owner of the contract
    uint256 public totalHashPower; // Total available hash power
    uint256 public rewardPool; // Total rewards available for distribution

    mapping(address => Renter) public renters; // Mapping of renters by address
    address[] public renterAddresses; // Array to track all renters' addresses

    modifier onlyOwner() {
        require(msg.sender == owner, "You are not the owner");
        _;
    }

    // Events for logging activities in the contract
    event HashPowerRented(address indexed renter, uint256 hashPower);
    event RewardsDistributed(uint256 totalRewards);
    event RewardsClaimed(address indexed renter, uint256 rewards);

    /**
     * @dev Constructor to initialize the contract
     * @param _totalHashPower Initial total hash power available
     */
    constructor(uint256 _totalHashPower) {
        owner = msg.sender;
        totalHashPower = _totalHashPower;
    }

    /**
     * @dev Function for renting hash power
     * @param hashPower Amount of hash power to rent
     */
    function rentHashPower(uint256 hashPower) external payable {
        require(hashPower > 0, "Hash power must be greater than zero");
        require(totalHashPower >= hashPower, "Insufficient hash power available");
        require(msg.value > 0, "Payment must be greater than zero");

        totalHashPower -= hashPower; // Reduce available hash power

        if (renters[msg.sender].hashPower == 0) {
            // New renter, add to list
            renterAddresses.push(msg.sender);
        }

        renters[msg.sender].hashPower += hashPower;

        emit HashPowerRented(msg.sender, hashPower);
    }

    /**
     * @dev Function to distribute rewards to renters based on hash power rented
     * @param _rewardPool Amount of rewards to distribute
     */
    function distributeRewards(uint256 _rewardPool) external onlyOwner {
        require(_rewardPool > 0, "Reward pool must be greater than zero");
        require(renterAddresses.length > 0, "No renters available for rewards");

        rewardPool += _rewardPool; // Add rewards to the pool

        // Distribute rewards to renters based on their share of hash power
        for (uint256 i = 0; i < renterAddresses.length; i++) {
            address renterAddress = renterAddresses[i];
            Renter storage renter = renters[renterAddress];

            uint256 renterShare = (renter.hashPower * _rewardPool) / (totalHashPower + _rewardPool);
            renter.rewards += renterShare;
        }

        emit RewardsDistributed(_rewardPool);
    }

    /**
     * @dev Function for renters to claim their rewards
     */
    function claimRewards() external {
        Renter storage renter = renters[msg.sender];
        require(renter.rewards > 0, "No rewards available to claim");

        uint256 rewardsToClaim = renter.rewards;
        renter.rewards = 0; // Reset renter's rewards
        rewardPool -= rewardsToClaim; // Deduct from total reward pool

        (bool success, ) = msg.sender.call{value: rewardsToClaim}("");
        require(success, "Transfer failed");

        emit RewardsClaimed(msg.sender, rewardsToClaim);
    }

    /**
     * @dev Function to add more hash power to the pool
     * @param hashPower Amount of hash power to add
     */
    function addHashPower(uint256 hashPower) external onlyOwner {
        require(hashPower > 0, "Hash power must be greater than zero");
        totalHashPower += hashPower;
    }

    /**
     * @dev Function to withdraw contract funds
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdraw failed");
    }

    /**
     * @dev Fallback function to receive Ether
     */
    receive() external payable {}

    /**
     * @dev Function to retrieve renter details
     * @param renterAddress Address of the renter
     * @return hashPower Rented hash power
     * @return rewards Accumulated rewards
     */
    function getRenterDetails(address renterAddress)
        external
        view
        returns (uint256 hashPower, uint256 rewards)
    {
        Renter memory renter = renters[renterAddress];
        return (renter.hashPower, renter.rewards);
    }
}
```
