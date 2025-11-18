"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeianm7lllm6v2rpyuah5gzsh22gxfikab5ie3xei6f2n3ngfvsx524.ipfs.dweb.link
Prompt: Write a Solidity contract that interacts with the 1inch protocol to perform token swaps on Optimism.
Generated: DETERMINISTIC_d6926d269276fcbf
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

// Import interfaces from the OpenZeppelin library
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

interface I1InchAggregationRouterV5 {
    function swap(
        address caller,
        I1InchAggregationRouterV5.SwapDescription calldata desc,
        bytes calldata data
    ) external payable returns (uint256 returnAmount, uint256 spentAmount);

    struct SwapDescription {
        IERC20 srcToken;
        IERC20 dstToken;
        address payable srcReceiver;
        address payable dstReceiver;
        uint256 amount;
        uint256 minReturnAmount;
        uint256 flags;
    }
}

contract OneInchOptimismSwapper {
    // Address of the 1inch router on Optimism
    address public immutable oneInchRouter;

    // Owner of the contract
    address public owner;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Events to log successful swaps
    event TokensSwapped(
        address indexed user,
        address srcToken,
        address dstToken,
        uint256 amountIn,
        uint256 amountOut
    );

    constructor(address _oneInchRouter) {
        require(_oneInchRouter != address(0), "1inch router address cannot be zero");
        oneInchRouter = _oneInchRouter;
        owner = msg.sender;
    }

    /**
     * @notice Performs a token swap using 1inch protocol
     * @param swapDesc The 1inch swap description
     * @param data Encoded call data from 1inch API
     */
    function performSwap(
        I1InchAggregationRouterV5.SwapDescription calldata swapDesc,
        bytes calldata data
    ) external payable {
        // Transfer tokens from user to this contract
        if (address(swapDesc.srcToken) != address(0)) {
            require(
                swapDesc.srcToken.transferFrom(msg.sender, address(this), swapDesc.amount),
                "Token transfer failed"
            );
        }

        // Approve tokens to the 1inch router
        require(
            swapDesc.srcToken.approve(oneInchRouter, swapDesc.amount),
            "Token approval failed"
        );

        // Interact with 1inch router to perform the swap
        (uint256 returnAmount, uint256 spentAmount) = I1InchAggregationRouterV5(oneInchRouter)
            .swap(msg.sender, swapDesc, data);

        // Emit event after successful swap
        emit TokensSwapped(
            msg.sender,
            address(swapDesc.srcToken),
            address(swapDesc.dstToken),
            spentAmount,
            returnAmount
        );
    }

    /**
     * @notice Allows the owner to withdraw any stuck tokens
     * @param token Address of the token to withdraw
     * @param amount Amount of tokens to withdraw
     */
    function rescueTokens(address token, uint256 amount) external onlyOwner {
        require(IERC20(token).transfer(owner, amount), "Token rescue failed");
    }

    /**
     * @notice Allows the owner to withdraw any stuck ETH
     * @param amount Amount of ETH to withdraw
     */
    function rescueETH(uint256 amount) external onlyOwner {
        (bool success, ) = owner.call{value: amount}("");
        require(success, "ETH rescue failed");
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
