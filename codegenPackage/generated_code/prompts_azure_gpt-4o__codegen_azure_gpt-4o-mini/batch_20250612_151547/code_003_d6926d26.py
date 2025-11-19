"""
Generated Code Metadata:
========================
Original URL: https://bafybeianm7lllm6v2rpyuah5gzsh22gxfikab5ie3xei6f2n3ngfvsx524.ipfs.dweb.link
Prompt: Write a Solidity contract that interacts with the 1inch protocol to perform token swaps on Optimism.
Generated: DETERMINISTIC_d6926d269276fcbf
Batch ID: 20250612_151547
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

// Importing the necessary interfaces for ERC20 and the 1inch protocol
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

interface IOneInch {
    function swap(
        address caller,
        address srcToken,
        address dstToken,
        uint256 amount,
        uint256 minReturnAmount,
        bytes calldata data
    ) external payable returns (uint256 returnAmount);
}

contract TokenSwap is Ownable {
    // Address of the 1inch protocol contract
    IOneInch public oneInch;

    // Event emitted when a swap is executed
    event SwapExecuted(address indexed user, address srcToken, address dstToken, uint256 amount, uint256 returnAmount);

    // Constructor to set the 1inch contract address
    constructor(address _oneInch) {
        require(_oneInch != address(0), "Invalid 1inch address");
        oneInch = IOneInch(_oneInch);
    }

    // Function to perform a token swap
    function swapTokens(
        address srcToken,
        address dstToken,
        uint256 amount,
        uint256 minReturnAmount,
        bytes calldata data
    ) external {
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(srcToken).balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer the tokens from the user to this contract
        IERC20(srcToken).transferFrom(msg.sender, address(this), amount);

        // Approve the 1inch contract to spend the tokens
        IERC20(srcToken).approve(address(oneInch), amount);

        // Execute the swap
        uint256 returnAmount = oneInch.swap(msg.sender, srcToken, dstToken, amount, minReturnAmount, data);

        // Emit the swap event
        emit SwapExecuted(msg.sender, srcToken, dstToken, amount, returnAmount);
    }

    // Function to withdraw tokens from the contract (for emergency purposes)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer the tokens to the owner
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
