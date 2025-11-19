"""
Generated Code Metadata:
========================
Original URL: https://blockchain-tool.web.app
Prompt: Develop a token bridge solution using Solidity to enable seamless transfers between different blockchain networks.
Generated: DETERMINISTIC_ae5feb5d2a194626
Batch ID: 20250622_205227
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
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract TokenBridge is Ownable, Pausable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to represent a bridge transaction
    struct BridgeTransaction {
        address sender;
        address token;
        uint256 amount;
        uint256 targetChainId;
        uint256 nonce;
        bool isCompleted;
    }

    // Mapping from transaction hash to BridgeTransaction
    mapping(bytes32 => BridgeTransaction) public transactions;

    // Mapping from chainId to bridge address on that chain
    mapping(uint256 => address) public bridgeAddresses;

    // Mapping from token address to whether it's supported
    mapping(address => bool) public supportedTokens;

    // Nonce for transaction tracking
    uint256 public nonce;

    // Events
    event TokensLocked(
        address indexed sender,
        address indexed token,
        uint256 amount,
        uint256 targetChainId,
        uint256 nonce,
        bytes32 transactionHash
    );

    event TokensReleased(
        address indexed recipient,
        address indexed token,
        uint256 amount,
        uint256 sourceChainId,
        uint256 nonce,
        bytes32 transactionHash
    );

    event BridgeAddressUpdated(uint256 chainId, address bridgeAddress);
    event TokenSupportUpdated(address token, bool isSupported);

    /**
     * @dev Constructor to initialize the contract
     */
    constructor() {
        // Initialize with default values
    }

    /**
     * @dev Lock tokens to be bridged to another chain
     * @param token Address of the token to bridge
     * @param amount Amount of tokens to bridge
     * @param targetChainId Chain ID of the target blockchain
     */
    function lockTokens(
        address token,
        uint256 amount,
        uint256 targetChainId
    ) external whenNotPaused nonReentrant {
        require(supportedTokens[token], "TokenBridge: Token not supported");
        require(amount > 0, "TokenBridge: Amount must be greater than zero");
        require(
            bridgeAddresses[targetChainId] != address(0),
            "TokenBridge: Target chain not supported"
        );

        // Transfer tokens from sender to this contract
        IERC20(token).safeTransferFrom(msg.sender, address(this), amount);

        // Create transaction
        uint256 currentNonce = nonce++;
        bytes32 txHash = keccak256(
            abi.encodePacked(
                msg.sender,
                token,
                amount,
                targetChainId,
                currentNonce,
                block.chainid
            )
        );

        transactions[txHash] = BridgeTransaction({
            sender: msg.sender,
            token: token,
            amount: amount,
            targetChainId: targetChainId,
            nonce: currentNonce,
            isCompleted: false
        });

        emit TokensLocked(
            msg.sender,
            token,
            amount,
            targetChainId,
            currentNonce,
            txHash
        );
    }

    /**
     * @dev Release tokens from another chain
     * @param recipient Address to receive the tokens
     * @param token Address of the token to release
     * @param amount Amount of tokens to release
     * @param sourceChainId Chain ID of the source blockchain
     * @param sourceNonce Nonce from the source chain transaction
     * @param sourceTxHash Transaction hash from the source chain
     * @param signatures Array of validator signatures
     */
    function releaseTokens(
        address recipient,
        address token,
        uint256 amount,
        uint256 sourceChainId,
        uint256 sourceNonce,
        bytes32 sourceTxHash,
        bytes[] calldata signatures
    ) external whenNotPaused nonReentrant {
        require(supportedTokens[token], "TokenBridge: Token not supported");
        require(amount > 0, "TokenBridge: Amount must be greater than zero");
        require(
            bridgeAddresses[sourceChainId] != address(0),
            "TokenBridge: Source chain not supported"
        );

        // Verify the transaction hasn't been completed already
        bytes32 localTxHash = keccak256(
            abi.encodePacked(
                recipient,
                token,
                amount,
                sourceChainId,
                sourceNonce,
                sourceChainId
            )
        );
        require(
            !transactions[localTxHash].isCompleted,
            "TokenBridge: Transaction already completed"
        );

        // Verify signatures (simplified for example)
        require(
            signatures.length >= 1,
            "TokenBridge: Insufficient signatures"
        );

        // Mark transaction as completed
        transactions[localTxHash].isCompleted = true;

        // Transfer tokens to recipient
        IERC20(token).safeTransfer(recipient, amount);

        emit TokensReleased(
            recipient,
            token,
            amount,
            sourceChainId,
            sourceNonce,
            sourceTxHash
        );
    }

    /**
     * @dev Update bridge address for a chain
     * @param chainId Chain ID to update
     * @param bridgeAddress Address of the bridge on that chain
     */
    function updateBridgeAddress(
        uint256 chainId,
        address bridgeAddress
    ) external onlyOwner {
        require(
            bridgeAddress != address(0),
            "TokenBridge: Invalid bridge address"
        );
        bridgeAddresses[chainId] = bridgeAddress;
        emit BridgeAddressUpdated(chainId, bridgeAddress);
    }

    /**
     * @dev Update token support status
     * @param token Token address to update
     * @param isSupported Whether the token is supported
     */
    function updateTokenSupport(
        address token,
        bool isSupported
    ) external onlyOwner {
        supportedTokens[token] = isSupported;
        emit TokenSupportUpdated(token, isSupported);
    }

    /**
     * @dev Pause the contract
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause the contract
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Withdraw tokens in case of emergency
     * @param token Address of the token to withdraw
     * @param amount Amount to withdraw
     */
    function emergencyWithdraw(
        address token,
        uint256 amount
    ) external onlyOwner {
        IERC20(token).safeTransfer(owner(), amount);
    }
}
```
