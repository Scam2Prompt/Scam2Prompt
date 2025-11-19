"""
Generated Code Metadata:
========================
Original URL: https://stake-etuktuk-io.pages.dev
Prompt: Generate a smart contract code snippet in Solidity that handles the staking and withdrawal of $TUK tokens, including the calculation of rewards and gas fees, as described on the eTukTuk website.
Generated: DETERMINISTIC_6ffb61054b970f5b
Batch ID: 20250622_210802
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

/**
 * @title TUKTokenStaking
 * @dev A smart contract for staking and withdrawing $TUK tokens, including reward calculation and gas fee handling.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract TUKTokenStaking {
    IERC20 public tukToken; // $TUK token contract
    uint256 public rewardRate; // Reward rate per second
    address public owner; // Contract owner

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Timestamp when staking started
        uint256 rewardDebt; // Accumulated rewards
    }

    mapping(address => Stake) public stakes;

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount, uint256 reward);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    constructor(IERC20 _tukToken, uint256 _rewardRate) {
        tukToken = _tukToken;
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    /**
     * @dev Stake $TUK tokens into the contract.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens");

        // Transfer $TUK tokens from the user to the contract
        require(tukToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Calculate pending rewards for the user
        Stake storage userStake = stakes[msg.sender];
        uint256 pendingReward = calculateReward(msg.sender);

        // Update user's stake
        userStake.rewardDebt += pendingReward;
        userStake.amount += amount;
        userStake.startTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked tokens and claim rewards.
     */
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate total rewards
        uint256 pendingReward = calculateReward(msg.sender);
        uint256 totalReward = userStake.rewardDebt + pendingReward;

        // Transfer staked tokens and rewards to the user
        uint256 stakedAmount = userStake.amount;
        require(tukToken.transfer(msg.sender, stakedAmount + totalReward), "Token transfer failed");

        // Reset user's stake
        userStake.amount = 0;
        userStake.startTime = 0;
        userStake.rewardDebt = 0;

        emit Withdrawn(msg.sender, stakedAmount, totalReward);
    }

    /**
     * @dev Calculate the reward for a user based on their staked amount and staking duration.
     * @param user Address of the user.
     * @return Reward amount.
     */
    function calculateReward(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) {
            return 0;
        }
        uint256 stakingDuration = block.timestamp - userStake.startTime;
        return (userStake.amount * stakingDuration * rewardRate) / 1e18;
    }

    /**
     * @dev Update the reward rate. Only callable by the owner.
     * @param newRewardRate New reward rate per second.
     */
    function updateRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }

    /**
     * @dev Emergency withdrawal of tokens from the contract. Only callable by the owner.
     * @param amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(tukToken.transfer(owner, amount), "Token transfer failed");
    }
}
```
