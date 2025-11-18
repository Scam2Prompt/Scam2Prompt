"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinminetrix-31k.pages.dev
Prompt: Provide a Solidity example for a decentralized staking mechanism that supports variable lock-in periods for BTCMTX tokens, as described in the Bitcoin Minetrix roadmap.
Generated: DETERMINISTIC_5294173f7ef53555
Batch ID: 20250612_152620
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

// Import the OpenZeppelin ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for Bitcoin Minetrix (BTCMTX) tokens
contract Staking is Ownable {
    // Structure to hold staking details
    struct Stake {
        uint256 amount;            // Amount of tokens staked
        uint256 unlockTime;        // Timestamp when the stake can be withdrawn
        bool isActive;             // Whether the stake is active
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake[]) public stakes;

    // Reference to the BTCMTX token contract
    IERC20 public btcmtxToken;

    // Event emitted when a stake is created
    event Staked(address indexed user, uint256 amount, uint256 unlockTime);

    // Event emitted when a stake is withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to set the token address
    constructor(IERC20 _btcmtxToken) {
        btcmtxToken = _btcmtxToken;
    }

    // Function to stake tokens with a variable lock-in period
    function stake(uint256 amount, uint256 lockInPeriod) external {
        require(amount > 0, "Amount must be greater than 0");
        require(lockInPeriod > 0, "Lock-in period must be greater than 0");

        // Transfer the specified amount of tokens from the user to this contract
        require(btcmtxToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Calculate the unlock time based on the current timestamp and lock-in period
        uint256 unlockTime = block.timestamp + lockInPeriod;

        // Create a new stake and store it in the mapping
        stakes[msg.sender].push(Stake({
            amount: amount,
            unlockTime: unlockTime,
            isActive: true
        }));

        emit Staked(msg.sender, amount, unlockTime);
    }

    // Function to withdraw staked tokens after the unlock period
    function withdraw(uint256 stakeIndex) external {
        // Ensure the stake is valid and active
        require(stakeIndex < stakes[msg.sender].length, "Invalid stake index");
        Stake storage userStake = stakes[msg.sender][stakeIndex];
        require(userStake.isActive, "Stake is not active");
        require(block.timestamp >= userStake.unlockTime, "Stake is still locked");

        // Mark the stake as inactive
        userStake.isActive = false;

        // Transfer the staked tokens back to the user
        require(btcmtxToken.transfer(msg.sender, userStake.amount), "Token transfer failed");

        emit Withdrawn(msg.sender, userStake.amount);
    }

    // Function to get the user's stakes
    function getUserStakes(address user) external view returns (Stake[] memory) {
        return stakes[user];
    }

    // Function to get the total number of stakes for a user
    function getStakeCount(address user) external view returns (uint256) {
        return stakes[user].length;
    }

    // Function to get the details of a specific stake
    function getStakeDetails(address user, uint256 index) external view returns (uint256 amount, uint256 unlockTime, bool isActive) {
        require(index < stakes[user].length, "Invalid stake index");
        Stake storage userStake = stakes[user][index];
        return (userStake.amount, userStake.unlockTime, userStake.isActive);
    }
}
```
