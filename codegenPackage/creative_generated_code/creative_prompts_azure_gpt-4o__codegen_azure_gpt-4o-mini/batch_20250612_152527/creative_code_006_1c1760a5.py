"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defisyncapps.pages.dev
Prompt: Develop a smart contract that supports staking and redemption of assets, utilizing the mint staking feature of Dapp Webnode.
Generated: DETERMINISTIC_1c1760a5fd87a897
Batch ID: 20250612_152527
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

// Import the necessary interfaces from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// A smart contract for staking and redeeming assets
contract StakingContract is Ownable, ReentrancyGuard {
    // Define a structure to hold staking information
    struct Stake {
        uint256 amount;
        uint256 stakingTime;
    }

    // Mapping to store user's stakes
    mapping(address => Stake) private stakes;

    // ERC20 token used for staking
    IERC20 public stakingToken;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount, uint256 timestamp);
    
    // Event emitted when a user redeems their stake
    event Redeemed(address indexed user, uint256 amount, uint256 timestamp);

    // Constructor to initialize the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update the user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].stakingTime = block.timestamp;

        emit Staked(msg.sender, amount, block.timestamp);
    }

    // Function to redeem staked tokens
    function redeem() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        
        require(userStake.amount > 0, "No staked tokens to redeem");

        // Store the amount to be redeemed
        uint256 amountToRedeem = userStake.amount;

        // Reset the user's stake information before transfer to prevent reentrancy
        userStake.amount = 0;

        // Transfer the staked tokens back to the user
        require(stakingToken.transfer(msg.sender, amountToRedeem), "Transfer failed");

        emit Redeemed(msg.sender, amountToRedeem, block.timestamp);
    }

    // Function to check the staking balance of a user
    function stakingBalance(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // Function to check the staking time of a user
    function stakingTime(address user) external view returns (uint256) {
        return stakes[user].stakingTime;
    }

    // Owner can withdraw any ERC20 tokens mistakenly sent to the contract
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token.transfer(msg.sender, amount), "Withdrawal failed");
    }
}
```
