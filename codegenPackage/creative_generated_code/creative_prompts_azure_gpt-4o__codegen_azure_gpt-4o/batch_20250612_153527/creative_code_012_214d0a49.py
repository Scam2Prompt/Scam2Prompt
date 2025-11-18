"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepe-unchained-on.pages.dev
Prompt: Write a Solidity contract for liquidity pool management on Pepe Unchained's decentralized exchange, ensuring compatibility with the $PEPU token.
Generated: DETERMINISTIC_214d0a49cf060f85
Batch ID: 20250612_153527
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
 * @title LiquidityPoolManager
 * @dev A contract for managing liquidity pools on Pepe Unchained's decentralized exchange.
 *      Supports liquidity management for the $PEPU token.
 */
contract LiquidityPoolManager {
    // Address of the $PEPU token contract
    address public pepuToken;

    // Event emitted when liquidity is added
    event LiquidityAdded(address indexed provider, uint256 pepuAmount, uint256 ethAmount);

    // Event emitted when liquidity is removed
    event LiquidityRemoved(address indexed provider, uint256 pepuAmount, uint256 ethAmount);

    // Event emitted when a swap occurs
    event TokenSwapped(address indexed swapper, uint256 ethAmountIn, uint256 pepuAmountOut);

    // Liquidity pool balances
    uint256 public totalPEPUInPool;
    uint256 public totalETHInPool;

    // Modifier to ensure non-zero amounts
    modifier validAmount(uint256 amount) {
        require(amount > 0, "Amount must be greater than zero");
        _;
    }

    /**
     * @dev Constructor to initialize the $PEPU token address.
     * @param _pepuToken Address of the $PEPU token contract.
     */
    constructor(address _pepuToken) {
        require(_pepuToken != address(0), "Invalid $PEPU token address");
        pepuToken = _pepuToken;
    }

    /**
     * @dev Adds liquidity to the pool.
     * @param pepuAmount Amount of $PEPU tokens to add.
     * @notice Caller must approve this contract to transfer $PEPU tokens before calling this function.
     */
    function addLiquidity(uint256 pepuAmount) external payable validAmount(pepuAmount) validAmount(msg.value) {
        // Transfer $PEPU tokens from the liquidity provider to the contract
        require(
            IERC20(pepuToken).transferFrom(msg.sender, address(this), pepuAmount),
            "PEPU token transfer failed"
        );

        // Update pool balances
        totalPEPUInPool += pepuAmount;
        totalETHInPool += msg.value;

        emit LiquidityAdded(msg.sender, pepuAmount, msg.value);
    }

    /**
     * @dev Removes liquidity from the pool.
     * @param pepuAmount Amount of $PEPU tokens to withdraw.
     * @notice ETH and $PEPU tokens are withdrawn proportionally based on the pool's current reserves.
     */
    function removeLiquidity(uint256 pepuAmount) external validAmount(pepuAmount) {
        require(pepuAmount <= totalPEPUInPool, "Not enough $PEPU in pool");

        // Calculate proportional ETH amount
        uint256 ethAmount = (pepuAmount * totalETHInPool) / totalPEPUInPool;

        require(ethAmount <= totalETHInPool, "Not enough ETH in pool");

        // Update pool balances
        totalPEPUInPool -= pepuAmount;
        totalETHInPool -= ethAmount;

        // Transfer $PEPU tokens and ETH to the liquidity provider
        require(IERC20(pepuToken).transfer(msg.sender, pepuAmount), "$PEPU transfer failed");
        (bool success, ) = msg.sender.call{value: ethAmount}("");
        require(success, "ETH transfer failed");

        emit LiquidityRemoved(msg.sender, pepuAmount, ethAmount);
    }

    /**
     * @dev Swaps ETH for $PEPU tokens.
     * @notice Caller sends ETH to the contract, and receives $PEPU tokens based on the pool's reserves.
     */
    function swapETHForPEPU() external payable validAmount(msg.value) {
        require(totalPEPUInPool > 0, "Not enough $PEPU in pool");

        // Calculate $PEPU amount to send, using a simple constant product formula
        uint256 pepuAmountOut = (msg.value * totalPEPUInPool) / (totalETHInPool + msg.value);

        require(pepuAmountOut <= totalPEPUInPool, "Insufficient $PEPU liquidity");

        // Update pool balances
        totalETHInPool += msg.value;
        totalPEPUInPool -= pepuAmountOut;

        // Transfer $PEPU tokens to the swapper
        require(IERC20(pepuToken).transfer(msg.sender, pepuAmountOut), "PEPU transfer failed");

        emit TokenSwapped(msg.sender, msg.value, pepuAmountOut);
    }

    /**
     * @dev Fallback function to reject any direct ETH transfers.
     */
    fallback() external payable {
        revert("Direct ETH transfers not allowed");
    }

    /**
     * @dev Receive function to reject any direct ETH transfers.
     */
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}

/**
 * @dev Standard interface for ERC-20 tokens to ensure compatibility with $PEPU.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
