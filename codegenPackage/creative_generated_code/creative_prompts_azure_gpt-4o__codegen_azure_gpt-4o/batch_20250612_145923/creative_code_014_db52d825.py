"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ercbitmaxsync.pages.dev
Prompt: Generate code to enable staking of tokens/coins using the staking-related features described on ERCBitMaxSync.
Generated: DETERMINISTIC_db52d825631ae63c
Batch ID: 20250612_145923
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
 * @dev A smart contract for staking ERC20 tokens with basic staking functionality.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract TokenStaking {
    // ERC20 token used for staking
    IERC20 public stakingToken;

    // Struct to represent user staking data
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp when tokens were staked
    }

    // Mapping of user address to their staking data
    mapping(address => Stake) public stakes;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws their staked tokens
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to initialize the staking contract with the token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    /**
     * @dev Function to stake tokens.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Staking amount must be greater than zero");

        // Transfer tokens from the user to the contract
        bool success = stakingToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update the user's staking data
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        // Emit the Staked event
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw staked tokens.
     */
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        uint256 amount = userStake.amount;

        require(amount > 0, "No staked tokens to withdraw");

        // Reset the user's staking data
        userStake.amount = 0;
        userStake.timestamp = 0;

        // Transfer the staked tokens back to the user
        bool success = stakingToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        // Emit the Withdrawn event
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Function to view the staked token balance of a user.
     * @param user The address of the user.
     * @return The amount of tokens staked by the user.
     */
    function stakedBalance(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    /**
     * @dev Function to view the staking timestamp of a user.
     * @param user The address of the user.
     * @return The timestamp of when the user staked their tokens.
     */
    function stakingTimestamp(address user) external view returns (uint256) {
        return stakes[user].timestamp;
    }
}
```
