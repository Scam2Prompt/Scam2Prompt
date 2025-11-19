"""
Generated Code Metadata:
========================
Original URL: https://green-bitcoins-en.pages.dev
Prompt: Design a smart contract for a prediction-based staking system, similar to Green Bitcoin's, using Solidity and the Ethereum blockchain.
Generated: DETERMINISTIC_2ccaa6b843cc664b
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title PredictionStaking
 * @dev A smart contract for a prediction-based staking system.
 * Users can stake ETH and make predictions. Rewards are distributed based on the accuracy of predictions.
 */
contract PredictionStaking {
    // Struct to store user stakes and predictions
    struct Stake {
        uint256 amount; // Amount of ETH staked
        string prediction; // User's prediction
        bool claimed; // Whether the reward has been claimed
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Event emitted when a user stakes ETH
    event Staked(address indexed user, uint256 amount, string prediction);

    // Event emitted when rewards are distributed
    event RewardDistributed(address indexed user, uint256 reward);

    // Owner of the contract
    address public owner;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows users to stake ETH and submit a prediction.
     * @param _prediction The user's prediction as a string.
     */
    function stake(string memory _prediction) external payable {
        require(msg.value > 0, "Stake amount must be greater than zero");
        require(bytes(_prediction).length > 0, "Prediction cannot be empty");

        // Ensure the user has not already staked
        require(stakes[msg.sender].amount == 0, "You have already staked");

        // Record the user's stake and prediction
        stakes[msg.sender] = Stake({
            amount: msg.value,
            prediction: _prediction,
            claimed: false
        });

        emit Staked(msg.sender, msg.value, _prediction);
    }

    /**
     * @dev Allows the owner to distribute rewards based on prediction accuracy.
     * @param _user The address of the user to distribute rewards to.
     * @param _reward The reward amount in wei.
     */
    function distributeReward(address _user, uint256 _reward) external onlyOwner {
        require(_user != address(0), "Invalid user address");
        require(_reward > 0, "Reward must be greater than zero");
        require(stakes[_user].amount > 0, "User has not staked");
        require(!stakes[_user].claimed, "Reward already claimed");

        // Transfer the reward to the user
        (bool success, ) = _user.call{value: _reward}("");
        require(success, "Reward transfer failed");

        // Mark the reward as claimed
        stakes[_user].claimed = true;

        emit RewardDistributed(_user, _reward);
    }

    /**
     * @dev Allows the owner to withdraw contract balance.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Fallback function to accept ETH deposits.
     */
    receive() external payable {}

    /**
     * @dev Function to get the contract's balance.
     * @return The balance of the contract in wei.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
