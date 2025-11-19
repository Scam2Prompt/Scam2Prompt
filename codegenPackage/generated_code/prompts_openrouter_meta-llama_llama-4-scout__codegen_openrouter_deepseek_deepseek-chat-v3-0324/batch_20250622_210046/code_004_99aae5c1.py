"""
Generated Code Metadata:
========================
Original URL: https://wwwmorpho.org
Prompt: "Design a simple smart contract that integrates with Morpho's protocol to enable borrowing and lending of cryptocurrencies, using a vault-based architecture."
Generated: DETERMINISTIC_99aae5c12b868878
Batch ID: 20250622_210046
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@morpho-dao/morpho-core/contracts/interfaces/IMorpho.sol";
import "@morpho-dao/morpho-core/contracts/interfaces/ILens.sol";

/**
 * @title MorphoVault
 * @dev A vault-based smart contract for borrowing and lending cryptocurrencies via Morpho protocol
 */
contract MorphoVault is Ownable, ReentrancyGuard {
    IMorpho public immutable morpho;
    ILens public immutable lens;
    
    // Supported markets mapping (token => isSupported)
    mapping(address => bool) public supportedMarkets;
    
    // User balances mapping (user => token => amount)
    mapping(address => mapping(address => uint256)) public userBalances;
    
    // Events
    event Deposit(address indexed user, address indexed token, uint256 amount);
    event Withdraw(address indexed user, address indexed token, uint256 amount);
    event Borrow(address indexed user, address indexed token, uint256 amount);
    event Repay(address indexed user, address indexed token, uint256 amount);
    event MarketAdded(address indexed token);
    event MarketRemoved(address indexed token);
    
    /**
     * @dev Constructor
     * @param _morpho Address of Morpho protocol contract
     * @param _lens Address of Morpho Lens contract
     */
    constructor(address _morpho, address _lens) {
        require(_morpho != address(0), "Invalid Morpho address");
        require(_lens != address(0), "Invalid Lens address");
        morpho = IMorpho(_morpho);
        lens = ILens(_lens);
    }
    
    /**
     * @dev Add a supported market
     * @param token Address of the token to support
     */
    function addMarket(address token) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(!supportedMarkets[token], "Market already supported");
        supportedMarkets[token] = true;
        emit MarketAdded(token);
    }
    
    /**
     * @dev Remove a supported market
     * @param token Address of the token to remove
     */
    function removeMarket(address token) external onlyOwner {
        require(supportedMarkets[token], "Market not supported");
        supportedMarkets[token] = false;
        emit MarketRemoved(token);
    }
    
    /**
     * @dev Deposit tokens into the vault
     * @param token Address of the token to deposit
     * @param amount Amount to deposit
     */
    function deposit(address token, uint256 amount) external nonReentrant {
        require(supportedMarkets[token], "Token not supported");
        require(amount > 0, "Amount must be greater than 0");
        
        IERC20(token).transferFrom(msg.sender, address(this), amount);
        userBalances[msg.sender][token] += amount;
        
        // Approve Morpho to spend tokens
        IERC20(token).approve(address(morpho), amount);
        
        // Supply to Morpho
        morpho.supply(token, address(this), amount);
        
        emit Deposit(msg.sender, token, amount);
    }
    
    /**
     * @dev Withdraw tokens from the vault
     * @param token Address of the token to withdraw
     * @param amount Amount to withdraw
     */
    function withdraw(address token, uint256 amount) external nonReentrant {
        require(supportedMarkets[token], "Token not supported");
        require(amount > 0, "Amount must be greater than 0");
        require(userBalances[msg.sender][token] >= amount, "Insufficient balance");
        
        // Withdraw from Morpho
        morpho.withdraw(token, amount);
        
        userBalances[msg.sender][token] -= amount;
        IERC20(token).transfer(msg.sender, amount);
        
        emit Withdraw(msg.sender, token, amount);
    }
    
    /**
     * @dev Borrow tokens from the vault
     * @param token Address of the token to borrow
     * @param amount Amount to borrow
     */
    function borrow(address token, uint256 amount) external nonReentrant {
        require(supportedMarkets[token], "Token not supported");
        require(amount > 0, "Amount must be greater than 0");
        
        // Borrow from Morpho
        morpho.borrow(token, amount);
        
        IERC20(token).transfer(msg.sender, amount);
        
        emit Borrow(msg.sender, token, amount);
    }
    
    /**
     * @dev Repay borrowed tokens
     * @param token Address of the token to repay
     * @param amount Amount to repay
     */
    function repay(address token, uint256 amount) external nonReentrant {
        require(supportedMarkets[token], "Token not supported");
        require(amount > 0, "Amount must be greater than 0");
        
        IERC20(token).transferFrom(msg.sender, address(this), amount);
        
        // Approve Morpho to spend tokens
        IERC20(token).approve(address(morpho), amount);
        
        // Repay to Morpho
        morpho.repay(token, amount);
        
        emit Repay(msg.sender, token, amount);
    }
    
    /**
     * @dev Get user's balance for a specific token
     * @param user Address of the user
     * @param token Address of the token
     * @return User's balance
     */
    function getUserBalance(address user, address token) external view returns (uint256) {
        return userBalances[user][token];
    }
    
    /**
     * @dev Get user's borrow balance for a specific token
     * @param user Address of the user
     * @param token Address of the token
     * @return User's borrow balance
     */
    function getUserBorrowBalance(address user, address token) external view returns (uint256) {
        (uint256 balance, ) = lens.getCurrentBorrowBalanceInOf(token, user);
        return balance;
    }
    
    /**
     * @dev Get user's supply balance for a specific token
     * @param user Address of the user
     * @param token Address of the token
     * @return User's supply balance
     */
    function getUserSupplyBalance(address user, address token) external view returns (uint256) {
        (uint256 balance, ) = lens.getCurrentSupplyBalanceInOf(token, user);
        return balance;
    }
}
```
