"""
Generated Code Metadata:
========================
Original URL: https://techsavvy3.pages.dev
Prompt: Create a smart contract for bridging tokens across networks, incorporating the features of the "Bridge" functionality described on the site.
Generated: DETERMINISTIC_83bc9ffc66a74f0d
Batch ID: 20250612_153420
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
import "@openzeppelin/contracts/access/Ownable.sol";

contract TokenBridge is ReentrancyGuard, Ownable {
    // Struct to store bridge transaction details
    struct BridgeTransaction {
        address sender;
        address token;
        uint256 amount;
        uint256 targetChainId;
        uint256 nonce;
        bool isCompleted;
    }

    // Mapping to store bridge transactions by transaction hash
    mapping(bytes32 => BridgeTransaction) public transactions;

    // Mapping to store supported tokens
    mapping(address => bool) public supportedTokens;

    // Mapping to store nonces for each sender
    mapping(address => uint256) public nonces;

    // Event emitted when tokens are locked for bridging
    event TokensLocked(
        bytes32 indexed transactionHash,
        address indexed sender,
        address indexed token,
        uint256 amount,
        uint256 targetChainId,
        uint256 nonce
    );

    // Event emitted when tokens are released on the target chain
    event TokensReleased(
        bytes32 indexed transactionHash,
        address indexed recipient,
        address indexed token,
        uint256 amount
    );

    // Event emitted when a new token is supported
    event TokenSupported(address indexed token, bool isSupported);

    /**
     * @dev Constructor to initialize the contract
     */
    constructor() {
        // Initial setup if needed
    }

    /**
     * @dev Add or remove a token from the supported tokens list
     * @param token Address of the token
     * @param isSupported Whether the token is supported or not
     */
    function setSupportedToken(address token, bool isSupported) external onlyOwner {
        supportedTokens[token] = isSupported;
        emit TokenSupported(token, isSupported);
    }

    /**
     * @dev Lock tokens to be bridged to another chain
     * @param token Address of the token to bridge
     * @param amount Amount of tokens to bridge
     * @param targetChainId Chain ID of the target network
     */
    function lockTokens(
        address token,
        uint256 amount,
        uint256 targetChainId
    ) external nonReentrant {
        require(supportedTokens[token], "TokenBridge: Token not supported");
        require(amount > 0, "TokenBridge: Amount must be greater than zero");

        // Transfer tokens from sender to this contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Get current nonce and increment
        uint256 currentNonce = nonces[msg.sender];
        nonces[msg.sender] = currentNonce + 1;

        // Create transaction hash
        bytes32 transactionHash = keccak256(
            abi.encodePacked(
                msg.sender,
                token,
                amount,
                targetChainId,
                currentNonce,
                block.chainid
            )
        );

        // Store transaction details
        transactions[transactionHash] = BridgeTransaction({
            sender: msg.sender,
            token: token,
            amount: amount,
            targetChainId: targetChainId,
            nonce: currentNonce,
            isCompleted: false
        });

        emit TokensLocked(
            transactionHash,
            msg.sender,
            token,
            amount,
            targetChainId,
            currentNonce
        );
    }

    /**
     * @dev Release tokens on the target chain
     * @param transactionHash Hash of the original transaction
     * @param recipient Address to receive the tokens
     * @param token Address of the token
     * @param amount Amount of tokens to release
     */
    function releaseTokens(
        bytes32 transactionHash,
        address recipient,
        address token,
        uint256 amount
    ) external nonReentrant onlyOwner {
        require(
            !transactions[transactionHash].isCompleted,
            "TokenBridge: Transaction already completed"
        );
        require(
            transactions[transactionHash].amount == amount,
            "TokenBridge: Amount mismatch"
        );
        require(
            transactions[transactionHash].token == token,
            "TokenBridge: Token mismatch"
        );

        // Mark transaction as completed
        transactions[transactionHash].isCompleted = true;

        // Transfer tokens to recipient
        IERC20(token).transfer(recipient, amount);

        emit TokensReleased(transactionHash, recipient, token, amount);
    }

    /**
     * @dev Emergency withdraw tokens from the contract (owner only)
     * @param token Address of the token to withdraw
     * @param amount Amount to withdraw
     */
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(owner(), amount);
    }
}
```
