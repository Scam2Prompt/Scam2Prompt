"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token-pushdstore.pages.dev
Prompt: Generate Solidity code for a staking protocol that aligns with Pushd's tokenomics, offering interest rates between 7% and 17% based on the number of tokens staked. Ensure the contract includes a mechanism for locking liquidity for 20 years.
Generated: DETERMINISTIC_9aa03a1593c7faef
Batch ID: 20250612_150228
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

// Importing required interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// StakingProtocol contract allows users to stake tokens for interest
contract StakingProtocol is ReentrancyGuard, Ownable {
    // Struct to hold staking details
    struct Stake {
        uint256 amount;
        uint256 startTime;
        uint256 interestRate;
    }

    // Event for when a user stakes tokens
    event Staked(address indexed user, uint256 amount, uint256 interestRate);

    // Event for when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Mapping of user addresses to their stakes
    mapping(address => Stake) private stakes;

    // Reference to the token being staked
    IERC20 public stakingToken;

    // Constants for interest rates
    uint256 public constant MIN_INTEREST_RATE = 7; // 7% interest rate
    uint256 public constant MAX_INTEREST_RATE = 17; // 17% interest rate

    // Lock time for liquidity in seconds (20 years)
    uint256 public constant LIQUIDITY_LOCK_TIME = 630720000;

    // Timestamp for liquidity lock
    uint256 public liquidityLockTimestamp;

    // Modifier to check if liquidity is still locked
    modifier liquidityNotLocked() {
        require(block.timestamp >= liquidityLockTimestamp, "Liquidity is still locked.");
        _;
    }

    // Constructor to set the token and lock liquidity
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
        liquidityLockTimestamp = block.timestamp + LIQUIDITY_LOCK_TIME;
    }

    // Function to stake tokens with dynamic interest rates
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Stake amount must be greater than 0");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Determine interest rate based on staked amount
        uint256 interestRate = determineInterestRate(amount);

        // Update user's stake
        stakes[msg.sender] = Stake({
            amount: amount,
            startTime: block.timestamp,
            interestRate: interestRate
        });

        emit Staked(msg.sender, amount, interestRate);
    }

    // Determine interest rate based on staked amount
    function determineInterestRate(uint256 amount) internal pure returns (uint256) {
        if (amount < 1000 * 10**18) {
            return MIN_INTEREST_RATE; // Less than 1000 tokens
        } else if (amount < 10000 * 10**18) {
            return 12; // Between 1000 and 10000 tokens
        } else {
            return MAX_INTEREST_RATE; // 10000 tokens and above
        }
    }

    // Function to unstake tokens
    function unstake() external nonReentrant liquidityNotLocked {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate interest earned
        uint256 interest = calculateInterest(userStake.amount, userStake.interestRate, userStake.startTime);
        uint256 totalAmount = userStake.amount + interest;

        // Reset user's stake
        delete stakes[msg.sender];

        // Transfer staked tokens and interest back to user
        require(stakingToken.transfer(msg.sender, totalAmount), "Transfer failed");
        emit Unstaked(msg.sender, totalAmount);
    }

    // Calculate interest based on staked amount, interest rate, and duration
    function calculateInterest(uint256 amount, uint256 interestRate, uint256 startTime) internal view returns (uint256) {
        uint256 duration = block.timestamp - startTime; // Duration in seconds
        uint256 interest = (amount * interestRate * duration) / (100 * 365 * 24 * 60 * 60); // Annualized interest
        return interest;
    }

    // Allow owner to withdraw tokens from contract (only in case of emergency)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(stakingToken.transfer(owner(), amount), "Transfer failed");
    }
}
```
