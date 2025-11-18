"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeigix4apwqk6fyecm444vwmi65rxaxhb23mlme4in2u5oa4cl7abza.ipfs.dweb.link
Prompt: Generate Solidity code for deploying a decentralized application (dApp) on the Botanix EVM that utilizes Bitcoin as the native asset for staking.
Generated: DETERMINISTIC_47e9317d1bc131ff
Batch ID: 20250612_152249
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

// Decentralized application (dApp) contract for staking Bitcoin (BTC) on Botanix EVM
contract BitcoinStakingDApp {
    // Struct to hold staking information
    struct Stake {
        uint256 amount; // Amount of BTC staked
        uint256 timestamp; // Timestamp when the staking occurred
    }

    // Mapping to store stakes by user address
    mapping(address => Stake) private stakes;

    // Total BTC staked in the contract
    uint256 private totalStaked;

    // Event to notify when a user stakes BTC
    event Staked(address indexed user, uint256 amount);

    // Event to notify when a user withdraws staked BTC
    event Withdrawn(address indexed user, uint256 amount);

    // Modifier to ensure a valid stake amount
    modifier validStakeAmount(uint256 amount) {
        require(amount > 0, "Stake amount must be greater than zero.");
        _;
    }

    /**
     * @dev Function to stake BTC in the contract.
     * @param amount The amount of BTC to stake.
     */
    function stake(uint256 amount) external validStakeAmount(amount) {
        // Update the user's stake
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.timestamp = block.timestamp;

        // Update total staked BTC
        totalStaked += amount;

        // Emit the staking event
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw staked BTC.
     */
    function withdraw() external {
        // Retrieve the user's stake
        Stake storage userStake = stakes[msg.sender];
        uint256 amount = userStake.amount;

        // Ensure the user has staked BTC
        require(amount > 0, "No BTC staked to withdraw.");

        // Reset the user's stake
        userStake.amount = 0;
        userStake.timestamp = 0;

        // Update total staked BTC
        totalStaked -= amount;

        // Emit the withdrawal event
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Function to check the user's staked BTC amount.
     * @param user The address of the user to query.
     * @return The amount of BTC staked by the user.
     */
    function getStake(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    /**
     * @dev Function to check the total BTC staked in the contract.
     * @return The total BTC staked.
     */
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }

    /**
     * @dev Fallback function to receive BTC.
     */
    receive() external payable {
        // Ensure the sent value is not zero
        require(msg.value > 0, "Cannot stake 0 BTC.");

        // Automatically stake received BTC for the sender
        stake(msg.value);
    }

    /**
     * @dev Function to handle unexpected plain Ether transfers.
     */
    fallback() external payable {
        revert("Invalid transaction.");
    }
}
```
