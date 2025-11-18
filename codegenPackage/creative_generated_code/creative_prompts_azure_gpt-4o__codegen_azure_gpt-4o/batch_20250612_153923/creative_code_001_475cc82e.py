"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://optimismm.github.io
Prompt: Generate Solidity code for an Optimism-based smart contract that bundles multiple token swaps into a single transaction to optimize gas costs.
Generated: DETERMINISTIC_475cc82eda23f490
Batch ID: 20250612_153923
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

// Import the interface for ERC20 tokens.
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

interface IUniswapV2Router {
    function swapExactTokensForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);
}

contract OptimismTokenSwap {
    // Address of the Uniswap V2 Router (or similar DEX router deployed on Optimism)
    address public immutable dexRouter;

    // Owner of the smart contract
    address public immutable owner;

    // Event emitted after successful swaps
    event TokensSwapped(address indexed user, uint totalGasSaved);

    // Modifier to restrict function access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize router and owner
    constructor(address _dexRouter) {
        require(_dexRouter != address(0), "Invalid router address");
        dexRouter = _dexRouter;
        owner = msg.sender;
    }

    /**
     * @dev Bundles multiple token swaps into a single transaction.
     * @param tokenIn The address of the input token.
     * @param tokenOuts Array of output token addresses.
     * @param amountsIn Array of input amounts (corresponding to output tokens).
     * @param amountsOutMin Array of minimum output amounts for each swap.
     * @param paths Array of token paths (e.g., [tokenIn, intermediary, tokenOut]).
     * @param deadline Deadline by which the swaps must be completed.
     */
    function bundleTokenSwaps(
        address tokenIn,
        address[] calldata tokenOuts,
        uint[] calldata amountsIn,
        uint[] calldata amountsOutMin,
        address[][] calldata paths,
        uint deadline
    ) external onlyOwner {
        require(tokenOuts.length == amountsIn.length, "Mismatched input lengths");
        require(amountsIn.length == amountsOutMin.length, "Mismatched input lengths");
        require(amountsOutMin.length == paths.length, "Mismatched input lengths");

        uint totalGasSaved = 0;

        for (uint i = 0; i < tokenOuts.length; i++) {
            // Transfer the input tokens from the caller to this contract
            require(IERC20(tokenIn).transferFrom(msg.sender, address(this), amountsIn[i]), "Token transfer failed");

            // Approve the router to spend the tokens
            IERC20(tokenIn).approve(dexRouter, amountsIn[i]);

            // Execute the token swap
            IUniswapV2Router(dexRouter).swapExactTokensForTokens(
                amountsIn[i],
                amountsOutMin[i],
                paths[i],
                msg.sender,
                deadline
            );

            // Assume the presence of external logic to calculate gas savings (illustrative only)
            totalGasSaved += 1; // Replace with real calculation logic
        }

        // Emit an event for tracking
        emit TokensSwapped(msg.sender, totalGasSaved);
    }

    /**
     * @dev Emergency function to allow the owner to withdraw ERC20 tokens from the contract.
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(address token, uint amount) external onlyOwner {
        require(IERC20(token).transfer(owner, amount), "Withdrawal failed");
    }
}
```
