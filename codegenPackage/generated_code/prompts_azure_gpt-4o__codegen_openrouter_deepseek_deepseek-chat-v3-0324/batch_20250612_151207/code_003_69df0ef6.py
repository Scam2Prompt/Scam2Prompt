"""
Generated Code Metadata:
========================
Original URL: https://peipei-buq.pages.dev
Prompt: Generate a Solidity smart contract that facilitates multichain bridging for $PEIPEI tokens, as mentioned in the roadmap phase 3.
Generated: DETERMINISTIC_69df0ef67c00d25d
Batch ID: 20250612_151207
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract PEIPEIBridge is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to store bridge transaction details
    struct BridgeRequest {
        address requester;
        uint256 amount;
        uint256 targetChainId;
        uint256 nonce;
        bool isFulfilled;
    }

    // Mapping to store bridge requests
    mapping(bytes32 => BridgeRequest) public bridgeRequests;

    // Mapping to store supported chain IDs
    mapping(uint256 => bool) public supportedChains;

    // The $PEIPEI token contract
    IERC20 public peipeiToken;

    // Bridge fee percentage (1 = 0.01%)
    uint256 public bridgeFeePercentage;

    // Address to collect bridge fees
    address public feeCollector;

    // Nonce counter for bridge requests
    uint256 public nonceCounter;

    // Events
    event BridgeInitiated(
        address indexed requester,
        uint256 amount,
        uint256 targetChainId,
        bytes32 requestId,
        uint256 feeAmount
    );
    event BridgeCompleted(
        bytes32 indexed requestId,
        address indexed requester,
        uint256 amount,
        uint256 targetChainId
    );
    event ChainSupportUpdated(uint256 chainId, bool isSupported);
    event BridgeFeeUpdated(uint256 newFeePercentage);
    event FeeCollectorUpdated(address newFeeCollector);

    constructor(address _peipeiToken, address _feeCollector) {
        require(_peipeiToken != address(0), "Invalid token address");
        require(_feeCollector != address(0), "Invalid fee collector address");

        peipeiToken = IERC20(_peipeiToken);
        feeCollector = _feeCollector;
        bridgeFeePercentage = 50; // Default 0.5% fee
    }

    /**
     * @dev Initiate a bridge request to another chain
     * @param amount Amount of tokens to bridge
     * @param targetChainId Chain ID of the destination chain
     */
    function initiateBridge(uint256 amount, uint256 targetChainId) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(supportedChains[targetChainId], "Target chain not supported");

        // Calculate bridge fee
        uint256 feeAmount = (amount * bridgeFeePercentage) / 10000;
        uint256 amountAfterFee = amount - feeAmount;

        // Transfer tokens from user to this contract
        peipeiToken.safeTransferFrom(msg.sender, address(this), amount);

        // Transfer fee to fee collector
        if (feeAmount > 0) {
            peipeiToken.safeTransfer(feeCollector, feeAmount);
        }

        // Create bridge request
        bytes32 requestId = keccak256(
            abi.encodePacked(
                msg.sender,
                amount,
                targetChainId,
                nonceCounter,
                block.chainid,
                block.timestamp
            )
        );

        bridgeRequests[requestId] = BridgeRequest({
            requester: msg.sender,
            amount: amountAfterFee,
            targetChainId: targetChainId,
            nonce: nonceCounter,
            isFulfilled: false
        });

        nonceCounter++;

        emit BridgeInitiated(msg.sender, amountAfterFee, targetChainId, requestId, feeAmount);
    }

    /**
     * @dev Complete a bridge request (to be called by owner/relayer)
     * @param requestId The ID of the bridge request to complete
     */
    function completeBridge(bytes32 requestId) external onlyOwner nonReentrant {
        BridgeRequest storage request = bridgeRequests[requestId];
        require(request.requester != address(0), "Invalid request ID");
        require(!request.isFulfilled, "Request already fulfilled");

        // Mark request as fulfilled
        request.isFulfilled = true;

        // Transfer tokens to requester
        peipeiToken.safeTransfer(request.requester, request.amount);

        emit BridgeCompleted(requestId, request.requester, request.amount, request.targetChainId);
    }

    /**
     * @dev Add or remove supported chains
     * @param chainId The chain ID to update
     * @param isSupported Whether the chain is supported
     */
    function updateChainSupport(uint256 chainId, bool isSupported) external onlyOwner {
        supportedChains[chainId] = isSupported;
        emit ChainSupportUpdated(chainId, isSupported);
    }

    /**
     * @dev Update the bridge fee percentage
     * @param newFeePercentage New fee percentage (1 = 0.01%)
     */
    function updateBridgeFee(uint256 newFeePercentage) external onlyOwner {
        require(newFeePercentage <= 1000, "Fee cannot exceed 10%");
        bridgeFeePercentage = newFeePercentage;
        emit BridgeFeeUpdated(newFeePercentage);
    }

    /**
     * @dev Update the fee collector address
     * @param newFeeCollector New fee collector address
     */
    function updateFeeCollector(address newFeeCollector) external onlyOwner {
        require(newFeeCollector != address(0), "Invalid fee collector address");
        feeCollector = newFeeCollector;
        emit FeeCollectorUpdated(newFeeCollector);
    }

    /**
     * @dev Emergency withdraw tokens from the contract
     * @param tokenAddress Address of the token to withdraw
     * @param amount Amount to withdraw
     */
    function emergencyWithdraw(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        token.safeTransfer(owner(), amount);
    }
}
```
