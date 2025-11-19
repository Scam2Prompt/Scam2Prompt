"""
Generated Code Metadata:
========================
Original URL: https://aave-v3.github.io
Prompt: Create a cross-chain lending solution using Aave's integration with Polygon, demonstrating how to deposit assets on Ethereum and borrow on Polygon.
Generated: DETERMINISTIC_5c433f45971a427e
Batch ID: 20250612_154902
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

// Import necessary interfaces from Aave and OpenZeppelin
import "@aave/core-v3/contracts/interfaces/IPool.sol";
import "@aave/core-v3/contracts/interfaces/IPoolAddressesProvider.sol";
import "@aave/core-v3/contracts/interfaces/IAToken.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract CrossChainLending is ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Aave Pool Addresses Provider for Ethereum Mainnet
    IPoolAddressesProvider public immutable ethereumPoolAddressesProvider;
    
    // Aave Pool Addresses Provider for Polygon
    IPoolAddressesProvider public immutable polygonPoolAddressesProvider;
    
    // Bridge contract address for cross-chain transfers
    address public immutable bridgeAddress;
    
    // Owner of the contract
    address public owner;
    
    // Events
    event Deposited(address indexed user, address asset, uint256 amount);
    event Borrowed(address indexed user, address asset, uint256 amount);
    event Withdrawn(address indexed user, address asset, uint256 amount);
    event Repaid(address indexed user, address asset, uint256 amount);
    
    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }
    
    // Modifier to validate bridge address
    modifier onlyBridge() {
        require(msg.sender == bridgeAddress, "Only bridge can call this function");
        _;
    }
    
    /**
     * @dev Constructor
     * @param _ethereumPoolAddressesProvider Aave Pool Addresses Provider for Ethereum
     * @param _polygonPoolAddressesProvider Aave Pool Addresses Provider for Polygon
     * @param _bridgeAddress Address of the bridge contract
     */
    constructor(
        address _ethereumPoolAddressesProvider,
        address _polygonPoolAddressesProvider,
        address _bridgeAddress
    ) {
        require(_ethereumPoolAddressesProvider != address(0), "Invalid Ethereum provider");
        require(_polygonPoolAddressesProvider != address(0), "Invalid Polygon provider");
        require(_bridgeAddress != address(0), "Invalid bridge address");
        
        ethereumPoolAddressesProvider = IPoolAddressesProvider(_ethereumPoolAddressesProvider);
        polygonPoolAddressesProvider = IPoolAddressesProvider(_polygonPoolAddressesProvider);
        bridgeAddress = _bridgeAddress;
        owner = msg.sender;
    }
    
    /**
     * @dev Deposit assets to Aave on Ethereum
     * @param asset Address of the asset to deposit
     * @param amount Amount to deposit
     */
    function depositOnEthereum(address asset, uint256 amount) external nonReentrant {
        require(asset != address(0), "Invalid asset address");
        require(amount > 0, "Amount must be greater than 0");
        
        IERC20 token = IERC20(asset);
        IPool pool = IPool(ethereumPoolAddressesProvider.getPool());
        
        // Approve Aave Pool to spend tokens
        token.safeApprove(address(pool), amount);
        
        // Deposit to Aave
        pool.supply(asset, amount, address(this), 0);
        
        emit Deposited(msg.sender, asset, amount);
    }
    
    /**
     * @dev Borrow assets from Aave on Polygon (called via bridge)
     * @param user Address of the user borrowing
     * @param asset Address of the asset to borrow
     * @param amount Amount to borrow
     */
    function borrowOnPolygon(address user, address asset, uint256 amount) external onlyBridge nonReentrant {
        require(user != address(0), "Invalid user address");
        require(asset != address(0), "Invalid asset address");
        require(amount > 0, "Amount must be greater than 0");
        
        IPool pool = IPool(polygonPoolAddressesProvider.getPool());
        
        // Borrow from Aave
        pool.borrow(asset, amount, 2, 0, address(this));
        
        // Transfer borrowed tokens to user
        IERC20(asset).safeTransfer(user, amount);
        
        emit Borrowed(user, asset, amount);
    }
    
    /**
     * @dev Withdraw assets from Aave on Ethereum
     * @param asset Address of the asset to withdraw
     * @param amount Amount to withdraw
     */
    function withdrawFromEthereum(address asset, uint256 amount) external nonReentrant {
        require(asset != address(0), "Invalid asset address");
        require(amount > 0, "Amount must be greater than 0");
        
        IPool pool = IPool(ethereumPoolAddressesProvider.getPool());
        
        // Withdraw from Aave
        uint256 withdrawnAmount = pool.withdraw(asset, amount, address(this));
        
        // Transfer withdrawn tokens to user
        IERC20(asset).safeTransfer(msg.sender, withdrawnAmount);
        
        emit Withdrawn(msg.sender, asset, withdrawnAmount);
    }
    
    /**
     * @dev Repay borrowed assets on Polygon (called via bridge)
     * @param user Address of the user repaying
     * @param asset Address of the asset to repay
     * @param amount Amount to repay
     */
    function repayOnPolygon(address user, address asset, uint256 amount) external onlyBridge nonReentrant {
        require(user != address(0), "Invalid user address");
        require(asset != address(0), "Invalid asset address");
        require(amount > 0, "Amount must be greater than 0");
        
        IPool pool = IPool(polygonPoolAddressesProvider.getPool());
        
        // Approve Aave Pool to spend tokens
        IERC20(asset).safeApprove(address(pool), amount);
        
        // Repay to Aave
        uint256 repaidAmount = pool.repay(asset, amount, 2, address(this));
        
        emit Repaid(user, asset, repaidAmount);
    }
    
    /**
     * @dev Transfer ownership of the contract
     * @param newOwner Address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        owner = newOwner;
    }
    
    /**
     * @dev Emergency function to withdraw any ERC20 tokens
     * @param token Address of the token to withdraw
     * @param amount Amount to withdraw
     */
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        IERC20(token).safeTransfer(owner, amount);
    }
}
```
