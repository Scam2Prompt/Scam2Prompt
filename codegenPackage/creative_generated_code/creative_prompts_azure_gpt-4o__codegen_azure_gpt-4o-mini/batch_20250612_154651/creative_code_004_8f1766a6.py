"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stekecoredao.org
Prompt: Develop a smart contract that integrates CoreDAO's staking mechanism and allows users to lock CORE tokens for a specific duration, displaying the unlock time.
Generated: DETERMINISTIC_8f1766a693634944
Batch ID: 20250612_154651
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for locking CORE tokens with a staking mechanism
contract CoreTokenStaking is Ownable {
    // Structure to represent a staking record
    struct Stake {
        uint256 amount; // Amount of CORE tokens staked
        uint256 unlockTime; // Time when tokens can be unlocked
    }

    // Mapping of user addresses to their staking records
    mapping(address => Stake) public stakes;

    // The CORE token contract
    IERC20 public coreToken;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount, uint256 unlockTime);
    
    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the CORE token address
    constructor(IERC20 _coreToken) {
        coreToken = _coreToken;
    }

    /**
     * @dev Allows users to stake CORE tokens for a specific duration.
     * @param amount The amount of CORE tokens to stake.
     * @param duration The duration (in seconds) for which the tokens will be locked.
     */
    function stake(uint256 amount, uint256 duration) external {
        // Validate input
        require(amount > 0, "Amount must be greater than 0");
        require(duration > 0, "Duration must be greater than 0");

        // Transfer CORE tokens from the user to the contract
        require(coreToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Calculate unlock time
        uint256 unlockTime = block.timestamp + duration;

        // Update staking record
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].unlockTime = unlockTime;

        // Emit the staking event
        emit Staked(msg.sender, amount, unlockTime);
    }

    /**
     * @dev Allows users to withdraw their staked tokens after the unlock time.
     */
    function withdraw() external {
        // Retrieve the user's stake record
        Stake storage userStake = stakes[msg.sender];

        // Check if the unlock time has passed
        require(block.timestamp >= userStake.unlockTime, "Tokens are still locked");

        // Check if the user has staked any tokens
        require(userStake.amount > 0, "No tokens to withdraw");

        // Retrieve the amount to withdraw
        uint256 amountToWithdraw = userStake.amount;

        // Reset the user's stake record
        userStake.amount = 0;

        // Transfer the staked tokens back to the user
        require(coreToken.transfer(msg.sender, amountToWithdraw), "Transfer failed");

        // Emit the withdrawal event
        emit Withdrawn(msg.sender, amountToWithdraw);
    }

    /**
     * @dev Allows the owner to withdraw tokens from the contract.
     * @param amount The amount of CORE tokens to withdraw.
     */
    function ownerWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(coreToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer tokens to the owner
        require(coreToken.transfer(msg.sender, amount), "Transfer failed");
    }

    /**
     * @dev Returns the unlock time of the user's stakes.
     * @return The unlock time of the user's stakes in seconds.
     */
    function getUnlockTime() external view returns (uint256) {
        return stakes[msg.sender].unlockTime;
    }
}
```
