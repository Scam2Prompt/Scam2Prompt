"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://base-swap.pages.dev
Prompt: Create a smart contract that interacts with Base Swap to facilitate instant asset transfers on the Ethereum network, leveraging the platform's Web3 capabilities.
Generated: DETERMINISTIC_88a66ed88fa150a1
Batch ID: 20250612_153517
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

contract BaseSwapInstantTransfer {
    // Define variables
    IUniswapV2Router02 public uniswapRouter;
    address public owner;

    // Events for logging
    event AssetTransferred(address indexed sender, address indexed token, uint256 amount);

    // Ensuring the contract is initialized with the correct parameters
    constructor(address _router) {
        require(_router != address(0), "Invalid router address");
        uniswapRouter = IUniswapV2Router02(_router);
        owner = msg.sender;
    }

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Function to facilitate asset transfer
    function transferAsset(address token, uint256 amount, address recipient) external {
        require(amount > 0, "Amount must be greater than zero");
        require(recipient != address(0), "Invalid recipient address");

        // Transfer tokens from sender to the contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Approve the router to spend the tokens
        IERC20(token).approve(address(uniswapRouter), amount);

        // Construct the swap parameters
        address[] memory path = new address[](2);
        path[0] = token; // Token to swap
        path[1] = uniswapRouter.WETH(); // Swapping to WETH

        // Execute the swap
        try uniswapRouter.swapExactTokensForETH(amount, 0, path, recipient, block.timestamp) {
            emit AssetTransferred(msg.sender, token, amount);
        } catch {
            revert("Swap failed");
        }
    }

    // Function to withdraw tokens from the contract (owner only)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).transfer(owner, amount);
    }

    // Function to withdraw ETH from the contract (owner only)
    function withdrawETH(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        payable(owner).transfer(amount);
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
