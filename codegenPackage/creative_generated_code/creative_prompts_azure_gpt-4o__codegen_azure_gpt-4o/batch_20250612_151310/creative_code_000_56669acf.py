"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kelexocrypto.pages.dev
Prompt: Write a smart contract for a cryptocurrency presale similar to KoalaKash, ensuring that team tokens are locked for 550 days and liquidity is locked for life. Include comments explaining each step.
Generated: DETERMINISTIC_56669acfe2e6d243
Batch ID: 20250612_151310
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
 * @title CryptoPresale
 * @dev A smart contract for cryptocurrency presale with token locking mechanisms.
 */
contract CryptoPresale {
    // Token details
    address public tokenAddress;
    address public owner;
    
    // Team token lock details
    uint256 public constant TEAM_LOCK_PERIOD = 550 days;
    uint256 public teamLockStartTime;
    uint256 public teamTokensLocked;

    // Liquidity lock details
    bool public liquidityLocked;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event LiquidityLocked();
    event TeamTokensReleased(uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier teamTokensUnlocked() {
        require(block.timestamp >= teamLockStartTime + TEAM_LOCK_PERIOD, "Team tokens are still locked");
        _;
    }

    constructor(address _tokenAddress) {
        tokenAddress = _tokenAddress;
        owner = msg.sender;
        liquidityLocked = false;
        teamLockStartTime = block.timestamp; // Record the lock start time
    }

    /**
     * @dev Function to purchase presale tokens
     * @param buyer The address of the buyer
     * @param amount The amount of tokens to purchase
     */
    function purchaseTokens(address buyer, uint256 amount) external {
        require(buyer != address(0), "Invalid buyer address");
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens to the buyer
        // Requires proper token approval prior to calling this function
        (bool success) = ERC20(tokenAddress).transferFrom(owner, buyer, amount);
        require(success, "Token transfer failed");

        emit TokensPurchased(buyer, amount);
    }

    /**
     * @dev Function to lock liquidity permanently
     */
    function lockLiquidity() external onlyOwner {
        require(!liquidityLocked, "Liquidity is already locked");
        liquidityLocked = true;

        emit LiquidityLocked();
    }

    /**
     * @dev Function to release team tokens after the lock period
     */
    function releaseTeamTokens(uint256 amount) external onlyOwner teamTokensUnlocked {
        require(amount > 0, "Amount must be greater than zero");
        require(amount <= teamTokensLocked, "Insufficient locked tokens");

        teamTokensLocked -= amount;

        // Transfer tokens back to the owner
        (bool success) = ERC20(tokenAddress).transfer(owner, amount);
        require(success, "Token transfer failed");

        emit TeamTokensReleased(amount);
    }

    /**
     * @dev Emergency function to reclaim locked tokens
     * Must only be used when there is no liquidity compromise.
     */
    function emergencyReleaseLockedTokens() only
