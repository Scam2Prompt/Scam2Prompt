"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wlfi.vercel.app
Prompt: Write a Solidity smart contract that interacts with the $WLFI token contract to enable staking functionality for users.
Generated: DETERMINISTIC_c97ea7088868e62e
Batch ID: 20250612_151932
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

// Importing the ERC20 interface for the $WLFI token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract WLFIStaking is Ownable {
    // The $WLFI token contract
    IERC20 public wlfiToken;

    // Struct to hold user staking information
    struct Staker {
        uint256 amountStaked;   // Amount of $WLFI staked
        uint256 lastStakedTime; // Last time the user staked tokens
    }

    // Mapping of user addresses to their staking information
    mapping(address => Staker) public stakers;

    // Events for staking and unstaking
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to set the $WLFI token address
    constructor(address _wlfiTokenAddress) {
        require(_wlfiTokenAddress != address(0), "Invalid token address");
        wlfiToken = IERC20(_wlfiTokenAddress);
    }

    // Function to stake $WLFI tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        require(wlfiToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer the tokens from the user to the contract
        bool success = wlfiToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += amount;
        staker.lastStakedTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake $WLFI tokens
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Update staker information
        staker.amountStaked -= amount;

        // Transfer the tokens back to the user
        bool success = wlfiToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to check the staking balance of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakers[user].amountStaked;
    }

    // Function to check the total staked amount in the contract
    function totalStaked() external view returns (uint256) {
        uint256 total = 0;
        for (uint256 i = 0; i < stakers.length; i++) {
            total += stakers[stakersList[i]].amountStaked;
        }
        return total;
    }
}
```
