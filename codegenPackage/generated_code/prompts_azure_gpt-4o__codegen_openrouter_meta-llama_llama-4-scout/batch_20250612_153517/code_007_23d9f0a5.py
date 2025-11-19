"""
Generated Code Metadata:
========================
Original URL: https://peng-six.vercel.app
Prompt: Design a smart contract for a meme token similar to $PENG, ensuring it includes features like revoked minting and liquidity freezing.
Generated: DETERMINISTIC_23d9f0a56d2f3328
Batch ID: 20250612_153517
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
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MemeToken
 * @author [Your Name]
 * @notice A meme token with revoked minting and liquidity freezing features.
 */
contract MemeToken is ERC20, ERC20Burnable, ReentrancyGuard, Ownable {
    // Mapping of addresses to their respective balances
    mapping(address => uint256) private _balances;

    // Mapping of addresses to their respective allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    // Total supply of the token
    uint256 private _totalSupply;

    // Flag to track if minting is revoked
    bool private _mintingRevoked;

    // Flag to track if liquidity is frozen
    bool private _liquidityFrozen;

    // Address of the liquidity pool
    address private _liquidityPool;

    /**
     * @notice Constructor for the MemeToken contract.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     * @param initialSupply The initial supply of the token.
     */
    constructor(string memory name, string memory symbol, uint256 initialSupply) ERC20(name, symbol) {
        _totalSupply = initialSupply;
        _balances[msg.sender] = initialSupply;
        emit Transfer(address(0), msg.sender, initialSupply);
    }

    /**
     * @notice Mints new tokens.
     * @param amount The amount of tokens to mint.
     * @dev Only callable by the owner if minting is not revoked.
     */
    function mint(uint256 amount) public onlyOwner {
        require(!_mintingRevoked, "Minting has been revoked");
        _totalSupply += amount;
        _balances[msg.sender] += amount;
        emit Transfer(address(0), msg.sender, amount);
    }

    /**
     * @notice Revokes minting of new tokens.
     * @dev Only callable by the owner.
     */
    function revokeMinting() public onlyOwner {
        _mintingRevoked = true;
    }

    /**
     * @notice Freezes liquidity.
     * @dev Only callable by the owner.
     */
    function freezeLiquidity() public onlyOwner {
        _liquidityFrozen = true;
    }

    /**
     * @notice Unfreezes liquidity.
     * @dev Only callable by the owner.
     */
    function unfreezeLiquidity() public onlyOwner {
        _liquidityFrozen = false;
    }

    /**
     * @notice Transfers tokens to another address.
     * @param to The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     * @dev Checks if liquidity is frozen and if the recipient is the liquidity pool.
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        require(!(_liquidityFrozen && to == _liquidityPool), "Liquidity is frozen");
        return super.transfer(to, amount);
    }

    /**
     * @notice Transfers tokens from one address to another.
     * @param from The address to transfer tokens from.
     * @param to The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     * @dev Checks if liquidity is frozen and if the recipient is the liquidity pool.
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        require(!(_liquidityFrozen && to == _liquidityPool), "Liquidity is frozen");
        return super.transferFrom(from, to, amount);
    }

    /**
     * @notice Returns the total supply of tokens.
     * @return The total supply of tokens.
     */
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    /**
     * @notice Returns the balance of an address.
     * @param account The address to get the balance of.
     * @return The balance of the address.
     */
    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    /**
     * @notice Returns the allowance of an address.
     * @param owner The address to get the allowance of.
     * @param spender The address to get the allowance for.
     * @return The allowance of the address.
     */
    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowances[owner][spender];
    }

    /**
     * @notice Approves an address to spend tokens.
     * @param spender The address to approve.
     * @param amount The amount of tokens to approve.
     * @return A boolean indicating whether the approval was successful.
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @notice Increases the allowance of an address.
     * @param spender The address to increase the allowance of.
     * @param addedValue The amount to increase the allowance by.
     * @return A boolean indicating whether the increase was successful.
     */
    function increaseAllowance(address spender, uint256 addedValue) public override returns (bool) {
        uint256 currentAllowance = _allowances[msg.sender][spender];
        _allowances[msg.sender][spender] = currentAllowance + addedValue;
        emit Approval(msg.sender, spender, _allowances[msg.sender][spender]);
        return true;
    }

    /**
     * @notice Decreases the allowance of an address.
     * @param spender The address to decrease the allowance of.
     * @param subtractedValue The amount to decrease the allowance by.
     * @return A boolean indicating whether the decrease was successful.
     */
    function decreaseAllowance(address spender, uint256 subtractedValue) public override returns (bool) {
        uint256 currentAllowance = _allowances[msg.sender][spender];
        require(currentAllowance >= subtractedValue, "ERC20: decreased allowance below zero");
        _allowances[msg.sender][spender] = currentAllowance - subtractedValue;
        emit Approval(msg.sender, spender, _allowances[msg.sender][spender]);
        return true;
    }

    /**
     * @notice Burns tokens.
     * @param amount The amount of tokens to burn.
     * @dev Only callable by the owner or if the sender has sufficient balance.
     */
    function burn(uint256 amount) public override {
        require(_balances[msg.sender] >= amount, "ERC20: burn amount exceeds balance");
        _balances[msg.sender] -= amount;
        _totalSupply -= amount;
        emit Transfer(msg.sender, address(0), amount);
    }
}
```
