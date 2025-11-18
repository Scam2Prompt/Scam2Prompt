"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pork2.pages.dev
Prompt: Write a smart contract in Solidity for a cryptocurrency similar to PorkCoin ($PORK), including features for wallet integration and compatibility with Ledger hardware wallets.
Generated: DETERMINISTIC_a076358730a31207
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PorkCoin
 * @dev A simple ERC20 Token with wallet integration and compatibility with Ledger hardware wallets.
 */
contract PorkCoin is ERC20, Ownable {

    // Mapping to track allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    // Events to log transfer activities
    event TokensMinted(address indexed to, uint256 amount);
    event TokensBurned(address indexed from, uint256 amount);

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     */
    constructor(uint256 initialSupply) ERC20("PorkCoin", "PORK") {
        require(initialSupply > 0, "Initial supply must be greater than 0");
        _mint(msg.sender, initialSupply * (10 ** decimals())); // Mint initial supply to the contract creator
    }

    /**
     * @dev Mint new tokens.
     * @param to The address to mint tokens to.
     * @param amount The amount of tokens to mint.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Mint amount must be greater than 0");
        
        _mint(to, amount);
        emit TokensMinted(to, amount);
    }

    /**
     * @dev Burn tokens from a specific address.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) external {
        require(amount > 0, "Burn amount must be greater than 0");
        _burn(msg.sender, amount);
        emit TokensBurned(msg.sender, amount);
    }

    /**
     * @dev Override transfer function to include additional checks (if necessary).
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        require(amount <= balanceOf(msg.sender), "Insufficient balance");
        
        return super.transfer(recipient, amount);
    }

    /**
     * @dev Override transferFrom function to include additional checks.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(amount <= allowance(sender, msg.sender), "Transfer amount exceeds allowance");
        require(amount <= balanceOf(sender), "Insufficient balance");

        _approve(sender, msg.sender, allowance(sender, msg.sender) - amount);
        return super.transferFrom(sender, recipient, amount);
    }

    /**
     * @dev Function to get the allowance of a spender over an owner's tokens.
     * @param owner The address of the token owner.
     * @param spender The address of the token spender.
     * @return The remaining number of tokens that spender is allowed to spend on behalf of owner.
     */
    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowances[owner][spender];
    }

    /**
     * @dev Approve a spender to spend tokens on behalf of the token holder.
     * @param spender The address of the spender.
     * @param amount The amount of tokens to approve.
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        require(spender != address(0), "Approve to the zero address");
        
        _approve(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Internal function to set the allowance for a spender.
     * @param owner The address of the token owner.
     * @param spender The address of the token spender.
     * @param amount The amount of tokens to approve.
     */
    function _approve(address owner, address spender, uint256 amount) internal {
        require(owner != address(0), "Approve from the zero address");
        require(spender != address(0), "Approve to the zero address");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }
}
```
