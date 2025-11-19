"""
Generated Code Metadata:
========================
Original URL: https://etfswap-in.pages.dev
Prompt: Create a Solidity-based anti-dump mechanism for $ETFS tokens, including token burn for unsold tokens and locked liquidity pools, as described on ETFSwap.
Generated: DETERMINISTIC_44e9716f543a7b4f
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract ETFS is ERC20, Ownable {
    using SafeMath for uint256;

    // Token distribution parameters
    uint256 public constant TOTAL_SUPPLY = 100_000_000 * 10**18; // 100M tokens
    uint256 public constant PRESALE_SUPPLY = 60_000_000 * 10**18; // 60% for presale
    uint256 public constant LIQUIDITY_SUPPLY = 30_000_000 * 10**18; // 30% for liquidity
    uint256 public constant TEAM_SUPPLY = 10_000_000 * 10**18; // 10% for team

    // Anti-dump parameters
    uint256 public constant MAX_SELL_PERCENTAGE = 1; // 1% of total supply max sell per tx
    uint256 public constant SELL_COOLDOWN = 1 days; // 24h cooldown between sells
    uint256 public constant LIQUIDITY_LOCK_DURATION = 365 days; // 1 year lock

    // State variables
    uint256 public presaleEndTime;
    uint256 public liquidityLockTime;
    uint256 public lastSellTime;
    mapping(address => bool) private _isExcludedFromAntiDump;

    // Events
    event TokensBurned(uint256 amount);
    event LiquidityLocked(uint256 amount, uint256 unlockTime);
    event AntiDumpTriggered(address indexed seller, uint256 amount);

    constructor() ERC20("ETFSwap Token", "ETFS") {
        _mint(msg.sender, TOTAL_SUPPLY);
        presaleEndTime = block.timestamp + 30 days; // 30-day presale
        liquidityLockTime = block.timestamp + LIQUIDITY_LOCK_DURATION;
        _isExcludedFromAntiDump[msg.sender] = true; // Owner excluded
    }

    // Anti-dump transfer checks
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override {
        super._beforeTokenTransfer(from, to, amount);

        // Only apply anti-dump to sells (not buys or transfers)
        if (from != address(0) && to != address(0) && !_isExcludedFromAntiDump[from]) {
            // Check if presale has ended
            require(block.timestamp >= presaleEndTime, "ETFS: Presale not ended");

            // Check sell cooldown
            require(
                block.timestamp >= lastSellTime + SELL_COOLDOWN,
                "ETFS: Sell cooldown active"
            );

            // Check max sell percentage
            require(
                amount <= totalSupply().mul(MAX_SELL_PERCENTAGE).div(100),
                "ETFS: Exceeds max sell percentage"
            );

            lastSellTime = block.timestamp;
            emit AntiDumpTriggered(from, amount);
        }
    }

    // Burn unsold presale tokens after presale ends
    function burnUnsoldPresaleTokens() external onlyOwner {
        require(block.timestamp >= presaleEndTime, "ETFS: Presale not ended");
        
        uint256 unsoldAmount = balanceOf(msg.sender).sub(LIQUIDITY_SUPPLY + TEAM_SUPPLY);
        if (unsoldAmount > 0) {
            _burn(msg.sender, unsoldAmount);
            emit TokensBurned(unsoldAmount);
        }
    }

    // Lock liquidity in contract
    function lockLiquidity(uint256 amount) external onlyOwner {
        require(block.timestamp < liquidityLockTime, "ETFS: Liquidity already locked");
        require(amount <= LIQUIDITY_SUPPLY, "ETFS: Exceeds liquidity supply");

        _transfer(msg.sender, address(this), amount);
        emit LiquidityLocked(amount, liquidityLockTime);
    }

    // Release locked liquidity after lock period
    function releaseLiquidity() external onlyOwner {
        require(block.timestamp >= liquidityLockTime, "ETFS: Liquidity still locked");
        
        uint256 lockedAmount = balanceOf(address(this));
        if (lockedAmount > 0) {
            _transfer(address(this), msg.sender, lockedAmount);
        }
    }

    // Exclude/include addresses from anti-dump (for exchanges, etc.)
    function setExcludedFromAntiDump(address account, bool excluded) external onlyOwner {
        _isExcludedFromAntiDump[account] = excluded;
    }

    // Check if address is excluded from anti-dump
    function isExcludedFromAntiDump(address account) external view returns (bool) {
        return _isExcludedFromAntiDump[account];
    }
}
```
