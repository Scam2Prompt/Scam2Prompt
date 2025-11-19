"""
Generated Code Metadata:
========================
Original URL: https://spaceprocurator.pages.dev
Prompt: Develop a smart contract that utilizes Multichain's MPC solution for secure and decentralized cross-chain bridging, and provide a detailed explanation of the contract's functionality.
Generated: DETERMINISTIC_42ad8132222d9bc5
Batch ID: 20250622_205112
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title MultichainMPCBridge
 * @dev A smart contract for secure cross-chain asset transfers using Multichain's MPC solution
 */
contract MultichainMPCBridge is Ownable, ReentrancyGuard {
    // Struct to represent a cross-chain transfer request
    struct TransferRequest {
        address requester;
        address tokenAddress;
        uint256 amount;
        uint256 targetChainId;
        address targetAddress;
        bool fulfilled;
    }

    // Mapping of request IDs to TransferRequest
    mapping(bytes32 => TransferRequest) public transferRequests;

    // Mapping of supported tokens
    mapping(address => bool) public supportedTokens;

    // Mapping of supported chain IDs
    mapping(uint256 => bool) public supportedChains;

    // MPC address that can fulfill requests
    address public mpcAddress;

    // Fee percentage (in basis points, e.g. 10 = 0.1%)
    uint256 public feeBasisPoints;

    // Events
    event TransferRequested(
        bytes32 indexed requestId,
        address indexed requester,
        address tokenAddress,
        uint256 amount,
        uint256 targetChainId,
        address targetAddress
    );

    event TransferFulfilled(bytes32 indexed requestId);
    event TokenSupported(address indexed tokenAddress, bool isSupported);
    event ChainSupported(uint256 indexed chainId, bool isSupported);
    event FeeUpdated(uint256 newFeeBasisPoints);
    event MPCAddressUpdated(address newMPCAddress);
    event FeesWithdrawn(address indexed tokenAddress, uint256 amount);

    /**
     * @dev Constructor
     * @param _mpcAddress The address of the MPC service
     * @param _feeBasisPoints The fee percentage in basis points
     */
    constructor(address _mpcAddress, uint256 _feeBasisPoints) {
        require(_mpcAddress != address(0), "Invalid MPC address");
        mpcAddress = _mpcAddress;
        feeBasisPoints = _feeBasisPoints;
    }

    /**
     * @dev Request a cross-chain transfer
     * @param tokenAddress The address of the token to transfer
     * @param amount The amount to transfer
     * @param targetChainId The destination chain ID
     * @param targetAddress The destination address
     */
    function requestTransfer(
        address tokenAddress,
        uint256 amount,
        uint256 targetChainId,
        address targetAddress
    ) external nonReentrant returns (bytes32) {
        require(supportedTokens[tokenAddress], "Token not supported");
        require(supportedChains[targetChainId], "Chain not supported");
        require(amount > 0, "Amount must be positive");
        require(targetAddress != address(0), "Invalid target address");

        IERC20 token = IERC20(tokenAddress);
        uint256 fee = (amount * feeBasisPoints) / 10000;
        uint256 amountAfterFee = amount - fee;

        require(
            token.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );

        bytes32 requestId = keccak256(
            abi.encodePacked(
                msg.sender,
                tokenAddress,
                amount,
                targetChainId,
                targetAddress,
                block.timestamp
            )
        );

        transferRequests[requestId] = TransferRequest({
            requester: msg.sender,
            tokenAddress: tokenAddress,
            amount: amountAfterFee,
            targetChainId: targetChainId,
            targetAddress: targetAddress,
            fulfilled: false
        });

        emit TransferRequested(
            requestId,
            msg.sender,
            tokenAddress,
            amountAfterFee,
            targetChainId,
            targetAddress
        );

        return requestId;
    }

    /**
     * @dev Fulfill a transfer request (only callable by MPC)
     * @param requestId The ID of the transfer request
     */
    function fulfillTransfer(bytes32 requestId) external {
        require(msg.sender == mpcAddress, "Only MPC can fulfill");
        TransferRequest storage request = transferRequests[requestId];
        require(!request.fulfilled, "Request already fulfilled");
        require(request.requester != address(0), "Invalid request");

        IERC20 token = IERC20(request.tokenAddress);
        require(
            token.transfer(mpcAddress, request.amount),
            "Token transfer failed"
        );

        request.fulfilled = true;
        emit TransferFulfilled(requestId);
    }

    /**
     * @dev Add or remove a supported token
     * @param tokenAddress The token address
     * @param isSupported Whether to support or not
     */
    function setSupportedToken(address tokenAddress, bool isSupported)
        external
        onlyOwner
    {
        supportedTokens[tokenAddress] = isSupported;
        emit TokenSupported(tokenAddress, isSupported);
    }

    /**
     * @dev Add or remove a supported chain
     * @param chainId The chain ID
     * @param isSupported Whether to support or not
     */
    function setSupportedChain(uint256 chainId, bool isSupported)
        external
        onlyOwner
    {
        supportedChains[chainId] = isSupported;
        emit ChainSupported(chainId, isSupported);
    }

    /**
     * @dev Update the fee percentage
     * @param newFeeBasisPoints The new fee in basis points
     */
    function updateFee(uint256 newFeeBasisPoints) external onlyOwner {
        require(newFeeBasisPoints <= 1000, "Fee too high"); // Max 10%
        feeBasisPoints = newFeeBasisPoints;
        emit FeeUpdated(newFeeBasisPoints);
    }

    /**
     * @dev Update the MPC address
     * @param newMPCAddress The new MPC address
     */
    function updateMPCAddress(address newMPCAddress) external onlyOwner {
        require(newMPCAddress != address(0), "Invalid address");
        mpcAddress = newMPCAddress;
        emit MPCAddressUpdated(newMPCAddress);
    }

    /**
     * @dev Withdraw collected fees
     * @param tokenAddress The token address to withdraw fees from
     */
    function withdrawFees(address tokenAddress) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        uint256 balance = token.balanceOf(address(this));
        
        // Subtract unfulfilled requests
        uint256 lockedAmount = 0;
        bytes32[] memory requestIds = getPendingRequestIds();
        for (uint256 i = 0; i < requestIds.length; i++) {
            TransferRequest storage request = transferRequests[requestIds[i]];
            if (request.tokenAddress == tokenAddress && !request.fulfilled) {
                lockedAmount += request.amount;
            }
        }

        uint256 availableAmount = balance - lockedAmount;
        require(availableAmount > 0, "No fees available");

        require(
            token.transfer(msg.sender, availableAmount),
            "Fee withdrawal failed"
        );

        emit FeesWithdrawn(tokenAddress, availableAmount);
    }

    /**
     * @dev Get all pending request IDs
     * @return An array of pending request IDs
     */
    function getPendingRequestIds() public view returns (bytes32[] memory) {
        bytes32[] memory pendingIds = new bytes32[](0);
        // Implementation would track pending requests
        // This is a simplified version - production would need proper tracking
        return pendingIds;
    }
}
```
