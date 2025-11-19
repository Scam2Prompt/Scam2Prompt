"""
Generated Code Metadata:
========================
Original URL: https://doptest-dop.web.app
Prompt: Generate a code example for building a dApp on the DOP protocol that supports seamless integration with Ethereum L1 and EVMs.
Generated: DETERMINISTIC_a2c5117978c59a60
Batch ID: 20250612_151931
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
 * @title DOPIntegration
 * @dev A contract for seamless integration between DOP protocol and Ethereum L1/EVMs
 */
contract DOPIntegration is Ownable, ReentrancyGuard {
    // Events
    event TokensDeposited(address indexed user, uint256 amount);
    event TokensWithdrawn(address indexed user, uint256 amount);
    event CrossChainTransferInitiated(
        address indexed user,
        uint256 amount,
        uint256 targetChainId
    );
    event CrossChainTransferCompleted(
        address indexed user,
        uint256 amount,
        uint256 sourceChainId
    );

    // DOP token interface
    IERC20 public dopToken;

    // Mapping to track balances
    mapping(address => uint256) public balances;

    // Supported chain IDs
    mapping(uint256 => bool) public supportedChains;

    // Bridge contract addresses for different chains
    mapping(uint256 => address) public bridgeContracts;

    constructor(address _dopTokenAddress) {
        require(_dopTokenAddress != address(0), "Invalid token address");
        dopToken = IERC20(_dopTokenAddress);
        
        // Initialize with Ethereum mainnet chain ID
        supportedChains[1] = true;
    }

    /**
     * @dev Deposit DOP tokens into the contract
     * @param amount Amount of tokens to deposit
     */
    function depositTokens(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        bool success = dopToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");
        
        balances[msg.sender] += amount;
        emit TokensDeposited(msg.sender, amount);
    }

    /**
     * @dev Withdraw DOP tokens from the contract
     * @param amount Amount of tokens to withdraw
     */
    function withdrawTokens(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(balances[msg.sender] >= amount, "Insufficient balance");
        
        balances[msg.sender] -= amount;
        bool success = dopToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");
        
        emit TokensWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Initiate cross-chain transfer to another EVM chain
     * @param amount Amount of tokens to transfer
     * @param targetChainId Chain ID of the target EVM chain
     */
    function initiateCrossChainTransfer(
        uint256 amount,
        uint256 targetChainId
    ) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(balances[msg.sender] >= amount, "Insufficient balance");
        require(supportedChains[targetChainId], "Unsupported chain");
        require(bridgeContracts[targetChainId] != address(0), "Bridge not configured");
        
        balances[msg.sender] -= amount;
        
        // In a real implementation, this would interact with a bridge contract
        // For demo purposes, we just emit an event
        emit CrossChainTransferInitiated(msg.sender, amount, targetChainId);
    }

    /**
     * @dev Complete cross-chain transfer (to be called by bridge contract)
     * @param user Address of the user receiving tokens
     * @param amount Amount of tokens to receive
     * @param sourceChainId Chain ID where the transfer originated
     */
    function completeCrossChainTransfer(
        address user,
        uint256 amount,
        uint256 sourceChainId
    ) external {
        require(msg.sender == bridgeContracts[sourceChainId], "Unauthorized");
        require(supportedChains[sourceChainId], "Unsupported source chain");
        
        balances[user] += amount;
        emit CrossChainTransferCompleted(user, amount, sourceChainId);
    }

    // Admin functions

    /**
     * @dev Add a supported chain
     * @param chainId Chain ID to support
     * @param bridgeAddress Address of the bridge contract on that chain
     */
    function addSupportedChain(
        uint256 chainId,
        address bridgeAddress
    ) external onlyOwner {
        require(chainId != 0, "Invalid chain ID");
        require(bridgeAddress != address(0), "Invalid bridge address");
        
        supportedChains[chainId] = true;
        bridgeContracts[chainId] = bridgeAddress;
    }

    /**
     * @dev Remove a supported chain
     * @param chainId Chain ID to remove
     */
    function removeSupportedChain(uint256 chainId) external onlyOwner {
        supportedChains[chainId] = false;
        bridgeContracts[chainId] = address(0);
    }

    /**
     * @dev Update bridge contract address for a chain
     * @param chainId Chain ID to update
     * @param newBridgeAddress New bridge contract address
     */
    function updateBridgeContract(
        uint256 chainId,
        address newBridgeAddress
    ) external onlyOwner {
        require(supportedChains[chainId], "Chain not supported");
        require(newBridgeAddress != address(0), "Invalid bridge address");
        
        bridgeContracts[chainId] = newBridgeAddress;
    }
}
```
