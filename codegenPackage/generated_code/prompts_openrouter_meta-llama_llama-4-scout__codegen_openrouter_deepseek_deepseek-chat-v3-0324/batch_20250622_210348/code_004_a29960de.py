"""
Generated Code Metadata:
========================
Original URL: https://pulsechain-app.pages.dev
Prompt: Explain the process of bridging assets from Ethereum to PulseChain, including the role of the PulseBridge contract.
Generated: DETERMINISTIC_a29960decfcb706a
Batch ID: 20250622_210348
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
 * @title PulseBridge
 * @dev Contract for bridging ERC20 tokens from Ethereum to PulseChain
 */
contract PulseBridge is Ownable, ReentrancyGuard {
    // Mapping to track locked tokens
    mapping(address => mapping(address => uint256)) public lockedTokens;
    
    // Mapping to track supported tokens
    mapping(address => bool) public supportedTokens;
    
    // Bridge fee in basis points (e.g., 50 = 0.5%)
    uint256 public bridgeFeeBasisPoints;
    
    // Minimum bridge amount to prevent dust attacks
    uint256 public minBridgeAmount;
    
    // Events
    event TokenLocked(
        address indexed sender,
        address indexed token,
        uint256 amount,
        uint256 fee,
        uint256 timestamp
    );
    
    event TokenUnlocked(
        address indexed recipient,
        address indexed token,
        uint256 amount,
        uint256 timestamp
    );
    
    event TokenSupportUpdated(
        address indexed token,
        bool supported,
        uint256 timestamp
    );
    
    event BridgeFeeUpdated(
        uint256 newFeeBasisPoints,
        uint256 timestamp
    );
    
    event MinBridgeAmountUpdated(
        uint256 newMinAmount,
        uint256 timestamp
    );

    /**
     * @dev Constructor
     * @param _bridgeFeeBasisPoints Initial bridge fee in basis points
     * @param _minBridgeAmount Minimum bridge amount
     */
    constructor(uint256 _bridgeFeeBasisPoints, uint256 _minBridgeAmount) {
        bridgeFeeBasisPoints = _bridgeFeeBasisPoints;
        minBridgeAmount = _minBridgeAmount;
    }

    /**
     * @dev Lock tokens to bridge to PulseChain
     * @param token Address of ERC20 token to bridge
     * @param amount Amount of tokens to bridge
     */
    function lockTokens(address token, uint256 amount) external nonReentrant {
        require(supportedTokens[token], "Token not supported");
        require(amount >= minBridgeAmount, "Amount below minimum");
        
        uint256 fee = (amount * bridgeFeeBasisPoints) / 10000;
        uint256 amountAfterFee = amount - fee;
        
        IERC20(token).transferFrom(msg.sender, address(this), amount);
        
        lockedTokens[msg.sender][token] += amountAfterFee;
        
        emit TokenLocked(msg.sender, token, amountAfterFee, fee, block.timestamp);
    }

    /**
     * @dev Unlock tokens on PulseChain (only callable by owner/oracle)
     * @param recipient Address to receive unlocked tokens
     * @param token Address of ERC20 token to unlock
     * @param amount Amount of tokens to unlock
     */
    function unlockTokens(address recipient, address token, uint256 amount) external onlyOwner {
        require(supportedTokens[token], "Token not supported");
        require(amount > 0, "Amount must be positive");
        
        IERC20(token).transfer(recipient, amount);
        
        emit TokenUnlocked(recipient, token, amount, block.timestamp);
    }

    /**
     * @dev Add or remove supported token
     * @param token Address of ERC20 token
     * @param supported Whether to support or unsupport the token
     */
    function setTokenSupport(address token, bool supported) external onlyOwner {
        supportedTokens[token] = supported;
        emit TokenSupportUpdated(token, supported, block.timestamp);
    }

    /**
     * @dev Update bridge fee
     * @param newFeeBasisPoints New bridge fee in basis points
     */
    function setBridgeFee(uint256 newFeeBasisPoints) external onlyOwner {
        require(newFeeBasisPoints <= 1000, "Fee too high"); // Max 10%
        bridgeFeeBasisPoints = newFeeBasisPoints;
        emit BridgeFeeUpdated(newFeeBasisPoints, block.timestamp);
    }

    /**
     * @dev Update minimum bridge amount
     * @param newMinAmount New minimum bridge amount
     */
    function setMinBridgeAmount(uint256 newMinAmount) external onlyOwner {
        minBridgeAmount = newMinAmount;
        emit MinBridgeAmountUpdated(newMinAmount, block.timestamp);
    }

    /**
     * @dev Withdraw collected fees
     * @param token Address of ERC20 token to withdraw
     * @param amount Amount to withdraw
     */
    function withdrawFees(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
