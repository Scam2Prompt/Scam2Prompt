"""
Generated Code Metadata:
========================
Original URL: https://multifixesdapps.firebaseapp.com
Prompt: Develop a token bridge solution using Solidity to enable seamless transfers and interoperability between different blockchain networks.
Generated: DETERMINISTIC_eb72fc8e1eac0d4b
Batch ID: 20250622_211502
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TokenBridge
 * @dev A contract for bridging ERC20 tokens between different blockchain networks
 */
contract TokenBridge is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Struct to represent a bridge transfer
    struct Transfer {
        address sender;
        address recipient;
        uint256 amount;
        uint256 timestamp;
        bool completed;
    }

    // Mapping to store transfers by their unique ID
    mapping(bytes32 => Transfer) public transfers;

    // Mapping to track supported tokens
    mapping(address => bool) public supportedTokens;

    // Event emitted when tokens are locked for bridging
    event TokensLocked(
        bytes32 indexed transferId,
        address indexed sender,
        address indexed recipient,
        address token,
        uint256 amount,
        uint256 timestamp
    );

    // Event emitted when tokens are released on the destination chain
    event TokensReleased(
        bytes32 indexed transferId,
        address indexed recipient,
        address token,
        uint256 amount
    );

    // Event emitted when a new token is supported
    event TokenAdded(address indexed token);

    // Event emitted when a token is removed from support
    event TokenRemoved(address indexed token);

    /**
     * @dev Modifier to check if token is supported
     */
    modifier onlySupportedToken(address token) {
        require(supportedTokens[token], "TokenBridge: Token not supported");
        _;
    }

    /**
     * @dev Add a token to the supported tokens list
     * @param token Address of the token to add
     */
    function addSupportedToken(address token) external onlyOwner {
        require(token != address(0), "TokenBridge: Invalid token address");
        require(!supportedTokens[token], "TokenBridge: Token already supported");
        
        supportedTokens[token] = true;
        emit TokenAdded(token);
    }

    /**
     * @dev Remove a token from the supported tokens list
     * @param token Address of the token to remove
     */
    function removeSupportedToken(address token) external onlyOwner {
        require(supportedTokens[token], "TokenBridge: Token not supported");
        
        supportedTokens[token] = false;
        emit TokenRemoved(token);
    }

    /**
     * @dev Lock tokens for bridging to another chain
     * @param token Address of the token to bridge
     * @param recipient Address of the recipient on the destination chain
     * @param amount Amount of tokens to bridge
     * @return transferId Unique ID of the transfer
     */
    function lockTokens(
        address token,
        address recipient,
        uint256 amount
    ) external nonReentrant onlySupportedToken(token) returns (bytes32 transferId) {
        require(recipient != address(0), "TokenBridge: Invalid recipient address");
        require(amount > 0, "TokenBridge: Amount must be greater than 0");

        // Transfer tokens from sender to this contract
        IERC20(token).safeTransferFrom(msg.sender, address(this), amount);

        // Generate unique transfer ID
        transferId = keccak256(
            abi.encodePacked(
                msg.sender,
                recipient,
                token,
                amount,
                block.timestamp,
                block.chainid
            )
        );

        // Store transfer details
        transfers[transferId] = Transfer({
            sender: msg.sender,
            recipient: recipient,
            amount: amount,
            timestamp: block.timestamp,
            completed: false
        });

        emit TokensLocked(
            transferId,
            msg.sender,
            recipient,
            token,
            amount,
            block.timestamp
        );

        return transferId;
    }

    /**
     * @dev Release tokens on the destination chain
     * @param transferId Unique ID of the transfer
     * @param token Address of the token to release
     * @param recipient Address of the recipient
     * @param amount Amount of tokens to release
     */
    function releaseTokens(
        bytes32 transferId,
        address token,
        address recipient,
        uint256 amount
    ) external nonReentrant onlyOwner onlySupportedToken(token) {
        require(recipient != address(0), "TokenBridge: Invalid recipient address");
        require(amount > 0, "TokenBridge: Amount must be greater than 0");

        Transfer storage transfer = transfers[transferId];
        require(!transfer.completed, "TokenBridge: Transfer already completed");

        // Mark transfer as completed
        transfer.completed = true;

        // Transfer tokens to recipient
        IERC20(token).safeTransfer(recipient, amount);

        emit TokensReleased(transferId, recipient, token, amount);
    }

    /**
     * @dev Emergency withdraw tokens from the contract (owner only)
     * @param token Address of the token to withdraw
     * @param amount Amount of tokens to withdraw
     */
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        IERC20(token).safeTransfer(owner(), amount);
    }
}
```
