"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shibasaga-io.web.app
Prompt: Write a smart contract in Solidity that integrates staking functionality for $SHIA tokens, ensuring reward multipliers for early stakers and voting power based on the amount staked.
Generated: DETERMINISTIC_0ab46c4dd96e9fe4
Batch ID: 20250612_152827
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract ShiTokenStaking is Ownable {
    using SafeMath for uint256;

    // Struct to represent a staker's information
    struct Staker {
        uint256 amountStaked;
        uint256 rewardMultiplier; // Multiplier based on early staking
        uint256 lastClaimed;
    }

    // Mappings to store staking information
    mapping(address => Staker) public stakers;
    IERC20 public shiaToken;
    
    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Reward calculation variables
    uint256 public constant BASE_REWARD = 1 ether; // Base reward per block
    uint256 public constant REWARD_MULTIPLIER = 2; // Multiplier for early stakers

    // Track total staked tokens
    uint256 public totalStaked;

    // Constructor to set the token address
    constructor(address _shiaToken) {
        shiaToken = IERC20(_shiaToken);
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(shiaToken.balanceOf(msg.sender) >= amount, "Insufficient balance");
        
        // Transfer tokens from the user to the contract
        shiaToken.transferFrom(msg.sender, address(this), amount);
        
        // Update the staker's information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked = staker.amountStaked.add(amount);
        staker.rewardMultiplier = calculateRewardMultiplier(msg.sender);
        staker.lastClaimed = block.number;

        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Calculate any pending rewards before unstaking
        claimRewards();

        // Update the staker's information
        staker.amountStaked = staker.amountStaked.sub(amount);
        totalStaked = totalStaked.sub(amount);
        
        // Transfer tokens back to the user
        shiaToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() public {
        Staker storage staker = stakers[msg.sender];
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available");

        // Update last claimed block
        staker.lastClaimed = block.number;

        // Transfer rewards to the staker
        payable(msg.sender).transfer(rewards);
        
        emit RewardsClaimed(msg.sender, rewards);
    }

    // Internal function to calculate rewards based on staked amount and multiplier
    function calculateRewards(address stakerAddress) internal view returns (uint256) {
        Staker memory staker = stakers[stakerAddress];
        uint256 blocksStaked = block.number.sub(staker.lastClaimed);
        return blocksStaked.mul(BASE_REWARD).mul(staker.rewardMultiplier);
    }

    // Internal function to calculate reward multiplier based on staking duration
    function calculateRewardMultiplier(address stakerAddress) internal view returns (uint256) {
        // Implement your logic to determine the multiplier for early stakers
        // For example, you can use the time staked as a criterion.
        return REWARD_MULTIPLIER; // Placeholder for actual multiplier logic
    }

    // Fallback function to accept ETH for rewards
    receive() external payable {}

    // Function to withdraw any accidental Ether sent to the contract
    function withdrawEther() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```
