"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://v2-stargate.net
Prompt: Create a smart contract that leverages Stargate Finance's composable infrastructure to enable seamless DeFi swaps across multiple blockchains.
Generated: DETERMINISTIC_907acca17fb33328
Batch ID: 20250612_154842
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@stargate.finance/contracts/interfaces/IStargateRouter.sol";

contract MultiChainSwap is Ownable {
    using Counters for Counters.Counter;

    // Stargate Router interface
    IStargateRouter public stargateRouter;

    // To keep track of swap requests
    Counters.Counter private swapIdCounter;

    // Event emitted after a successful swap
    event SwapExecuted(
        uint256 indexed swapId,
        address indexed sender,
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOut,
        uint256 destinationChainId
    );

    constructor(address _stargateRouter) {
        require(_stargateRouter != address(0), "Invalid router address");
        stargateRouter = IStargateRouter(_stargateRouter);
    }

    // Function to execute a swap across chains
    function executeSwap(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 destinationChainId,
        uint256 minAmountOut,
        bytes calldata destinationAddress
    ) external {
        require(amountIn > 0, "Amount must be greater than 0");
        require(minAmountOut > 0, "Minimum amount out must be greater than 0");

        // Transfer tokenIn from sender to this contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Approve the Stargate Router to spend tokenIn
        IERC20(tokenIn).approve(address(stargateRouter), amountIn);

        // Execute the swap through Stargate Router
        uint256 swapId = swapIdCounter.current();
        swapIdCounter.increment();

        // Assuming there is a function in StargateRouter to swap. 
        // This will depend on the actual interface provided by Stargate.
        uint256 amountOut = stargateRouter.swap{value: msg.value}(
            tokenIn,
            tokenOut,
            amountIn,
            destinationChainId,
            minAmountOut,
            destinationAddress
        );

        // Emit an event for the swap
        emit SwapExecuted(swapId, msg.sender, tokenIn, tokenOut, amountIn, amountOut, destinationChainId);
    }

    // Function to withdraw tokens accidentally sent to the contract
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(msg.sender, amount);
    }

    // Function to handle Ether received (if any)
    receive() external payable {}

    // Function to withdraw Ether from the contract
    function withdrawEther(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient balance");
        payable(msg.sender).transfer(amount);
    }
}
```
