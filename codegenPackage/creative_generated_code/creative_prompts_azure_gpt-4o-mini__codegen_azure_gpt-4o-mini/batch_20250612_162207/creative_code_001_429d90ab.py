"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubetas-ai.pages.dev
Prompt: Generate a code snippet to implement a staking mechanism for $QUBE tokens that allows users to earn rewards from a 5% sell tax.
Generated: DETERMINISTIC_429d90aba902fdec
Batch ID: 20250612_162207
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract QubeStaking {
    using SafeMath for uint256;

    // State variables
    IERC20 public qubeToken; // Reference to the $QUBE token contract
    address public owner; // Owner of the contract

    struct Stake {
        uint256 amount; // Amount of $QUBE staked
        uint256 rewardDebt; // Rewards owed to the staker
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes
    uint256 public totalStaked; // Total amount of $QUBE staked
    uint256 public totalRewards; // Total rewards accumulated
    uint256 public rewardRate; // Reward rate based on sell tax

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event Claimed(address indexed user, uint256 reward);

    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    constructor(address _qubeToken, uint256 _rewardRate) {
        qubeToken = IERC20(_qubeToken);
        owner = msg.sender;
        rewardRate = _rewardRate; // Set reward rate (5% sell tax)
    }

    // Function to stake $QUBE tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        require(qubeToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update total staked amount
        totalStaked = totalStaked.add(amount);

        // Update user's stake details
        Stake storage userStake = stakes[msg.sender];
        userStake.amount = userStake.amount.add(amount);
        userStake.rewardDebt = userStake.rewardDebt.add(calculatePendingRewards(msg.sender));

        emit Staked(msg.sender, amount);
    }

    // Function to unstake $QUBE tokens and claim rewards
    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake 0 tokens");
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked balance");

        // Calculate and distribute rewards before unstaking
        uint256 pendingRewards = calculatePendingRewards(msg.sender);
        if (pendingRewards > 0) {
            totalRewards = totalRewards.add(pendingRewards);
            userStake.rewardDebt = 0; // Reset reward debt for the user
            qubeToken.transfer(msg.sender, pendingRewards);
            emit Claimed(msg.sender, pendingRewards);
        }

        // Update user's stake details
        userStake.amount = userStake.amount.sub(amount);
        totalStaked = totalStaked.sub(amount);
        require(qubeToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Calculate pending rewards for a user
    function calculatePendingRewards(address user) internal view returns (uint256) {
        Stake memory userStake = stakes[user];
        return userStake.amount.mul(rewardRate).div(100).sub(userStake.rewardDebt);
    }

    // Function for the owner to withdraw accumulated rewards (e.g., from sell tax)
    function withdrawRewards(uint256 amount) external onlyOwner {
        require(amount <= totalRewards, "Insufficient rewards");
        totalRewards = totalRewards.sub(amount);
        require(qubeToken.transfer(owner, amount), "Transfer failed");
    }

    // Function to view user's staked amount
    function viewStake() external view returns (uint256) {
        return stakes[msg.sender].amount;
    }

    // Function to view user's pending rewards
    function viewPendingRewards() external view returns (uint256) {
        return calculatePendingRewards(msg.sender);
    }
}
```
