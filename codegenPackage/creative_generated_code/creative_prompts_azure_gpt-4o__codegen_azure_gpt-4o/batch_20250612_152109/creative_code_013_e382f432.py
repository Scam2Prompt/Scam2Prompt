"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://penguins-gainsassociates.pages.dev
Prompt: Develop a Solidity smart contract for distributing rewards in a multichain Web3 gaming ecosystem, similar to Kewl's features mentioned on the GAINS Associates platform.
Generated: DETERMINISTIC_e382f432e3249370
Batch ID: 20250612_152109
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
 * @title RewardDistributor
 * @notice A smart contract for distributing rewards in a multichain Web3 gaming ecosystem.
 * @dev This contract supports reward distribution to players based on their contribution.
 */
contract RewardDistributor {
    // Owner of the contract
    address public owner;

    // Mapping to store rewards for each player
    mapping(address => uint256) public rewards;

    // Event emitted when rewards are distributed
    event RewardDistributed(address indexed player, uint256 amount);

    // Event emitted when the owner is changed
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @notice Function to distribute rewards to players.
     * @param _player Address of the player receiving the reward.
     * @param _amount The reward amount to be distributed.
     * @dev Only the owner can call this function.
     */
    function distributeReward(address _player, uint256 _amount) external onlyOwner {
        require(_player != address(0), "Invalid player address");
        require(_amount > 0, "Reward amount must be greater than zero");

        // Update rewards mapping
        rewards[_player] += _amount;

        // Emit the reward distribution event
        emit RewardDistributed(_player, _amount);
    }

    /**
     * @notice Function for players to claim their rewards.
     * @dev Rewards are transferred to the player's address.
     */
    function claimReward() external {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards available to claim");

        // Reset the reward balance for the player before transferring
        rewards[msg.sender] = 0;

        // Transfer reward to the player
        (bool success, ) = msg.sender.call{value: reward}("");
        require(success, "Reward transfer failed");
    }

    /**
     * @notice Function to transfer ownership of the contract to a new owner.
     * @param _newOwner Address of the new owner.
     * @dev Only the current owner can call this function.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "New owner address cannot be zero");
        emit OwnershipTransferred(owner, _newOwner);
        owner = _newOwner;
    }

    /**
     * @notice Fallback function to accept ether deposits.
     * @dev This is needed to fund the contract for reward distribution.
     */
    receive() external payable {}

    /**
     * @notice Function to withdraw unused funds from the contract.
     * @param _amount The amount to withdraw.
     * @dev Only the owner can call this function.
     */
    function withdrawFunds(uint256 _amount) external onlyOwner {
        require(_amount <= address(this).balance, "Insufficient contract balance");

        (bool success, ) = msg.sender.call{value: _amount}("");
        require(success, "Withdrawal failed");
    }
}
```
