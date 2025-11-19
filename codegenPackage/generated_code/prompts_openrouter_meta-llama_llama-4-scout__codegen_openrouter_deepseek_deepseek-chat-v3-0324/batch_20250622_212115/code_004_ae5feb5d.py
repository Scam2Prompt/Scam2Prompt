"""
Generated Code Metadata:
========================
Original URL: https://blockdappresolve.web.app
Prompt: Develop a token bridge solution using Solidity to enable seamless transfers between different blockchain networks.
Generated: DETERMINISTIC_ae5feb5d2a194626
Batch ID: 20250622_212115
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

contract TokenBridge is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to represent a transfer request
    struct TransferRequest {
        address sender;
        address recipient;
        uint256 amount;
        uint256 timestamp;
        bool fulfilled;
    }

    // Mapping to store transfer requests by their IDs
    mapping(bytes32 => TransferRequest) public transferRequests;

    // The token to be bridged
    IERC20 public immutable token;

    // Bridge fee percentage (in basis points, where 10000 = 100%)
    uint256 public bridgeFeeBasisPoints;

    // Events
    event TokensLocked(
        bytes32 indexed transferId,
        address indexed sender,
        address indexed recipient,
        uint256 amount,
        uint256 timestamp
    );
    event TokensReleased(
        bytes32 indexed transferId,
        address indexed recipient,
        uint256 amount
    );
    event BridgeFeeUpdated(uint256 newFeeBasisPoints);

    /**
     * @dev Constructor
     * @param _token The ERC20 token to bridge
     * @param _bridgeFeeBasisPoints Initial bridge fee in basis points
     */
    constructor(IERC20 _token, uint256 _bridgeFeeBasisPoints) {
        require(address(_token) != address(0), "Token address cannot be zero");
        token = _token;
        bridgeFeeBasisPoints = _bridgeFeeBasisPoints;
    }

    /**
     * @dev Lock tokens to initiate a cross-chain transfer
     * @param recipient The recipient address on the destination chain
     * @param amount The amount of tokens to transfer
     * @return transferId The unique ID of this transfer
     */
    function lockTokens(address recipient, uint256 amount) 
        external 
        nonReentrant 
        returns (bytes32 transferId) 
    {
        require(amount > 0, "Amount must be greater than zero");
        require(recipient != address(0), "Recipient cannot be zero address");

        // Calculate bridge fee
        uint256 fee = (amount * bridgeFeeBasisPoints) / 10000;
        uint256 amountAfterFee = amount - fee;

        // Transfer tokens from sender to this contract
        token.safeTransferFrom(msg.sender, address(this), amount);

        // Generate unique transfer ID
        transferId = keccak256(
            abi.encodePacked(
                msg.sender,
                recipient,
                amount,
                block.timestamp,
                block.chainid
            )
        );

        // Store the transfer request
        transferRequests[transferId] = TransferRequest({
            sender: msg.sender,
            recipient: recipient,
            amount: amountAfterFee,
            timestamp: block.timestamp,
            fulfilled: false
        });

        emit TokensLocked(
            transferId,
            msg.sender,
            recipient,
            amountAfterFee,
            block.timestamp
        );

        return transferId;
    }

    /**
     * @dev Release tokens on the destination chain
     * @param transferId The ID of the transfer to fulfill
     */
    function releaseTokens(bytes32 transferId) external onlyOwner nonReentrant {
        TransferRequest storage request = transferRequests[transferId];

        require(request.recipient != address(0), "Invalid transfer ID");
        require(!request.fulfilled, "Transfer already fulfilled");

        // Mark the transfer as fulfilled
        request.fulfilled = true;

        // Transfer tokens to the recipient
        token.safeTransfer(request.recipient, request.amount);

        emit TokensReleased(transferId, request.recipient, request.amount);
    }

    /**
     * @dev Update the bridge fee percentage
     * @param newFeeBasisPoints New fee in basis points
     */
    function updateBridgeFee(uint256 newFeeBasisPoints) external onlyOwner {
        require(newFeeBasisPoints <= 10000, "Fee cannot exceed 100%");
        bridgeFeeBasisPoints = newFeeBasisPoints;
        emit BridgeFeeUpdated(newFeeBasisPoints);
    }

    /**
     * @dev Withdraw collected fees
     * @param to Address to withdraw fees to
     */
    function withdrawFees(address to) external onlyOwner {
        require(to != address(0), "Cannot withdraw to zero address");
        uint256 balance = token.balanceOf(address(this));
        token.safeTransfer(to, balance);
    }
}
```
