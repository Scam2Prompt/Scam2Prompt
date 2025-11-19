"""
Generated Code Metadata:
========================
Original URL: https://basedonpepe.pages.dev
Prompt: Write a code snippet for a smart contract that mimics the features of Based $PEPE, including 0% tax and liquidity locking.
Generated: DETERMINISTIC_6724761aa1250a95
Batch ID: 20250612_163807
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

contract BasedPepe is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of addresses to their respective balances
    mapping(address => uint256) private _balances;

    // Mapping of addresses to their respective allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    // Total supply of tokens
    uint256 private _totalSupply;

    // Flag to track if liquidity is locked
    bool private _liquidityLocked;

    // Address of the liquidity pool
    address private _liquidityPool;

    // Address of the contract owner
    address private _owner;

    /**
     * @dev Constructor function
     * @param name_ Name of the token
     * @param symbol_ Symbol of the token
     * @param totalSupply_ Total supply of tokens
     */
    constructor(string memory name_, string memory symbol_, uint256 totalSupply_) ERC20(name_, symbol_) {
        _totalSupply = totalSupply_;
        _balances[msg.sender] = totalSupply_;
        _owner = msg.sender;
        _liquidityLocked = false;
    }

    /**
     * @dev Function to handle token transfers
     * @param from Address of the sender
     * @param to Address of the recipient
     * @param amount Amount of tokens to transfer
     * @return bool indicating success or failure
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        require(to != address(0), "ERC20: transfer to the zero address");
        require(amount > 0, "ERC20: transfer amount must be greater than zero");

        _balances[msg.sender] = _balances[msg.sender].sub(amount);
        _balances[to] = _balances[to].add(amount);

        emit Transfer(msg.sender, to, amount);
        return true;
    }

    /**
     * @dev Function to handle token approvals
     * @param spender Address of the spender
     * @param amount Amount of tokens to approve
     * @return bool indicating success or failure
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        require(spender != address(0), "ERC20: approve to the zero address");

        _allowances[msg.sender][spender] = amount;

        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Function to handle token transfers with allowance
     * @param from Address of the sender
     * @param to Address of the recipient
     * @param amount Amount of tokens to transfer
     * @return bool indicating success or failure
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        require(from != address(0), "ERC20: transferFrom from the zero address");
        require(to != address(0), "ERC20: transferFrom to the zero address");
        require(amount > 0, "ERC20: transferFrom amount must be greater than zero");
        require(
            _allowances[from][msg.sender] >= amount,
            "ERC20: transferFrom amount exceeds allowance"
        );

        _allowances[from][msg.sender] = _allowances[from][msg.sender].sub(amount);
        _balances[from] = _balances[from].sub(amount);
        _balances[to] = _balances[to].add(amount);

        emit Transfer(from, to, amount);
        return true;
    }

    /**
     * @dev Function to lock liquidity
     * @param liquidityPool Address of the liquidity pool
     */
    function lockLiquidity(address liquidityPool) public {
        require(msg.sender == _owner, "Only the owner can lock liquidity");
        require(!_liquidityLocked, "Liquidity is already locked");
        require(liquidityPool != address(0), "Liquidity pool address cannot be zero");

        _liquidityPool = liquidityPool;
        _liquidityLocked = true;

        emit LiquidityLocked(liquidityPool);
    }

    /**
     * @dev Function to unlock liquidity
     */
    function unlockLiquidity() public {
        require(msg.sender == _owner, "Only the owner can unlock liquidity");
        require(_liquidityLocked, "Liquidity is not locked");

        _liquidityLocked = false;

        emit LiquidityUnlocked();
    }

    /**
     * @dev Function to get the total supply of tokens
     * @return uint256 total supply
     */
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    /**
     * @dev Function to get the balance of an address
     * @param account Address to get balance for
     * @return uint256 balance
     */
    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    /**
     * @dev Function to get the allowance of an address
     * @param owner Address of the owner
     * @param spender Address of the spender
     * @return uint256 allowance
     */
    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowances[owner][spender];
    }

    /**
     * @dev Function to burn tokens
     * @param amount Amount of tokens to burn
     */
    function burn(uint256 amount) public override {
        require(amount > 0, "Burn amount must be greater than zero");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        _balances[msg.sender] = _balances[msg.sender].sub(amount);
        _totalSupply = _totalSupply.sub(amount);

        emit Transfer(msg.sender, address(0), amount);
    }

    /**
     * @dev Function to mint tokens
     * @param to Address to mint tokens for
     * @param amount Amount of tokens to mint
     */
    function mint(address to, uint256 amount) public {
        require(msg.sender == _owner, "Only the owner can mint tokens");
        require(to != address(0), "Mint to address cannot be zero");
        require(amount > 0, "Mint amount must be greater than zero");

        _balances[to] = _balances[to].add(amount);
        _totalSupply = _totalSupply.add(amount);

        emit Transfer(address(0), to, amount);
    }

    // Events
    event LiquidityLocked(address liquidityPool);
    event LiquidityUnlocked();
}
```
