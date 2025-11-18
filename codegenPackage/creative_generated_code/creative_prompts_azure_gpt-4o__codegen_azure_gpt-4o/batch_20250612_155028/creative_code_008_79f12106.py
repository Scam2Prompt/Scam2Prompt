"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shdw.so
Prompt: Create a smart contract to enforce lengthy lock-up periods for liquidity providers, incorporating incentives for long-term ecosystem participation.
Generated: DETERMINISTIC_79f121062213b4ec
Batch ID: 20250612_155028
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
 * @title LiquidityLockup
 * @dev Smart contract to enforce lock-up periods for liquidity providers and incentivize long-term participation.
 */
contract LiquidityLockup {
    // Struct to store information about a liquidity provider's deposit
    struct Deposit {
        uint256 amount;           // Amount of tokens deposited
        uint256 lockupUntil;      // Timestamp until funds are locked
        bool claimed;             // Whether the deposit has been claimed
    }

    // Mapping of user addresses to their deposits
    mapping(address => Deposit) public deposits;

    // Event emitted when a deposit is made
    event DepositMade(address indexed user, uint256 amount, uint256 lockupUntil);

    // Event emitted when a deposit is claimed
    event DepositClaimed(address indexed user, uint256 amount);

    // Incentive rate for long-term participation (e.g., 5% annual incentive)
    uint256 public constant ANNUAL_INCENTIVE_RATE = 5;

    // Minimum lock-up period in seconds (e.g., 1 year)
    uint256 public constant MIN_LOCKUP_PERIOD = 365 days;

    // Token being used for liquidity (ERC20-compliant)
    IERC20 public immutable liquidityToken;

    /**
     * @dev Constructor sets the liquidity token address.
     * @param _liquidityToken Address of the ERC20-compliant token.
     */
    constructor(IERC20 _liquidityToken) {
        liquidityToken = _liquidityToken;
    }

    /**
     * @dev Allows a user to deposit tokens with a lock-up period.
     * @param _amount Amount of tokens to deposit.
     * @param _lockupPeriod Desired lock-up period (in seconds).
     */
    function deposit(uint256 _amount, uint256 _lockupPeriod) external {
        require(_amount > 0, "Deposit amount must be greater than zero");
        require(
            _lockupPeriod >= MIN_LOCKUP_PERIOD,
            "Lock-up period must be at least the minimum required"
        );

        // Transfer tokens from the user to the contract
        require(
            liquidityToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Calculate lock-up end timestamp
        uint256 lockupUntil = block.timestamp + _lockupPeriod;

        // Ensure user has no active deposits
        require(
            deposits[msg.sender].amount == 0,
            "Existing deposit must be claimed first"
        );

        // Store the deposit information
        deposits[msg.sender] = Deposit(_amount, lockupUntil, false);

        emit DepositMade(msg.sender, _amount, lockupUntil);
    }

    /**
     * @dev Allows a user to claim their deposit after the lock-up period has expired.
     */
    function claim() external {
        Deposit storage userDeposit = deposits[msg.sender];

        // Ensure there is an active deposit
        require(userDeposit.amount > 0, "No active deposit found");

        // Ensure the lock-up period has expired
        require(
            block.timestamp >= userDeposit.lockupUntil,
            "Lock-up period has not expired yet"
        );

        // Ensure the deposit has not been claimed already
        require(!userDeposit.claimed, "Deposit already claimed");

        // Calculate incentive based on lock-up duration
        uint256 lockupDuration = userDeposit.lockupUntil - (block.timestamp - userDeposit.lockupUntil);
        uint256 incentive = (userDeposit.amount * ANNUAL_INCENTIVE_RATE * lockupDuration) / (365 days * 100);

        // Mark deposit as claimed to prevent double-spending
        userDeposit.claimed = true;

        // Transfer original deposit amount plus incentive to the user
        uint256 totalAmount = userDeposit.amount + incentive;
        require(
            liquidityToken.transfer(msg.sender, totalAmount),
            "Token transfer failed"
        );

        emit DepositClaimed(msg.sender, totalAmount);
    }

    /**
     * @dev Allows the contract owner to recover any excess tokens that are not part of user deposits.
     */
    function recoverExcessTokens() external {
        // Implement recovery functionality if needed
    }
}

/**
 * @title IERC20
 * @dev Minimal interface for ERC20 tokens used in the contract.
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
