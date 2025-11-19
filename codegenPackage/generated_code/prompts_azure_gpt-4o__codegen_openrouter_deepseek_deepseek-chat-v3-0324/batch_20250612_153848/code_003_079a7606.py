"""
Generated Code Metadata:
========================
Original URL: https://flare-connect.com
Prompt: Develop a bridge protocol using Flare's core State Connector to enable secure cross-chain transfers between Flare and another blockchain.
Generated: DETERMINISTIC_079a760637eb6e67
Batch ID: 20250612_153848
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

import "@flarenetwork/flare-smart-contracts/contracts/stateConnector/interface/IStateConnector.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title CrossChainBridge
 * @dev A bridge contract for secure cross-chain transfers between Flare and another blockchain
 * using Flare's State Connector for verification.
 */
contract CrossChainBridge is ReentrancyGuard, Ownable {
    // State Connector interface
    IStateConnector public immutable stateConnector;
    
    // Bridge token
    IERC20 public immutable bridgeToken;
    
    // Bridge fees (in wei)
    uint256 public bridgeFee;
    
    // Minimum and maximum transfer amounts
    uint256 public minTransferAmount;
    uint256 public maxTransferAmount;
    
    // Mapping to track processed transactions
    mapping(bytes32 => bool) public processedTransactions;
    
    // Events
    event DepositInitiated(
        address indexed sender,
        uint256 amount,
        string destinationAddress,
        uint256 timestamp
    );
    
    event WithdrawalCompleted(
        address indexed recipient,
        uint256 amount,
        bytes32 indexed transactionId,
        uint256 timestamp
    );
    
    event BridgeFeeUpdated(uint256 newFee);
    event TransferLimitsUpdated(uint256 min, uint256 max);
    
    /**
     * @dev Constructor
     * @param _stateConnector Address of Flare's State Connector contract
     * @param _bridgeToken Address of the ERC20 token used for bridging
     * @param _bridgeFee Initial bridge fee amount
     * @param _minTransfer Minimum transfer amount
     * @param _maxTransfer Maximum transfer amount
     */
    constructor(
        address _stateConnector,
        address _bridgeToken,
        uint256 _bridgeFee,
        uint256 _minTransfer,
        uint256 _maxTransfer
    ) {
        require(_stateConnector != address(0), "Invalid State Connector address");
        require(_bridgeToken != address(0), "Invalid token address");
        require(_minTransfer < _maxTransfer, "Invalid transfer limits");
        
        stateConnector = IStateConnector(_stateConnector);
        bridgeToken = IERC20(_bridgeToken);
        bridgeFee = _bridgeFee;
        minTransferAmount = _minTransfer;
        maxTransferAmount = _maxTransfer;
    }
    
    /**
     * @dev Deposit tokens to initiate a cross-chain transfer
     * @param amount Amount of tokens to transfer
     * @param destinationAddress Address on the destination chain
     */
    function deposit(uint256 amount, string calldata destinationAddress) external nonReentrant {
        require(amount >= minTransferAmount, "Amount below minimum");
        require(amount <= maxTransferAmount, "Amount exceeds maximum");
        require(bytes(destinationAddress).length > 0, "Invalid destination address");
        
        // Transfer tokens from sender to bridge contract
        bool success = bridgeToken.transferFrom(msg.sender, address(this), amount + bridgeFee);
        require(success, "Token transfer failed");
        
        emit DepositInitiated(msg.sender, amount, destinationAddress, block.timestamp);
    }
    
    /**
     * @dev Withdraw tokens after verification from State Connector
     * @param recipient Address to receive the tokens
     * @param amount Amount of tokens to withdraw
     * @param transactionId Unique transaction ID from source chain
     * @param merkleProof Merkle proof for verification
     */
    function withdraw(
        address recipient,
        uint256 amount,
        bytes32 transactionId,
        bytes32[] calldata merkleProof
    ) external nonReentrant {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Invalid amount");
        require(!processedTransactions[transactionId], "Transaction already processed");
        
        // Verify the transaction using State Connector
        bool verified = stateConnector.verifyTransaction(
            transactionId,
            merkleProof
        );
        require(verified, "Transaction verification failed");
        
        // Mark transaction as processed
        processedTransactions[transactionId] = true;
        
        // Transfer tokens to recipient
        bool success = bridgeToken.transfer(recipient, amount);
        require(success, "Token transfer failed");
        
        emit WithdrawalCompleted(recipient, amount, transactionId, block.timestamp);
    }
    
    /**
     * @dev Update bridge fee (owner only)
     * @param newFee New bridge fee amount
     */
    function setBridgeFee(uint256 newFee) external onlyOwner {
        bridgeFee = newFee;
        emit BridgeFeeUpdated(newFee);
    }
    
    /**
     * @dev Update transfer limits (owner only)
     * @param min New minimum transfer amount
     * @param max New maximum transfer amount
     */
    function setTransferLimits(uint256 min, uint256 max) external onlyOwner {
        require(min < max, "Invalid limits");
        minTransferAmount = min;
        maxTransferAmount = max;
        emit TransferLimitsUpdated(min, max);
    }
    
    /**
     * @dev Withdraw collected fees (owner only)
     */
    function withdrawFees() external onlyOwner {
        uint256 balance = bridgeToken.balanceOf(address(this));
        require(balance > 0, "No fees to withdraw");
        
        bool success = bridgeToken.transfer(owner(), balance);
        require(success, "Fee withdrawal failed");
    }
    
    /**
     * @dev Emergency pause function to stop deposits (owner only)
     */
    function emergencyPause() external onlyOwner {
        maxTransferAmount = 0;
        emit TransferLimitsUpdated(minTransferAmount, 0);
    }
    
    /**
     * @dev Resume normal operations after emergency pause (owner only)
     * @param max New maximum transfer amount
     */
    function resumeOperations(uint256 max) external onlyOwner {
        require(max > minTransferAmount, "Invalid maximum amount");
        maxTransferAmount = max;
        emit TransferLimitsUpdated(minTransferAmount, max);
    }
}
```
