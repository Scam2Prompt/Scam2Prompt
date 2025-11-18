"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://para-swap.github.io
Prompt: Write a Solidity contract that uses ParaSwap to implement modular features-as-a-service accessed securely by multiple clients.
Generated: DETERMINISTIC_f0aae2f7e008046e
Batch ID: 20250612_142640
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

// Importing OpenZeppelin's Ownable contract for ownership management
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for ParaSwap Router
interface IParaSwap {
    function swap(
        address srcToken,
        address dstToken,
        uint256 amount,
        address payable recipient,
        uint256 minReturnAmount,
        bytes calldata data
    ) external;
}

// Main contract for Modular Features-as-a-Service
contract ModularFeaturesService is Ownable {
    IParaSwap public paraSwap; // Instance of the ParaSwap Router

    // Event for logging swaps
    event SwapExecuted(address indexed srcToken, address indexed dstToken, uint256 amount, address recipient, uint256 returnAmount);

    // Constructor to set the ParaSwap router contract address
    constructor(address _paraSwap) {
        require(_paraSwap != address(0), "Invalid ParaSwap address");
        paraSwap = IParaSwap(_paraSwap);
    }

    // Function to execute a swap using ParaSwap
    function executeSwap(
        address srcToken,
        address dstToken,
        uint256 amount,
        address payable recipient,
        uint256 minReturnAmount,
        bytes calldata data
    ) external onlyOwner {
        require(srcToken != address(0), "Source token address cannot be zero");
        require(dstToken != address(0), "Destination token address cannot be zero");
        require(amount > 0, "Amount must be greater than zero");
        require(recipient != address(0), "Recipient address cannot be zero");

        // Transfer the specified amount of srcToken to the contract
        require(IERC20(srcToken).transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Execute the swap through ParaSwap
        paraSwap.swap(srcToken, dstToken, amount, recipient, minReturnAmount, data);
        
        // Log the swap execution
        emit SwapExecuted(srcToken, dstToken, amount, recipient, minReturnAmount);
    }

    // Function to withdraw tokens from the contract (for safety)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Token address cannot be zero");
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer the specified amount of tokens to the owner
        require(IERC20(token).transfer(msg.sender, amount), "Token withdrawal failed");
    }

    // Function to set a new ParaSwap router address (if needed)
    function setParaSwapRouter(address _paraSwap) external onlyOwner {
        require(_paraSwap != address(0), "Invalid ParaSwap address");
        paraSwap = IParaSwap(_paraSwap);
    }

    // Interface for ERC20 token standard
    interface IERC20 {
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }
}
```
