"""
Generated Code Metadata:
========================
Original URL: https://help.quicksfixai.com
Prompt: "Implement a staking and unstaking feature for tokens using a decentralized protocol and handle potential errors."
Generated: DETERMINISTIC_9da1cebe476babdd
Batch ID: 20250622_205006
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
 * @title TokenStaking
 * @dev A contract for staking and unstaking tokens using a decentralized protocol.
 */
contract TokenStaking {
    // State variables
    IERC20 public stakingToken; // ERC20 token used for staking
    mapping(address => uint256) public stakedBalances; // Tracks staked balances for each user
    mapping(address => uint256) public stakingTimestamps; // Tracks staking timestamps for each user
    uint256 public totalStaked; // Total amount of tokens staked in the contract

    // Events
    event Staked(address indexed user, uint256 amount, uint256 timestamp);
    event Unstaked(address indexed user, uint256 amount, uint256 timestamp);

    /**
     * @dev Constructor to initialize the staking token.
     * @param _stakingToken Address of the ERC20 token used for staking.
     */
    constructor(IERC20 _stakingToken) {
        require(address(_stakingToken) != address(0), "Invalid token address");
        stakingToken = _stakingToken;
    }

    /**
     * @dev Stake tokens into the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the user to the contract
        bool success = stakingToken.transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");

        // Update state variables
        stakedBalances[msg.sender] += _amount;
        stakingTimestamps[msg.sender] = block.timestamp;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount, block.timestamp);
    }

    /**
     * @dev Unstake tokens from the contract.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(stakedBalances[msg.sender] >= _amount, "Insufficient staked balance");

        // Update state variables
        stakedBalances[msg.sender] -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to the user
        bool success = stakingToken.transfer(msg.sender, _amount);
        require(success, "Token transfer failed");

        emit Unstaked(msg.sender, _amount, block.timestamp);
    }

    /**
     * @dev Get the staked balance of a user.
     * @param _user Address of the user.
     * @return The staked balance of the user.
     */
    function getStakedBalance(address _user) external view returns (uint256) {
        return stakedBalances[_user];
    }

    /**
     * @dev Get the staking timestamp of a user.
     * @param _user Address of the user.
     * @return The staking timestamp of the user.
     */
    function getStakingTimestamp(address _user) external view returns (uint256) {
        return stakingTimestamps[_user];
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
