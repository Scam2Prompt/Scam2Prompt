"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeicbp4v36pb5mqdwiyqegjmf62ex6eneyd5bhgvnobirakblg5rkze.ipfs.dweb.link
Prompt: Provide an example of how to implement a staking mechanism for $MEME tokens, referencing the Memeland Stakeland functionality.
Generated: DETERMINISTIC_fe15d12126d90d10
Batch ID: 20250612_152249
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// A staking contract for $MEME tokens similar to Memeland Stakeland functionality.
contract MemeStaking is ReentrancyGuard, Ownable {
    IERC20 public memeToken; // The address of the $MEME token contract

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Time when tokens were staked
    }
    
    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes
    uint256 public totalStaked; // Total amount of tokens staked in the contract

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    constructor(IERC20 _memeToken) {
        memeToken = _memeToken; // Initialize the $MEME token
    }

    // Function to stake $MEME tokens
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(memeToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Update the user's stake
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake $MEME tokens
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount >= _amount, "Insufficient staked amount");

        // Update the user's stake
        stakes[msg.sender].amount -= _amount;
        totalStaked -= _amount;

        // Transfer the tokens back to the user
        require(memeToken.transfer(msg.sender, _amount), "Transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address _user) external view returns (uint256) {
        return stakes[_user].amount;
    }

    // Function to get the total staked amount in the contract
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }

    // Function to withdraw any tokens sent to the contract by mistake (only owner)
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");
        require(token.transfer(owner(), amount), "Transfer failed");
    }
}
```
