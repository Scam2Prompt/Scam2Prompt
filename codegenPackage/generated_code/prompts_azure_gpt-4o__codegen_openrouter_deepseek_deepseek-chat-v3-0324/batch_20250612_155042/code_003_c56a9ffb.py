"""
Generated Code Metadata:
========================
Original URL: https://etherealize.fi
Prompt: Provide an example of how to use Ethereum to create a global, private, and programmable financial system, as outlined by Etherealize's product suite.
Generated: DETERMINISTIC_c56a9ffb6f1dd783
Batch ID: 20250612_155042
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
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title GlobalPrivateBank
 * @dev A private, programmable financial system with multi-currency support,
 * private transactions, and programmable rules.
 */
contract GlobalPrivateBank is ERC20, Ownable, Pausable {
    using SafeMath for uint256;

    struct Account {
        uint256 balance;
        bool isFrozen;
        uint256 lastTransactionTime;
    }

    mapping(address => Account) private _accounts;
    mapping(address => bool) private _whitelist;
    mapping(address => bool) private _blacklist;
    mapping(address => uint256) private _transactionLimits;

    uint256 private _dailyLimit;
    uint256 private _transactionFee;
    address private _feeCollector;

    event Deposited(address indexed account, uint256 amount);
    event Withdrawn(address indexed account, uint256 amount);
    event TransferPrivate(address indexed from, address indexed to, uint256 amount);
    event AccountFrozen(address indexed account, bool isFrozen);
    event Whitelisted(address indexed account, bool isWhitelisted);
    event Blacklisted(address indexed account, bool isBlacklisted);

    constructor(
        string memory name_,
        string memory symbol_,
        uint256 dailyLimit_,
        uint256 transactionFee_,
        address feeCollector_
    ) ERC20(name_, symbol_) {
        _dailyLimit = dailyLimit_;
        _transactionFee = transactionFee_;
        _feeCollector = feeCollector_;
    }

    modifier onlyWhitelisted(address account) {
        require(_whitelist[account], "Account not whitelisted");
        _;
    }

    modifier notBlacklisted(address account) {
        require(!_blacklist[account], "Account is blacklisted");
        _;
    }

    modifier withinDailyLimit(address account, uint256 amount) {
        require(
            _accounts[account].lastTransactionTime.add(1 days) < block.timestamp ||
                amount <= _dailyLimit,
            "Daily limit exceeded"
        );
        _;
    }

    function deposit() external payable whenNotPaused notBlacklisted(msg.sender) {
        uint256 amount = msg.value;
        _accounts[msg.sender].balance = _accounts[msg.sender].balance.add(amount);
        _accounts[msg.sender].lastTransactionTime = block.timestamp;
        emit Deposited(msg.sender, amount);
    }

    function withdraw(uint256 amount) external whenNotPaused notBlacklisted(msg.sender) {
        require(_accounts[msg.sender].balance >= amount, "Insufficient balance");
        require(!_accounts[msg.sender].isFrozen, "Account is frozen");

        _accounts[msg.sender].balance = _accounts[msg.sender].balance.sub(amount);
        payable(msg.sender).transfer(amount);
        _accounts[msg.sender].lastTransactionTime = block.timestamp;
        emit Withdrawn(msg.sender, amount);
    }

    function transferPrivate(
        address to,
        uint256 amount
    ) external whenNotPaused onlyWhitelisted(msg.sender) onlyWhitelisted(to) {
        require(_accounts[msg.sender].balance >= amount, "Insufficient balance");
        require(!_accounts[msg.sender].isFrozen, "Account is frozen");
        require(!_accounts[to].isFrozen, "Recipient account is frozen");

        uint256 fee = amount.mul(_transactionFee).div(10000);
        uint256 transferAmount = amount.sub(fee);

        _accounts[msg.sender].balance = _accounts[msg.sender].balance.sub(amount);
        _accounts[to].balance = _accounts[to].balance.add(transferAmount);
        _accounts[_feeCollector].balance = _accounts[_feeCollector].balance.add(fee);

        _accounts[msg.sender].lastTransactionTime = block.timestamp;
        emit TransferPrivate(msg.sender, to, amount);
    }

    function setDailyLimit(uint256 newLimit) external onlyOwner {
        _dailyLimit = newLimit;
    }

    function setTransactionFee(uint256 newFee) external onlyOwner {
        _transactionFee = newFee;
    }

    function setFeeCollector(address newCollector) external onlyOwner {
        _feeCollector = newCollector;
    }

    function freezeAccount(address account, bool freeze) external onlyOwner {
        _accounts[account].isFrozen = freeze;
        emit AccountFrozen(account, freeze);
    }

    function whitelistAccount(address account, bool whitelist) external onlyOwner {
        _whitelist[account] = whitelist;
        emit Whitelisted(account, whitelist);
    }

    function blacklistAccount(address account, bool blacklist) external onlyOwner {
        _blacklist[account] = blacklist;
        emit Blacklisted(account, blacklist);
    }

    function getBalance(address account) external view returns (uint256) {
        return _accounts[account].balance;
    }

    function isWhitelisted(address account) external view returns (bool) {
        return _whitelist[account];
    }

    function isBlacklisted(address account) external view returns (bool) {
        return _blacklist[account];
    }

    function isAccountFrozen(address account) external view returns (bool) {
        return _accounts[account].isFrozen;
    }

    function pause() external onlyOwner {
        _pause();
    }

    function unpause() external onlyOwner {
        _unpause();
    }
}
```
