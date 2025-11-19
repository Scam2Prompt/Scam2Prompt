"""
Generated Code Metadata:
========================
Original URL: https://op-enocean.github.io
Prompt: Create a Solidity contract that uses Open Ocean to modularize core DeFi protocol logic, ensuring composability and upgradability.
Generated: DETERMINISTIC_4c7b0f7e36b20b27
Batch ID: 20250612_153424
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

// Importing OpenOcean interfaces and libraries
import "@openzeppelin/contracts/proxy/utils/Initializable.sol";
import "@openzeppelin/contracts/proxy/utils/UUPSUpgradeable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Interface for the OpenOcean Router
interface IOpenOceanRouter {
    function swapExactTokensForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);
}

// Core DeFi Protocol Contract
contract DeFiProtocol is Initializable, UUPSUpgradeable, Ownable {
    IOpenOceanRouter public openOceanRouter;

    // Event emitted when tokens are swapped
    event TokensSwapped(address indexed user, uint amountIn, uint amountOut);

    // Initialize the contract with the OpenOcean router address
    function initialize(address _openOceanRouter) public initializer {
        require(_openOceanRouter != address(0), "Invalid router address");
        openOceanRouter = IOpenOceanRouter(_openOceanRouter);
    }

    // Function to swap tokens using OpenOcean
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint amountIn,
        uint amountOutMin,
        uint deadline
    ) external {
        require(amountIn > 0, "Amount in must be greater than zero");
        require(deadline >= block.timestamp, "Deadline has passed");

        // Transfer tokens from the user to this contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Approve the OpenOcean router to spend the tokens
        IERC20(tokenIn).approve(address(openOceanRouter), amountIn);

        // Define the path for the swap
        address[] memory path = new address[](2);
        path[0] = tokenIn;
        path[1] = tokenOut;

        // Perform the token swap
        uint[] memory amounts = openOceanRouter.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            msg.sender,
            deadline
        );

        // Emit an event for the swap
        emit TokensSwapped(msg.sender, amounts[0], amounts[1]);
    }

    // Function to upgrade the contract
    function _authorizeUpgrade(address newImplementation) internal override onlyOwner {}

    // Function to withdraw tokens from the contract (for emergency purposes)
    function withdrawTokens(address token, uint amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
