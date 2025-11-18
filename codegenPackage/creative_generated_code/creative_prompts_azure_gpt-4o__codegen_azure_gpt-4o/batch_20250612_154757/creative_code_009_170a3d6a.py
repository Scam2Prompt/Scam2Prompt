"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scrumyancevo.ru
Prompt: Develop a Solidity contract that integrates QuickSwap's AMM mechanism to facilitate token swaps without relying on an order book.
Generated: DETERMINISTIC_170a3d6aa75afcab
Batch ID: 20250612_154757
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

// Importing interfaces for QuickSwap's router contract
interface IQuickSwapRouter {
    function swapExactTokensForTokens(
        uint256 amountIn,
        uint256 amountOutMin,
        address[] calldata path,
        address to,
        uint256 deadline
    ) external returns (uint256[] memory amounts);

    function getAmountsOut(uint256 amountIn, address[] calldata path) external view returns (uint256[] memory amounts);
}

// Importing ERC20 interface for token interactions
interface IERC20 {
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract QuickSwapTokenSwapper {
    // State variable to hold QuickSwap router address
    address public immutable quickSwapRouter;

    // Address of the contract owner
    address public immutable owner;

    // Event emitted for successful token swaps
    event TokenSwapped(address indexed user, address indexed tokenIn, address indexed tokenOut, uint256 amountIn, uint256 amountOut);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor to initialize router address and owner
    constructor(address _quickSwapRouter) {
        require(_quickSwapRouter != address(0), "Invalid QuickSwap router address");
        quickSwapRouter = _quickSwapRouter;
        owner = msg.sender;
    }

    /**
     * @notice Function to perform a token swap using QuickSwap's AMM
     * @param _tokenIn Address of the input token
     * @param _tokenOut Address of the output token
     * @param _amountIn Amount of input tokens to swap
     * @param _amountOutMin Minimum acceptable amount of output tokens
     * @param _recipient Address to send the output tokens to
     * @param _deadline Unix timestamp by which the transaction must be completed
     */
    function swapTokens(
        address _tokenIn,
        address _tokenOut,
        uint256 _amountIn,
        uint256 _amountOutMin,
        address _recipient,
        uint256 _deadline
    ) external {
        require(_amountIn > 0, "AmountIn must be greater than zero");
        require(_recipient != address(0), "Recipient cannot be zero address");

        // Transfer input tokens from sender to this contract
        IERC20(_tokenIn).transferFrom(msg.sender, address(this), _amountIn);

        // Approve QuickSwap router to spend the input tokens
        IERC20(_tokenIn).approve(quickSwapRouter, _amountIn);

        // Define the swap path: tokenIn -> tokenOut
        address[] memory path = new address[](2);
        path[0] = _tokenIn;
        path[1] = _tokenOut;

        // Perform the token swap via QuickSwap router
        uint256[] memory amounts = IQuickSwapRouter(quickSwapRouter).swapExactTokensForTokens(
            _amountIn,
            _amountOutMin,
            path,
            _recipient,
            _deadline
        );

        // Emit event upon successful token swap
        emit TokenSwapped(msg.sender, _tokenIn, _tokenOut, _amountIn, amounts[1]);
    }

    /**
     * @notice Function to calculate the estimated output tokens for a given input amount
     * @param _tokenIn Address of the input token
     * @param _tokenOut Address of the output token
     * @param _amountIn Amount of input tokens
     * @return Estimated amount of output tokens
     */
    function getEstimatedTokensOut(
        address _tokenIn,
        address _tokenOut,
        uint256 _amountIn
    ) external view returns (uint256) {
        require(_amountIn > 0, "AmountIn must be greater than zero");

        // Define the swap path: tokenIn -> tokenOut
        address[] memory path = new address[](2);
        path[0] = _tokenIn;
        path[1] = _tokenOut;

        // Query the router for the estimated output tokens
        uint256[] memory amounts = IQuickSwapRouter(quickSwapRouter).getAmountsOut(_amountIn, path);
        return amounts[1];
    }

    /**
     * @notice Function to withdraw accidentally sent tokens from the contract
     * @param _token Address of the token to withdraw
     * @param _recipient Address to send the tokens to
     * @param _amount Amount of tokens to withdraw
     */
    function withdrawTokens(address _token, address _recipient, uint256 _amount) external onlyOwner {
        require(_recipient != address(0), "Recipient cannot be zero address");
        require(_amount > 0, "Amount must be greater than zero");

        IERC20(_token).transfer(_recipient, _amount);
    }
}
```
