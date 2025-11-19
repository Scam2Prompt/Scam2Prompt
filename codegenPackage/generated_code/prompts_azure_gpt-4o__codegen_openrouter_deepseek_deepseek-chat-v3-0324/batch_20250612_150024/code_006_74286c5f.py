"""
Generated Code Metadata:
========================
Original URL: https://zkbridge.pages.dev
Prompt: Develop a cross-chain DeFi protocol that leverages zkBridge for multi-chain liquidity and efficient verification of remote blockchain transactions.
Generated: DETERMINISTIC_74286c5fbca4ef3f
Batch ID: 20250612_150024
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

interface IZKBridge {
    function verifyProof(
        bytes32 root,
        bytes32[] calldata proof,
        bytes32 leaf
    ) external view returns (bool);
    
    function sendMessage(
        uint256 destinationChainId,
        bytes calldata message
    ) external payable;
}

contract CrossChainDeFi is ReentrancyGuard {
    using SafeMath for uint256;
    
    // Contract owner
    address public owner;
    
    // zkBridge contract interface
    IZKBridge public zkBridge;
    
    // Supported chains mapping
    mapping(uint256 => bool) public supportedChains;
    
    // Token balances per chain
    mapping(address => mapping(uint256 => uint256)) public balances;
    
    // Pending transfers
    struct PendingTransfer {
        address user;
        address token;
        uint256 amount;
        uint256 timestamp;
    }
    
    mapping(bytes32 => PendingTransfer) public pendingTransfers;
    
    // Events
    event Deposit(
        address indexed user,
        address indexed token,
        uint256 amount,
        uint256 chainId
    );
    
    event WithdrawInitiated(
        address indexed user,
        address indexed token,
        uint256 amount,
        uint256 sourceChainId,
        uint256 destinationChainId,
        bytes32 proofRoot
    );
    
    event WithdrawCompleted(
        address indexed user,
        address indexed token,
        uint256 amount,
        uint256 sourceChainId
    );
    
    event ChainSupportUpdated(
        uint256 chainId,
        bool supported
    );
    
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }
    
    constructor(address _zkBridgeAddress) {
        owner = msg.sender;
        zkBridge = IZKBridge(_zkBridgeAddress);
    }
    
    /**
     * @dev Deposit tokens to be available on another chain
     * @param token Address of the token to deposit
     * @param amount Amount to deposit
     * @param destinationChainId Chain ID where tokens should be available
     */
    function deposit(
        address token,
        uint256 amount,
        uint256 destinationChainId
    ) external nonReentrant {
        require(supportedChains[destinationChainId], "Chain not supported");
        require(amount > 0, "Amount must be greater than 0");
        
        IERC20(token).transferFrom(msg.sender, address(this), amount);
        balances[token][destinationChainId] = balances[token][destinationChainId].add(amount);
        
        emit Deposit(msg.sender, token, amount, destinationChainId);
    }
    
    /**
     * @dev Initiate withdrawal of tokens from another chain
     * @param token Address of the token to withdraw
     * @param amount Amount to withdraw
     * @param sourceChainId Chain ID where tokens are currently held
     * @param proofRoot Merkle root of the proof
     * @param proof Merkle proof
     */
    function initiateWithdraw(
        address token,
        uint256 amount,
        uint256 sourceChainId,
        bytes32 proofRoot,
        bytes32[] calldata proof
    ) external payable nonReentrant {
        require(supportedChains[sourceChainId], "Source chain not supported");
        require(amount > 0, "Amount must be greater than 0");
        
        // Generate leaf from withdrawal details
        bytes32 leaf = keccak256(abi.encodePacked(
            msg.sender,
            token,
            amount,
            sourceChainId,
            block.chainid
        ));
        
        // Verify proof using zkBridge
        require(
            zkBridge.verifyProof(proofRoot, proof, leaf),
            "Invalid proof"
        );
        
        // Create pending transfer
        bytes32 transferId = keccak256(abi.encodePacked(
            leaf,
            block.timestamp
        ));
        
        pendingTransfers[transferId] = PendingTransfer({
            user: msg.sender,
            token: token,
            amount: amount,
            timestamp: block.timestamp
        });
        
        // Send message to source chain to lock funds
        bytes memory message = abi.encode(
            msg.sender,
            token,
            amount,
            sourceChainId,
            block.chainid,
            transferId
        );
        
        zkBridge.sendMessage{value: msg.value}(sourceChainId, message);
        
        emit WithdrawInitiated(
            msg.sender,
            token,
            amount,
            sourceChainId,
            block.chainid,
            proofRoot
        );
    }
    
    /**
     * @dev Complete withdrawal after verification from source chain
     * @param transferId ID of the pending transfer
     * @param sourceChainId Chain ID where tokens were locked
     */
    function completeWithdraw(
        bytes32 transferId,
        uint256 sourceChainId
    ) external nonReentrant {
        PendingTransfer memory transfer = pendingTransfers[transferId];
        require(transfer.user != address(0), "Transfer not found");
        require(block.timestamp <= transfer.timestamp.add(7 days), "Transfer expired");
        
        // Verify the message came from the source chain's bridge
        require(msg.sender == address(zkBridge), "Only bridge can complete");
        
        // Transfer tokens to user
        IERC20(transfer.token).transfer(transfer.user, transfer.amount);
        
        // Clean up
        delete pendingTransfers[transferId];
        
        emit WithdrawCompleted(
            transfer.user,
            transfer.token,
            transfer.amount,
            sourceChainId
        );
    }
    
    /**
     * @dev Update supported chains
     * @param chainId Chain ID to update
     * @param supported Whether to support the chain
     */
    function updateChainSupport(
        uint256 chainId,
        bool supported
    ) external onlyOwner {
        supportedChains[chainId] = supported;
        emit ChainSupportUpdated(chainId, supported);
    }
    
    /**
     * @dev Update zkBridge address
     * @param newBridge Address of the new zkBridge contract
     */
    function updateZKBridge(address newBridge) external onlyOwner {
        require(newBridge != address(0), "Invalid bridge address");
        zkBridge = IZKBridge(newBridge);
    }
    
    /**
     * @dev Emergency withdraw tokens from contract
     * @param token Address of token to withdraw
     */
    function emergencyWithdraw(address token) external onlyOwner {
        uint256 balance = IERC20(token).balanceOf(address(this));
        IERC20(token).transfer(owner, balance);
    }
}
```
