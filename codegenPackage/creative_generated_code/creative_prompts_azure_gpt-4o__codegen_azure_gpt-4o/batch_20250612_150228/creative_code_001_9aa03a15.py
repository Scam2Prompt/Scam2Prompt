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

/**
 * @title StakingContract
 * @dev A staking protocol implementing Pushd's tokenomics, with interest rates 
 * between 7% and 17% based on the number of tokens staked. Liquidity is locked 
 * for 20 years.
 */

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract StakingContract {
    // Token being staked
    IERC20 public immutable stakingToken;

    // Liquidity lock timestamp (20 years from contract deployment)
    uint256 public immutable liquidityLockTimestamp;

    // Interest rate variables
    uint256 public constant MIN_INTEREST_RATE = 7; // 7%
    uint256 public constant MAX_INTEREST_RATE = 17; // 17%
    uint256 public constant TOKEN_THRESHOLD = 1000 * 10**18; // Threshold for max interest rate

    // Struct for storing staking information
    struct Stake {
        uint256 amount;
        uint256 startTime;
    }

    // Mapping to track staking balances and timestamps for each user
    mapping(address => Stake) public stakes;

    // Events for logging staking and withdrawal
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount, uint256 interestEarned);

    /**
     * @dev Constructor initializes the contract with the staking token and liquidity lock timestamp.
     * @param _stakingToken Address of the staking token contract.
     */
    constructor(address _stakingToken) {
        require(_stakingToken != address(0), "Invalid token address");
        stakingToken = IERC20(_stakingToken);
        liquidityLockTimestamp = block.timestamp + 20 * 365 days; // Lock liquidity for 20 years
    }

    /**
     * @dev Allows users to stake tokens. Tokens are locked until withdrawn.
     * @param _amount Number of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");

        // Transfer tokens from the user's wallet to the contract
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staking information
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].startTime = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Calculates the applicable interest rate based on the amount staked.
     * @param _amount Number of tokens staked.
     * @return Interest rate percentage.
     */
    function calculateInterestRate(uint256 _amount) public pure returns (uint256) {
        if (_amount >= TOKEN_THRESHOLD) {
            return MAX_INTEREST_RATE;
        }

        // Calculate interest rate proportionally between MIN_INTEREST_RATE and MAX_INTEREST_RATE
        return MIN_INTEREST_RATE + ((_amount * (MAX_INTEREST_RATE - MIN_INTEREST_RATE)) / TOKEN_THRESHOLD);
    }

    /**
     * @dev Allows users to withdraw their staked tokens along with earned interest.
     */
    function withdraw() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");
        require(block.timestamp >= liquidityLockTimestamp, "Liquidity is locked");

        // Calculate interest
        uint256 stakingDuration = block.timestamp - userStake.startTime;
        uint256 interestRate = calculateInterestRate(userStake.amount);
        uint256 interestEarned = (userStake.amount * interestRate * stakingDuration) / (100 * 365 days);

        // Reset staking information
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].startTime = 0;

        // Transfer original staked tokens + interest back to the user
        uint256 totalAmount = userStake.amount + interestEarned;
        require(stakingToken.transfer(msg.sender, totalAmount), "Token transfer failed");

        emit Withdrawn(msg.sender, userStake.amount, interestEarned);
    }

    /**
     * @dev Returns the staked amount for a user.
     * @param _user Address of the user.
     * @return Amount of tokens staked.
     */
    function getStakedAmount(address _user) external view returns (uint256) {
        return stakes[_user].amount;
    }

    /**
     * @dev Returns the liquidity lock status.
     * @return True if liquidity is locked, false otherwise.
     */
    function isLiquidityLocked() external view returns (bool) {
        return block.timestamp < liquidityLockTimestamp;
    }
}
```
