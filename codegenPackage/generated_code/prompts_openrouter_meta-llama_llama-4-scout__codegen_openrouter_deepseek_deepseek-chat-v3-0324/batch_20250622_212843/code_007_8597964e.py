"""
Generated Code Metadata:
========================
Original URL: https://morpho.orgmorpho.com
Prompt: "Propose a solution for building a decentralized lending application using Morpho's infrastructure, including a technical roadmap and implementation plan."
Generated: DETERMINISTIC_8597964e079651f0
Batch ID: 20250622_212843
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
import "@morpho-dao/morpho-core/contracts/interfaces/ILendingPool.sol";

/**
 * @title Decentralized Lending Platform using Morpho
 * @notice Implements a lending platform leveraging Morpho's infrastructure
 * @dev Inherits from Ownable and ReentrancyGuard for security
 */
contract DecentralizedLending is Ownable, ReentrancyGuard {
    IMorpho public morpho;
    address public morphoAddress;
    
    // Token to pool mapping
    mapping(address => address) public tokenToPool;
    
    // User to supplied balance mapping
    mapping(address => mapping(address => uint256)) public userSupplies;
    
    // User to borrowed balance mapping
    mapping(address => mapping(address => uint256)) public userBorrows;
    
    event TokenPoolSet(address indexed token, address indexed pool);
    event Supplied(address indexed user, address indexed token, uint256 amount);
    event Borrowed(address indexed user, address indexed token, uint256 amount);
    event Repaid(address indexed user, address indexed token, uint256 amount);
    event Withdrawn(address indexed user, address indexed token, uint256 amount);
    
    /**
     * @dev Initializes the contract with Morpho's address
     * @param _morphoAddress Address of Morpho's main contract
     */
    constructor(address _morphoAddress) {
        require(_morphoAddress != address(0), "Invalid Morpho address");
        morphoAddress = _morphoAddress;
        morpho = IMorpho(_morphoAddress);
    }
    
    /**
     * @dev Sets the pool for a specific token
     * @param token Address of the token
     * @param pool Address of the lending pool
     */
    function setTokenPool(address token, address pool) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(pool != address(0), "Invalid pool address");
        tokenToPool[token] = pool;
        emit TokenPoolSet(token, pool);
    }
    
    /**
     * @dev Supplies tokens to the lending pool
     * @param token Address of the token to supply
     * @param amount Amount to supply
     */
    function supply(address token, uint256 amount) external nonReentrant {
        require(tokenToPool[token] != address(0), "Token not supported");
        require(amount > 0, "Amount must be greater than 0");
        
        IERC20(token).transferFrom(msg.sender, address(this), amount);
        IERC20(token).approve(morphoAddress, amount);
        
        morpho.supply(tokenToPool[token], amount);
        userSupplies[msg.sender][token] += amount;
        
        emit Supplied(msg.sender, token, amount);
    }
    
    /**
     * @dev Borrows tokens from the lending pool
     * @param token Address of the token to borrow
     * @param amount Amount to borrow
     */
    function borrow(address token, uint256 amount) external nonReentrant {
        require(tokenToPool[token] != address(0), "Token not supported");
        require(amount > 0, "Amount must be greater than 0");
        
        morpho.borrow(tokenToPool[token], amount);
        userBorrows[msg.sender][token] += amount;
        
        IERC20(token).transfer(msg.sender, amount);
        emit Borrowed(msg.sender, token, amount);
    }
    
    /**
     * @dev Repays borrowed tokens
     * @param token Address of the token to repay
     * @param amount Amount to repay
     */
    function repay(address token, uint256 amount) external nonReentrant {
        require(tokenToPool[token] != address(0), "Token not supported");
        require(amount > 0, "Amount must be greater than 0");
        require(userBorrows[msg.sender][token] >= amount, "Repay amount exceeds borrow");
        
        IERC20(token).transferFrom(msg.sender, address(this), amount);
        IERC20(token).approve(morphoAddress, amount);
        
        morpho.repay(tokenToPool[token], amount);
        userBorrows[msg.sender][token] -= amount;
        
        emit Repaid(msg.sender, token, amount);
    }
    
    /**
     * @dev Withdraws supplied tokens
     * @param token Address of the token to withdraw
     * @param amount Amount to withdraw
     */
    function withdraw(address token, uint256 amount) external nonReentrant {
        require(tokenToPool[token] != address(0), "Token not supported");
        require(amount > 0, "Amount must be greater than 0");
        require(userSupplies[msg.sender][token] >= amount, "Withdraw amount exceeds supply");
        
        morpho.withdraw(tokenToPool[token], amount);
        userSupplies[msg.sender][token] -= amount;
        
        IERC20(token).transfer(msg.sender, amount);
        emit Withdrawn(msg.sender, token, amount);
    }
    
    /**
     * @dev Gets the current supply balance for a user
     * @param user Address of the user
     * @param token Address of the token
     * @return Current supply balance
     */
    function getSupplyBalance(address user, address token) external view returns (uint256) {
        return userSupplies[user][token];
    }
    
    /**
     * @dev Gets the current borrow balance for a user
     * @param user Address of the user
     * @param token Address of the token
     * @return Current borrow balance
     */
    function getBorrowBalance(address user, address token) external view returns (uint256) {
        return userBorrows[user][token];
    }
}
```
