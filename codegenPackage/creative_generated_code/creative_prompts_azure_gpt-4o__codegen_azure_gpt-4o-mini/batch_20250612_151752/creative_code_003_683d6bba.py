"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereum.fit
Prompt: Create a smart contract in Solidity that utilizes Ethereum FIT's functionalities as described in the 2022 documentation.
Generated: DETERMINISTIC_683d6bbabbfb979f
Batch ID: 20250612_151752
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

// Importing libraries for ERC20 token standard and Ownable contract
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract definition
contract FITSmartContract is Ownable {
    // State variables
    IERC20 public fitToken; // The FIT token contract
    uint256 public totalStaked; // Total amount of FIT tokens staked
    mapping(address => uint256) public stakedBalances; // Mapping of user addresses to their staked balance
    mapping(address => uint256) public rewardBalances; // Mapping of user addresses to their reward balance

    // Events for logging
    event TokensStaked(address indexed user, uint256 amount);
    event TokensUnstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the FIT token address
    constructor(address _fitTokenAddress) {
        require(_fitTokenAddress != address(0), "Invalid token address");
        fitToken = IERC20(_fitTokenAddress);
    }

    // Function to stake FIT tokens
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens");
        require(fitToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staking state
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;

        emit TokensStaked(msg.sender, amount);
    }

    // Function to unstake FIT tokens
    function unstakeTokens(uint256 amount) external {
        require(amount > 0, "Cannot unstake zero tokens");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update staking state
        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to user
        require(fitToken.transfer(msg.sender, amount), "Transfer failed");

        emit TokensUnstaked(msg.sender, amount);
    }

    // Function to calculate rewards (dummy implementation for illustration)
    function calculateRewards(address user) internal view returns (uint256) {
        // Simple reward calculation based on staked amount
        return stakedBalances[user] * 10 / 100; // 10% rewards
    }

    // Function for users to claim their rewards
    function claimRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available");

        // Update reward state
        rewardBalances[msg.sender] += rewards;

        // Transfer rewards to user (assuming rewards are in FIT tokens)
        require(fitToken.transfer(msg.sender, rewards), "Transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to withdraw any ERC20 tokens accidentally sent to the contract
    function withdrawToken(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(fitToken), "Cannot withdraw FIT tokens");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }

    // Function to set a new FIT token address (onlyOwner)
    function setFitTokenAddress(address newTokenAddress) external onlyOwner {
        require(newTokenAddress != address(0), "Invalid token address");
        fitToken = IERC20(newTokenAddress);
    }
}
```
