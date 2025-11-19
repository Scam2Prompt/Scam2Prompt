"""
Generated Code Metadata:
========================
Original URL: https://eosgas.io
Prompt: Develop a smart contract that allows coin holders to loan or stake their tokens quarterly, representing electricity available for miners, as per eosGAS's staking mechanism.
Generated: DETERMINISTIC_3bab38002b1ad462
Batch ID: 20250612_151912
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

/**
 * @title StakingContract
 * @dev A smart contract that allows token holders to stake their tokens quarterly.
 *      This contract represents electricity available for miners, similar to eosGAS's staking mechanism.
 */
contract StakingContract is Ownable {
    IERC20 public token; // The ERC20 token being staked
    uint256 public constant STAKING_PERIOD = 90 days; // Duration for each staking period

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Timestamp when the stake was created
        bool isActive; // Status of the stake
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the token address.
     * @param _token Address of the ERC20 token to be staked.
     */
    constructor(IERC20 _token) {
        require(address(_token) != address(0), "Token address cannot be zero");
        token = _token;
    }

    /**
     * @dev Allows users to stake their tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakes[msg.sender].isActive == false, "Existing active stake found");

        // Transfer tokens from the user to the contract
        token.transferFrom(msg.sender, address(this), amount);

        // Create a new stake
        stakes[msg.sender] = Stake({
            amount: amount,
            startTime: block.timestamp,
            isActive: true
        });

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to unstake their tokens after the staking period.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.isActive, "No active stake found");
        require(block.timestamp >= userStake.startTime + STAKING_PERIOD, "Staking period not yet completed");

        // Transfer staked tokens back to the user
        uint256 amountToUnstake = userStake.amount;
        userStake.isActive = false; // Mark the stake as inactive

        // Reset the stake details
        userStake.amount = 0;
        userStake.startTime = 0;

        token.transfer(msg.sender, amountToUnstake);
        emit Unstaked(msg.sender, amountToUnstake);
    }

    /**
     * @dev Allows the owner to withdraw tokens from the contract.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance in contract");

        token.transfer(msg.sender, amount);
    }

    /**
     * @dev Returns the details of a user's stake.
     * @param user Address of the user.
     * @return amount Amount of tokens staked.
     * @return startTime Timestamp when the stake was created.
     * @return isActive Status of the stake.
     */
    function getStakeDetails(address user) external view returns (uint256 amount, uint256 startTime, bool isActive) {
        Stake storage userStake = stakes[user];
        return (userStake.amount, userStake.startTime, userStake.isActive);
    }
}
```
