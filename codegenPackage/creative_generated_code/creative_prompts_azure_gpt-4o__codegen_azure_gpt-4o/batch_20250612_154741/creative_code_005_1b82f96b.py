"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://labsprotocol.co
Prompt: Develop a smart contract that integrates LabsProtocol's staking pool functionality to allow users to stake and unstake tokens.
Generated: DETERMINISTIC_1b82f96bed63992e
Batch ID: 20250612_154741
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
 * @title LabsProtocolStakingPool
 * @dev Smart contract to enable staking and unstaking of tokens using LabsProtocol's staking pool functionality.
 *      Follows Solidity best practices and includes proper error handling.
 */
interface ILabsProtocolStakingPool {
    function stake(uint256 amount) external;
    function unstake(uint256 amount) external;
    function getStakedBalance(address user) external view returns (uint256);
}

contract LabsProtocolStaking {
    // Address of the LabsProtocol staking pool contract
    ILabsProtocolStakingPool public stakingPool;

    // Token used for staking (ERC-20)
    IERC20 public stakingToken;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the staking pool and staking token.
     * @param _stakingPool Address of the LabsProtocol staking pool contract.
     * @param _stakingToken Address of the ERC-20 token used for staking.
     */
    constructor(address _stakingPool, address _stakingToken) {
        require(_stakingPool != address(0), "Invalid staking pool address");
        require(_stakingToken != address(0), "Invalid staking token address");

        stakingPool = ILabsProtocolStakingPool(_stakingPool);
        stakingToken = IERC20(_stakingToken);
    }

    /**
     * @dev Function to stake tokens into the LabsProtocol staking pool.
     * @param amount Amount of tokens to stake.
     */
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the user to the contract
        bool success = stakingToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Approve the staking pool to spend the tokens
        stakingToken.approve(address(stakingPool), amount);

        // Call the staking pool's stake function
        stakingPool.stake(amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to unstake tokens from the LabsProtocol staking pool.
     * @param amount Amount of tokens to unstake.
     */
    function unstakeTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Call the staking pool's unstake function
        stakingPool.unstake(amount);

        // Transfer the unstaked tokens back to the user
        bool success = stakingToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Function to check the staked balance of a user in the LabsProtocol staking pool.
     * @param user Address of the user.
     * @return The staked balance of the user.
     */
    function getUserStakedBalance(address user) external view returns (uint256) {
        return stakingPool.getStakedBalance(user);
    }
}

/**
 * @dev Interface for ERC-20 token standard.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
}
```
