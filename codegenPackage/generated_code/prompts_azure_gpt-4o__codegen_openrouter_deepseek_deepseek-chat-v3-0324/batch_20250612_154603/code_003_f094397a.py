"""
Generated Code Metadata:
========================
Original URL: https://swiftdecentralizedapp.com
Prompt: Create a smart contract for a decentralized application with multichain support, ensuring compatibility with self-custodial wallets as described on Swift Decentralized Dapps.
Generated: DETERMINISTIC_f094397abeacebc4
Batch ID: 20250612_154603
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

/**
 * @title MultiChainDapp
 * @dev A decentralized application contract with multichain support
 * and compatibility with self-custodial wallets
 */
contract MultiChainDapp is Ownable, ReentrancyGuard {
    // Chain ID to contract address mapping for cross-chain compatibility
    mapping(uint256 => address) public chainIdToContract;

    // Supported tokens for cross-chain operations
    mapping(address => bool) public supportedTokens;

    // Events
    event ChainSupported(uint256 chainId, address contractAddress);
    event TokenSupported(address tokenAddress);
    event CrossChainTransfer(
        address indexed sender,
        uint256 fromChainId,
        uint256 toChainId,
        address token,
        uint256 amount
    );
    event Deposit(address indexed user, address token, uint256 amount);
    event Withdrawal(address indexed user, address token, uint256 amount);

    /**
     * @dev Modifier to check if token is supported
     */
    modifier onlySupportedToken(address token) {
        require(supportedTokens[token], "Token not supported");
        _;
    }

    /**
     * @dev Modifier to check if chain is supported
     */
    modifier onlySupportedChain(uint256 chainId) {
        require(chainIdToContract[chainId] != address(0), "Chain not supported");
        _;
    }

    /**
     * @dev Add support for a new chain
     * @param chainId The chain ID to support
     * @param contractAddress The address of the contract on the target chain
     */
    function addChainSupport(uint256 chainId, address contractAddress) external onlyOwner {
        require(chainId != 0, "Invalid chain ID");
        require(contractAddress != address(0), "Invalid contract address");
        
        chainIdToContract[chainId] = contractAddress;
        emit ChainSupported(chainId, contractAddress);
    }

    /**
     * @dev Add support for a new token
     * @param tokenAddress The address of the token to support
     */
    function addTokenSupport(address tokenAddress) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        
        supportedTokens[tokenAddress] = true;
        emit TokenSupported(tokenAddress);
    }

    /**
     * @dev Deposit tokens into the contract
     * @param tokenAddress The address of the token to deposit
     * @param amount The amount of tokens to deposit
     */
    function deposit(address tokenAddress, uint256 amount) 
        external 
        nonReentrant 
        onlySupportedToken(tokenAddress) 
    {
        require(amount > 0, "Amount must be greater than 0");
        
        IERC20 token = IERC20(tokenAddress);
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        emit Deposit(msg.sender, tokenAddress, amount);
    }

    /**
     * @dev Withdraw tokens from the contract
     * @param tokenAddress The address of the token to withdraw
     * @param amount The amount of tokens to withdraw
     */
    function withdraw(address tokenAddress, uint256 amount) 
        external 
        nonReentrant 
        onlySupportedToken(tokenAddress) 
    {
        require(amount > 0, "Amount must be greater than 0");
        
        IERC20 token = IERC20(tokenAddress);
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        require(token.transfer(msg.sender, amount), "Transfer failed");
        
        emit Withdrawal(msg.sender, tokenAddress, amount);
    }

    /**
     * @dev Initiate a cross-chain transfer
     * @param toChainId The destination chain ID
     * @param tokenAddress The address of the token to transfer
     * @param amount The amount of tokens to transfer
     */
    function initiateCrossChainTransfer(
        uint256 toChainId,
        address tokenAddress,
        uint256 amount
    ) 
        external 
        nonReentrant 
        onlySupportedToken(tokenAddress)
        onlySupportedChain(toChainId)
    {
        require(amount > 0, "Amount must be greater than 0");
        
        IERC20 token = IERC20(tokenAddress);
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        // In a real implementation, this would trigger a cross-chain message
        // via a bridge or messaging protocol like LayerZero, Wormhole, etc.
        emit CrossChainTransfer(
            msg.sender,
            block.chainid,
            toChainId,
            tokenAddress,
            amount
        );
    }

    /**
     * @dev Emergency withdraw tokens (owner only)
     * @param tokenAddress The address of the token to withdraw
     */
    function emergencyWithdraw(address tokenAddress) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(token.transfer(owner(), balance), "Transfer failed");
    }
}
```
