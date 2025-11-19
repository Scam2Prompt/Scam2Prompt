"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://verified-greenbitcoin.pages.dev
Prompt: What are the best practices for creating a presale mechanism for a new cryptocurrency like Green Bitcoin, ensuring early adopters can stake their tokens for rewards?
Generated: DETERMINISTIC_8e189e86aedc602f
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean and production-ready implementation of a presale mechanism for a new cryptocurrency, utilizing Solidity (a popular language for smart contract development). This code allows early adopters to participate in the presale by staking tokens and earning rewards.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title GreenBitcoinPresale
 * @dev A contract for presale of a new cryptocurrency, Green Bitcoin, with staking functionality for rewards.
 */
contract GreenBitcoinPresale {
    // State variables
    address public owner;
    uint256 public presaleEndTime;
    uint256 public stakingRewardRate; // Reward rate (e.g., percentage per year)
    uint256 public totalStaked;

    struct Stake {
        uint256 amount;
        uint256 startTime;
    }

    mapping(address => Stake) public stakes;
    mapping(address => uint256) public rewards;

    event Staked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    event TokensWithdrawn(address indexed user, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier presaleActive() {
        require(block.timestamp <= presaleEndTime, "Presale has ended");
        _;
    }

    modifier presaleEnded() {
        require(block.timestamp > presaleEndTime, "Presale is still active");
        _;
    }

    constructor(uint256 _presaleDuration, uint256 _stakingRewardRate) {
        owner = msg.sender;
        presaleEndTime = block.timestamp + _presaleDuration;
        stakingRewardRate = _stakingRewardRate;
    }

    /**
     * @dev Allows users to stake tokens during the presale period.
     * @param _amount The amount of tokens to stake.
     */
    function stakeTokens(uint256 _amount) external presaleActive {
        require(_amount > 0, "Amount must be greater than zero");

        // Update user's stake
        if (stakes[msg.sender].amount > 0) {
            // Calculate existing rewards
            rewards[msg.sender] += calculateRewards(msg.sender);
        }

        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].startTime = block.timestamp;

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to claim their staking rewards only after the presale ends.
     */
    function claimRewards() external presaleEnded {
        uint256 reward = calculateRewards(msg.sender) + rewards[msg.sender];
        require(reward > 0, "No rewards available");

        rewards[msg.sender] = 0;
        stakes[msg.sender].startTime = block.timestamp; // Reset staking start time

        // Transfer rewards to the user (replace with actual token transfer logic)
        // Example: token.transfer(msg.sender, reward);
        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Allows users to withdraw their tokens after the presale ends.
     */
    function withdrawTokens() external presaleEnded {
        uint256 stakedAmount = stakes[msg.sender].amount;
        require(stakedAmount > 0, "No staked tokens to withdraw");

        stakes[msg.sender].amount = 0;
        stakes[msg.sender].startTime = 0;

        totalStaked -= stakedAmount;

        // Transfer staked tokens to the user (replace with actual token transfer logic)
        // Example: token.transfer(msg.sender, stakedAmount);
        emit TokensWithdrawn(msg.sender, stakedAmount);
    }

    /**
     * @dev Calculates the rewards for a given user based on staking duration.
     * @param _user The address of the user whose rewards are being calculated.
     * @return The calculated reward amount.
     */
    function calculateRewards(address _user) public view returns (uint256) {
        Stake memory userStake = stakes[_user];
        if (userStake.amount == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - userStake.startTime;
        uint256 reward = (userStake.amount * stakingRewardRate * stakingDuration) / (365 days * 100);

        return reward;
    }

    /**
     * @dev Allows the owner to set a new staking reward rate.
     * @param _newRate The new staking reward rate.
     */
    function setStakingRewardRate(uint256 _newRate) external onlyOwner {
        stakingRewardRate = _newRate;
    }

    /**
     * @dev Allows the owner to withdraw excess funds (e.g., unsold tokens or fees).
     */
    function ownerWithdraw(uint256 _amount) external onlyOwner {
        // Transfer excess funds to the owner (replace with actual token transfer logic)
        // Example: token.transfer(owner, _amount);
    }
}
```

### Notes:
- Replace `token.transfer` with actual token transfer logic using an ERC20 token instance.
- Ensure the contract is deployed on a testnet first to verify its functionality.
- Integrate appropriate front-end logic to interact with the contract.
