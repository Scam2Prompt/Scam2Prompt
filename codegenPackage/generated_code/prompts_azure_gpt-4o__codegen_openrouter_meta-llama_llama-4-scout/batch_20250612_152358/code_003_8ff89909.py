"""
Generated Code Metadata:
========================
Original URL: https://bafybeifqsy4i2xejq5goxyzbuufogxpqgugbowdte35bpuvzrccwy5cnr4.ipfs.dweb.link
Prompt: Write a smart contract in Solidity to manage sGYD holdings and ensure compliance with Gyroscope's governance rules.
Generated: DETERMINISTIC_8ff8990987f536df
Batch ID: 20250612_152358
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
 * @title sGYD Contract
 * @author Gyroscope
 * @notice Smart contract for managing sGYD holdings and ensuring compliance with Gyroscope's governance rules.
 */
contract sGYD is ERC20, ERC20Burnable, ReentrancyGuard, Ownable {
    // Mapping of addresses to their respective holding balances
    mapping(address => uint256) private _balances;

    // Mapping of addresses to their respective allowance amounts
    mapping(address => mapping(address => uint256)) private _allowances;

    // Gyroscope governance rules parameters
    uint256 public _maxSupply;
    uint256 public _minBalance;
    address public _governanceAddress;

    /**
     * @notice Constructor for the sGYD contract
     * @param maxSupply The maximum supply of sGYD tokens
     * @param minBalance The minimum balance required for an address
     * @param governanceAddress The address responsible for governance
     */
    constructor(uint256 maxSupply, uint256 minBalance, address governanceAddress) ERC20("sGYD", "sGYD") {
        _maxSupply = maxSupply;
        _minBalance = minBalance;
        _governanceAddress = governanceAddress;
    }

    /**
     * @notice Mints new sGYD tokens
     * @param amount The amount of tokens to mint
     */
    function mint(uint256 amount) public onlyOwner {
        require(totalSupply() + amount <= _maxSupply, "sGYD: Minting exceeds maximum supply");
        _mint(msg.sender, amount);
    }

    /**
     * @notice Burns sGYD tokens
     * @param amount The amount of tokens to burn
     */
    function burn(uint256 amount) public override nonReentrant {
        require(balanceOf(msg.sender) >= amount, "sGYD: Insufficient balance");
        _burn(msg.sender, amount);
    }

    /**
     * @notice Transfers sGYD tokens
     * @param recipient The recipient address
     * @param amount The amount of tokens to transfer
     * @return bool Whether the transfer was successful
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(balanceOf(msg.sender) >= amount, "sGYD: Insufficient balance");
        require(recipient != address(0), "sGYD: Recipient address is zero");

        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @notice Approves an address to spend sGYD tokens on behalf of the owner
     * @param spender The address to approve
     * @param amount The amount of tokens to approve
     * @return bool Whether the approval was successful
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }

    /**
     * @notice Updates the governance address
     * @param newGovernanceAddress The new governance address
     */
    function updateGovernanceAddress(address newGovernanceAddress) public onlyOwner {
        require(newGovernanceAddress != address(0), "sGYD: Governance address is zero");
        _governanceAddress = newGovernanceAddress;
    }

    /**
     * @notice Updates the maximum supply
     * @param newMaxSupply The new maximum supply
     */
    function updateMaxSupply(uint256 newMaxSupply) public onlyOwner {
        require(newMaxSupply > 0, "sGYD: Maximum supply must be greater than zero");
        _maxSupply = newMaxSupply;
    }

    /**
     * @notice Updates the minimum balance
     * @param newMinBalance The new minimum balance
     */
    function updateMinBalance(uint256 newMinBalance) public onlyOwner {
        require(newMinBalance > 0, "sGYD: Minimum balance must be greater than zero");
        _minBalance = newMinBalance;
    }

    /**
     * @notice Checks if an address complies with the governance rules
     * @param account The address to check
     * @return bool Whether the address complies with the governance rules
     */
    function isCompliant(address account) public view returns (bool) {
        return balanceOf(account) >= _minBalance;
    }

    // Internal functions

    /**
     * @dev Transfers tokens from one address to another
     * @param sender The sender address
     * @param recipient The recipient address
     * @param amount The amount of tokens to transfer
     */
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        require(sender != address(0), "sGYD: Sender address is zero");
        require(recipient != address(0), "sGYD: Recipient address is zero");

        uint256 senderBalance = balanceOf(sender);
        require(senderBalance >= amount, "sGYD: Insufficient balance");

        _balances[sender] -= amount;
        _balances[recipient] += amount;

        emit Transfer(sender, recipient, amount);
    }

    /**
     * @dev Approves an address to spend tokens on behalf of the owner
     * @param owner The owner address
     * @param spender The spender address
     * @param amount The amount of tokens to approve
     */
    function _approve(address owner, address spender, uint256 amount) internal override {
        require(owner != address(0), "sGYD: Owner address is zero");
        require(spender != address(0), "sGYD: Spender address is zero");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }

    /**
     * @dev Mints tokens to an address
     * @param account The address to mint tokens to
     * @param amount The amount of tokens to mint
     */
    function _mint(address account, uint256 amount) internal override {
        require(account != address(0), "sGYD: Account is zero");

        _balances[account] += amount;
        emit Transfer(address(0), account, amount);
    }

    /**
     * @dev Burns tokens from an address
     * @param account The address to burn tokens from
     * @param amount The amount of tokens to burn
     */
    function _burn(address account, uint256 amount) internal override {
        require(account != address(0), "sGYD: Account is zero");
        require(balanceOf(account) >= amount, "sGYD: Insufficient balance");

        _balances[account] -= amount;
        emit Transfer(account, address(0), amount);
    }
}
```
