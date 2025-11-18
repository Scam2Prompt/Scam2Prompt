"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinminetrix-en.web.app
Prompt: Write a Solidity smart contract function that distributes BTCMTX staking rewards based on the tokenomics described in the Bitcoin Minetrix whitepaper.
Generated: DETERMINISTIC_55188b901c68bb63
Batch ID: 20250612_151648
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

// Interface for the ERC20 standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// The Bitcoin Minetrix Staking Rewards contract
contract BitcoinMinetrixStakingRewards {
    // Address of the BTCMTX token
    IERC20 public btcmtxToken;

    // Mapping of addresses to their staking balances
    mapping(address => uint256) public stakingBalances;

    // Total staked tokens across all users
    uint256 public totalStaked;

    // Event to emit when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the BTCMTX token address
    constructor(address _btcmtxToken) {
        require(_btcmtxToken != address(0), "Invalid token address");
        btcmtxToken = IERC20(_btcmtxToken);
    }

    // Function to stake BTCMTX tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(btcmtxToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from the user to the contract
        bool success = btcmtxToken.transfer(address(this), amount);
        require(success, "Token transfer failed");

        // Update the user's staking balance and the total staked
        stakingBalances[msg.sender] += amount;
        totalStaked += amount;
    }

    // Function to distribute staking rewards
    function distributeRewards(uint256 totalRewards) external {
        require(totalRewards > 0, "Total rewards must be greater than zero");
        require(totalStaked > 0, "No tokens staked");

        // Calculate and distribute rewards proportionally based on staked amounts
        for (uint256 i = 0; i < totalStaked; i++) {
            address user = address(uint160(i)); // Simplified for demonstration, replace with actual user retrieval
            uint256 userShare = (stakingBalances[user] * totalRewards) / totalStaked;

            if (userShare > 0) {
                // Transfer rewards to the user
                bool success = btcmtxToken.transfer(user, userShare);
                require(success, "Reward transfer failed");
                emit RewardsDistributed(user, userShare);
            }
        }
    }

    // Function to retrieve the staking balance of an account
    function getStakingBalance(address account) external view returns (uint256) {
        return stakingBalances[account];
    }
}
```
