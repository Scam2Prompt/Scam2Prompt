"""
Generated Code Metadata:
========================
Original URL: https://sunpumpsun.com
Prompt: Write a Solidity smart contract for a meme coin on the TRON blockchain with fast transaction capabilities.
Generated: DETERMINISTIC_f286bda6b89cf473
Batch ID: 20250622_205726
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
 * @title MemeCoin Contract
 * @author [Your Name]
 * @notice A meme coin contract with fast transaction capabilities on the TRON blockchain.
 */
contract MemeCoin is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of addresses to their respective balances
    mapping(address => uint256) private _balances;

    // Mapping of addresses to their respective allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    // Total supply of the meme coin
    uint256 private _totalSupply;

    // Transaction fee (in %) for fast transaction capabilities
    uint256 public transactionFee;

    /**
     * @notice Constructor for the MemeCoin contract
     * @param name_ Name of the meme coin
     * @param symbol_ Symbol of the meme coin
     * @param totalSupply_ Total supply of the meme coin
     * @param transactionFee_ Transaction fee (in %) for fast transaction capabilities
     */
    constructor(string memory name_, string memory symbol_, uint256 totalSupply_, uint256 transactionFee_) ERC20(name_, symbol_) {
        _totalSupply = totalSupply_;
        _balances[msg.sender] = _totalSupply;
        transactionFee = transactionFee_;
    }

    /**
     * @notice Returns the total supply of the meme coin
     * @return uint256 Total supply of the meme coin
     */
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    /**
     * @notice Returns the balance of a specific address
     * @param account Address to retrieve balance for
     * @return uint256 Balance of the specified address
     */
    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    /**
     * @notice Transfers meme coins from one address to another
     * @param recipient Address to transfer meme coins to
     * @param amount Amount of meme coins to transfer
     * @return bool Whether the transfer was successful
     */
    function transfer(address recipient, uint256 amount) public override nonReentrant returns (bool) {
        uint256 fee = amount.mul(transactionFee).div(100);
        uint256 sendAmount = amount.sub(fee);
        _balances[msg.sender] = _balances[msg.sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(sendAmount);
        emit Transfer(msg.sender, recipient, sendAmount);
        if (fee > 0) {
            _balances[address(this)] = _balances[address(this)].add(fee);
            emit Transfer(msg.sender, address(this), fee);
        }
        return true;
    }

    /**
     * @notice Approves an address to spend a specific amount of meme coins on behalf of the owner
     * @param spender Address to approve
     * @param amount Amount of meme coins to approve
     * @return bool Whether the approval was successful
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @notice Transfers meme coins from one address to another on behalf of the owner
     * @param sender Address to transfer meme coins from
     * @param recipient Address to transfer meme coins to
     * @param amount Amount of meme coins to transfer
     * @return bool Whether the transfer was successful
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override nonReentrant returns (bool) {
        uint256 currentAllowance = _allowances[sender][msg.sender];
        if (currentAllowance != type(uint256).max) {
            _allowances[sender][msg.sender] = currentAllowance.sub(amount);
        }
        _balances[sender] = _balances[sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(amount);
        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @notice Burns a specific amount of meme coins
     * @param amount Amount of meme coins to burn
     */
    function burn(uint256 amount) public override {
        _balances[msg.sender] = _balances[msg.sender].sub(amount);
        _totalSupply = _totalSupply.sub(amount);
        emit Transfer(msg.sender, address(0), amount);
    }
}
```
