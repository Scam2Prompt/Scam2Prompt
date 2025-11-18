"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchained-as.web.app
Prompt: Create a smart contract on Ethereum Layer 2 that facilitates double staking rewards for $PEPU tokens, ensuring compatibility with the Pepe Unchained ecosystem.
Generated: DETERMINISTIC_fe8daec2af89f76f
Batch ID: 20250612_152727
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

// Import necessary OpenZeppelin contracts for ERC20 and Ownable functionalities
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// This contract facilitates double staking rewards for $PEPU tokens
contract DoubleStakingRewards is Ownable {
    // State variables
    IERC20 public pepuToken; // Reference to the PEPU token contract
    uint256 public rewardRate; // Reward rate for staking
    mapping(address => uint256) public stakedAmount; // Tracks staked amount of users
    mapping(address => uint256) public rewards; // Tracks earned rewards of users

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    
    // Constructor to initialize the contract with the PEPU token address and reward rate
    constructor(address _pepuToken, uint256 _rewardRate) {
        require(_pepuToken != address(0), "Invalid PEPU token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        
        pepuToken = IERC20(_pepuToken);
        rewardRate = _rewardRate; // Set the reward rate
    }

    // Function for users to stake $PEPU tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer $PEPU tokens from the user to this contract
        pepuToken.transferFrom(msg.sender, address(this), amount);
        
        // Update staked amount and rewards for the user
        stakedAmount[msg.sender] += amount;
        rewards[msg.sender] += calculateReward(msg.sender);

        emit Staked(msg.sender, amount);
    }

    // Function for users to unstake their $PEPU tokens
    function unstake(uint256 amount) external {
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        // Update rewards before unstaking
        rewards[msg.sender] += calculateReward(msg.sender);
        
        // Update staked amount
        stakedAmount[msg.sender] -= amount;

        // Transfer $PEPU tokens back to the user
        pepuToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim earned rewards
    function claimRewards() external {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards available");

        // Reset the user's rewards after claiming
        rewards[msg.sender] = 0;

        // Transfer the rewards to the user
        pepuToken.transfer(msg.sender, reward);

        emit RewardPaid(msg.sender, reward);
    }

    // Internal function to calculate rewards based on staked amount
    function calculateReward(address user) internal view returns (uint256) {
        return stakedAmount[user] * rewardRate; // Calculate based on reward rate
    }

    // Owner function to update the reward rate
    function updateRewardRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Reward rate must be greater than zero");
        rewardRate = newRate;
    }

    // Function to withdraw tokens from the contract (for emergency purposes)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(pepuToken), "Cannot withdraw PEPU tokens");
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
