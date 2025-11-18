"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://waveexcellentwork.net
Prompt: Write a smart contract to facilitate token staking and unstaking, ensuring compatibility with MainnetSync.
Generated: DETERMINISTIC_20d1a65ab96511de
Batch ID: 20250612_153915
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
 * @dev A smart contract for staking and unstaking ERC20 tokens with compatibility for MainnetSync.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract TokenStaking {
    // Address of the ERC20 token contract
    IERC20 public token;

    // Struct to hold staking information
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping to track stakes by user address
    mapping(address => Stake) public stakes;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the ERC20 token address
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        token = IERC20(_tokenAddress);
    }

    /**
     * @dev Allows users to stake tokens.
     * @param _amount The amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer tokens from the user to the contract
        bool success = token.transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");

        // Update the user's stake
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;

        // Emit the Staked event
        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to unstake their tokens.
     * Note: All tokens are unstaked at once.
     */
    function unstake() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens to unstake");

        // Transfer the staked tokens back to the user
        bool success = token.transfer(msg.sender, userStake.amount);
        require(success, "Token transfer failed");

        // Reset the user's stake
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].timestamp = 0;

        // Emit the Unstaked event
        emit Unstaked(msg.sender, userStake.amount);
    }

    /**
     * @dev Retrieves the staked token amount for a user.
     * @param _user The address of the user.
     * @return The amount of staked tokens.
     */
    function getStakeAmount(address _user) external view returns (uint256) {
        return stakes[_user].amount;
    }

    /**
     * @dev Retrieves the staking timestamp for a user.
     * @param _user The address of the user.
     * @return The timestamp of the user's stake.
     */
    function getStakeTimestamp(address _user) external view returns (uint256) {
        return stakes[_user].timestamp;
    }
}
```
