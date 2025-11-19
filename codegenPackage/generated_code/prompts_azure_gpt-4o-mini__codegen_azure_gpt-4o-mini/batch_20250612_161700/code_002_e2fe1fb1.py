"""
Generated Code Metadata:
========================
Original URL: https://basedbrett-in.web.app
Prompt: Create a Solidity contract that allows staking and unstaking of BASE’d BRETT tokens on the Base Chain.
Generated: DETERMINISTIC_e2fe1fb108a5ccd8
Batch ID: 20250612_161700
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

// Importing the ERC20 interface for BRETT token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for BASE'd BRETT tokens
contract BrettStaking is Ownable {
    // Token to be staked
    IERC20 public brettToken;

    // Struct to hold staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of the stake
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Events for staking and unstaking
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to set the BRETT token address
    constructor(IERC20 _brettToken) {
        brettToken = _brettToken;
    }

    // Function to stake BRETT tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(brettToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to contract
        brettToken.transferFrom(msg.sender, address(this), amount);

        // Update the user's stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake BRETT tokens
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update the user's stake
        userStake.amount -= amount;

        // Transfer tokens back to the user
        brettToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // Function to get the staking timestamp of a user
    function getStakeTimestamp(address user) external view returns (uint256) {
        return stakes[user].timestamp;
    }
}
```
