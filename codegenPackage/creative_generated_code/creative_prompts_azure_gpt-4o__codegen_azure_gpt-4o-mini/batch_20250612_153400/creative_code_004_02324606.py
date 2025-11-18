"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://too1m.pages.dev
Prompt: Write a smart contract that leverages the BASE chain ecosystem to create a staking mechanism for $POON tokens, ensuring compatibility with the memecoin's roadmap.
Generated: DETERMINISTIC_0232460620aad91d
Batch ID: 20250612_153400
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

// Import OpenZeppelin Contracts for ERC20 and Ownable functionalities
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for $POON tokens
contract POONStaking is Ownable {
    // The $POON token interface
    IERC20 public poonToken;

    // Staking structure to hold user information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Time of staking
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Events for staking and unstaking
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the $POON token address
    constructor(IERC20 _poonToken) {
        poonToken = _poonToken;
    }

    // Modifier to check if the user has staked tokens
    modifier hasStake() {
        require(stakes[msg.sender].amount > 0, "No stake found");
        _;
    }

    // Function to stake $POON tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(poonToken.balanceOf(msg.sender) >= _amount, "Insufficient balance");
        require(poonToken.allowance(msg.sender, address(this)) >= _amount, "Token allowance insufficient");

        // Transfer tokens from user to contract
        poonToken.transferFrom(msg.sender, address(this), _amount);

        // Update stake information
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake $POON tokens
    function unstake(uint256 _amount) external hasStake {
        Stake storage stakeData = stakes[msg.sender];
        require(_amount > 0 && _amount <= stakeData.amount, "Invalid unstake amount");

        // Update stake amount
        stakeData.amount -= _amount;

        // Transfer tokens back to user
        poonToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Function to check the stake of a user
    function getStake(address _user) external view returns (uint256 amount, uint256 timestamp) {
        Stake storage stakeData = stakes[_user];
        return (stakeData.amount, stakeData.timestamp);
    }

    // Function to withdraw all tokens (only owner can call this)
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(poonToken.balanceOf(address(this)) >= _amount, "Insufficient contract balance");
        poonToken.transfer(msg.sender, _amount);
    }
}
```
