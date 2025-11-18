"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bpetrarz.pages.dev
Prompt: Write a smart contract for staking tokens on the Fantom chain, incorporating gas fee optimization techniques mentioned on the site.
Generated: DETERMINISTIC_5b0918a177ae65a9
Batch ID: 20250612_152630
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
 * @title TokenStaking
 * @dev A simple staking contract for ERC20 tokens on the Fantom blockchain.
 * Optimized for gas efficiency and security.
 */
contract TokenStaking {
    // Address of the token being staked
    IERC20 public stakingToken;

    // Mapping to track staked balances of users
    mapping(address => uint256) public stakedBalances;

    // Mapping to track the last timestamp of staking
    mapping(address => uint256) public lastStakedTimestamp;

    // Total staked tokens in the contract
    uint256 public totalStaked;

    // Event declarations for transparency
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the staking token.
     * @param _stakingToken Address of the ERC20 token to stake.
     */
    constructor(IERC20 _stakingToken) {
        require(address(_stakingToken) != address(0), "Invalid token address");
        stakingToken = _stakingToken;
    }

    /**
     * @dev Stake a specific amount of tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens");

        // Update state before interacting with external contracts
        stakedBalances[msg.sender] += amount;
        lastStakedTimestamp[msg.sender] = block.timestamp;
        totalStaked += amount;

        // Transfer tokens from user to the contract
        require(
            stakingToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake a specific amount of tokens.
     * @param amount Amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake zero tokens");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update state before transferring tokens
        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        require(
            stakingToken.transfer(msg.sender, amount),
            "Token transfer failed"
        );

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Get the staked balance of a user.
     * @param user Address of the user.
     * @return The staked balance of the user.
     */
    function getStakedBalance(address user) external view returns (uint256) {
        return stakedBalances[user];
    }

    /**
     * @dev Get the total staked tokens in the contract.
     * @return Total staked tokens.
     */
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }
}

// Minimal interface for interacting with ERC20 tokens
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
