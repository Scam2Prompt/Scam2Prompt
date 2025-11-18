"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://basedbrettoken.web.app
Prompt: Write Solidity code to implement a staking mechanism for the BRETT token within the BASE chain ecosystem.
Generated: DETERMINISTIC_81a0994f47fb9de1
Batch ID: 20250612_152710
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

// Importing the interface for ERC20 token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract BrettStaking is Ownable {
    // Token to be staked
    IERC20 public brettToken;

    // Structure to hold user staking data
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of staking
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Events for logging staking and unstaking actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to set the BRETT token address
    constructor(IERC20 _brettToken) {
        brettToken = _brettToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(brettToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to contract
        brettToken.transferFrom(msg.sender, address(this), amount);

        // Update user's staking information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];

        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update user's staked amount
        userStake.amount -= amount;

        // Transfer tokens back to the user
        brettToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to view staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // Function to view the timestamp of a user's stake
    function getStakeTimestamp(address user) external view returns (uint256) {
        return stakes[user].timestamp;
    }

    // Function to withdraw accidentally sent tokens (not BRETT token)
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token != brettToken, "Cannot withdraw BRETT tokens");
        require(token.balanceOf(address(this)) >= amount, "Insufficient token balance in contract");

        token.transfer(msg.sender, amount);
    }
}
```
