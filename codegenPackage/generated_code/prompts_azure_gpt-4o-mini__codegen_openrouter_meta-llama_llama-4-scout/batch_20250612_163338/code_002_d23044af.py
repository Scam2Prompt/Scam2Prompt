"""
Generated Code Metadata:
========================
Original URL: https://claimtontigertokenapp.pages.dev
Prompt: Generate a Solidity smart contract for a token that follows the tokenomics principles outlined for $TIGER on the claimtontigertokenapp page.
Generated: DETERMINISTIC_d23044af9aad3382
Batch ID: 20250612_163338
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
 * @title TigerToken
 * @author [Your Name]
 * @notice A token contract following tokenomics principles for $TIGER.
 */
contract TigerToken is ERC20, ERC20Burnable, ReentrancyGuard, Ownable {
    // Mapping of addresses to their respective balances and allowances
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    // Tokenomics parameters
    uint256 public _totalSupply;
    uint256 public _maxSupply;
    uint256 public _initialSupply;
    uint256 public _burnRate;

    /**
     * @notice Constructor for the TigerToken contract.
     * @param maxSupply The maximum supply of tokens.
     * @param initialSupply The initial supply of tokens.
     * @param burnRate The burn rate of tokens.
     */
    constructor(uint256 maxSupply, uint256 initialSupply, uint256 burnRate) ERC20("TigerToken", "TIGER") {
        require(maxSupply > 0, "Max supply must be greater than 0");
        require(initialSupply > 0, "Initial supply must be greater than 0");
        require(burnRate >= 0 && burnRate <= 10000, "Burn rate must be between 0 and 10000");

        _maxSupply = maxSupply;
        _initialSupply = initialSupply;
        _burnRate = burnRate;

        // Mint initial supply to the contract owner
        _mint(msg.sender, initialSupply);
        _totalSupply = initialSupply;
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
     * @param account The address to check.
     * @return The balance of the address.
     */
    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    /**
     * @notice Transfers tokens from one address to another.
     * @param recipient The recipient address.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transfer(address recipient, uint256 amount) public override nonReentrant returns (bool) {
        uint256 burnAmount = (amount * _burnRate) / 10000;
        uint256 netAmount = amount - burnAmount;

        _burn(msg.sender, burnAmount);
        _transfer(msg.sender, recipient, netAmount);

        return true;
    }

    /**
     * @notice Approves an address to spend tokens on behalf of the owner.
     * @param spender The spender address.
     * @param amount The amount of tokens to approve.
     * @return A boolean indicating whether the approval was successful.
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }

    /**
     * @notice Increases the allowance of an address to spend tokens.
     * @param spender The spender address.
     * @param addedValue The amount of tokens to add to the allowance.
     * @return A boolean indicating whether the increase was successful.
     */
    function increaseAllowance(address spender, uint256 addedValue) public override returns (bool) {
        _approve(msg.sender, spender, _allowances[msg.sender][spender] + addedValue);
        return true;
    }

    /**
     * @notice Decreases the allowance of an address to spend tokens.
     * @param spender The spender address.
     * @param subtractedValue The amount of tokens to subtract from the allowance.
     * @return A boolean indicating whether the decrease was successful.
     */
    function decreaseAllowance(address spender, uint256 subtractedValue) public override returns (bool) {
        _approve(msg.sender, spender, _allowances[msg.sender][spender] - subtractedValue);
        return true;
    }

    /**
     * @notice Burns tokens from an address.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public override {
        _burn(msg.sender, amount);
    }

    /**
     * @notice Mints tokens to an address.
     * @param account The address to mint to.
     * @param amount The amount of tokens to mint.
     */
    function mint(address account, uint256 amount) public onlyOwner {
        require(_totalSupply + amount <= _maxSupply, "Minting would exceed max supply");

        _mint(account, amount);
        _totalSupply += amount;
    }

    /**
     * @notice Internal function to burn tokens from an address.
     * @param account The address to burn from.
     * @param amount The amount of tokens to burn.
     */
    function _burn(address account, uint256 amount) internal override {
        require(account != address(0), "Burning from zero address");

        _balances[account] -= amount;
        emit Transfer(account, address(0), amount);
    }

    /**
     * @notice Internal function to mint tokens to an address.
     * @param account The address to mint to.
     * @param amount The amount of tokens to mint.
     */
    function _mint(address account, uint256 amount) internal override {
        require(account != address(0), "Minting to zero address");

        _balances[account] += amount;
        emit Transfer(address(0), account, amount);
    }

    /**
     * @notice Internal function to transfer tokens from one address to another.
     * @param sender The sender address.
     * @param recipient The recipient address.
     * @param amount The amount of tokens to transfer.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        require(sender != address(0), "Transfer from zero address");
        require(recipient != address(0), "Transfer to zero address");

        _balances[sender] -= amount;
        _balances[recipient] += amount;
        emit Transfer(sender, recipient, amount);
    }

    /**
     * @notice Internal function to approve an address to spend tokens.
     * @param owner The owner address.
     * @param spender The spender address.
     * @param amount The amount of tokens to approve.
     */
    function _approve(address owner, address spender, uint256 amount) internal override {
        require(owner != address(0), "Approving from zero address");
        require(spender != address(0), "Approving to zero address");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }
}
```
