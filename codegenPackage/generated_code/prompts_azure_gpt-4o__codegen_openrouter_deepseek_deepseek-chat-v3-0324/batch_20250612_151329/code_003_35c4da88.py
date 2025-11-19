"""
Generated Code Metadata:
========================
Original URL: https://fffrfh.pages.dev
Prompt: Write a detailed explanation of how Protocol Owned Liquidity (PoL) is implemented in the Morpheus ecosystem, and provide a code example of a smart contract function that uses stETH yield to buy back MOR tokens and add liquidity to Uniswap.
Generated: DETERMINISTIC_35c4da884d473f90
Batch ID: 20250612_151329
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
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

/**
 * @title MorpheusPoLManager
 * @dev Manages Protocol Owned Liquidity (PoL) for the Morpheus ecosystem
 * - Uses stETH yield to buy back MOR tokens
 * - Adds liquidity to Uniswap MOR/ETH pair
 */
contract MorpheusPoLManager {
    using SafeERC20 for IERC20;

    // Token addresses
    IERC20 public immutable stETH;
    IERC20 public immutable MOR;
    IERC20 public immutable lpToken;

    // Uniswap Router
    IUniswapV2Router02 public immutable uniswapRouter;

    // Address to receive leftover stETH (if any)
    address public treasury;

    // Events
    event BuybackAndLiquidityAdded(
        uint256 stETHAmount,
        uint256 morBought,
        uint256 ethAdded,
        uint256 liquidityAdded
    );

    /**
     * @dev Constructor
     * @param _stETH Address of stETH token
     * @param _mor Address of MOR token
     * @param _lpToken Address of Uniswap LP token (MOR/ETH pair)
     * @param _uniswapRouter Address of Uniswap V2 Router
     * @param _treasury Treasury address
     */
    constructor(
        address _stETH,
        address _mor,
        address _lpToken,
        address _uniswapRouter,
        address _treasury
    ) {
        require(_stETH != address(0), "Invalid stETH address");
        require(_mor != address(0), "Invalid MOR address");
        require(_lpToken != address(0), "Invalid LP token address");
        require(_uniswapRouter != address(0), "Invalid Uniswap router");
        require(_treasury != address(0), "Invalid treasury address");

        stETH = IERC20(_stETH);
        MOR = IERC20(_mor);
        lpToken = IERC20(_lpToken);
        uniswapRouter = IUniswapV2Router02(_uniswapRouter);
        treasury = _treasury;
    }

    /**
     * @dev Executes the PoL strategy:
     * 1. Converts stETH to ETH via Uniswap
     * 2. Uses half the ETH to buy MOR tokens
     * 3. Adds the other half ETH and bought MOR as liquidity
     * @param amount The amount of stETH to use for the operation
     */
    function executePoL(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        // Transfer stETH from sender
        stETH.safeTransferFrom(msg.sender, address(this), amount);

        // Approve Uniswap router to spend stETH
        stETH.safeApprove(address(uniswapRouter), amount);

        // Path for stETH -> ETH swap
        address[] memory path = new address[](2);
        path[0] = address(stETH);
        path[1] = uniswapRouter.WETH();

        // Swap stETH for ETH (50% of amount)
        uint256 ethAmount = amount / 2;
        uint256[] memory amounts = uniswapRouter.swapExactTokensForETH(
            ethAmount,
            0, // Accept any amount of ETH
            path,
            address(this),
            block.timestamp + 1 hours
        );

        uint256 ethReceived = amounts[1];
        require(ethReceived > 0, "Received 0 ETH from swap");

        // Path for ETH -> MOR swap
        address[] memory morPath = new address[](2);
        morPath[0] = uniswapRouter.WETH();
        morPath[1] = address(MOR);

        // Swap ETH for MOR tokens
        uint256[] memory morAmounts = uniswapRouter.swapExactETHForTokens{value: ethReceived}(
            0, // Accept any amount of MOR
            morPath,
            address(this),
            block.timestamp + 1 hours
        );

        uint256 morBought = morAmounts[1];
        require(morBought > 0, "Received 0 MOR from swap");

        // Approve Uniswap router to spend MOR
        MOR.safeApprove(address(uniswapRouter), morBought);

        // Add liquidity with remaining ETH and MOR
        (uint256 ethUsed, uint256 morUsed, uint256 liquidity) = uniswapRouter.addLiquidityETH{value: address(this).balance}(
            address(MOR),
            morBought,
            0, // Accept any amount of MOR
            0, // Accept any amount of ETH
            address(this),
            block.timestamp + 1 hours
        );

        // Send any remaining stETH to treasury
        uint256 remainingStETH = stETH.balanceOf(address(this));
        if (remainingStETH > 0) {
            stETH.safeTransfer(treasury, remainingStETH);
        }

        emit BuybackAndLiquidityAdded(amount, morBought, ethUsed, liquidity);
    }

    // Allow contract to receive ETH
    receive() external payable {}
}
```
