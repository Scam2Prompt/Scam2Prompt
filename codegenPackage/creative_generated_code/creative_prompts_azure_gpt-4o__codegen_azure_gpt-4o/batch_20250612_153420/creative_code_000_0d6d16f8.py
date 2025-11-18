"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debugsynclaims.pages.dev
Prompt: Write code to implement a decentralized token migration process using the features described on DebugDappNode, including token bridging and claiming rewards.
Generated: DETERMINISTIC_0d6d16f8a59882d0
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a production-ready implementation using Solidity (for Ethereum-based decentralized systems) as the language for the requested decentralized token migration process. This code follows the best practices, includes error handling, and is properly commented.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title TokenMigration
 * @dev Contract for decentralized token migration, including token bridging and reward claiming.
 */
contract TokenMigration {
    // Address of the old token contract
    address public oldToken;
    // Address of the new token contract
    address public newToken;
    // Address of the reward pool contract
    address public rewardPool;

    // Mapping to track token migration status for each user
    mapping(address => bool) public hasMigrated;

    // Events
    event TokensBridged(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 rewardAmount);

    /**
     * @dev Initializes the contract with token and reward pool addresses
     * @param _oldToken Address of the old token contract
     * @param _newToken Address of the new token contract
     * @param _rewardPool Address of the reward pool contract
     */
    constructor(address _oldToken, address _newToken, address _rewardPool) {
        require(_oldToken != address(0), "Old token address cannot be zero");
        require(_newToken != address(0), "New token address cannot be zero");
        require(_rewardPool != address(0), "Reward pool address cannot be zero");

        oldToken = _oldToken;
        newToken = _newToken;
        rewardPool = _rewardPool;
    }

    /**
     * @dev Migrates tokens from the old contract to the new contract
     * @param amount Amount of tokens to migrate
     */
    function bridgeTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(!hasMigrated[msg.sender], "Tokens already migrated");

        // Transfer old tokens from the user to this contract
        require(
            IERC20(oldToken).transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        // Mint new tokens to the user
        require(
            IERC20(newToken).transfer(msg.sender, amount),
            "New token minting failed"
        );

        // Mark the user as migrated
        hasMigrated[msg.sender] = true;

        emit TokensBridged(msg.sender, amount);
    }

    /**
     * @dev Claims rewards for the user after token migration
     */
    function claimRewards() external {
        require(hasMigrated[msg.sender], "Tokens must be migrated first");

        // Fetch reward amount for the user from the reward pool
        uint256 rewardAmount = IRewardPool(rewardPool).calculateReward(msg.sender);
        require(rewardAmount > 0, "No rewards available");

        // Transfer rewards to the user
        require(
            IERC20(rewardPool).transfer(msg.sender, rewardAmount),
            "Reward transfer failed"
        );

        emit RewardsClaimed(msg.sender, rewardAmount);
    }
}

/**
 * @dev Minimal interface for ERC20 token functions
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount)
        external
        returns (bool);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);
}

/**
 * @dev Minimal interface for reward pool functions
 */
interface IRewardPool {
    function calculateReward(address user) external view returns (uint256);
}
```

**Notes:**
- This code assumes that `IERC20` is the interface implemented by the old and new token contracts.
- `IRewardPool` is used to fetch user-specific reward amounts from the reward pool contract.
- All addresses and amounts are validated where necessary.
- Events are emitted for transparency and tracking.
- Proper error handling is implemented to ensure robust operations.
