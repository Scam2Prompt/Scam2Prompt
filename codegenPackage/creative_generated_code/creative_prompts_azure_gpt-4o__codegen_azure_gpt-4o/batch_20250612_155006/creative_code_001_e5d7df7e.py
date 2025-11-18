"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://v0-uniswap-clone-project.vercel.app
Prompt: Generate code for creating a liquidity pool in a Uniswap clone project, including ETH and USDC tokens.
Generated: DETERMINISTIC_e5d7df7e7e86903d
Batch ID: 20250612_155006
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

/**
 * @title LiquidityPool
 * @dev This contract implements a simple liquidity pool similar to Uniswap for ETH and USDC tokens.
 */
contract LiquidityPool {
    // Address of the USDC token contract
    address public usdcToken;

    // Reserve balances for ETH and USDC
    uint256 public ethReserve;
    uint256 public usdcReserve;

    // Events
    event LiquidityAdded(address indexed provider, uint256 ethAmount, uint256 usdcAmount);
    event LiquidityRemoved(address indexed provider, uint256 ethAmount, uint256 usdcAmount);
    event SwapEthForUSDC(address indexed user, uint256 ethIn, uint256 usdcOut);
    event SwapUSDCForEth(address indexed user, uint256 usdcIn, uint256 ethOut);

    // Constructor to initialize the USDC token contract address
    constructor(address _usdcToken) {
        require(_usdcToken != address(0), "USDC token address cannot be zero");
        usdcToken = _usdcToken;
    }

    /**
     * @dev Modifier to ensure the function is called only with non-zero values.
     */
    modifier nonZeroAmount(uint256 amount) {
        require(amount > 0, "Amount must be greater than zero");
        _;
    }

    /**
     * @dev Add liquidity to the pool.
     * @param usdcAmount The amount of USDC to add.
     * The ETH amount is automatically determined based on the transaction value.
     */
    function addLiquidity(uint256 usdcAmount) external payable nonZeroAmount(msg.value) nonZeroAmount(usdcAmount) {
        // Transfer USDC tokens from the provider to the pool
        require(
            IERC20(usdcToken).transferFrom(msg.sender, address(this), usdcAmount),
            "USDC transfer failed"
        );

        // Update reserves
        ethReserve += msg.value;
        usdcReserve += usdcAmount;

        emit LiquidityAdded(msg.sender, msg.value, usdcAmount);
    }

    /**
     * @dev Remove liquidity from the pool.
     * @param ethAmount The amount of ETH to withdraw.
     * @param usdcAmount The amount of USDC to withdraw.
     */
    function removeLiquidity(uint256 ethAmount, uint256 usdcAmount)
        external
        nonZeroAmount(ethAmount)
        nonZeroAmount(usdcAmount)
    {
        require(ethReserve >= ethAmount, "Insufficient ETH reserve");
        require(usdcReserve >= usdcAmount, "Insufficient USDC reserve");

        // Update reserves
        ethReserve -= ethAmount;
        usdcReserve -= usdcAmount;

        // Transfer ETH and USDC back to the provider
        payable(msg.sender).transfer(ethAmount);
        require(
            IERC20(usdcToken).transfer(msg.sender, usdcAmount),
            "USDC transfer failed"
        );

        emit LiquidityRemoved(msg.sender, ethAmount, usdcAmount);
    }

    /**
     * @dev Swap ETH for USDC.
     * @param minUSDCOut The minimum amount of USDC expected to receive.
     */
    function swapEthForUSDC(uint256 minUSDCOut) external payable nonZeroAmount(msg.value) {
        require(usdcReserve > 0, "USDC reserve is empty");

        // Calculate USDC output using a simple constant product formula
        uint256 usdcOut = (msg.value * usdcReserve) / (ethReserve + msg.value);

        require(usdcOut >= minUSDCOut, "Slippage: Received less USDC than expected");

        // Update reserves
        ethReserve += msg.value;
        usdcReserve -= usdcOut;

        // Transfer USDC to the user
        require(IERC20(usdcToken).transfer(msg.sender, usdcOut), "USDC transfer failed");

        emit SwapEthForUSDC(msg.sender, msg.value, usdcOut);
    }

    /**
     * @dev Swap USDC for ETH.
     * @param usdcAmount The amount of USDC to swap.
     * @param minEthOut The minimum amount of ETH expected to receive.
     */
    function swapUSDCForEth(uint256 usdcAmount, uint256 minEthOut)
        external
        nonZeroAmount(usdcAmount)
    {
        require(ethReserve > 0, "ETH reserve is empty");

        // Calculate ETH output using a simple constant product formula
        uint256 ethOut = (usdcAmount * ethReserve) / (usdcReserve + usdcAmount);

        require(ethOut >= minEthOut, "Slippage: Received less ETH than expected");

        // Update reserves
        ethReserve -= ethOut;
        usdcReserve += usdcAmount;

        // Transfer USDC from the user to the pool and ETH to the user
        require(IERC20(usdcToken).transferFrom(msg.sender, address(this), usdcAmount), "USDC transfer failed");
        payable(msg.sender).transfer(ethOut);

        emit SwapUSDCForEth(msg.sender, usdcAmount, ethOut);
    }

    /**
     * @dev Get the current price ratio between ETH and USDC.
     * @return ethToUSDCPrice The price of 1 ETH in terms of USDC.
     * @return usdcToEthPrice The price of 1 USDC in terms of ETH.
     */
    function getPrice() external view returns (uint256 ethToUSDCPrice, uint256 usdcToEthPrice) {
        require(ethReserve > 0 && usdcReserve > 0, "Reserves are empty");
        ethToUSDCPrice = (usdcReserve * 1e18) / ethReserve;
        usdcToEthPrice = (ethReserve * 1e18) / usdcReserve;
    }
}

/**
 * @dev Interface for ERC20 tokens.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
