"""
Generated Code Metadata:
========================
Original URL: https://proposal-ownthedoge.com
Prompt: Generate a smart contract in Solidity for distributing rewards to $DOG and $COCORO holders, referencing the voting system mentioned on the website.
Generated: DETERMINISTIC_a8a64d2580606582
Batch ID: 20250612_154631
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for distributing rewards to $DOG and $COCORO holders
contract RewardDistributor is Ownable {
    // State variables
    IERC20 public dogToken;      // Reference to the $DOG token contract
    IERC20 public cocoroToken;   // Reference to the $COCORO token contract
    uint256 public rewardRate;    // Reward rate per token holder

    // Mapping to track rewards for each holder
    mapping(address => uint256) public rewards;

    // Event to log reward distribution
    event RewardsDistributed(address indexed holder, uint256 amount);

    // Constructor to initialize the contract with token addresses and reward rate
    constructor(address _dogToken, address _cocoroToken, uint256 _rewardRate) {
        require(_dogToken != address(0), "Invalid $DOG token address");
        require(_cocoroToken != address(0), "Invalid $COCORO token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        dogToken = IERC20(_dogToken);
        cocoroToken = IERC20(_cocoroToken);
        rewardRate = _rewardRate;
    }

    // Function to distribute rewards to holders based on their token balance
    function distributeRewards() external onlyOwner {
        uint256 totalDogSupply = dogToken.totalSupply();
        uint256 totalCocoroSupply = cocoroToken.totalSupply();

        // Ensure there are holders to distribute rewards to
        require(totalDogSupply > 0 || totalCocoroSupply > 0, "No tokens in circulation");

        // Distributing rewards to $DOG holders
        for (uint256 i = 0; i < totalDogSupply; i++) {
            address holder = dogToken.holderAt(i); // Assuming a function to get holder address
            uint256 holderBalance = dogToken.balanceOf(holder);
            uint256 rewardAmount = holderBalance * rewardRate;

            // Update rewards mapping
            rewards[holder] += rewardAmount;

            // Emit event for reward distribution
            emit RewardsDistributed(holder, rewardAmount);
        }

        // Distributing rewards to $COCORO holders
        for (uint256 j = 0; j < totalCocoroSupply; j++) {
            address holder = cocoroToken.holderAt(j); // Assuming a function to get holder address
            uint256 holderBalance = cocoroToken.balanceOf(holder);
            uint256 rewardAmount = holderBalance * rewardRate;

            // Update rewards mapping
            rewards[holder] += rewardAmount;

            // Emit event for reward distribution
            emit RewardsDistributed(holder, rewardAmount);
        }
    }

    // Function to allow holders to claim their rewards
    function claimRewards() external {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        // Reset the reward for the holder
        rewards[msg.sender] = 0;

        // Transfer the reward to the holder
        require(dogToken.transfer(msg.sender, rewardAmount), "Transfer failed");
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 _newRewardRate) external onlyOwner {
        require(_newRewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _newRewardRate;
    }
}
```
