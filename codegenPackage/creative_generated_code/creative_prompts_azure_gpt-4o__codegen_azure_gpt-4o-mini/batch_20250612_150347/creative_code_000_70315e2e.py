"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-popofrog.pages.dev
Prompt: Write a smart contract in Solidity for staking $FROP tokens, ensuring compatibility with multiple blockchain networks like BNB Chain, Ethereum, and Polygon, as described in the Popo ecosystem.
Generated: DETERMINISTIC_70315e2ed8f273cb
Batch ID: 20250612_150347
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

// Interface for interacting with the ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

/**
 * @title FROP Staking Contract
 * @dev This contract allows users to stake their FROP tokens and earn rewards.
 * The contract is designed to be compatible with BNB Chain, Ethereum, and Polygon.
 */
contract FROPStaking {
    IERC20 public fropToken; // The FROP token contract
    address public owner; // Owner of the contract
    uint256 public totalStaked; // Total amount of FROP tokens staked
    uint256 public rewardRate; // Reward rate per block

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt to maintain the correct reward calculations
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    /**
     * @dev Constructor to set the FROP token address and initial reward rate
     * @param _fropToken Address of the FROP token contract
     * @param _rewardRate Initial reward rate per block
     */
    constructor(IERC20 _fropToken, uint256 _rewardRate) {
        fropToken = _fropToken;
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    /**
     * @dev Stake FROP tokens in the contract
     * @param amount The amount of tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        // Transfer tokens from user to the contract
        require(fropToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user's stake
        stakes[msg.sender].amount += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake FROP tokens from the contract
     * @param amount The amount of tokens to unstake
     */
    function unstake(uint256 amount) external {
        Stake storage stakeInfo = stakes[msg.sender];
        require(stakeInfo.amount >= amount, "Insufficient staked amount");

        // Update total staked amount
        stakeInfo.amount -= amount;
        totalStaked -= amount;

        // Transfer tokens back to user
        require(fropToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Withdraw accrued rewards for the caller
     */
    function withdrawRewards() external {
        Stake storage stakeInfo = stakes[msg.sender];
        uint256 pendingReward = calculateRewards(msg.sender); // Calculate pending rewards
        require(pendingReward > 0, "No rewards to withdraw");

        // Update reward debt before transferring
        stakeInfo.rewardDebt += pendingReward;

        // Transfer rewards to the user
        require(fropToken.transfer(msg.sender, pendingReward), "Reward transfer failed");

        emit RewardPaid(msg.sender, pendingReward);
    }

    /**
     * @dev Calculate the pending rewards for a given user
     * @param user The address of the user
     * @return The amount of pending rewards
     */
    function calculateRewards(address user) internal view returns (uint256) {
        Stake storage stakeInfo = stakes[user];
        return (stakeInfo.amount * rewardRate) - stakeInfo.rewardDebt;
    }

    /**
     * @dev Allows the owner to update the reward rate
     * @param newRewardRate The new reward rate to set
     */
    function updateRewardRate(uint256 newRewardRate) external {
        require(msg.sender == owner, "Only owner can update reward rate");
        rewardRate = newRewardRate;
    }

    /**
     * @dev Function to retrieve the amount of FROP tokens staked by a user
     * @param user The address of the user to query
     * @return The staked amount
     */
    function stakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    /**
     * @dev Function to retrieve the total amount of FROP tokens staked in the contract
     * @return The total staked amount
     */
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }
}
```
