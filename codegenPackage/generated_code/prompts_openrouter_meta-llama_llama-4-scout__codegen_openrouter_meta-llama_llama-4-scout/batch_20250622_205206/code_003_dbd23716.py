"""
Generated Code Metadata:
========================
Original URL: https://pepeunchained-ia.pages.dev
Prompt: Develop a simple smart contract in Solidity for deploying a meme coin on a layer 2 blockchain similar to Pepe Unchained.
Generated: DETERMINISTIC_dbd23716f87d1244
Batch ID: 20250622_205206
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
 * @title MemeCoin Contract
 * @author [Your Name]
 * @notice A simple ERC20 token contract for a meme coin.
 */
contract MemeCoin is ERC20, ERC20Burnable, ReentrancyGuard, Ownable {
    // Mapping of addresses to their respective balances
    mapping(address => uint256) private _balances;

    // Mapping of addresses to their respective allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    // Total supply of the token
    uint256 private _totalSupply;

    // Minting and burning events
    event Minted(address indexed to, uint256 amount);
    event Burned(address indexed from, uint256 amount);

    /**
     * @notice Constructor for the MemeCoin contract.
     * @param name_ The name of the token.
     * @param symbol_ The symbol of the token.
     * @param initialSupply The initial supply of the token.
     */
    constructor(string memory name_, string memory symbol_, uint256 initialSupply) ERC20(name_, symbol_) {
        _totalSupply = initialSupply;
        _balances[msg.sender] = initialSupply;
        emit Minted(msg.sender, initialSupply);
    }

    /**
     * @notice Mint additional tokens.
     * @param to The address to mint the tokens to.
     * @param amount The amount of tokens to mint.
     */
    function mint(address to, uint256 amount) public onlyOwner {
        _totalSupply += amount;
        _balances[to] += amount;
        emit Minted(to, amount);
    }

    /**
     * @notice Burn tokens from the owner's balance.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public override nonReentrant {
        _burn(msg.sender, amount);
    }

    /**
     * @notice Burn tokens from a specified address.
     * @param from The address to burn tokens from.
     * @param amount The amount of tokens to burn.
     */
    function burnFrom(address from, uint256 amount) public override onlyOwner nonReentrant {
        _burn(from, amount);
    }

    /**
     * @notice Internal function to burn tokens.
     * @param account The account to burn tokens from.
     * @param amount The amount of tokens to burn.
     */
    function _burn(address account, uint256 amount) internal {
        require(amount > 0, "MemeCoin: burn amount is zero");
        require(_balances[account] >= amount, "MemeCoin: burn amount exceeds balance");

        _balances[account] -= amount;
        _totalSupply -= amount;
        emit Burned(account, amount);
        emit Transfer(account, address(0), amount);
    }

    /**
     * @notice Get the total supply of tokens.
     * @return The total supply of tokens.
     */
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    /**
     * @notice Get the balance of a specified address.
     * @param account The address to get the balance of.
     * @return The balance of the specified address.
     */
    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    /**
     * @notice Get the allowance of a specified address.
     * @param owner The owner of the tokens.
     * @param spender The spender of the tokens.
     * @return The allowance of the specified address.
     */
    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowances[owner][spender];
    }

    /**
     * @notice Approve a spender to spend a specified amount of tokens.
     * @param spender The spender to approve.
     * @param amount The amount of tokens to approve.
     * @return A boolean indicating whether the approval was successful.
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @notice Transfer tokens from the owner's balance to a specified address.
     * @param from The owner of the tokens.
     * @param to The address to transfer the tokens to.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transferFrom(address from, address to, uint256 amount) public override returns (bool) {
        uint256 currentAllowance = _allowances[from][msg.sender];
        require(currentAllowance >= amount, "MemeCoin: transfer amount exceeds allowance");

        _allowances[from][msg.sender] -= amount;
        _transfer(from, to, amount);
        return true;
    }

    /**
     * @notice Internal function to transfer tokens.
     * @param from The owner of the tokens.
     * @param to The address to transfer the tokens to.
     */
    function _transfer(address from, address to, uint256 amount) internal {
        require(amount > 0, "MemeCoin: transfer amount is zero");
        require(_balances[from] >= amount, "MemeCoin: transfer amount exceeds balance");

        _balances[from] -= amount;
        _balances[to] += amount;
        emit Transfer(from, to, amount);
    }
}
```
