"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-earthmetasite.web.app
Prompt: Write a smart contract in Solidity for staking $EMT tokens that calculates rewards based on the presale bonus structure described on the EarthMeta platform.
Generated: DETERMINISTIC_bc66e9fc576528dc
Batch ID: 20250612_152658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

// Smart contract for staking EMT tokens with a reward system based on a presale bonus structure
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);

    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);

    function balanceOf(address account) external view returns (uint256);

    function approve(address spender, uint256 amount) external returns (bool);
}

contract EMTStaking {
    // Token used for staking
    IERC20 public immutable emtToken;

    // Owner of the contract
    address public owner;

    // Struct for staker information
    struct Staker {
        uint256 stakedAmount;
        uint256 rewardsClaimed;
        uint256 stakingStartTime;
    }

    // Mapping to store staker data
    mapping(address => Staker) public stakers;

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Presale bonus structure
    uint256 constant BONUS_RATE = 20; // 20% bonus
    uint256 constant STAKING_DURATION = 30 days; // Reward period duration

    modifier onlyOwner() {
        require(msg.sender == owner, "Not contract owner");
        _;
    }

    constructor(address _emtToken) {
        emtToken = IERC20(_emtToken);
        owner = msg.sender;
    }

    /**
     * @dev Allows users to stake EMT tokens.
     * @param _amount The amount of EMT tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer tokens from sender to contract
        require(
            emtToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        Staker storage staker = stakers[msg.sender];

        // Update staker data
        staker.stakedAmount += _amount;
        staker.stakingStartTime = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Calculate rewards for a staker based on the presale bonus structure.
     * @param _user Address of the staker.
     * @return Rewards amount for the staker.
     */
    function calculateRewards(address _user) public view returns (uint256) {
        Staker storage staker = stakers[_user];

        // Ensure staking duration has been passed
        if (block.timestamp < staker.stakingStartTime + STAKING_DURATION) {
            return 0; // No rewards yet
        }

        // Calculate base rewards (20% of staked amount)
        uint256 baseRewards = (staker.stakedAmount * BONUS_RATE) / 100;

        // Subtract already claimed rewards
        uint256 pendingRewards = baseRewards - staker.rewardsClaimed;

        return pendingRewards;
    }

    /**
     * @dev Allows users to claim their staking rewards.
     */
    function claimRewards() external {
        uint256 pendingRewards = calculateRewards(msg.sender);
        require(pendingRewards > 0, "No rewards available to claim");

        Staker storage staker = stakers[msg.sender];

        // Update staker data
        staker.rewardsClaimed += pendingRewards;

        // Transfer rewards to the staker
        require(emtToken.transfer(msg.sender, pendingRewards), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, pendingRewards);
    }

    /**
     * @dev Allows users to unstake their EMT tokens.
     */
    function unstake() external {
        Staker storage staker = stakers[msg.sender];
        uint256 stakedAmount = staker.stakedAmount;

        require(stakedAmount > 0, "No staked tokens to withdraw");

        // Transfer staked tokens back to user
        require(emtToken.transfer(msg.sender, stakedAmount), "Unstake transfer failed");

        // Reset staker data
        staker.stakedAmount = 0;
        staker.rewardsClaimed = 0;
        staker.stakingStartTime = 0;

        emit Unstaked(msg.sender, stakedAmount);
    }

    /**
     * @dev Allows the owner to withdraw EMT tokens from the contract.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Withdrawal amount must be greater than zero");
        require(
            emtToken.transfer(owner, _amount),
            "Owner withdrawal transfer failed"
        );
    }
}
```
