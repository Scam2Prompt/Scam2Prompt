"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memekombat-chain.pages.dev
Prompt: Write a smart contract in Solidity for staking $MK tokens on the Meme Kombat platform, ensuring users can earn APY during the presale phase.
Generated: DETERMINISTIC_ae01d0d2fcbe74ad
Batch ID: 20250612_152249
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
 * @title Meme Kombat Staking Contract
 * @dev This contract allows users to stake $MK tokens during the presale phase
 *      and earn APY rewards. It includes mechanisms for deposit, withdrawal, 
 *      and reward calculation.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract MemeKombatStaking {
    // State variables
    IERC20 public mkToken; // $MK token contract address
    uint256 public annualPercentageYield; // APY percentage
    uint256 public presaleEndTime; // Timestamp for when presale ends
    address public owner; // Contract owner

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // When the stake was made
        uint256 rewardClaimed; // Rewards already claimed by the user
    }

    mapping(address => Stake) public stakes; // Mapping of users to their stakes

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Not contract owner");
        _;
    }

    modifier isPresaleActive() {
        require(block.timestamp < presaleEndTime, "Presale phase has ended");
        _;
    }

    constructor(
        address _mkToken,
        uint256 _annualPercentageYield,
        uint256 _presaleEndTime
    ) {
        mkToken = IERC20(_mkToken);
        annualPercentageYield = _annualPercentageYield;
        presaleEndTime = _presaleEndTime;
        owner = msg.sender;
    }

    /**
     * @notice Allows users to stake $MK tokens during the presale phase
     * @param _amount Amount of $MK tokens to stake
     */
    function stake(uint256 _amount) external isPresaleActive {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer $MK tokens from user to contract
        require(mkToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update user's stake
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += _amount;
        userStake.startTime = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Allows users to withdraw their staked tokens after the presale phase
     */
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens to withdraw");
        require(block.timestamp >= presaleEndTime, "Cannot withdraw during presale");

        uint256 stakedAmount = userStake.amount;
        userStake.amount = 0; // Reset user's staked amount

        // Transfer staked tokens back to the user
        require(mkToken.transfer(msg.sender, stakedAmount), "Token transfer failed");

        emit Withdrawn(msg.sender, stakedAmount);
    }

    /**
     * @notice Allows users to claim their accumulated rewards during presale
     */
    function claimReward() external isPresaleActive {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked tokens");

        // Calculate reward: APY * stakedAmount * (timeElapsed / 365 days)
        uint256 timeElapsed = block.timestamp - userStake.startTime;
        uint256 reward = (userStake.amount * annualPercentageYield * timeElapsed) / (365 days * 100);

        // Ensure rewards are not claimed twice
        uint256 claimableReward = reward - userStake.rewardClaimed;
        require(claimableReward > 0, "No rewards available");

        // Update the reward claimed by the user
        userStake.rewardClaimed += claimableReward;

        // Transfer reward tokens to the user
        require(mkToken.transfer(msg.sender, claimableReward), "Token transfer failed");

        emit RewardClaimed(msg.sender, claimableReward);
    }

    /**
     * @notice Updates the APY percentage (only owner can call)
     * @param _newAPY New APY percentage
     */
    function updateAPY(uint256 _newAPY) external onlyOwner {
        require(_newAPY > 0, "APY must be greater than zero");
        annualPercentageYield = _newAPY;
    }

    /**
     * @notice Updates the presale end time (only owner can call)
     * @param _newEndTime New presale end timestamp
     */
    function updatePresaleEndTime(uint256 _newEndTime) external onlyOwner {
        require(_newEndTime > block.timestamp, "End time must be in the future");
        presaleEndTime = _newEndTime;
    }

    /**
     * @notice Emergency withdrawal function (only owner can call)
     * @dev Allows owner to withdraw all tokens from the contract
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 contractBalance = mkToken.balanceOf(address(this));
        require(mkToken.transfer(owner, contractBalance), "Token transfer failed");
    }
}
```
