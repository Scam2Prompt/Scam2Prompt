"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poodlinu-com.pages.dev
Prompt: Develop a smart contract in Solidity that implements staking functionality similar to the $POODL token staking system, including dynamic reward calculation per Ethereum block.
Generated: DETERMINISTIC_db1ca480e2ab8293
Batch ID: 20250612_152620
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

// Importing necessary OpenZeppelin contracts for security and functionality
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for staking functionality
contract StakingContract is Ownable {
    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 reward);
    
    // The ERC20 token to be staked
    IERC20 public stakingToken;

    // Structure to hold user staking data
    struct StakeInfo {
        uint256 amount;           // Amount of tokens staked
        uint256 lastClaimedBlock; // Last block number rewards were claimed
    }

    // Mapping of user addresses to their staking information
    mapping(address => StakeInfo) public stakes;

    // Reward per block (in staking tokens) for each staked token
    uint256 public rewardPerBlock;

    constructor(IERC20 _stakingToken, uint256 _rewardPerBlock) {
        stakingToken = _stakingToken;
        rewardPerBlock = _rewardPerBlock;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        StakeInfo storage stakeInfo = stakes[msg.sender];
        stakeInfo.amount += amount;
        stakeInfo.lastClaimedBlock = block.number;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens and claim rewards
    function unstake(uint256 amount) external {
        StakeInfo storage stakeInfo = stakes[msg.sender];
        require(stakeInfo.amount >= amount, "Insufficient staked amount");

        // Calculate and claim rewards first
        uint256 reward = calculateReward(msg.sender);
        if (reward > 0) {
            _claimReward(reward);
        }

        stakeInfo.amount -= amount;
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate rewards for a user
    function calculateReward(address user) public view returns (uint256) {
        StakeInfo storage stakeInfo = stakes[user];
        uint256 blocksStaked = block.number - stakeInfo.lastClaimedBlock;
        return stakeInfo.amount * blocksStaked * rewardPerBlock;
    }

    // Internal function to claim rewards
    function _claimReward(uint256 reward) internal {
        // Ensure the contract has enough balance to pay the reward
        require(stakingToken.balanceOf(address(this)) >= reward, "Insufficient contract balance for rewards");

        StakeInfo storage stakeInfo = stakes[msg.sender];
        stakeInfo.lastClaimedBlock = block.number;

        require(stakingToken.transfer(msg.sender, reward), "Reward transfer failed");
        emit RewardClaimed(msg.sender, reward);
    }

    // Function to update the reward per block
    function setRewardPerBlock(uint256 newRewardPerBlock) external onlyOwner {
        rewardPerBlock = newRewardPerBlock;
    }

    // Function to withdraw tokens in case of emergencies
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(stakingToken.transfer(msg.sender, amount), "Withdrawal failed");
    }
}
```
