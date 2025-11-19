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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract BambooMemeCoin is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of addresses to their respective balances and allowances
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    // Treasury and liquidity locker
    address private treasury;
    bool private _liquidityLocked;
    uint256 private _liquidityLockEnd;
    uint256 private constant _liquidityLockDuration = 365 days; // 1 year

    // Treasury unlocking schedule
    uint256 private constant _treasuryUnlockDuration = 3 years;
    uint256 private _treasuryUnlockStart;
    uint256 private _treasuryUnlockEnd;
    uint256 private _treasuryUnlockAmount;

    // Token supply
    uint256 private constant _totalSupply = 1_000_000_000 * 10**18; // 1 billion tokens with 18 decimals

    // Renounce ownership
    bool private _ownershipRenounced;

    constructor() ERC20("Bamboo Meme Coin", "BMEME") {
        // Mint initial supply to treasury
        _balances[treasury] = _totalSupply;
        emit Transfer(address(0), treasury, _totalSupply);

        // Initialize treasury unlocking schedule
        _treasuryUnlockStart = block.timestamp;
        _treasuryUnlockEnd = _treasuryUnlockStart + _treasuryUnlockDuration;
        _treasuryUnlockAmount = _totalSupply / 3;

        // Lock liquidity for 1 year
        _liquidityLocked = true;
        _liquidityLockEnd = block.timestamp + _liquidityLockDuration;
    }

    // Override transfer and transferFrom to prevent reentrancy
    function transfer(address recipient, uint256 amount) public override nonReentrant returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, _allowances[sender][msg.sender].sub(amount));
        return true;
    }

    // Override _beforeTokenTransfer to enforce liquidity lock
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256[] memory ids,
        uint256[] memory amounts
    ) internal override {
        if (_liquidityLocked && from == address(0) && to != treasury) {
            require(block.timestamp >= _liquidityLockEnd, "Liquidity is locked");
        }
    }

    // Override _mint and _burn to prevent minting and burning after renouncing ownership
    function _mint(address account, uint256 amount) internal override {
        require(!_ownershipRenounced, "Ownership has been renounced");
        super._mint(account, amount);
    }

    function _burn(address account, uint256 amount) internal override {
        require(!_ownershipRenounced, "Ownership has been renounced");
        super._burn(account, amount);
    }

    // Function to renounce ownership
    function renounceOwnership() public {
        require(msg.sender == owner(), "Only the owner can renounce ownership");
        _ownershipRenounced = true;
    }

    // Function to unlock treasury funds
    function unlockTreasury() public {
        require(msg.sender == treasury, "Only the treasury can unlock funds");
        require(block.timestamp >= _treasuryUnlockStart && block.timestamp <= _treasuryUnlockEnd, "Treasury unlock window has passed");
        uint256 unlockAmount = _treasuryUnlockAmount;
        _transfer(treasury, msg.sender, unlockAmount);
    }

    // Disable buy/sell tax by overriding _transfer
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal override {
        uint256 senderBalance = _balances[sender];
        require(senderBalance >= amount, "Insufficient balance");
        _balances[sender] = senderBalance.sub(amount);
        _balances[recipient] = _balances[recipient].add(amount);
        emit Transfer(sender, recipient, amount);
    }
}
```
