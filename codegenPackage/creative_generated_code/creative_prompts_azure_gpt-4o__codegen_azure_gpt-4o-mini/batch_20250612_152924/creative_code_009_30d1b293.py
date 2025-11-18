"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbitcoin-in.pages.dev
Prompt: Create a tutorial for integrating Green Bitcoin's staking mechanics into a decentralized application (dApp) using Ethereum's blockchain and smart contract functionality.
Generated: DETERMINISTIC_30d1b2932a29fb08
Batch ID: 20250612_152924
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

// Importing OpenZeppelin's ERC20 interface and Ownable contract
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for GreenBitcoin Staking
contract GreenBitcoinStaking is Ownable {
    // ERC20 token that will be staked
    IERC20 public greenBitcoinToken;

    // Struct to hold user's stake information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of when the stake was made
    }

    // Mapping to store stakes for each user
    mapping(address => Stake) public stakes;

    // Events for staking and unstaking
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    
    // Constructor to set the GreenBitcoin token contract address
    constructor(address _tokenAddress) {
        greenBitcoinToken = IERC20(_tokenAddress);
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");

        // Transfer tokens from the user to this contract
        greenBitcoinToken.transferFrom(msg.sender, address(this), _amount);

        // Update user's stake information
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount >= _amount, "Insufficient staked amount");

        // Update stake amount
        stakes[msg.sender].amount -= _amount;

        // Transfer tokens back to the user
        greenBitcoinToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Function to get the staking balance of a user
    function getStakedAmount(address _user) external view returns (uint256) {
        return stakes[_user].amount;
    }

    // Function to get the staking timestamp of a user
    function getStakeTimestamp(address _user) external view returns (uint256) {
        return stakes[_user].timestamp;
    }
}
```

This smart contract provides the basic staking mechanics for integrating Green Bitcoin’s staking functionality into a decentralized application (dApp) on the Ethereum blockchain. Be sure to test and audit the contract in a safe environment before deploying it to the main network.
