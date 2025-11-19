"""
Generated Code Metadata:
========================
Original URL: https://amlwd.com
Prompt: Provide a step-by-step guide to integrate USDC liquidity pools into a DeFi trading platform, similar to the LP mechanism described for MCDEX on https://amlwd.com.
Generated: DETERMINISTIC_727a4b4cebe86ae2
Batch ID: 20250612_150241
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract USDCLiquidityPool is ReentrancyGuard {
    using SafeERC20 for IERC20;
    using SafeMath for uint256;

    // Token addresses
    IERC20 public immutable usdcToken;
    IERC20 public immutable lpToken;

    // Pool parameters
    uint256 public totalLiquidity;
    uint256 public totalShares;
    uint256 public constant MINIMUM_LIQUIDITY = 10**3;

    // Events
    event LiquidityAdded(address indexed provider, uint256 usdcAmount, uint256 lpAmount);
    event LiquidityRemoved(address indexed provider, uint256 usdcAmount, uint256 lpAmount);
    event Swapped(address indexed trader, uint256 usdcIn, uint256 usdcOut);

    constructor(address _usdcToken, address _lpToken) {
        require(_usdcToken != address(0), "Invalid USDC address");
        require(_lpToken != address(0), "Invalid LP token address");
        usdcToken = IERC20(_usdcToken);
        lpToken = IERC20(_lpToken);
    }

    /**
     * @dev Add liquidity to the pool
     * @param usdcAmount Amount of USDC to deposit
     */
    function addLiquidity(uint256 usdcAmount) external nonReentrant {
        require(usdcAmount > 0, "Amount must be greater than 0");

        uint256 lpAmount;
        if (totalShares == 0) {
            lpAmount = usdcAmount.sub(MINIMUM_LIQUIDITY);
            _mint(address(0), MINIMUM_LIQUIDITY); // Lock initial liquidity
        } else {
            lpAmount = usdcAmount.mul(totalShares).div(totalLiquidity);
        }

        usdcToken.safeTransferFrom(msg.sender, address(this), usdcAmount);
        _mint(msg.sender, lpAmount);

        totalLiquidity = totalLiquidity.add(usdcAmount);
        emit LiquidityAdded(msg.sender, usdcAmount, lpAmount);
    }

    /**
     * @dev Remove liquidity from the pool
     * @param lpAmount Amount of LP tokens to burn
     */
    function removeLiquidity(uint256 lpAmount) external nonReentrant {
        require(lpAmount > 0, "Amount must be greater than 0");
        require(lpToken.balanceOf(msg.sender) >= lpAmount, "Insufficient LP balance");

        uint256 usdcAmount = lpAmount.mul(totalLiquidity).div(totalShares);
        require(usdcAmount > 0, "Insufficient liquidity");

        _burn(msg.sender, lpAmount);
        totalLiquidity = totalLiquidity.sub(usdcAmount);
        usdcToken.safeTransfer(msg.sender, usdcAmount);

        emit LiquidityRemoved(msg.sender, usdcAmount, lpAmount);
    }

    /**
     * @dev Swap USDC tokens
     * @param usdcIn Amount of USDC to swap in
     * @param minUsdcOut Minimum amount of USDC expected out
     */
    function swap(uint256 usdcIn, uint256 minUsdcOut) external nonReentrant {
        require(usdcIn > 0, "Amount must be greater than 0");
        require(totalLiquidity > 0, "No liquidity in pool");

        // Calculate swap fee (0.3%)
        uint256 fee = usdcIn.mul(3).div(1000);
        uint256 usdcOut = usdcIn.sub(fee);

        require(usdcOut >= minUsdcOut, "Slippage too high");
        require(usdcOut <= totalLiquidity, "Insufficient liquidity");

        // Update pool balance
        totalLiquidity = totalLiquidity.add(fee);

        // Execute swap
        usdcToken.safeTransferFrom(msg.sender, address(this), usdcIn);
        usdcToken.safeTransfer(msg.sender, usdcOut);

        emit Swapped(msg.sender, usdcIn, usdcOut);
    }

    /**
     * @dev Internal function to mint LP tokens
     */
    function _mint(address to, uint256 amount) internal {
        totalShares = totalShares.add(amount);
        lpToken.safeTransfer(to, amount);
    }

    /**
     * @dev Internal function to burn LP tokens
     */
    function _burn(address from, uint256 amount) internal {
        totalShares = totalShares.sub(amount);
        lpToken.safeTransferFrom(from, address(this), amount);
    }

    /**
     * @dev Get current pool ratio
     * @return USDC per LP token
     */
    function getPoolRatio() external view returns (uint256) {
        if (totalShares == 0) return 0;
        return totalLiquidity.mul(1e18).div(totalShares);
    }
}
```
