"""
Generated Code Metadata:
========================
Original URL: https://v2-orbiter.net
Prompt: Generate Solidity code for a non-custodial smart contract that facilitates secure asset transfers across Ethereum Layer 2 networks, inspired by Orbiter Finance's bridging mechanics.
Generated: DETERMINISTIC_4a055f8816890482
Batch ID: 20250612_154820
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

/**
 * @title Orbiter Finance-inspired Non-Custodial Bridge Contract
 * @author [Your Name]
 * @notice This contract facilitates secure asset transfers across Ethereum Layer 2 networks.
 */
contract L2Bridge is ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Mapping of L2 networks to their respective bridge configurations
    mapping(address => BridgeConfig) public bridgeConfigs;

    // Mapping of transfer requests
    mapping(bytes32 => TransferRequest) public transferRequests;

    // Event emitted when a transfer request is initiated
    event TransferRequested(
        bytes32 indexed requestId,
        address indexed from,
        address indexed to,
        uint256 amount,
        address token,
        uint256 l2ChainId
    );

    // Event emitted when a transfer is executed
    event TransferExecuted(bytes32 indexed requestId);

    // Event emitted when a transfer is failed
    event TransferFailed(bytes32 indexed requestId, string reason);

    /**
     * @dev Struct representing a bridge configuration
     */
    struct BridgeConfig {
        address l2Token;
        uint256 l2ChainId;
        address counterpartyBridge;
    }

    /**
     * @dev Struct representing a transfer request
     */
    struct TransferRequest {
        address from;
        address to;
        uint256 amount;
        address token;
        uint256 l2ChainId;
        bool executed;
        bool failed;
    }

    /**
     * @dev Initializes the bridge contract
     * @param _bridgeConfig The initial bridge configuration
     */
    constructor(BridgeConfig memory _bridgeConfig) {
        bridgeConfigs[msg.sender] = _bridgeConfig;
    }

    /**
     * @dev Initiates a transfer request
     * @param _to The recipient address on the destination L2 network
     * @param _amount The amount of tokens to transfer
     * @param _token The address of the token to transfer
     * @param _l2ChainId The chain ID of the destination L2 network
     */
    function initiateTransfer(
        address _to,
        uint256 _amount,
        address _token,
        uint256 _l2ChainId
    ) external nonReentrant {
        // Validate input parameters
        require(_to != address(0), "Invalid recipient address");
        require(_amount > 0, "Invalid transfer amount");
        require(_token != address(0), "Invalid token address");
        require(_l2ChainId != 0, "Invalid L2 chain ID");

        // Get the bridge configuration for the source L2 network
        BridgeConfig memory config = bridgeConfigs[msg.sender];
        require(config.l2ChainId != 0, "Bridge not configured for this L2 network");

        // Validate the token address
        require(IERC20(_token).balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        // Generate a unique request ID
        bytes32 requestId = keccak256(abi.encodePacked(msg.sender, _to, _amount, _token, _l2ChainId));

        // Create a new transfer request
        transferRequests[requestId] = TransferRequest(
            msg.sender,
            _to,
            _amount,
            _token,
            _l2ChainId,
            false,
            false
        );

        // Emit the transfer requested event
        emit TransferRequested(requestId, msg.sender, _to, _amount, _token, _l2ChainId);

        // Lock the tokens on the source L2 network
        IERC20(_token).safeTransferFrom(msg.sender, address(this), _amount);
    }

    /**
     * @dev Executes a transfer request on the destination L2 network
     * @param _requestId The ID of the transfer request
     * @param _proof The proof of the transfer request
     */
    function executeTransfer(bytes32 _requestId, bytes calldata _proof) external nonReentrant {
        // Get the transfer request
        TransferRequest memory request = transferRequests[_requestId];
        require(request.from != address(0), "Transfer request not found");
        require(!request.executed && !request.failed, "Transfer request already executed or failed");

        // Validate the proof
        // NOTE: Implement proof validation logic here (e.g., verifying the Merkle proof)
        // For demonstration purposes, assume the proof is valid

        // Get the bridge configuration for the destination L2 network
        BridgeConfig memory config = bridgeConfigs[msg.sender];
        require(config.l2ChainId == request.l2ChainId, "Invalid bridge configuration");

        // Unlock the tokens on the destination L2 network
        IERC20(request.token).safeTransfer(request.to, request.amount);

        // Mark the transfer request as executed
        transferRequests[_requestId].executed = true;

        // Emit the transfer executed event
        emit TransferExecuted(_requestId);
    }

    /**
     * @dev Fails a transfer request
     * @param _requestId The ID of the transfer request
     * @param _reason The reason for failing the transfer request
     */
    function failTransfer(bytes32 _requestId, string memory _reason) external nonReentrant {
        // Get the transfer request
        TransferRequest memory request = transferRequests[_requestId];
        require(request.from != address(0), "Transfer request not found");
        require(!request.executed && !request.failed, "Transfer request already executed or failed");

        // Mark the transfer request as failed
        transferRequests[_requestId].failed = true;

        // Emit the transfer failed event
        emit TransferFailed(_requestId, _reason);

        // Refund the tokens to the sender
        IERC20(request.token).safeTransfer(request.from, request.amount);
    }
}
```
