"""
Generated Code Metadata:
========================
Original URL: https://across-to.com
Prompt: Implement a smart contract using Solidity that utilizes Across Protocol's optimized routing for cross-chain transactions.
Generated: DETERMINISTIC_1ca21e2fcd5caf5a
Batch ID: 20250622_211853
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

import "@across-protocol/contracts-v2/contracts/interfaces/IAcrossSpokePool.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title CrossChainSender
 * @dev A smart contract that utilizes Across Protocol's optimized routing for cross-chain transactions.
 */
contract CrossChainSender is ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Address of the Across SpokePool contract
    IAcrossSpokePool public immutable spokePool;

    // Chain ID of the destination chain
    uint256 public immutable destinationChainId;

    // Events
    event CrossChainTransferInitiated(
        address indexed sender,
        address indexed recipient,
        address indexed token,
        uint256 amount,
        uint256 destinationChainId,
        uint64 relayerFeePct,
        uint32 depositId
    );

    /**
     * @dev Constructor initializes the contract with Across SpokePool and destination chain ID.
     * @param _spokePool Address of the Across SpokePool contract.
     * @param _destinationChainId Chain ID of the destination chain.
     */
    constructor(address _spokePool, uint256 _destinationChainId) {
        require(_spokePool != address(0), "Invalid SpokePool address");
        require(_destinationChainId != 0, "Invalid chain ID");

        spokePool = IAcrossSpokePool(_spokePool);
        destinationChainId = _destinationChainId;
    }

    /**
     * @dev Initiates a cross-chain transfer using Across Protocol.
     * @param recipient Address of the recipient on the destination chain.
     * @param token Address of the token to transfer.
     * @param amount Amount of tokens to transfer.
     * @param relayerFeePct Percentage fee for the relayer (in 1e18 units).
     * @param quoteTimestamp Timestamp for the quote.
     */
    function sendCrossChain(
        address recipient,
        address token,
        uint256 amount,
        uint64 relayerFeePct,
        uint32 quoteTimestamp
    ) external nonReentrant {
        require(recipient != address(0), "Invalid recipient");
        require(token != address(0), "Invalid token");
        require(amount > 0, "Amount must be > 0");

        // Transfer tokens from sender to this contract
        IERC20(token).safeTransferFrom(msg.sender, address(this), amount);

        // Approve SpokePool to spend tokens
        IERC20(token).safeApprove(address(spokePool), amount);

        // Initiate the deposit
        uint32 depositId = spokePool.deposit(
            recipient,
            token,
            amount,
            destinationChainId,
            relayerFeePct,
            quoteTimestamp
        );

        emit CrossChainTransferInitiated(
            msg.sender,
            recipient,
            token,
            amount,
            destinationChainId,
            relayerFeePct,
            depositId
        );
    }

    /**
     * @dev Emergency function to withdraw tokens stuck in the contract.
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token");
        require(amount > 0, "Amount must be > 0");

        IERC20(token).safeTransfer(msg.sender, amount);
    }

    modifier onlyOwner() {
        require(msg.sender == address(0), "Not authorized"); // Replace with actual owner check
        _;
    }
}
```
