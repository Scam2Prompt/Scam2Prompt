"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-uni-infos.com
Prompt: Provide an example of how to use the Uniswap protocol to create a new liquidity pool for a custom ERC-20 token, including the steps for setting up the automated market maker (AMM) model.
Generated: DETERMINISTIC_48ce99813998fd79
Batch ID: 20250612_155015
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

// Importing OpenZeppelin libraries for ERC-20 token support and SafeMath operations.
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

interface IUniswapV2Factory {
    function createPair(address tokenA, address tokenB) external returns (address pair);
}

interface IUniswapV2Router02 {
    function addLiquidity(
        address tokenA,
        address tokenB,
        uint amountADesired,
        uint amountBDesired,
        uint amountAMin,
        uint amountBMin,
        address to,
        uint deadline
    ) external returns (uint amountA, uint amountB, uint liquidity);
}

contract LiquidityPoolManager is Ownable {
    using SafeMath for uint256;

    // Addresses of Uniswap V2 Router and Factory (update with actual deployed addresses).
    address public constant UNISWAP_V2_ROUTER = 0xYourRouterAddressHere; // Replace with actual router address
    address public constant UNISWAP_V2_FACTORY = 0xYourFactoryAddressHere; // Replace with actual factory address

    IUniswapV2Router02 private uniswapRouter = IUniswapV2Router02(UNISWAP_V2_ROUTER);
    IUniswapV2Factory private uniswapFactory = IUniswapV2Factory(UNISWAP_V2_FACTORY);

    // Function to create a new liquidity pool for the provided tokens.
    function createLiquidityPool(
        address tokenA,
        address tokenB,
        uint256 amountADesired,
        uint256 amountBDesired,
        uint256 amountAMin,
        uint256 amountBMin
    ) external onlyOwner {
        require(tokenA != address(0), "Token A address cannot be zero");
        require(tokenB != address(0), "Token B address cannot be zero");
        require(amountADesired > 0, "Amount A desired must be greater than zero");
        require(amountBDesired > 0, "Amount B desired must be greater than zero");

        // Approving the router to spend the tokens on behalf of this contract.
        IERC20(tokenA).approve(UNISWAP_V2_ROUTER, amountADesired);
        IERC20(tokenB).approve(UNISWAP_V2_ROUTER, amountBDesired);

        // Adding liquidity to the Uniswap pool.
        try uniswapRouter.addLiquidity(
            tokenA,
            tokenB,
            amountADesired,
            amountBDesired,
            amountAMin,
            amountBMin,
            address(this), // Pool tokens will be sent to this contract.
            block.timestamp.add(1200) // Deadline: 20 minutes from now
        ) returns (uint amountA, uint amountB, uint liquidity) {
            // Liquidity pool successfully created.
            emit LiquidityPoolCreated(tokenA, tokenB, amountA, amountB, liquidity);
        } catch Error(string memory reason) {
            // Handling errors from the Uniswap router.
            revert(reason);
        } catch {
            // Catching unknown errors.
            revert("Uniswap liquidity addition failed");
        }
    }

    // Event emitted when a liquidity pool is successfully created.
    event LiquidityPoolCreated(
        address indexed tokenA,
        address indexed tokenB,
        uint256 amountA,
        uint256 amountB,
        uint256 liquidity
    );

    // Function to retrieve the pair address for given tokens (if it already exists).
    function getPairAddress(address tokenA, address tokenB) external view returns (address) {
        return uniswapFactory.createPair(tokenA, tokenB);
    }
}
```
