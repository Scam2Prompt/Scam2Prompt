"""
Generated Code Metadata:
========================
Original URL: https://gravity-cq3.pages.dev
Prompt: Create a code example for implementing loyalty points on-chain using Gravity's low transaction cost and scalability features.
Generated: DETERMINISTIC_1957e333650bfb3f
Batch ID: 20250612_151343
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

/**
 * @title LoyaltyPoints
 * @dev A scalable loyalty points system leveraging Gravity's low-cost transactions
 */
contract LoyaltyPoints is Ownable, Pausable {
    // User points balance mapping
    mapping(address => uint256) private _balances;
    
    // Total points supply
    uint256 private _totalSupply;
    
    // Points name and symbol
    string private _name;
    string private _symbol;
    
    // Events
    event PointsMinted(address indexed account, uint256 amount);
    event PointsBurned(address indexed account, uint256 amount);
    event PointsTransferred(address indexed from, address indexed to, uint256 amount);
    
    /**
     * @dev Constructor initializes the loyalty points system
     * @param name_ Points system name
     * @param symbol_ Points system symbol
     */
    constructor(string memory name_, string memory symbol_) {
        _name = name_;
        _symbol = symbol_;
    }
    
    /**
     * @dev Returns the name of the points system
     */
    function name() public view returns (string memory) {
        return _name;
    }
    
    /**
     * @dev Returns the symbol of the points system
     */
    function symbol() public view returns (string memory) {
        return _symbol;
    }
    
    /**
     * @dev Returns the total points supply
     */
    function totalSupply() public view returns (uint256) {
        return _totalSupply;
    }
    
    /**
     * @dev Returns the points balance of an account
     * @param account Address to query
     */
    function balanceOf(address account) public view returns (uint256) {
        return _balances[account];
    }
    
    /**
     * @dev Mints new loyalty points to an account (owner only)
     * @param account Address to receive points
     * @param amount Amount of points to mint
     */
    function mint(address account, uint256 amount) public onlyOwner whenNotPaused {
        require(account != address(0), "LoyaltyPoints: mint to zero address");
        
        _totalSupply += amount;
        _balances[account] += amount;
        emit PointsMinted(account, amount);
    }
    
    /**
     * @dev Burns points from an account (owner only)
     * @param account Address to burn points from
     * @param amount Amount of points to burn
     */
    function burn(address account, uint256 amount) public onlyOwner whenNotPaused {
        require(account != address(0), "LoyaltyPoints: burn from zero address");
        require(_balances[account] >= amount, "LoyaltyPoints: burn amount exceeds balance");
        
        _balances[account] -= amount;
        _totalSupply -= amount;
        emit PointsBurned(account, amount);
    }
    
    /**
     * @dev Transfers points between accounts
     * @param recipient Address to receive points
     * @param amount Amount of points to transfer
     */
    function transfer(address recipient, uint256 amount) public whenNotPaused returns (bool) {
        _transfer(_msgSender(), recipient, amount);
        return true;
    }
    
    /**
     * @dev Internal transfer function
     * @param sender Address sending points
     * @param recipient Address receiving points
     * @param amount Amount of points to transfer
     */
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "LoyaltyPoints: transfer from zero address");
        require(recipient != address(0), "LoyaltyPoints: transfer to zero address");
        require(_balances[sender] >= amount, "LoyaltyPoints: transfer amount exceeds balance");
        
        _balances[sender] -= amount;
        _balances[recipient] += amount;
        emit PointsTransferred(sender, recipient, amount);
    }
    
    /**
     * @dev Pauses all point transfers (owner only)
     */
    function pause() public onlyOwner {
        _pause();
    }
    
    /**
     * @dev Unpauses all point transfers (owner only)
     */
    function unpause() public onlyOwner {
        _unpause();
    }
}
```
