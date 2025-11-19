"""
Generated Code Metadata:
========================
Original URL: https://cryptotokenhub.com
Prompt: Create a customizable ERC-20 token with a reflection feature that distributes a 5% transaction fee to all token holders.
Generated: DETERMINISTIC_b87ab7e0d9c36187
Batch ID: 20250622_210026
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

/**
 * @title ReflectionToken
 * @author [Your Name]
 * @notice A customizable ERC-20 token with a reflection feature that distributes a 5% transaction fee to all token holders.
 */
contract ReflectionToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of token holder balances and reflection balances
    mapping(address => uint256) private _balances;
    mapping(address => uint256) private _reflectionBalances;

    // Total reflection balance
    uint256 private _totalReflectionBalance;

    // Total token supply
    uint256 private _totalSupply;

    // Transaction fee (5%)
    uint256 private constant _transactionFee = 500;

    /**
     * @notice Constructor
     * @param name Token name
     * @param symbol Token symbol
     * @param totalSupply Total token supply
     */
    constructor(string memory name, string memory symbol, uint256 totalSupply) ERC20(name, symbol) {
        _totalSupply = totalSupply;
        _balances[msg.sender] = totalSupply;
        _reflectionBalances[msg.sender] = totalSupply;
        _totalReflectionBalance = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @notice Returns the total token supply
     */
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    /**
     * @notice Returns the balance of a token holder
     * @param account Token holder address
     */
    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    /**
     * @notice Transfers tokens from one address to another
     * @param from Sender address
     * @param to Receiver address
     * @param amount Token amount
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        uint256 fee = amount.mul(_transactionFee).div(10000);
        uint256 sendAmount = amount.sub(fee);
        _balances[msg.sender] = _balances[msg.sender].sub(amount);
        _balances[to] = _balances[to].add(sendAmount);
        _reflectionBalances[msg.sender] = _reflectionBalances[msg.sender].sub(amount);
        _reflectionBalances[to] = _reflectionBalances[to].add(sendAmount);
        _distributeReflection(fee);
        emit Transfer(msg.sender, to, sendAmount);
        emit Transfer(msg.sender, address(this), fee);
        return true;
    }

    /**
     * @notice Transfers tokens from one address to another
     * @param from Sender address
     * @param to Receiver address
     * @param amount Token amount
     */
    function transferFrom(address from, address to, uint256 amount) public override nonReentrant returns (bool) {
        uint256 fee = amount.mul(_transactionFee).div(10000);
        uint256 sendAmount = amount.sub(fee);
        _balances[from] = _balances[from].sub(amount);
        _balances[to] = _balances[to].add(sendAmount);
        _reflectionBalances[from] = _reflectionBalances[from].sub(amount);
        _reflectionBalances[to] = _reflectionBalances[to].add(sendAmount);
        _distributeReflection(fee);
        emit Transfer(from, to, sendAmount);
        emit Transfer(from, address(this), fee);
        return true;
    }

    /**
     * @notice Distributes the transaction fee to all token holders
     * @param amount Transaction fee
     */
    function _distributeReflection(uint256 amount) internal {
        _totalReflectionBalance = _totalReflectionBalance.add(amount);
        uint256 totalSupply = totalSupply();
        for (address holder in _balances) {
            uint256 balance = _balances[holder];
            uint256 reflection = balance.mul(_totalReflectionBalance).div(totalSupply);
            _reflectionBalances[holder] = reflection;
        }
    }

    /**
     * @notice Burns tokens
     * @param amount Token amount
     */
    function burn(uint256 amount) public override nonReentrant {
        _balances[msg.sender] = _balances[msg.sender].sub(amount);
        _totalSupply = _totalSupply.sub(amount);
        _reflectionBalances[msg.sender] = _reflectionBalances[msg.sender].sub(amount);
        emit Transfer(msg.sender, address(0), amount);
    }

    /**
     * @notice Returns the reflection balance of a token holder
     * @param account Token holder address
     */
    function reflectionBalanceOf(address account) public view returns (uint256) {
        return _reflectionBalances[account];
    }
}
```
