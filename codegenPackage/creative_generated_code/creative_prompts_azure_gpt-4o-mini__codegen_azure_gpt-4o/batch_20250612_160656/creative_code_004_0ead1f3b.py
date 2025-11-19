"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://corgiaixyz.pages.dev
Prompt: Provide an example of how to set up liquidity mining for the $CORGIAI token on a decentralized exchange (DEX).
Generated: DETERMINISTIC_0ead1f3b27a1405c
Batch ID: 20250612_160656
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
 * @title LiquidityMining
 * @dev This contract sets up liquidity mining for the $CORGIAI token on a decentralized exchange (DEX).
 * Users can stake LP tokens and earn $CORGIAI rewards over time.
 */
contract LiquidityMining {
    // State variables
    address public owner; // Owner of the contract
    address public corgiaiToken; // Address of the $CORGIAI ERC-20 token contract
    address public lpToken; // Address of the LP token contract

    uint256 public rewardRate; // Reward rate (amount of $CORGIAI distributed per second)
    uint256 public totalStaked; // Total amount of LP tokens staked

    // Mapping to store user stakes and reward balances
    mapping(address => uint256) public userStake;
    mapping(address => uint256) public userRewardDebt;

    uint256 public lastRewardTimestamp; // Last time rewards were updated
    uint256 public accRewardPerShare; // Accumulated $CORGIAI rewards per LP token share

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event Harvested(address indexed user, uint256 reward);

    /**
     * @dev Modifier to restrict access to the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _corgiaiToken Address of the $CORGIAI token contract.
     * @param _lpToken Address of the LP token contract.
     * @param _rewardRate Reward rate (amount of $CORGIAI distributed per second).
     */
    constructor(address _corgiaiToken, address _lpToken, uint256 _rewardRate) {
        require(_corgiaiToken != address(0), "Invalid $CORGIAI token address");
        require(_lpToken != address(0), "Invalid LP token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        owner = msg.sender;
        corgiaiToken = _corgiaiToken;
        lpToken = _lpToken;
        rewardRate = _rewardRate;
        lastRewardTimestamp = block.timestamp;
    }

    /**
     * @dev Update rewards for all stakers.
     */
    function updateRewards() internal {
        if (totalStaked == 0) {
            lastRewardTimestamp = block.timestamp;
            return;
        }

        uint256 timeElapsed = block.timestamp - lastRewardTimestamp;
        uint256 reward = timeElapsed * rewardRate;

        accRewardPerShare += (reward * 1e18) / totalStaked;
        lastRewardTimestamp = block.timestamp;
    }

    /**
     * @dev Stake LP tokens to earn $CORGIAI rewards.
     * @param amount Amount of LP tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens");

        updateRewards(); // Update rewards before staking

        // Transfer LP tokens from user to contract
        require(
            IERC20(lpToken).transferFrom(msg.sender, address(this), amount),
            "LP token transfer failed"
        );

        // Update user state
        userStake[msg.sender] += amount;
        userRewardDebt[msg.sender] = (userStake[msg.sender] * accRewardPerShare) / 1e18;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked LP tokens.
     * @param amount Amount of LP tokens to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Cannot withdraw zero tokens");
        require(userStake[msg.sender] >= amount, "Insufficient staked balance");

        updateRewards(); // Update rewards before withdrawal

        // Calculate pending rewards
        uint256 pendingReward = ((userStake[msg.sender] * accRewardPerShare) / 1e18) -
            userRewardDebt[msg.sender];

        // Update user state
        userStake[msg.sender] -= amount;
        userRewardDebt[msg.sender] = (userStake[msg.sender] * accRewardPerShare) / 1e18;

        totalStaked -= amount;

        // Transfer LP tokens back to the user
        require(IERC20(lpToken).transfer(msg.sender, amount), "LP token transfer failed");

        // Transfer pending rewards
        if (pendingReward > 0) {
            require(IERC20(corgiaiToken).transfer(msg.sender, pendingReward), "$CORGIAI transfer failed");
            emit Harvested(msg.sender, pendingReward);
        }

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Harvest $CORGIAI rewards without withdrawing LP tokens.
     */
    function harvest() external {
        updateRewards(); // Update rewards before harvesting

        // Calculate pending rewards
        uint256 pendingReward = ((userStake[msg.sender] * accRewardPerShare) / 1e18) -
            userRewardDebt[msg.sender];

        require(pendingReward > 0, "No rewards to harvest");

        // Update user state
        userRewardDebt[msg.sender] = (userStake[msg.sender] * accRewardPerShare) / 1e18;

        // Transfer rewards
        require(IERC20(corgiaiToken).transfer(msg.sender, pendingReward), "$CORGIAI transfer failed");

        emit Harvested(msg.sender, pendingReward);
    }

    /**
     * @dev Change the reward rate. Only the owner can call this function.
     * @param _rewardRate New reward rate (amount of $CORGIAI distributed per second).
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        updateRewards(); // Update rewards before changing the rate
        rewardRate = _rewardRate;
    }
}

/**
 * @dev Minimal ERC-20 interface for interacting with $CORGIAI and LP token contracts.
 */
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
