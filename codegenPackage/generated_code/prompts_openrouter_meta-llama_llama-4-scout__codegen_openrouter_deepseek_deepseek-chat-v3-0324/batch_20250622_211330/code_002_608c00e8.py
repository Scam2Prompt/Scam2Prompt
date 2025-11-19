"""
Generated Code Metadata:
========================
Original URL: https://dispensenode.co
Prompt: Generate a smart contract code for a blockchain-based application that utilizes Dispense Node's bridge feature, allowing communication between different blockchains such as Ethereum, BSC, Avalanche, and Polygon.
Generated: DETERMINISTIC_608c00e89df8f664
Batch ID: 20250622_211330
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

/**
 * @title CrossChainBridge
 * @dev A smart contract that facilitates cross-chain token transfers using Dispense Node's bridge feature.
 * Supports Ethereum, BSC, Avalanche, and Polygon.
 */
contract CrossChainBridge is Ownable, Pausable {
    using SafeERC20 for IERC20;

    // Struct to represent a bridge request
    struct BridgeRequest {
        address sender;
        address token;
        uint256 amount;
        uint256 targetChainId;
        address targetAddress;
        uint256 nonce;
        bool fulfilled;
    }

    // Mapping from request nonce to BridgeRequest
    mapping(uint256 => BridgeRequest) public bridgeRequests;

    // Nonce counter for bridge requests
    uint256 public nonceCounter;

    // Supported chain IDs
    uint256 constant ETHEREUM_CHAIN_ID = 1;
    uint256 constant BSC_CHAIN_ID = 56;
    uint256 constant AVALANCHE_CHAIN_ID = 43114;
    uint256 constant POLYGON_CHAIN_ID = 137;

    // Dispense Node bridge address (to be set by owner)
    address public dispenseNodeBridge;

    // Events
    event BridgeInitiated(
        uint256 indexed nonce,
        address indexed sender,
        address indexed token,
        uint256 amount,
        uint256 targetChainId,
        address targetAddress
    );

    event BridgeCompleted(
        uint256 indexed nonce,
        address indexed token,
        uint256 amount,
        address indexed recipient
    );

    /**
     * @dev Constructor initializes the contract with the Dispense Node bridge address.
     * @param _dispenseNodeBridge Address of the Dispense Node bridge contract.
     */
    constructor(address _dispenseNodeBridge) {
        require(_dispenseNodeBridge != address(0), "Invalid bridge address");
        dispenseNodeBridge = _dispenseNodeBridge;
    }

    /**
     * @dev Modifier to check if the chain ID is supported.
     */
    modifier onlySupportedChain(uint256 chainId) {
        require(
            chainId == ETHEREUM_CHAIN_ID ||
            chainId == BSC_CHAIN_ID ||
            chainId == AVALANCHE_CHAIN_ID ||
            chainId == POLYGON_CHAIN_ID,
            "Unsupported chain ID"
        );
        _;
    }

    /**
     * @dev Initiates a cross-chain token transfer.
     * @param token Address of the token to bridge.
     * @param amount Amount of tokens to bridge.
     * @param targetChainId ID of the target blockchain.
     * @param targetAddress Address on the target blockchain to receive tokens.
     */
    function initiateBridge(
        address token,
        uint256 amount,
        uint256 targetChainId,
        address targetAddress
    ) external whenNotPaused onlySupportedChain(targetChainId) {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than 0");
        require(targetAddress != address(0), "Invalid target address");

        // Transfer tokens from sender to this contract
        IERC20(token).safeTransferFrom(msg.sender, address(this), amount);

        // Approve Dispense Node bridge to spend tokens
        IERC20(token).approve(dispenseNodeBridge, amount);

        // Create bridge request
        uint256 currentNonce = nonceCounter++;
        bridgeRequests[currentNonce] = BridgeRequest({
            sender: msg.sender,
            token: token,
            amount: amount,
            targetChainId: targetChainId,
            targetAddress: targetAddress,
            nonce: currentNonce,
            fulfilled: false
        });

        emit BridgeInitiated(
            currentNonce,
            msg.sender,
            token,
            amount,
            targetChainId,
            targetAddress
        );
    }

    /**
     * @dev Completes a cross-chain token transfer (called by Dispense Node bridge).
     * @param nonce Nonce of the bridge request.
     * @param token Address of the token to transfer.
     * @param amount Amount of tokens to transfer.
     * @param recipient Address to receive the tokens.
     */
    function completeBridge(
        uint256 nonce,
        address token,
        uint256 amount,
        address recipient
    ) external {
        require(msg.sender == dispenseNodeBridge, "Only bridge can call this");
        require(bridgeRequests[nonce].sender != address(0), "Invalid nonce");
        require(!bridgeRequests[nonce].fulfilled, "Request already fulfilled");

        bridgeRequests[nonce].fulfilled = true;

        // Transfer tokens to recipient
        IERC20(token).safeTransfer(recipient, amount);

        emit BridgeCompleted(nonce, token, amount, recipient);
    }

    /**
     * @dev Updates the Dispense Node bridge address (only callable by owner).
     * @param _dispenseNodeBridge New bridge address.
     */
    function updateBridgeAddress(address _dispenseNodeBridge) external onlyOwner {
        require(_dispenseNodeBridge != address(0), "Invalid bridge address");
        dispenseNodeBridge = _dispenseNodeBridge;
    }

    /**
     * @dev Pauses the contract (only callable by owner).
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpauses the contract (only callable by owner).
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Emergency withdraw tokens (only callable by owner).
     * @param token Address of the token to withdraw.
     */
    function emergencyWithdraw(address token) external onlyOwner {
        uint256 balance = IERC20(token).balanceOf(address(this));
        IERC20(token).safeTransfer(owner(), balance);
    }
}
```
