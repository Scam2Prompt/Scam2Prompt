"""
Generated Code Metadata:
========================
Original URL: https://assets-mog.com
Prompt: Create a smart contract example for tokenized rewards or "winning" functionality, inspired by MOG Coin's branding of "tokenized winning."
Generated: DETERMINISTIC_5d27b1321cc87f7f
Batch ID: 20250612_154010
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title TokenizedWinning
 * @dev A token contract with built-in reward distribution functionality
 */
contract TokenizedWinning is ERC20, Ownable {
    using SafeMath for uint256;

    // Reward distribution variables
    uint256 public constant REWARD_INTERVAL = 1 weeks;
    uint256 public lastRewardDistribution;
    uint256 public rewardPercentage = 5; // 5% reward rate

    // Winner tracking
    address[] public winners;
    mapping(address => uint256) public winCounts;

    // Events
    event RewardDistributed(address indexed winner, uint256 amount);
    event NewWinnerAdded(address indexed winner);

    /**
     * @dev Constructor that initializes the token
     * @param initialSupply The initial token supply
     */
    constructor(uint256 initialSupply) ERC20("TokenizedWinning", "WIN") {
        _mint(msg.sender, initialSupply);
        lastRewardDistribution = block.timestamp;
    }

    /**
     * @dev Distributes rewards to random token holders
     */
    function distributeRewards() external onlyOwner {
        require(
            block.timestamp >= lastRewardDistribution.add(REWARD_INTERVAL),
            "Rewards can only be distributed once per week"
        );

        uint256 rewardPool = totalSupply().mul(rewardPercentage).div(100);
        require(rewardPool > 0, "No rewards to distribute");

        // Select random winner from token holders
        address winner = selectRandomWinner();
        require(winner != address(0), "No eligible winners");

        // Update winner tracking
        if (winCounts[winner] == 0) {
            winners.push(winner);
            emit NewWinnerAdded(winner);
        }
        winCounts[winner]++;

        // Distribute reward
        _mint(winner, rewardPool);
        lastRewardDistribution = block.timestamp;

        emit RewardDistributed(winner, rewardPool);
    }

    /**
     * @dev Selects a random winner from token holders
     * @return The address of the selected winner
     */
    function selectRandomWinner() internal view returns (address) {
        // This is a simplified version - in production you'd want a more secure random number
        uint256 index = uint256(
            keccak256(abi.encodePacked(block.timestamp, block.difficulty))
        ) % balanceOf(msg.sender);
        
        return tokenHolderAt(index);
    }

    /**
     * @dev Gets token holder at specific index
     * @param index The index of the holder
     * @return The address of the holder
     */
    function tokenHolderAt(uint256 index) internal view returns (address) {
        // In a real implementation, you'd need to maintain a list of holders
        // This is a simplified version that assumes the owner holds all tokens
        return owner();
    }

    /**
     * @dev Updates the reward percentage
     * @param newPercentage The new reward percentage
     */
    function setRewardPercentage(uint256 newPercentage) external onlyOwner {
        require(newPercentage <= 10, "Reward percentage cannot exceed 10%");
        rewardPercentage = newPercentage;
    }

    /**
     * @dev Gets all winners
     * @return Array of winner addresses
     */
    function getAllWinners() external view returns (address[] memory) {
        return winners;
    }

    /**
     * @dev Gets win count for a specific address
     * @param _address The address to check
     * @return The number of wins
     */
    function getWinCount(address _address) external view returns (uint256) {
        return winCounts[_address];
    }
}
```
