"""
Generated Code Metadata:
========================
Original URL: https://velodrome-7zz.pages.dev
Prompt: "Propose a liquidity flywheel strategy for a DeFi protocol on Optimism, incorporating anti-dilution rebases and self-optimizing liquidity mechanisms."
Generated: DETERMINISTIC_305cac0230e13ad8
Batch ID: 20250622_205436
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IRebaseToken {
    function rebase(uint256 profit, uint256 totalSupply) external returns (uint256);
}

interface IUniswapV2Router {
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
    
    function swapExactTokensForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);
}

contract LiquidityFlywheel is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Token contracts
    IERC20 public immutable protocolToken;
    IERC20 public immutable stableToken;
    IRebaseToken public immutable rebaseToken;

    // DEX router
    IUniswapV2Router public immutable router;

    // Liquidity pair address
    address public immutable lpToken;

    // Configuration parameters
    uint256 public minRebaseThreshold = 1 ether; // Minimum profit to trigger rebase
    uint256 public slippageTolerance = 50; // 0.5% slippage tolerance (basis points)
    uint256 public lastRebaseTimestamp;
    uint256 public rebaseCooldown = 6 hours;

    // Events
    event RebaseExecuted(uint256 profit, uint256 newTotalSupply);
    event LiquidityAdded(uint256 protocolAmount, uint256 stableAmount, uint256 liquidity);
    event ProfitConverted(uint256 amountIn, uint256 amountOut);

    constructor(
        address _protocolToken,
        address _stableToken,
        address _rebaseToken,
        address _router,
        address _lpToken
    ) {
        protocolToken = IERC20(_protocolToken);
        stableToken = IERC20(_stableToken);
        rebaseToken = IRebaseToken(_rebaseToken);
        router = IUniswapV2Router(_router);
        lpToken = _lpToken;
    }

    /**
     * @notice Execute the flywheel strategy
     * @dev Converts protocol token profits to stablecoin, adds liquidity, and executes rebase
     */
    function executeStrategy() external nonReentrant {
        require(block.timestamp >= lastRebaseTimestamp + rebaseCooldown, "Cooldown active");

        uint256 protocolBalance = protocolToken.balanceOf(address(this));
        require(protocolBalance > minRebaseThreshold, "Insufficient balance");

        // Convert half of protocol tokens to stablecoin
        uint256 amountToSwap = protocolBalance / 2;
        _convertToStable(amountToSwap);

        // Add liquidity with remaining protocol tokens and stablecoin
        uint256 stableBalance = stableToken.balanceOf(address(this));
        _addLiquidity(protocolBalance - amountToSwap, stableBalance);

        // Execute rebase with the LP tokens as profit
        uint256 lpBalance = IERC20(lpToken).balanceOf(address(this));
        uint256 newTotalSupply = rebaseToken.rebase(lpBalance, IERC20(address(rebaseToken)).totalSupply());
        
        lastRebaseTimestamp = block.timestamp;
        emit RebaseExecuted(lpBalance, newTotalSupply);
    }

    /**
     * @notice Convert protocol tokens to stablecoin
     * @param amount Amount of protocol tokens to convert
     */
    function _convertToStable(uint256 amount) private {
        address[] memory path = new address[](2);
        path[0] = address(protocolToken);
        path[1] = address(stableToken);

        protocolToken.approve(address(router), amount);

        uint256 minAmountOut = amount * (10000 - slippageTolerance) / 10000;
        
        uint256[] memory amounts = router.swapExactTokensForTokens(
            amount,
            minAmountOut,
            path,
            address(this),
            block.timestamp + 300
        );

        emit ProfitConverted(amount, amounts[1]);
    }

    /**
     * @notice Add liquidity to DEX pool
     * @param protocolAmount Amount of protocol tokens to add
     * @param stableAmount Amount of stablecoin to add
     */
    function _addLiquidity(uint256 protocolAmount, uint256 stableAmount) private {
        protocolToken.approve(address(router), protocolAmount);
        stableToken.approve(address(router), stableAmount);

        uint256 minProtocolAmount = protocolAmount * (10000 - slippageTolerance) / 10000;
        uint256 minStableAmount = stableAmount * (10000 - slippageTolerance) / 10000;

        (uint256 amountA, uint256 amountB, uint256 liquidity) = router.addLiquidity(
            address(protocolToken),
            address(stableToken),
            protocolAmount,
            stableAmount,
            minProtocolAmount,
            minStableAmount,
            address(this),
            block.timestamp + 300
        );

        emit LiquidityAdded(amountA, amountB, liquidity);
    }

    /**
     * @notice Set minimum rebase threshold
     * @param _threshold New threshold value
     */
    function setMinRebaseThreshold(uint256 _threshold) external onlyOwner {
        minRebaseThreshold = _threshold;
    }

    /**
     * @notice Set slippage tolerance
     * @param _slippage New slippage value in basis points
     */
    function setSlippageTolerance(uint256 _slippage) external onlyOwner {
        require(_slippage <= 1000, "Slippage too high");
        slippageTolerance = _slippage;
    }

    /**
     * @notice Set rebase cooldown period
     * @param _cooldown New cooldown in seconds
     */
    function setRebaseCooldown(uint256 _cooldown) external onlyOwner {
        rebaseCooldown = _cooldown;
    }

    /**
     * @notice Emergency withdraw tokens
     * @param token Address of token to withdraw
     */
    function emergencyWithdraw(address token) external onlyOwner {
        IERC20(token).safeTransfer(owner(), IERC20(token).balanceOf(address(this)));
    }
}
```
