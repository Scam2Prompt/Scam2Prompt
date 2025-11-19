"""
Generated Code Metadata:
========================
Original URL: https://smartrevenuetokens.web.app
Prompt: Design a smart contract for a token staking and unstaking mechanism with automatic synchronization across multiple non-custodial wallets.
Generated: DETERMINISTIC_284b9aa6e728fa16
Batch ID: 20250622_211159
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title StakingContract
 * @dev A smart contract for staking and unstaking ERC20 tokens with automatic synchronization.
 */
contract StakingContract is Ownable {
    using SafeMath for uint256;

    // ERC20 token to be staked
    IERC20 public stakingToken;

    // Struct to hold user staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of the last stake
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) private stakes;

    // Events for staking and unstaking
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the staking contract with the staking token.
     * @param _stakingToken Address of the ERC20 token to be staked.
     */
    constructor(IERC20 _stakingToken) {
        require(address(_stakingToken) != address(0), "Invalid token address");
        stakingToken = _stakingToken;
    }

    /**
     * @dev Stake tokens into the contract.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakingToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake information
        stakes[msg.sender].amount = stakes[msg.sender].amount.add(amount);
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens from the contract.
     * @param amount Amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        // Update user's stake information
        stakes[msg.sender].amount = stakes[msg.sender].amount.sub(amount);

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Get the staked amount of a user.
     * @param user Address of the user.
     * @return The amount of tokens staked by the user.
     */
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    /**
     * @dev Get the staking timestamp of a user.
     * @param user Address of the user.
     * @return The timestamp of the last stake.
     */
    function getStakeTimestamp(address user) external view returns (uint256) {
        return stakes[user].timestamp;
    }

    /**
     * @dev Emergency function to withdraw tokens from the contract.
     * @param amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(stakingToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens to the owner
        stakingToken.transfer(owner(), amount);
    }
}
```
