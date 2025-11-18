"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://et-erfi-v2.com
Prompt: Create a smart contract that supports optional restaking functionality, allowing users to boost yield without compromising security, inspired by EtherFi’s EigenLayer integration.
Generated: DETERMINISTIC_f6c16928bd4ab1d2
Batch ID: 20250612_153925
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title Smart Contract for Restaking Functionality
 * @dev This contract allows users to stake tokens and optionally restake for boosted yields.
 */
contract RestakingYield is Ownable {
    // Define token interface for interaction
    IERC20 public stakedToken;

    // Struct representing a user's stake
    struct Stake {
        uint256 amount;
        uint256 timestamp;
        bool isRestaked; // Indicates if the stake is restaked for boosted yield
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount, bool isRestaked);
    
    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when a user restakes tokens for boosted yield
    event Restaked(address indexed user, uint256 amount);

    // Constructor setting the staked token address
    constructor(address _stakedToken) {
        require(_stakedToken != address(0), "Invalid token address");
        stakedToken = IERC20(_stakedToken);
    }

    /**
     * @dev Stakes a specified amount of tokens.
     * @param amount The amount of tokens to stake.
     * @param useRestake A boolean indicating if the user wants to restake.
     */
    function stake(uint256 amount, bool useRestake) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        stakes[msg.sender] = Stake({
            amount: amount,
            timestamp: block.timestamp,
            isRestaked: useRestake
        });

        emit Staked(msg.sender, amount, useRestake);
    }

    /**
     * @dev Unstakes the previously staked tokens.
     */
    function unstake() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked amount found");

        uint256 amount = userStake.amount;
        delete stakes[msg.sender]; // Clear user stake

        require(stakedToken.transfer(msg.sender, amount), "Transfer failed");
        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Allows users to restake their tokens for boosted yield.
     */
    function restake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked amount found");
        require(!userStake.isRestaked, "Already restaked");

        userStake.isRestaked = true; // Mark as restaked
        emit Restaked(msg.sender, userStake.amount);
    }

    /**
     * @dev Returns the user stake information.
     * @param user The address of the user.
     * @return amount The amount staked.
     * @return timestamp The timestamp of the stake.
     * @return isRestaked Whether the stake is restaked.
     */
    function getUserStake(address user) external view returns (uint256 amount, uint256 timestamp, bool isRestaked) {
        Stake memory userStake = stakes[user];
        return (userStake.amount, userStake.timestamp, userStake.isRestaked);
    }
}
```
