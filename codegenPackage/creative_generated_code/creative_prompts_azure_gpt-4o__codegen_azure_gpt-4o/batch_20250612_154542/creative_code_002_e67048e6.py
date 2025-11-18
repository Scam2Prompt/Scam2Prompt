"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w1-poocoin.com
Prompt: Develop a Solidity smart contract that interacts with the PooCoin DEX to swap BEP-20 tokens securely and efficiently.
Generated: DETERMINISTIC_e67048e64743d6ce
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import OpenZeppelin Contracts for security and convenience
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IPooCoinRouter {
    function swapExactTokensForTokens(
        uint256 amountIn,
        uint256 amountOutMin,
        address[] calldata path,
        address to,
        uint256 deadline
    ) external returns (uint256[] memory amounts);
}

contract TokenSwapper is Ownable, ReentrancyGuard {
    // Address of the PooCoin router
    address public immutable pooCoinRouter;

    // Event emitted after a successful swap
    event TokensSwapped(
        address indexed sender,
        address indexed tokenIn,
        address indexed tokenOut,
        uint256 amountIn,
        uint256 amountOut
    );

    constructor(address _pooCoinRouter) {
        require(_pooCoinRouter != address(0), "Invalid router address");
        pooCoinRouter = _pooCoinRouter;
    }

    /**
     * @dev Swap BEP-20 tokens using the PooCoin DEX.
     * @param tokenIn Address of the token to swap from.
     * @param tokenOut Address of the token to swap to.
     * @param amountIn Amount of `tokenIn` to swap.
     * @param amountOutMin Minimum acceptable amount of `tokenOut` (slippage protection).
     * @param deadline Timestamp after which the swap will no longer be valid.
     */
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        uint256 deadline
    ) external nonReentrant {
        require(tokenIn != address(0), "Invalid tokenIn address");
        require(tokenOut != address(0), "Invalid tokenOut address");
        require(amountIn > 0, "Amount must be greater than zero");
        require(deadline > block.timestamp, "Deadline must be in the future");

        // Transfer `tokenIn` from the sender to the contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Approve the PooCoin router to spend `tokenIn`
        IERC20(tokenIn).approve(pooCoinRouter, amountIn);

        // Path for the swap: tokenIn -> tokenOut
        address[] memory path = new address[](2);
        path[0] = tokenIn;
        path[1] = tokenOut;

        // Call the PooCoin router to perform the swap
        uint256[] memory amounts = IPooCoinRouter(pooCoinRouter).swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            msg.sender,
            deadline
        );

        // Emit an event for logging
        emit TokensSwapped(msg.sender, tokenIn, tokenOut, amountIn, amounts[amounts.length - 1]);
    }

    /**
     * @dev Emergency withdrawal function for owner to recover stuck tokens.
     * @param token Address of the token to recover.
     * @param amount Amount of tokens to recover.
     */
    function recoverTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).transfer(owner(), amount);
    }
}
```
