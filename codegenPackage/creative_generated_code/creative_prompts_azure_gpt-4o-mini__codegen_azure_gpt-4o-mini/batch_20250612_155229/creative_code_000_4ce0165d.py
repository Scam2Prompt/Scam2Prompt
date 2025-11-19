"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://owy-wtf.pages.dev
Prompt: Generate a smart contract in Solidity for a functional memecoin similar to Owy, detailing its unique features and functionalities.
Generated: DETERMINISTIC_4ce0165d1b753cc0
Batch ID: 20250612_155229
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for the Memecoin
contract Memecoin is ERC20, Ownable {
    // Mapping to track the rewards for each address
    mapping(address => uint256) private _rewards;

    // Event for tracking reward distributions
    event RewardDistributed(address indexed recipient, uint256 amount);

    // Reward percentage on each transaction (in basis points, 100 basis points = 1%)
    uint256 public rewardPercentage = 500; // 5% rewards

    // Total supply of the token
    uint256 private constant TOTAL_SUPPLY = 1_000_000 * 10**18; // 1 million tokens with 18 decimals

    constructor() ERC20("Memecoin", "MEME") {
        // Mint the total supply to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    // Function to transfer tokens with a reward feature
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        // Calculate the reward amount
        uint256 rewardAmount = (amount * rewardPercentage) / 10_000;
        
        // Ensure that the sender has enough balance
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer the specified amount
        super.transfer(recipient, amount);
        
        // Distributing rewards
        _distributeReward(msg.sender, rewardAmount);

        return true;
    }

    // Function to change the reward percentage, callable only by the owner
    function setRewardPercentage(uint256 newRewardPercentage) external onlyOwner {
        require(newRewardPercentage <= 1000, "Reward percentage should not exceed 10%");
        rewardPercentage = newRewardPercentage;
    }

    // Internal function to distribute rewards
    function _distributeReward(address from, uint256 amount) internal {
        // Update the rewards mapping
        _rewards[from] += amount;

        // Emit an event for reward distribution
        emit RewardDistributed(from, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 rewardAmount = _rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        // Reset the reward balance for the claimant
        _rewards[msg.sender] = 0;

        // Transfer the reward tokens to the claimant
        _mint(msg.sender, rewardAmount);
    }

    // Function to check the rewards of a particular address
    function checkRewards(address account) external view returns (uint256) {
        return _rewards[account];
    }
}
```
