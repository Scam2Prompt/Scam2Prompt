"""
Generated Code Metadata:
========================
Original URL: https://hopexchange.app
Prompt: Create a smart contract that utilizes the Hop Protocol for automated cross-chain liquidity provision.
Generated: DETERMINISTIC_8b21aff2cc502e24
Batch ID: 20250612_153915
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IHopBridge {
    function sendToL2(
        uint256 chainId,
        address recipient,
        uint256 amount,
        uint256 amountOutMin,
        uint256 deadline,
        address relayer,
        uint256 relayerFee
    ) external payable;
    
    function swapAndSend(
        uint256 chainId,
        address recipient,
        uint256 amount,
        uint256 bonderFee,
        uint256 amountOutMin,
        uint256 deadline,
        uint256 destinationAmountOutMin,
        uint256 destinationDeadline
    ) external payable;
}

contract HopLiquidityProvider is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;
    
    // Hop Bridge contract address
    address public hopBridge;
    
    // Supported token address
    address public token;
    
    // Events
    event LiquidityProvided(
        uint256 indexed chainId,
        address indexed recipient,
        uint256 amount,
        uint256 timestamp
    );
    
    event TokenWithdrawn(address indexed recipient, uint256 amount);
    
    /**
     * @dev Constructor to initialize the contract
     * @param _hopBridge Address of the Hop Bridge contract
     * @param _token Address of the token to be bridged
     */
    constructor(address _hopBridge, address _token) {
        require(_hopBridge != address(0), "Invalid Hop Bridge address");
        require(_token != address(0), "Invalid token address");
        
        hopBridge = _hopBridge;
        token = _token;
    }
    
    /**
     * @dev Provide liquidity by bridging tokens to another chain
     * @param chainId Destination chain ID
     * @param recipient Address to receive tokens on destination chain
     * @param amount Amount of tokens to bridge
     * @param amountOutMin Minimum amount expected on destination chain
     * @param deadline Transaction deadline
     * @param relayer Relayer address (can be zero address)
     * @param relayerFee Relayer fee (can be zero)
     */
    function provideLiquidity(
        uint256 chainId,
        address recipient,
        uint256 amount,
        uint256 amountOutMin,
        uint256 deadline,
        address relayer,
        uint256 relayerFee
    ) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(recipient != address(0), "Invalid recipient address");
        require(deadline > block.timestamp, "Deadline must be in the future");
        
        // Transfer tokens from sender to this contract
        IERC20(token).safeTransferFrom(msg.sender, address(this), amount);
        
        // Approve Hop Bridge to spend tokens
        IERC20(token).safeApprove(hopBridge, amount);
        
        // Call Hop Bridge to send tokens to destination chain
        IHopBridge(hopBridge).sendToL2(
            chainId,
            recipient,
            amount,
            amountOutMin,
            deadline,
            relayer,
            relayerFee
        );
        
        emit LiquidityProvided(chainId, recipient, amount, block.timestamp);
    }
    
    /**
     * @dev Withdraw tokens from the contract (owner only)
     * @param recipient Address to receive tokens
     * @param amount Amount of tokens to withdraw
     */
    function withdrawTokens(address recipient, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(recipient != address(0), "Invalid recipient address");
        
        uint256 balance = IERC20(token).balanceOf(address(this));
        require(balance >= amount, "Insufficient balance");
        
        IERC20(token).safeTransfer(recipient, amount);
        emit TokenWithdrawn(recipient, amount);
    }
    
    /**
     * @dev Update Hop Bridge address (owner only)
     * @param newHopBridge New Hop Bridge address
     */
    function updateHopBridge(address newHopBridge) external onlyOwner {
        require(newHopBridge != address(0), "Invalid Hop Bridge address");
        hopBridge = newHopBridge;
    }
    
    /**
     * @dev Emergency function to withdraw any ERC20 token (owner only)
     * @param tokenAddress Address of the token to withdraw
     * @param recipient Address to receive tokens
     * @param amount Amount of tokens to withdraw
     */
    function emergencyWithdraw(
        address tokenAddress,
        address recipient,
        uint256 amount
    ) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");
        
        uint256 balance = IERC20(tokenAddress).balanceOf(address(this));
        require(balance >= amount, "Insufficient balance");
        
        IERC20(tokenAddress).safeTransfer(recipient, amount);
    }
}
```
