"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifck3tvl2afu34735yd3ul2g5ifecjinp2c7na6kdjx3q2no76q5i.ipfs.dweb.link
Prompt: Create a script in Solidity to implement token farming functionality compatible with the Joe crypto exchange, focusing on Avalanche network tokens.
Generated: DETERMINISTIC_a88b378e9cb71969
Batch ID: 20250612_150228
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the JoeRouter to interact with the Joe DEX
interface IJoeRouter {
    function addLiquidity(
        address tokenA,
        address tokenB,
        uint256 amountADesired,
        uint256 amountBDesired,
        uint256 amountAMin,
        uint256 amountBMin,
        address to,
        uint256 deadline
    ) external returns (uint256 amountA, uint256 amountB, uint256 liquidity);
}

// TokenFarming contract for token farming functionality
contract TokenFarming is Ownable {
    // State variables
    IERC20 public rewardToken; // Reward token (e.g., AVAX or another token)
    IJoeRouter public joeRouter; // Router for interacting with Joe DEX

    mapping(address => uint256) public stakedAmount; // User's staked amount
    mapping(address => uint256) public rewards; // User's earned rewards
    uint256 public totalStaked; // Total staked amount
    uint256 public rewardRate; // Rate of reward distribution per staked token

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to set initial values
    constructor(address _rewardToken, address _joeRouter, uint256 _rewardRate) {
        rewardToken = IERC20(_rewardToken);
        joeRouter = IJoeRouter(_joeRouter);
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");
        
        // Transfer tokens from user to contract
        rewardToken.transferFrom(msg.sender, address(this), amount);

        // Update user's staked amount and total staked amount
        stakedAmount[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake 0");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        // Update staked amounts
        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to user
        rewardToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate and distribute rewards
    function distributeRewards() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards to distribute");

        // Update the user's rewards
        rewards[msg.sender] += reward;

        emit RewardPaid(msg.sender, reward);
    }

    // Function to view earned rewards
    function viewRewards(address user) external view returns (uint256) {
        return calculateReward(user);
    }

    // Internal function to calculate rewards
    function calculateReward(address user) internal view returns (uint256) {
        return stakedAmount[user] * rewardRate;
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(msg.sender, amount);
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
```
