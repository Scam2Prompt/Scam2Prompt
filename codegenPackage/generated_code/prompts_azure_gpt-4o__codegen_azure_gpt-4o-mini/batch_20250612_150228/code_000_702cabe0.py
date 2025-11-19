"""
Generated Code Metadata:
========================
Original URL: https://bafybeig2qxervlifeg5gur3hrsbgo6hrco4esjxaz2r6nixoqkc6nhhjbe.ipfs.dweb.link
Prompt: Write a smart contract in Solidity for a farming system that integrates with the Pencils Protocol on the Scroll zkEVM ecosystem, ensuring compatibility with Ethereum mainnet security standards.
Generated: DETERMINISTIC_702cabe08defdcc3
Batch ID: 20250612_150228
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the Pencils Protocol
interface IPencilsProtocol {
    function stake(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function getStakedAmount(address user) external view returns (uint256);
}

// Farming contract for integrating with the Pencils Protocol
contract FarmingSystem is Ownable {
    // State variables
    IERC20 public rewardToken; // Token used for rewards
    IPencilsProtocol public pencilsProtocol; // Instance of the Pencils Protocol
    mapping(address => uint256) public stakedAmount; // Amount staked by each user
    mapping(address => uint256) public rewards; // Rewards for each user

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(IERC20 _rewardToken, IPencilsProtocol _pencilsProtocol) {
        rewardToken = _rewardToken;
        pencilsProtocol = _pencilsProtocol;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(rewardToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staked amount
        stakedAmount[msg.sender] += amount;

        // Stake in the Pencils Protocol
        pencilsProtocol.stake(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        // Update staked amount
        stakedAmount[msg.sender] -= amount;

        // Withdraw from the Pencils Protocol
        pencilsProtocol.withdraw(amount);

        // Transfer tokens back to the user
        require(rewardToken.transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards to claim");

        // Update rewards
        rewards[msg.sender] += reward;

        // Transfer rewards to the user
        require(rewardToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    // Function to calculate rewards (placeholder logic)
    function calculateRewards(address user) internal view returns (uint256) {
        // Placeholder for reward calculation logic
        return stakedAmount[user] / 10; // Example: 10% of staked amount as reward
    }

    // Function to get the staked amount of a user
    function getUserStakedAmount(address user) external view returns (uint256) {
        return stakedAmount[user];
    }

    // Function to get the total rewards of a user
    function getUserRewards(address user) external view returns (uint256) {
        return rewards[user];
    }
}
```
