"""
Generated Code Metadata:
========================
Original URL: https://bobothebear.pages.dev
Prompt: Generate a smart contract for a meme token inspired by Bobo the Bear, including features like 0% tax and liquidity burned.
Generated: DETERMINISTIC_022cdbfd8acc0e1c
Batch ID: 20250612_163601
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

/**
 * @title BoboTheBearToken
 * @author [Your Name]
 * @notice A meme token inspired by Bobo the Bear with 0% tax and liquidity burned.
 */
contract BoboTheBearToken is ERC20, ERC20Burnable, ReentrancyGuard {
    // Mapping of addresses to their respective balances
    mapping(address => uint256) private _balances;

    // Mapping of addresses to their respective allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    // Total supply of the token
    uint256 private _totalSupply;

    // Flag to track if liquidity has been burned
    bool private _liquidityBurned;

    // Address of the liquidity pool
    address private _liquidityPool;

    /**
     * @notice Constructor function to initialize the token.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        // Initialize total supply to 0
        _totalSupply = 0;

        // Initialize liquidity burned flag to false
        _liquidityBurned = false;
    }

    /**
     * @notice Function to mint new tokens.
     * @param amount The amount of tokens to mint.
     */
    function mint(uint256 amount) public {
        // Increase total supply by the amount
        _totalSupply += amount;

        // Mint the tokens to the msg.sender
        _balances[msg.sender] += amount;

        // Emit a Transfer event
        emit Transfer(address(0), msg.sender, amount);
    }

    /**
     * @notice Function to burn tokens.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public override {
        // Check if the msg.sender has sufficient balance
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        // Decrease the msg.sender's balance by the amount
        _balances[msg.sender] -= amount;

        // Decrease total supply by the amount
        _totalSupply -= amount;

        // Emit a Transfer event
        emit Transfer(msg.sender, address(0), amount);
    }

    /**
     * @notice Function to burn liquidity.
     */
    function burnLiquidity() public nonReentrant {
        // Check if liquidity has not been burned before
        require(!_liquidityBurned, "Liquidity already burned");

        // Get the liquidity pool address
        _liquidityPool = msg.sender;

        // Burn all tokens in the liquidity pool
        uint256 liquidityPoolBalance = _balances[_liquidityPool];
        _balances[_liquidityPool] = 0;
        _totalSupply -= liquidityPoolBalance;

        // Emit a Transfer event
        emit Transfer(_liquidityPool, address(0), liquidityPoolBalance);

        // Set liquidity burned flag to true
        _liquidityBurned = true;
    }

    /**
     * @notice Function to get the total supply of the token.
     * @return The total supply of the token.
     */
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    /**
     * @notice Function to get the balance of an address.
     * @param account The address to get the balance of.
     * @return The balance of the address.
     */
    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    /**
     * @notice Function to transfer tokens.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        // Check if the msg.sender has sufficient balance
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        // Decrease the msg.sender's balance by the amount
        _balances[msg.sender] -= amount;

        // Increase the recipient's balance by the amount
        _balances[recipient] += amount;

        // Emit a Transfer event
        emit Transfer(msg.sender, recipient, amount);

        return true;
    }

    /**
     * @notice Function to approve an address to spend tokens on behalf of the msg.sender.
     * @param spender The address to approve.
     * @param amount The amount of tokens to approve.
     * @return A boolean indicating whether the approval was successful.
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        // Update the allowance
        _allowances[msg.sender][spender] = amount;

        // Emit an Approval event
        emit Approval(msg.sender, spender, amount);

        return true;
    }

    /**
     * @notice Function to get the allowance of an address to spend tokens on behalf of the owner.
     * @param owner The address of the owner.
     * @param spender The address of the spender.
     * @return The allowance of the spender.
     */
    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowances[owner][spender];
    }

    /**
     * @notice Function to transfer tokens on behalf of the owner.
     * @param from The address of the owner.
     * @param to The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override returns (bool) {
        // Check if the spender has sufficient allowance
        require(_allowances[from][msg.sender] >= amount, "Insufficient allowance");

        // Decrease the owner's balance by the amount
        _balances[from] -= amount;

        // Increase the recipient's balance by the amount
        _balances[to] += amount;

        // Decrease the spender's allowance by the amount
        _allowances[from][msg.sender] -= amount;

        // Emit a Transfer event
        emit Transfer(from, to, amount);

        return true;
    }
}
```
