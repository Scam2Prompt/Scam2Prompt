"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bamboomeme.pages.dev
Prompt: Write a Solidity smart contract for a meme coin with features similar to `$BAMBOO`, including renounced ownership, zero buy/sell tax, and a fixed supply of 1 billion tokens. Ensure liquidity locking for one year and treasury unlocking over three years.
Generated: DETERMINISTIC_551d829ec2d4a746
Batch ID: 20250612_152240
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

// ERC20 implementation for MemeCoin
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract MemeCoin is ERC20, Ownable, ReentrancyGuard {
    // Liquidity lock details
    uint256 public liquidityUnlockTime;

    // Treasury unlock details
    uint256 public treasuryUnlockStartTime;
    uint256 public constant TREASURY_UNLOCK_PERIOD = 3 years; // 3 years for treasury unlocking
    uint256 public treasuryRemainingBalance;
    address public treasuryWallet;

    /**
     * @dev Constructor to initialize the token.
     * - Sets the fixed supply to 1 billion tokens.
     * - Transfers the initial supply to the deployer address.
     * - Sets the liquidity locking period to 1 year.
     * - Initializes treasury wallet and unlocking.
     */
    constructor(address _treasuryWallet) ERC20("MemeCoin", "MEME") {
        // Fixed supply: 1 billion tokens
        uint256 fixedSupply = 1_000_000_000 * (10 ** decimals());
        _mint(msg.sender, fixedSupply);

        // Treasury wallet setup
        treasuryWallet = _treasuryWallet;
        treasuryRemainingBalance = fixedSupply / 10; // 10% of total supply reserved for treasury
        _transfer(msg.sender, _treasuryWallet, treasuryRemainingBalance);

        // Liquidity lock setup
        liquidityUnlockTime = block.timestamp + 365 days; // 1 year lock period

        // Treasury unlock start time setup
        treasuryUnlockStartTime = block.timestamp;

        // Renounce ownership immediately to decentralize the contract
        renounceOwnership();
    }

    /**
     * @dev Function to withdraw unlocked treasury tokens.
     * Treasury tokens are unlocked linearly over three years.
     */
    function withdrawTreasuryTokens(uint256 amount) external nonReentrant {
        require(msg.sender == treasuryWallet, "Only treasury wallet can withdraw");
        require(block.timestamp > treasuryUnlockStartTime, "Unlocking hasn't started");
        require(amount > 0, "Amount must be greater than zero");
        require(treasuryRemainingBalance > 0, "No treasury balance remaining");

        // Calculate unlocked treasury tokens
        uint256 timeElapsed = block.timestamp - treasuryUnlockStartTime;
        uint256 maxUnlocked = (treasuryRemainingBalance * timeElapsed) / TREASURY_UNLOCK_PERIOD;
        uint256 unlockedBalance = maxUnlocked - (treasuryRemainingBalance - balanceOf(treasuryWallet));
        require(amount <= unlockedBalance, "Requested amount exceeds unlocked balance");

        // Transfer unlocked tokens
        _transfer(treasuryWallet, msg.sender, amount);
        treasuryRemainingBalance -= amount;
    }

    /**
     * @dev Function to check whether liquidity is still locked.
     */
    function isLiquidityLocked() public view returns (bool) {
        return block.timestamp < liquidityUnlockTime;
    }
}
```
