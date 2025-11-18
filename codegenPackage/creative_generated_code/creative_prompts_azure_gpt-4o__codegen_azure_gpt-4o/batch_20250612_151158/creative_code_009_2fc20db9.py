"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appwienerclaim.pages.dev
Prompt: Write a Solidity contract for a token staking system that supports high APY rewards and tracks the percentage of tokens staked, similar to WienerAI.
Generated: DETERMINISTIC_2fc20db9bcd38842
Batch ID: 20250612_151158
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
 * @dev A token staking contract that supports high APY rewards and tracks user stakes.
 * Users can stake tokens, earn rewards, and withdraw both their stake and rewards.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract StakingContract {
    // State variables
    IERC20 public stakingToken; // ERC20 token used for staking
    uint256 public apy; // Annual Percentage Yield for rewards
    uint256 public constant SECONDS_IN_YEAR = 365 * 24 * 60 * 60;

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Timestamp when the stake was made
    }

    mapping(address => Stake) public stakes; // Tracks stakes for each user
    uint256 public totalStaked; // Total tokens staked in the contract

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event APYUpdated(uint256 oldAPY, uint256 newAPY);

    // Constructor
    constructor(IERC20 _stakingToken, uint256 _apy) {
        require(_apy > 0, "APY must be greater than zero");
        stakingToken = _stakingToken;
        apy = _apy;
    }

    /**
     * @dev Allows a user to stake tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer tokens from user to the contract
        require(
            stakingToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update the user's stake
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += _amount;
        userStake.startTime = block.timestamp;

        // Update total staked
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows a user to unstake tokens and claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards
        uint256 stakingDuration = block.timestamp - userStake.startTime;
        uint256 reward = (userStake.amount * apy * stakingDuration) / (SECONDS_IN_YEAR * 100);

        // Transfer staked tokens and rewards to the user
        uint256 totalAmount = userStake.amount + reward;
        require(
            stakingToken.transfer(msg.sender, totalAmount),
            "Token transfer failed"
        );

        // Update total staked and reset user's stake
        totalStaked -= userStake.amount;
        userStake.amount = 0;
        userStake.startTime = 0;

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    /**
     * @dev Updates the APY, callable only by the contract owner.
     * @param _newAPY New APY value.
     */
    function updateAPY(uint256 _newAPY) external {
        // In a production contract, this should be restricted to the owner (e.g., using Ownable).
        require(_newAPY > 0, "APY must be greater than zero");

        uint256 oldAPY = apy;
        apy = _newAPY;

        emit APYUpdated(oldAPY, _newAPY);
    }

    /**
     * @dev Returns the percentage of total tokens staked by a user.
     * @param _user Address of the user.
     * @return Percentage of total tokens staked by the user.
     */
    function percentageStaked(address _user) external view returns (uint256) {
        Stake storage userStake = stakes[_user];
        if (totalStaked == 0) {
            return 0;
        }
        return (userStake.amount * 100) / totalStaked;
    }
}
```
