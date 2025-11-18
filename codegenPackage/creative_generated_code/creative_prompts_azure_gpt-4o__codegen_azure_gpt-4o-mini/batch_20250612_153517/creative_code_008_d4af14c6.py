"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-join.pages.dev
Prompt: Write a Solidity function to handle staking and distribution for a multi-chain fundraising platform, ensuring compatibility with multiple blockchains as described on the Airdrop platform.
Generated: DETERMINISTIC_d4af14c696fd0c34
Batch ID: 20250612_153517
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

// Interface for interacting with a multi-chain bridge
interface IMultiChainBridge {
    function transfer(address token, address to, uint256 amount) external returns (bool);
}

// Staking contract for handling fundraising
contract MultiChainStaking is Ownable {
    // Struct to store staking information
    struct Stake {
        uint256 amount; // Amount staked
        uint256 since;  // Timestamp of the stake
    }

    // Mapping of user addresses to their stake information
    mapping(address => Stake) private stakes;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount, uint256 timestamp);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount, uint256 timestamp);

    // Token used for staking
    IERC20 public stakingToken;
    // Multi-chain bridge instance
    IMultiChainBridge public bridge;

    // Constructor to set the staking token and bridge
    constructor(IERC20 _stakingToken, IMultiChainBridge _bridge) {
        stakingToken = _stakingToken;
        bridge = _bridge;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer tokens from user to this contract
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        // Update user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].since = block.timestamp;

        emit Staked(msg.sender, amount, block.timestamp);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked balance");
        
        // Update user's stake information
        stakes[msg.sender].amount -= amount;

        // Transfer tokens back to user
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount, block.timestamp);
    }

    // Function to distribute funds across chains
    function distributeFunds(address recipient, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer tokens to the multi-chain bridge for distribution
        require(stakingToken.transfer(address(bridge), amount), "Transfer failed");
        require(bridge.transfer(address(stakingToken), recipient, amount), "Bridge transfer failed");
    }

    // Function to get the stake of a user
    function getStake(address user) external view returns (uint256 amount, uint256 since) {
        Stake memory userStake = stakes[user];
        return (userStake.amount, userStake.since);
    }
}
```
