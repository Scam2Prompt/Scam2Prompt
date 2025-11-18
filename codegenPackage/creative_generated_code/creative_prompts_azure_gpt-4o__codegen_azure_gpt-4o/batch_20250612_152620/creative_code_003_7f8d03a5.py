"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinminetrix-31k.pages.dev
Prompt: Provide an example of a staking contract in Solidity that auto-manages user allocations of BTCMTX tokens and generates mining credits based on the amount staked.
Generated: DETERMINISTIC_7f8d03a5c5c55756
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

/**
 * @title StakingContract
 * @notice A contract for staking BTCMTX tokens and earning mining credits based on the amount staked.
 */
contract StakingContract {
    // Struct to store details of a user's stake
    struct Stake {
        uint256 amount;       // Amount of BTCMTX tokens staked
        uint256 miningCredits; // Mining credits earned by the staker
        uint256 lastUpdated;  // Timestamp of the last update
    }

    // Mapping to store staking details for each user
    mapping(address => Stake) public stakes;

    // Total number of BTCMTX tokens staked in the contract
    uint256 public totalStaked;

    // Token contract interface
    IERC20 public btcmtxToken;

    // Mining credit rate (credits per token per second)
    uint256 public miningCreditRate;

    // Events for logging activities
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event MiningCreditsClaimed(address indexed user, uint256 credits);

    /**
     * @notice Constructor to set the token contract address and mining credit rate.
     * @param _btcmtxToken Address of the BTCMTX token contract.
     * @param _miningCreditRate Mining credit rate (credits per token staked per second).
     */
    constructor(address _btcmtxToken, uint256 _miningCreditRate) {
        require(_btcmtxToken != address(0), "Invalid token address");
        require(_miningCreditRate > 0, "Mining credit rate must be greater than zero");
        btcmtxToken = IERC20(_btcmtxToken);
        miningCreditRate = _miningCreditRate;
    }

    /**
     * @notice Stake BTCMTX tokens in the contract.
     * @param _amount Amount of BTCMTX tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Update user's mining credits before staking
        updateMiningCredits(msg.sender);

        // Transfer BTCMTX tokens from the user to the staking contract
        require(
            btcmtxToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update user's staking record
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].lastUpdated = block.timestamp;

        // Update total staked
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake BTCMTX tokens from the contract.
     * @param _amount Amount of BTCMTX tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(
            stakes[msg.sender].amount >= _amount,
            "Insufficient staked amount"
        );

        // Update user's mining credits before unstaking
        updateMiningCredits(msg.sender);

        // Update user's staking record
        stakes[msg.sender].amount -= _amount;
        stakes[msg.sender].lastUpdated = block.timestamp;

        // Update total staked
        totalStaked -= _amount;

        // Transfer BTCMTX tokens back to the user
        require(
            btcmtxToken.transfer(msg.sender, _amount),
            "Token transfer failed"
        );

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Claim accumulated mining credits.
     */
    function claimMiningCredits() external {
        // Update user's mining credits
        updateMiningCredits(msg.sender);

        // Get the user's mining credits
        uint256 credits = stakes[msg.sender].miningCredits;
        require(credits > 0, "No mining credits to claim");

        // Reset user's mining credits
        stakes[msg.sender].miningCredits = 0;

        // Emit event for claiming credits
        emit MiningCreditsClaimed(msg.sender, credits);

        // Note: Actual implementation for redeeming mining credits depends on the specific use case.
    }

    /**
     * @notice Internal function to update mining credits for a user.
     * @param _user Address of the user.
     */
    function updateMiningCredits(address _user) internal {
        Stake storage userStake = stakes[_user];
        if (userStake.amount > 0) {
            // Calculate credits earned since the last update
            uint256 timeElapsed = block.timestamp - userStake.lastUpdated;
            uint256 creditsEarned = (userStake.amount * miningCreditRate * timeElapsed) / 1e18;

            // Update user's mining credits and last updated timestamp
            userStake.miningCredits += creditsEarned;
            userStake.lastUpdated = block.timestamp;
        }
    }
}

/**
 * @dev Simplified ERC20 interface.
 */
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);
}
```
