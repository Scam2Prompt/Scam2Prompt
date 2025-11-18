"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idegen-claims.pages.dev
Prompt: Write a Solidity function to manage staking and unstaking of $IDGN tokens, ensuring smooth trading as described in the tokenomics.
Generated: DETERMINISTIC_af5ff2906f4b46fa
Batch ID: 20250612_150426
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
 * @title IDGN Staking Contract
 * @dev Manages staking and unstaking of $IDGN tokens with smooth tokenomics handling.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract IDGNStaking {
    IERC20 public immutable idgnToken; // The $IDGN token contract

    mapping(address => uint256) public stakedBalances; // Tracks staked amounts per address
    mapping(address => uint256) public stakingTimestamps; // Tracks the time user staked tokens

    uint256 public constant MINIMUM_STAKE_PERIOD = 7 days; // Minimum staking period
    uint256 public constant REWARD_PERCENTAGE = 5; // Rewards in percentage for staking

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 rewards);

    constructor(IERC20 _idgnToken) {
        idgnToken = _idgnToken;
    }

    /**
     * @notice Allows users to stake $IDGN tokens.
     * @param _amount The amount of $IDGN tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");

        // Transfer the tokens from the user to the contract
        require(idgnToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update the user's staked balance and timestamp
        stakedBalances[msg.sender] += _amount;
        stakingTimestamps[msg.sender] = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Allows users to unstake $IDGN tokens after the minimum staking period.
     */
    function unstake() external {
        uint256 stakedAmount = stakedBalances[msg.sender];
        require(stakedAmount > 0, "No tokens to unstake");

        uint256 stakedTime = block.timestamp - stakingTimestamps[msg.sender];
        require(stakedTime >= MINIMUM_STAKE_PERIOD, "Tokens are still locked");

        // Calculate rewards
        uint256 rewards = (stakedAmount * REWARD_PERCENTAGE) / 100;

        // Reset user's staked balance and timestamp
        stakedBalances[msg.sender] = 0;
        stakingTimestamps[msg.sender] = 0;

        // Transfer staked amount + rewards back to the user
        require(idgnToken.transfer(msg.sender, stakedAmount + rewards), "Token transfer failed");

        emit Unstaked(msg.sender, stakedAmount, rewards);
    }

    /**
     * @notice Allows users to check their current staked balance.
     * @param _user The address of the user.
     * @return The amount of $IDGN tokens staked by the user.
     */
    function getStakedBalance(address _user) external view returns (uint256) {
        return stakedBalances[_user];
    }

    /**
     * @notice Allows users to check their staking start time.
     * @param _user The address of the user.
     * @return The timestamp when the user staked their tokens.
     */
    function getStakingTimestamp(address _user) external view returns (uint256) {
        return stakingTimestamps[_user];
    }
}
```
