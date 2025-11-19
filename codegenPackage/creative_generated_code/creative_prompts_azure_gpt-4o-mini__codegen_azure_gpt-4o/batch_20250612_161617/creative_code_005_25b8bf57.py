"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://green-bitcoins-en.pages.dev
Prompt: Create a sample Solidity contract that allows users to stake their $GBTC tokens and automatically calculates their rewards based on the staking duration.
Generated: DETERMINISTIC_25b8bf574cd59322
Batch ID: 20250612_161617
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
 * @title StakingContract
 * @dev Allows users to stake $GBTC tokens and receive rewards based on staking duration.
 */
contract StakingContract {
    
    // ERC20 interface for the token
    IERC20 public gbtcToken;

    // Reward rate per second (scaled to avoid decimals)
    uint256 public rewardRatePerSecond; 

    // Mapping to track user stakes
    mapping(address => uint256) public stakedAmount; // Amount of tokens staked by a user
    mapping(address => uint256) public stakingStartTime; // Time when staking began for a user

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 rewards);

    /**
     * @dev Constructor to initialize contract variables.
     * @param _gbtcToken Address of the $GBTC token contract.
     * @param _rewardRatePerSecond Reward rate (scaled) per second.
     */
    constructor(address _gbtcToken, uint256 _rewardRatePerSecond) {
        require(_gbtcToken != address(0), "Invalid token address");
        require(_rewardRatePerSecond > 0, "Reward rate must be positive");

        gbtcToken = IERC20(_gbtcToken);
        rewardRatePerSecond = _rewardRatePerSecond;
    }

    /**
     * @dev Stake $GBTC tokens.
     * @param _amount Amount of $GBTC tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(gbtcToken.balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        // Transfer tokens from user to contract
        bool success = gbtcToken.transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");

        // Update staking details
        stakedAmount[msg.sender] += _amount;
        stakingStartTime[msg.sender] = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake $GBTC tokens and claim rewards.
     */
    function unstake() external {
        uint256 amountStaked = stakedAmount[msg.sender];
        require(amountStaked > 0, "No tokens to unstake");

        // Calculate rewards
        uint256 stakingDuration = block.timestamp - stakingStartTime[msg.sender];
        uint256 rewards = stakingDuration * rewardRatePerSecond * amountStaked;

        // Reset staking details
        stakedAmount[msg.sender] = 0;
        stakingStartTime[msg.sender] = 0;

        // Transfer staked tokens and rewards to user
        bool tokenTransferSuccess = gbtcToken.transfer(msg.sender, amountStaked);
        require(tokenTransferSuccess, "Token transfer failed");

        bool rewardTransferSuccess = gbtcToken.transfer(msg.sender, rewards);
        require(rewardTransferSuccess, "Reward transfer failed");

        emit Unstaked(msg.sender, amountStaked, rewards);
    }

    /**
     * @dev View function to calculate pending rewards for a user.
     * @param _user Address of the user.
     * @return Pending rewards for the user.
     */
    function calculateRewards(address _user) external view returns (uint256) {
        uint256 amountStaked = stakedAmount[_user];
        if (amountStaked == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - stakingStartTime[_user];
        return stakingDuration * rewardRatePerSecond * amountStaked;
    }
}

/**
 * @dev Interface for ERC20 tokens.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
