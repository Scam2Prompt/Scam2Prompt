"""
Generated Code Metadata:
========================
Original URL: https://moonwell.site
Prompt: Develop a Solidity contract to test Moonwell's interoperability features, focusing on cross-chain asset transfers between Moonbeam and Moonriver.
Generated: DETERMINISTIC_548b3b136f4ff885
Batch ID: 20250612_145616
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

interface IXC20 {
    function deposit(uint256 amount) external;
    function withdraw(uint256 amount) external;
}

contract MoonwellInteropTester is Ownable, ReentrancyGuard {
    // Address of the XC20 precompile on Moonbeam/Moonriver
    address public xc20Precompile;
    
    // Mapping to track supported tokens (chainId => tokenAddress)
    mapping(uint256 => address) public supportedTokens;
    
    // Events
    event TokenDeposited(address indexed user, uint256 chainId, address token, uint256 amount);
    event TokenWithdrawn(address indexed user, uint256 chainId, address token, uint256 amount);
    event TokenAdded(uint256 chainId, address token);
    event TokenRemoved(uint256 chainId, address token);
    
    constructor(address _xc20Precompile) {
        require(_xc20Precompile != address(0), "Invalid XC20 precompile address");
        xc20Precompile = _xc20Precompile;
    }
    
    /**
     * @dev Add a supported token for cross-chain transfers
     * @param chainId The chain ID (Moonbeam = 1284, Moonriver = 1285)
     * @param tokenAddress The token address on the target chain
     */
    function addSupportedToken(uint256 chainId, address tokenAddress) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        require(chainId == 1284 || chainId == 1285, "Unsupported chain");
        
        supportedTokens[chainId] = tokenAddress;
        emit TokenAdded(chainId, tokenAddress);
    }
    
    /**
     * @dev Remove a supported token
     * @param chainId The chain ID to remove support for
     */
    function removeSupportedToken(uint256 chainId) external onlyOwner {
        require(supportedTokens[chainId] != address(0), "Token not supported");
        
        delete supportedTokens[chainId];
        emit TokenRemoved(chainId, address(0));
    }
    
    /**
     * @dev Deposit tokens to be transferred to another chain
     * @param chainId The target chain ID
     * @param token The token address on the source chain
     * @param amount The amount to transfer
     */
    function depositToken(uint256 chainId, address token, uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(supportedTokens[chainId] != address(0), "Token not supported for this chain");
        
        IERC20(token).transferFrom(msg.sender, address(this), amount);
        
        // Convert to XC20 format
        IXC20(xc20Precompile).deposit(amount);
        
        emit TokenDeposited(msg.sender, chainId, token, amount);
    }
    
    /**
     * @dev Withdraw tokens from another chain
     * @param chainId The source chain ID
     * @param token The XC20 token address
     * @param amount The amount to withdraw
     */
    function withdrawToken(uint256 chainId, address token, uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(supportedTokens[chainId] != address(0), "Token not supported for this chain");
        
        // Convert from XC20 format
        IXC20(xc20Precompile).withdraw(amount);
        
        IERC20(token).transfer(msg.sender, amount);
        
        emit TokenWithdrawn(msg.sender, chainId, token, amount);
    }
    
    /**
     * @dev Emergency withdraw any ERC20 tokens
     * @param token The token address
     * @param amount The amount to withdraw
     */
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(owner(), amount);
    }
}
```
