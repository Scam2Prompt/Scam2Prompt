"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimalvara.pages.dev
Prompt: Implement a function in Solidity to integrate the Uniswap V2 Router for buying and selling underlying tokens during the creation and withdrawal of ERC-7621 Basket Tokens.
Generated: DETERMINISTIC_7098329d1e83eeaf
Batch ID: 20250612_154820
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

// Importing necessary libraries and interfaces
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/// @title ERC-7621 Basket Token Integration with Uniswap V2
/// @notice This contract allows buying and selling tokens using Uniswap V2 Router
contract BasketToken is Ownable {
    IUniswapV2Router02 public uniswapRouter;
    address public WETH; // Wrapped ETH address

    // Events for tracking token actions
    event TokensPurchased(address indexed buyer, uint256 amountSpent, uint256 tokensReceived);
    event TokensSold(address indexed seller, uint256 tokensSold, uint256 amountReceived);

    /// @dev Constructor to initialize the Uniswap router and WETH address
    /// @param _router Address of the Uniswap V2 Router
    /// @param _weth Address of the Wrapped Ether token
    constructor(address _router, address _weth) {
        require(_router != address(0), "Invalid Uniswap Router address");
        require(_weth != address(0), "Invalid WETH address");
        
        uniswapRouter = IUniswapV2Router02(_router);
        WETH = _weth;
    }

    /// @notice Buy tokens using ETH via Uniswap
    /// @param tokenAddress Address of the token to purchase
    /// @param amountOutMin Minimum amount of tokens expected
    /// @param deadline Transaction deadline
    /// @dev Requires approval of the Uniswap Router to handle the tokens
    function buyTokens(
        address tokenAddress,
        uint256 amountOutMin,
        uint256 deadline
    ) external payable {
        require(msg.value > 0, "Must send ETH to buy tokens");

        // Creating an array of path for the swap
        address[] memory path = new address[](2);
        path[0] = WETH;
        path[1] = tokenAddress;

        // Performing the swap
        uint256[] memory amounts = uniswapRouter.swapExactETHForTokens{value: msg.value}(
            amountOutMin,
            path,
            msg.sender,
            deadline
        );

        emit TokensPurchased(msg.sender, msg.value, amounts[1]);
    }

    /// @notice Sell tokens for ETH via Uniswap
    /// @param tokenAddress Address of the token to sell
    /// @param tokenAmount Amount of tokens to sell
    /// @param amountOutMin Minimum amount of ETH expected
    /// @param deadline Transaction deadline
    /// @dev Requires the caller to approve the contract to spend tokens
    function sellTokens(
        address tokenAddress,
        uint256 tokenAmount,
        uint256 amountOutMin,
        uint256 deadline
    ) external {
        require(tokenAmount > 0, "Must sell a positive amount of tokens");

        // Transfer the tokens from the sender to the contract
        IERC20(tokenAddress).transferFrom(msg.sender, address(this), tokenAmount);

        // Approve the Uniswap Router to spend the tokens
        IERC20(tokenAddress).approve(address(uniswapRouter), tokenAmount);

        // Creating an array of path for the swap
        address[] memory path = new address[](2);
        path[0] = tokenAddress;
        path[1] = WETH;

        // Performing the swap
        uint256[] memory amounts = uniswapRouter.swapExactTokensForETH(
            tokenAmount,
            amountOutMin,
            path,
            msg.sender,
            deadline
        );

        emit TokensSold(msg.sender, tokenAmount, amounts[1]);
    }

    /// @dev Function to withdraw any ETH from the contract
    function withdrawETH() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");
        payable(owner()).transfer(balance);
    }

    /// @dev Fallback function to receive ETH
    receive() external payable {}
}
```
