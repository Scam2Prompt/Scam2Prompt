"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinminetrix-31k.pages.dev
Prompt: Write a smart contract in Solidity that implements a "Stake-to-Mine" mechanism for BTCMTX tokens, where users can stake ERC-20 tokens to earn non-transferable mining credits.
Generated: DETERMINISTIC_79ba23eaa5d6f981
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

// Importing the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for the Stake-to-Mine mechanism
contract StakeToMine is Ownable {
    // ERC20 token interface
    IERC20 public stakingToken;

    // Structure to hold user's staking data
    struct Staker {
        uint256 stakedAmount;
        uint256 miningCredits;
    }
    
    // Mapping to track stakers
    mapping(address => Staker) private stakers;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws tokens
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when mining credits are earned
    event MiningCreditsEarned(address indexed user, uint256 credits);

    // Constructor to initialize the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens and earn mining credits
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staker's data
        Staker storage staker = stakers[msg.sender];
        staker.stakedAmount += amount;

        // Calculate mining credits based on the staked amount
        uint256 creditsEarned = calculateMiningCredits(amount);
        staker.miningCredits += creditsEarned;

        emit Staked(msg.sender, amount);
        emit MiningCreditsEarned(msg.sender, creditsEarned);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.stakedAmount >= amount, "Insufficient staked amount");

        // Update staker's data
        staker.stakedAmount -= amount;

        // Transfer tokens back to the user
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    // Function to calculate mining credits based on staked amount
    function calculateMiningCredits(uint256 amount) internal pure returns (uint256) {
        // For simplicity, 1 token staked = 1 mining credit earned
        return amount;
    }

    // Function to get staker's information
    function getStakerInfo(address stakerAddress) external view returns (uint256 stakedAmount, uint256 miningCredits) {
        Staker storage staker = stakers[stakerAddress];
        return (staker.stakedAmount, staker.miningCredits);
    }

    // Function to withdraw any ERC20 tokens accidentally sent to the contract
    function recoverERC20(IERC20 token, uint256 amount) external onlyOwner {
        require(token != stakingToken, "Cannot withdraw staked token");
        require(token.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
