"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://basedbrett-in.web.app
Prompt: Create a Solidity contract that allows staking and unstaking of BASE’d BRETT tokens on the Base Chain.
Generated: DETERMINISTIC_e2fe1fb108a5ccd8
Batch ID: 20250612_161700
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

// Importing interfaces and libraries required for ERC20 support
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for BASE'd BRETT tokens
contract BrettStaking is Ownable {
    // Token being staked
    IERC20 public brettToken;

    // Struct to hold user staking data
    struct Stake {
        uint256 amount;      // Amount staked
        uint256 timestamp;   // Timestamp of the stake
    }

    // Mapping from user address to their stake
    mapping(address => Stake) public stakes;

    // Events for staking and unstaking
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to set the BRETT token address
    constructor(address _brettToken) {
        require(_brettToken != address(0), "Invalid token address");
        brettToken = IERC20(_brettToken);
    }

    // Function to stake BRETT tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");
        require(brettToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");
        require(brettToken.allowance(msg.sender, address(this)) >= amount, "Token allowance not set");

        // Transfer the tokens from the user to this contract
        brettToken.transferFrom(msg.sender, address(this), amount);
        
        // Update the user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake BRETT tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Unstake amount must be greater than zero");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        // Update the user's stake before transferring tokens
        stakes[msg.sender].amount -= amount;

        // Transfer the tokens back to the user
        brettToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to view user's staked amount
    function stakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }
    
    // Function to view user's staking duration
    function stakingDuration(address user) external view returns (uint256) {
        return block.timestamp - stakes[user].timestamp;
    }
}
```
