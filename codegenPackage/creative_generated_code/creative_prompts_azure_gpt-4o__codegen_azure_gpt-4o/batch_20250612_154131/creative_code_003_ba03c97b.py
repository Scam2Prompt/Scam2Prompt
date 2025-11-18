"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://curvefi.co
Prompt: Create a smart contract in Solidity that interacts with Curve Finance pools to perform stablecoin swaps on an EVM-compatible sidechain.
Generated: DETERMINISTIC_ba03c97bee1489fd
Batch ID: 20250612_154131
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
 * @title CurveFinanceStablecoinSwapper
 * @dev This contract enables swapping stablecoins using Curve Finance pools on an EVM-compatible sidechain.
 */
interface ICurvePool {
    function exchange(int128 i, int128 j, uint256 dx, uint256 minDy) external returns (uint256);
    function coins(uint256 index) external view returns (address);
}

interface IERC20 {
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}

contract CurveFinanceStablecoinSwapper {
    address public owner;
    ICurvePool public curvePool;

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Sets the Curve pool address and initializes the contract.
     * @param _curvePool Address of the Curve Finance pool contract.
     */
    constructor(address _curvePool) {
        require(_curvePool != address(0), "Invalid Curve pool address");
        owner = msg.sender;
        curvePool = ICurvePool(_curvePool);
    }

    /**
     * @dev Performs a swap between two stablecoins in the Curve pool.
     * @param i Index of the input coin in the Curve pool.
     * @param j Index of the output coin in the Curve pool.
     * @param dx Amount of the input coin to swap.
     * @param minDy Minimum acceptable amount of the output coin.
     */
    function swapStablecoins(int128 i, int128 j, uint256 dx, uint256 minDy) external {
        address inputToken = curvePool.coins(uint256(int256(i)));
        address outputToken = curvePool.coins(uint256(int256(j)));

        require(inputToken != address(0) && outputToken != address(0), "Invalid coin indexes");

        // Transfer input tokens from the sender to this contract
        IERC20(inputToken).transferFrom(msg.sender, address(this), dx);

        // Approve Curve pool to spend the input tokens
        IERC20(inputToken).approve(address(curvePool), dx);

        // Perform the swap
        uint256 outputAmount = curvePool.exchange(i, j, dx, minDy);

        require(outputAmount >= minDy, "Insufficient output amount");

        // Transfer swapped tokens to the sender
        IERC20(outputToken).transfer(msg.sender, outputAmount);
    }

    /**
     * @dev Allows the owner to update the Curve pool address.
     * @param _curvePool New address of the Curve Finance pool contract.
     */
    function updateCurvePool(address _curvePool) external onlyOwner {
        require(_curvePool != address(0), "Invalid Curve pool address");
        curvePool = ICurvePool(_curvePool);
    }

    /**
     * @dev Allows the owner to withdraw tokens accidentally sent to the contract.
     * @param token Address of the token to withdraw.
     * @param to Address to send the withdrawn tokens to.
     * @param amount Amount of tokens to withdraw.
     */
    function recoverTokens(address token, address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid recipient address");
        IERC20(token).transfer(to, amount);
    }
}
```
