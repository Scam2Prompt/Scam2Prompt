"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://888-9jr.pages.dev
Prompt: Generate a smart contract in Solidity to facilitate staking and delegation of EIGEN tokens on EigenLayer.
Generated: DETERMINISTIC_0730e0064397f34d
Batch ID: 20250612_153314
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

// Importing necessary interfaces for ERC20 and Ownable
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title EigenLayer Staking Contract
 * @dev This contract allows users to stake EIGEN tokens and delegate their staking rights.
 */
contract EigenLayerStaking is Ownable {
    // EIGEN token contract address
    IERC20 public eigToken;

    // Struct to represent a stake
    struct Stake {
        uint256 amount;
        uint256 timestamp;
        bool active;
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) private stakes;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event Delegated(address indexed delegator, address indexed delegatee, uint256 amount);

    // Constructor to initialize the EIGEN token address
    constructor(address _eigToken) {
        require(_eigToken != address(0), "Invalid token address");
        eigToken = IERC20(_eigToken);
    }

    /**
     * @dev Stake EIGEN tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(eigToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");
        require(eigToken.allowance(msg.sender, address(this)) >= amount, "Token allowance not sufficient");

        // Transfer tokens from the sender to the contract
        eigToken.transferFrom(msg.sender, address(this), amount);

        // Update the user's stake
        stakes[msg.sender] = Stake({
            amount: amount,
            timestamp: block.timestamp,
            active: true
        });

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake EIGEN tokens.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.active, "No active stake found");
        
        uint256 amountToUnstake = userStake.amount;

        // Reset the user's stake
        userStake.active = false;
        userStake.amount = 0;

        // Transfer tokens back to the user
        eigToken.transfer(msg.sender, amountToUnstake);

        emit Unstaked(msg.sender, amountToUnstake);
    }

    /**
     * @dev Delegate staking rights to another user.
     * @param delegatee Address of the user to delegate to.
     * @param amount Amount of tokens to delegate.
     */
    function delegate(address delegatee, uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.active, "No active stake found");
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update the stake amount
        userStake.amount -= amount;

        emit Delegated(msg.sender, delegatee, amount);
    }

    /**
     * @dev Get the stake details of a user.
     * @param user Address of the user.
     * @return amount Amount of staked tokens.
     * @return timestamp Timestamp of the stake.
     * @return active Whether the stake is active or not.
     */
    function getStakeDetails(address user) external view returns (uint256 amount, uint256 timestamp, bool active) {
        Stake storage userStake = stakes[user];
        return (userStake.amount, userStake.timestamp, userStake.active);
    }
}
```
