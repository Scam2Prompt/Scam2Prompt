"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-git-sharedswaptestliobranch-uniswap.vercel.app
Prompt: Write a smart contract in Solidity to interact with the Uniswap protocol for automated token swaps.
Generated: DETERMINISTIC_3675f86860a31da5
Batch ID: 20250612_153821
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

// Importing interfaces from Uniswap
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@uniswap/v2-core/contracts/interfaces/IERC20.sol";

contract TokenSwap {
    // State variables
    address public owner; // Contract owner
    IUniswapV2Router02 public immutable uniswapRouter; // Instance of Uniswap Router

    // Event for logging successful swaps
    event TokensSwapped(
        address indexed sender,
        address indexed tokenIn,
        address indexed tokenOut,
        uint amountIn,
        uint amountOut
    );

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Not contract owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _uniswapRouter) {
        require(_uniswapRouter != address(0), "Invalid router address");
        owner = msg.sender; // Set contract deployer as the owner
        uniswapRouter = IUniswapV2Router02(_uniswapRouter); // Set the Uniswap router instance
    }

    // Function to approve token spending
    function approveToken(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        IERC20(token).approve(address(uniswapRouter), amount);
    }

    /**
     * @dev Swap tokens using Uniswap protocol
     * @param tokenIn The address of the token to swap from
     * @param tokenOut The address of the token to swap to
     * @param amountIn The amount of tokenIn to swap
     * @param amountOutMin Minimum amount of tokenOut expected
     * @param recipient Recipient address for swapped tokens
     */
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint amountIn,
        uint amountOutMin,
        address recipient
    ) external {
        require(tokenIn != address(0) && tokenOut != address(0), "Invalid token address");
        require(amountIn > 0, "AmountIn must be greater than 0");
        require(recipient != address(0), "Invalid recipient address");

        // Transfer tokens from sender to this contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Approve Uniswap router to spend tokens
        IERC20(tokenIn).approve(address(uniswapRouter), amountIn);

        // Define the path for swapping (tokenIn -> tokenOut)
        address[] memory path = new address[](2);
        path[0] = tokenIn;
        path[1] = tokenOut;

        // Perform the swap using Uniswap router
        try uniswapRouter.swapExactTokensForTokens(
            amountIn, 
            amountOutMin, 
            path, 
            recipient, 
            block.timestamp
        ) returns (uint[] memory amounts) {
            emit TokensSwapped(msg.sender, tokenIn, tokenOut, amountIn, amounts[1]); // Log successful swap
        } catch {
            revert("Token swap failed"); // Handle swap failure
        }
    }

    // Function to withdraw any tokens accidentally sent to the contract
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        IERC20(token).transfer(owner, amount);
    }

    // Function to transfer ownership of the contract
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        owner = newOwner;
    }
}
```

### Additional Notes
- Make sure to install the Uniswap dependencies (`@uniswap/v2-periphery` and `@uniswap/v2-core`) in your project to compile and deploy the contract successfully.
- Test the contract thoroughly before deploying it to the production Ethereum network.
