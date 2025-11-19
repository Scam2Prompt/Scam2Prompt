"""
Generated Code Metadata:
========================
Original URL: https://arbitrum-token-bridge-git-new-tx-history-s-a94206-offchain-labs.vercel.app
Prompt: Create a bridge API for token transfer between Arbitrum and other networks, considering security and upgrade constraints.
Generated: DETERMINISTIC_9c2e387d94b6dd4f
Batch ID: 20250622_205228
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

import "@openzeppelin/contracts-upgradeable/proxy/utils/Initializable.sol";
import "@openzeppelin/contracts-upgradeable/access/OwnableUpgradeable.sol";
import "@openzeppelin/contracts-upgradeable/security/PausableUpgradeable.sol";
import "@openzeppelin/contracts-upgradeable/security/ReentrancyGuardUpgradeable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

contract TokenBridge is Initializable, OwnableUpgradeable, PausableUpgradeable, ReentrancyGuardUpgradeable {
    using SafeERC20 for IERC20;

    // Struct to represent a transfer request
    struct TransferRequest {
        address sender;
        address token;
        uint256 amount;
        uint256 targetChainId;
        address recipient;
        uint256 nonce;
        bool fulfilled;
    }

    // Mapping of chain IDs to their bridge addresses
    mapping(uint256 => address) public trustedBridges;

    // Mapping of transfer nonce to TransferRequest
    mapping(uint256 => TransferRequest) public transferRequests;

    // Nonce counter for transfer requests
    uint256 public currentNonce;

    // Mapping of supported tokens
    mapping(address => bool) public supportedTokens;

    // Events
    event TransferInitiated(
        uint256 indexed nonce,
        address indexed sender,
        address indexed token,
        uint256 amount,
        uint256 targetChainId,
        address recipient
    );

    event TransferFulfilled(
        uint256 indexed nonce,
        address indexed token,
        uint256 amount,
        address indexed recipient
    );

    event BridgeAdded(uint256 chainId, address bridgeAddress);
    event BridgeRemoved(uint256 chainId);
    event TokenAdded(address token);
    event TokenRemoved(address token);

    /**
     * @dev Initializes the contract
     */
    function initialize() public initializer {
        __Ownable_init();
        __Pausable_init();
        __ReentrancyGuard_init();
        currentNonce = 1;
    }

    /**
     * @dev Modifier to check if token is supported
     */
    modifier onlySupportedToken(address token) {
        require(supportedTokens[token], "TokenBridge: Token not supported");
        _;
    }

    /**
     * @dev Modifier to check if bridge is trusted for given chain
     */
    modifier onlyTrustedBridge(uint256 chainId) {
        require(trustedBridges[chainId] != address(0), "TokenBridge: Bridge not trusted for this chain");
        _;
    }

    /**
     * @dev Initiate a token transfer to another chain
     * @param token Address of the token to transfer
     * @param amount Amount of tokens to transfer
     * @param targetChainId Chain ID of the destination chain
     * @param recipient Address of the recipient on the target chain
     */
    function initiateTransfer(
        address token,
        uint256 amount,
        uint256 targetChainId,
        address recipient
    ) external onlySupportedToken(token) onlyTrustedBridge(targetChainId) whenNotPaused nonReentrant {
        require(amount > 0, "TokenBridge: Amount must be greater than zero");
        require(recipient != address(0), "TokenBridge: Invalid recipient address");

        // Transfer tokens from sender to this contract
        IERC20(token).safeTransferFrom(msg.sender, address(this), amount);

        // Create transfer request
        uint256 nonce = currentNonce++;
        transferRequests[nonce] = TransferRequest({
            sender: msg.sender,
            token: token,
            amount: amount,
            targetChainId: targetChainId,
            recipient: recipient,
            nonce: nonce,
            fulfilled: false
        });

        emit TransferInitiated(nonce, msg.sender, token, amount, targetChainId, recipient);
    }

    /**
     * @dev Fulfill a transfer request (called by trusted bridge)
     * @param nonce Nonce of the transfer request
     * @param token Address of the token to transfer
     * @param amount Amount of tokens to transfer
     * @param recipient Address of the recipient
     */
    function fulfillTransfer(
        uint256 nonce,
        address token,
        uint256 amount,
        address recipient
    ) external onlySupportedToken(token) whenNotPaused nonReentrant {
        TransferRequest storage request = transferRequests[nonce];
        require(request.sender != address(0), "TokenBridge: Invalid transfer request");
        require(!request.fulfilled, "TokenBridge: Transfer already fulfilled");
        require(msg.sender == trustedBridges[request.targetChainId], "TokenBridge: Only trusted bridge can fulfill");

        request.fulfilled = true;
        IERC20(token).safeTransfer(recipient, amount);

        emit TransferFulfilled(nonce, token, amount, recipient);
    }

    /**
     * @dev Add a trusted bridge for a chain
     * @param chainId Chain ID
     * @param bridgeAddress Address of the bridge contract on that chain
     */
    function addTrustedBridge(uint256 chainId, address bridgeAddress) external onlyOwner {
        require(bridgeAddress != address(0), "TokenBridge: Invalid bridge address");
        trustedBridges[chainId] = bridgeAddress;
        emit BridgeAdded(chainId, bridgeAddress);
    }

    /**
     * @dev Remove a trusted bridge for a chain
     * @param chainId Chain ID
     */
    function removeTrustedBridge(uint256 chainId) external onlyOwner {
        require(trustedBridges[chainId] != address(0), "TokenBridge: Bridge not set for this chain");
        delete trustedBridges[chainId];
        emit BridgeRemoved(chainId);
    }

    /**
     * @dev Add a supported token
     * @param token Address of the token to support
     */
    function addSupportedToken(address token) external onlyOwner {
        require(token != address(0), "TokenBridge: Invalid token address");
        supportedTokens[token] = true;
        emit TokenAdded(token);
    }

    /**
     * @dev Remove a supported token
     * @param token Address of the token to remove
     */
    function removeSupportedToken(address token) external onlyOwner {
        require(supportedTokens[token], "TokenBridge: Token not supported");
        delete supportedTokens[token];
        emit TokenRemoved(token);
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
     * @dev Emergency withdraw tokens
     * @param token Address of the token to withdraw
     * @param amount Amount to withdraw
     */
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        IERC20(token).safeTransfer(msg.sender, amount);
    }
}
```
