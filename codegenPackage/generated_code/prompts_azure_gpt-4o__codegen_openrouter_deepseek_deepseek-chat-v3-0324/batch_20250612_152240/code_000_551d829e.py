"""
Generated Code Metadata:
========================
Original URL: https://bamboomeme.pages.dev
Prompt: Write a Solidity smart contract for a meme coin with features similar to `$BAMBOO`, including renounced ownership, zero buy/sell tax, and a fixed supply of 1 billion tokens. Ensure liquidity locking for one year and treasury unlocking over three years.
Generated: DETERMINISTIC_551d829ec2d4a746
Batch ID: 20250612_152240
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

contract MemeCoin is ERC20, Ownable {
    using SafeMath for uint256;

    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens
    uint256 public constant TREASURY_SUPPLY = 200_000_000 * 10**18; // 20% of total supply
    uint256 public constant LIQUIDITY_SUPPLY = 800_000_000 * 10**18; // 80% of total supply

    address public treasuryWallet;
    address public liquidityWallet;

    uint256 public liquidityLockTime;
    uint256 public treasuryUnlockStart;
    uint256 public constant TREASURY_UNLOCK_DURATION = 3 * 365 days; // 3 years
    uint256 public constant LIQUIDITY_LOCK_DURATION = 365 days; // 1 year

    bool public ownershipRenounced = false;

    constructor(
        address _treasuryWallet,
        address _liquidityWallet
    ) ERC20("MemeCoin", "MEME") {
        require(_treasuryWallet != address(0), "Treasury wallet cannot be zero address");
        require(_liquidityWallet != address(0), "Liquidity wallet cannot be zero address");

        treasuryWallet = _treasuryWallet;
        liquidityWallet = _liquidityWallet;

        _mint(_treasuryWallet, TREASURY_SUPPLY);
        _mint(_liquidityWallet, LIQUIDITY_SUPPLY);

        liquidityLockTime = block.timestamp + LIQUIDITY_LOCK_DURATION;
        treasuryUnlockStart = block.timestamp;
    }

    function renounceOwnership() public override onlyOwner {
        require(!ownershipRenounced, "Ownership already renounced");
        ownershipRenounced = true;
        super.renounceOwnership();
    }

    function transferFromLiquidity(address recipient, uint256 amount) external {
        require(msg.sender == liquidityWallet, "Only liquidity wallet can transfer");
        require(block.timestamp >= liquidityLockTime, "Liquidity is still locked");
        _transfer(liquidityWallet, recipient, amount);
    }

    function transferFromTreasury(address recipient, uint256 amount) external {
        require(msg.sender == treasuryWallet, "Only treasury wallet can transfer");
        
        uint256 elapsed = block.timestamp - treasuryUnlockStart;
        uint256 unlockedPercentage = elapsed.mul(100).div(TREASURY_UNLOCK_DURATION);
        if (unlockedPercentage > 100) {
            unlockedPercentage = 100;
        }
        
        uint256 unlockedAmount = TREASURY_SUPPLY.mul(unlockedPercentage).div(100);
        uint256 spentAmount = TREASURY_SUPPLY - balanceOf(treasuryWallet);
        
        require(spentAmount.add(amount) <= unlockedAmount, "Amount exceeds unlocked treasury");
        _transfer(treasuryWallet, recipient, amount);
    }

    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override {
        super._beforeTokenTransfer(from, to, amount);
        require(from == address(0) || to == address(0) || amount > 0, "Zero amount transfer");
    }
}
```
