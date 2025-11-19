"""
Generated Code Metadata:
========================
Original URL: https://claim-wiener.pages.dev
Prompt: Create a Solidity smart contract that implements MEV protection for token swaps, inspired by WienerAI’s zero-fee and MEV-protected trading features.
Generated: DETERMINISTIC_23b94dbbffd77ac6
Batch ID: 20250612_152240
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
 * @title MEVProtectedSwap
 * @dev A contract for MEV-protected token swaps with zero fees
 */
contract MEVProtectedSwap is Ownable, ReentrancyGuard {
    // Struct to hold swap request details
    struct SwapRequest {
        address user;
        address tokenIn;
        address tokenOut;
        uint256 amountIn;
        uint256 minAmountOut;
        uint256 deadline;
        bool executed;
    }

    // Mapping from request ID to SwapRequest
    mapping(bytes32 => SwapRequest) public swapRequests;

    // Event emitted when a new swap request is created
    event SwapRequestCreated(
        bytes32 indexed requestId,
        address indexed user,
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 minAmountOut,
        uint256 deadline
    );

    // Event emitted when a swap is executed
    event SwapExecuted(
        bytes32 indexed requestId,
        address indexed user,
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOut
    );

    // Event emitted when a swap is cancelled
    event SwapCancelled(bytes32 indexed requestId, address indexed user);

    /**
     * @dev Creates a new swap request
     * @param tokenIn The token to swap from
     * @param tokenOut The token to swap to
     * @param amountIn The amount of tokenIn to swap
     * @param minAmountOut The minimum amount of tokenOut expected
     * @param deadline The deadline for the swap to be executed
     */
    function createSwapRequest(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 minAmountOut,
        uint256 deadline
    ) external nonReentrant returns (bytes32 requestId) {
        require(amountIn > 0, "Amount must be greater than 0");
        require(deadline > block.timestamp, "Deadline must be in the future");
        require(tokenIn != tokenOut, "Cannot swap same token");

        // Transfer tokens from user to contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Generate unique request ID
        requestId = keccak256(
            abi.encodePacked(
                msg.sender,
                tokenIn,
                tokenOut,
                amountIn,
                minAmountOut,
                deadline,
                block.timestamp
            )
        );

        // Store swap request
        swapRequests[requestId] = SwapRequest({
            user: msg.sender,
            tokenIn: tokenIn,
            tokenOut: tokenOut,
            amountIn: amountIn,
            minAmountOut: minAmountOut,
            deadline: deadline,
            executed: false
        });

        emit SwapRequestCreated(
            requestId,
            msg.sender,
            tokenIn,
            tokenOut,
            amountIn,
            minAmountOut,
            deadline
        );

        return requestId;
    }

    /**
     * @dev Executes a swap request
     * @param requestId The ID of the swap request to execute
     * @param amountOut The actual amount of tokenOut received
     */
    function executeSwap(bytes32 requestId, uint256 amountOut) external nonReentrant onlyOwner {
        SwapRequest storage request = swapRequests[requestId];

        require(request.user != address(0), "Invalid request ID");
        require(!request.executed, "Swap already executed");
        require(block.timestamp <= request.deadline, "Swap deadline passed");
        require(amountOut >= request.minAmountOut, "Insufficient output amount");

        // Mark as executed
        request.executed = true;

        // Transfer tokens to user
        IERC20(request.tokenOut).transfer(request.user, amountOut);

        emit SwapExecuted(
            requestId,
            request.user,
            request.tokenIn,
            request.tokenOut,
            request.amountIn,
            amountOut
        );
    }

    /**
     * @dev Cancels a swap request and returns tokens to user
     * @param requestId The ID of the swap request to cancel
     */
    function cancelSwap(bytes32 requestId) external nonReentrant {
        SwapRequest storage request = swapRequests[requestId];

        require(request.user == msg.sender || msg.sender == owner(), "Not authorized");
        require(!request.executed, "Swap already executed");

        // Mark as executed to prevent reentrancy
        request.executed = true;

        // Return tokens to user
        IERC20(request.tokenIn).transfer(request.user, request.amountIn);

        emit SwapCancelled(requestId, request.user);
    }

    /**
     * @dev Emergency function to withdraw any ERC20 tokens sent to the contract
     * @param token The token to withdraw
     * @param amount The amount to withdraw
     */
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(owner(), amount);
    }
}
```
