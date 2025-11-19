"""
Generated Code Metadata:
========================
Original URL: https://blockchainbetsclub-ai.pages.dev
Prompt: Write a function in Solidity to burn tokens and update the circulating supply, similar to the tokenomics described for Blockchain Bets.
Generated: DETERMINISTIC_44f48aa52c57b1fd
Batch ID: 20250612_151207
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
 * @title BlockchainBetsToken
 * @author [Your Name]
 * @notice Token contract for Blockchain Bets, allowing for burning tokens and updating circulating supply.
 */
contract BlockchainBetsToken is ERC20, ERC20Burnable, ReentrancyGuard {
    /**
     * @notice Mapping of addresses to their respective balances.
     */
    mapping(address => uint256) private _balances;

    /**
     * @notice Mapping of allowances.
     */
    mapping(address => mapping(address => uint256)) private _allowances;

    /**
     * @notice Total supply of tokens.
     */
    uint256 private _totalSupply;

    /**
     * @notice Circulating supply of tokens.
     */
    uint256 private _circulatingSupply;

    /**
     * @notice Event emitted when tokens are burned.
     */
    event TokensBurned(address indexed burner, uint256 amount);

    /**
     * @notice Constructor for the BlockchainBetsToken contract.
     * @param name Name of the token.
     * @param symbol Symbol of the token.
     * @param totalSupply Total supply of tokens.
     */
    constructor(string memory name, string memory symbol, uint256 totalSupply) ERC20(name, symbol) {
        _totalSupply = totalSupply;
        _circulatingSupply = totalSupply;
        _balances[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @notice Returns the total supply of tokens.
     */
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    /**
     * @notice Returns the circulating supply of tokens.
     */
    function circulatingSupply() public view returns (uint256) {
        return _circulatingSupply;
    }

    /**
     * @notice Burns tokens from the specified address.
     * @param amount Amount of tokens to burn.
     */
    function burn(uint256 amount) public override nonReentrant {
        _burn(msg.sender, amount);
    }

    /**
     * @notice Burns tokens from the specified address on behalf of the token owner.
     * @param account Account from which tokens will be burned.
     * @param amount Amount of tokens to burn.
     */
    function burnFrom(address account, uint256 amount) public override nonReentrant {
        _burnFrom(account, amount);
    }

    /**
     * @notice Internal function to burn tokens.
     * @param account Account from which tokens will be burned.
     * @param amount Amount of tokens to burn.
     */
    function _burn(address account, uint256 amount) internal override {
        require(amount > 0, "Burn amount must be greater than zero.");
        require(_balances[account] >= amount, "Insufficient balance.");

        _balances[account] -= amount;
        _circulatingSupply -= amount;
        _totalSupply -= amount;

        emit Transfer(account, address(0), amount);
        emit TokensBurned(account, amount);
    }

    /**
     * @notice Internal function to burn tokens on behalf of the token owner.
     * @param account Account from which tokens will be burned.
     * @param amount Amount of tokens to burn.
     */
    function _burnFrom(address account, uint256 amount) internal override {
        require(_allowances[account][msg.sender] >= amount, "Allowance exceeded.");

        _allowances[account][msg.sender] -= amount;
        _burn(account, amount);
    }

    /**
     * @notice Internal function to handle token transfers.
     * @param from Address from which tokens are being transferred.
     * @param to Address to which tokens are being transferred.
     * @param amount Amount of tokens being transferred.
     */
    function _transfer(address from, address to, uint256 amount) internal override {
        require(_balances[from] >= amount, "Insufficient balance.");

        _balances[from] -= amount;
        _balances[to] += amount;

        emit Transfer(from, to, amount);
    }

    /**
     * @notice Internal function to handle token approvals.
     * @param owner Owner of the tokens.
     * @param spender Address that will spend the tokens.
     * @param amount Amount of tokens being approved.
     */
    function _approve(address owner, address spender, uint256 amount) internal override {
        require(owner != address(0), "Owner address cannot be zero.");
        require(spender != address(0), "Spender address cannot be zero.");

        _allowances[owner][spender] = amount;

        emit Approval(owner, spender, amount);
    }
}
```
