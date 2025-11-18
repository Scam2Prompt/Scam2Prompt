"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeianm7lllm6v2rpyuah5gzsh22gxfikab5ie3xei6f2n3ngfvsx524.ipfs.dweb.link
Prompt: Write a Solidity contract that interacts with the 1inch protocol to perform token swaps on Optimism.
Generated: DETERMINISTIC_d6926d269276fcbf
Batch ID: 20250612_151547
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

// Import the necessary interfaces from the 1inch protocol
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

interface I1inch {
    function swap(
        address caller,
        address fromToken,
        address toToken,
        uint256 amount,
        uint256 minReturnAmount,
        bytes calldata data
    ) external payable returns (uint256 returnAmount);
}

contract TokenSwap is Ownable {
    // 1inch router address for Optimism
    address public constant ONE_INCH_ROUTER = 0x1111111254fb6c44bac0bed2854e76f906e9c6e;

    event TokenSwapped(address indexed fromToken, address indexed toToken, uint256 amountIn, uint256 amountOut);

    // Function to swap tokens using the 1inch protocol
    function swapTokens(
        address fromToken,
        address toToken,
        uint256 amount,
        uint256 minReturnAmount,
        bytes calldata data
    ) external payable onlyOwner returns (uint256 returnAmount) {
        require(amount > 0, "Amount must be greater than zero");
        require(minReturnAmount > 0, "Minimum return amount must be greater than zero");

        // Transfer specified amount of fromToken from the owner to the contract
        IERC20(fromToken).transferFrom(msg.sender, address(this), amount);

        // Approve the 1inch router to spend the tokens
        IERC20(fromToken).approve(ONE_INCH_ROUTER, amount);

        // Perform the token swap through the 1inch protocol
        returnAmount = I1inch(ONE_INCH_ROUTER).swap(
            msg.sender,
            fromToken,
            toToken,
            amount,
            minReturnAmount,
            data
        );

        // Emit an event for the swap
        emit TokenSwapped(fromToken, toToken, amount, returnAmount);
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).transfer(msg.sender, amount);
    }

    // Function to withdraw Ether in case of accidental Ether transfer
    function withdrawEther() external onlyOwner {
        payable(msg.sender).transfer(address(this).balance);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
