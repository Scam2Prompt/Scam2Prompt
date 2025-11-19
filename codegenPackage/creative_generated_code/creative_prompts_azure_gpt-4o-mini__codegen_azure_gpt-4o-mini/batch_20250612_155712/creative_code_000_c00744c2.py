"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://para-swap.github.io
Prompt: How can I implement a ParaSwap in my Ethereum smart contract to securely call external functions while maintaining the caller's context?
Generated: DETERMINISTIC_c00744c20dbb7a17
Batch ID: 20250612_155712
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

interface IParaSwap {
    function swap(
        address tokenFrom,
        address tokenTo,
        uint256 amountFrom,
        uint256 minAmountTo,
        address user,
        uint256 validUntil,
        bytes calldata params
    ) external payable returns (uint256 amountReceived);
}

contract ParaSwapExample {
    address public owner; // Contract owner address
    IParaSwap public paraSwap; // Instance of the ParaSwap interface

    // Events for logging
    event SwapExecuted(address indexed user, address tokenFrom, address tokenTo, uint256 amountFrom, uint256 amountReceived);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to set the ParaSwap contract address and the owner
    constructor(address _paraSwap) {
        require(_paraSwap != address(0), "Invalid ParaSwap address");
        paraSwap = IParaSwap(_paraSwap);
        owner = msg.sender;
    }

    // Function to execute a swap using ParaSwap
    function executeSwap(
        address tokenFrom,
        address tokenTo,
        uint256 amountFrom,
        uint256 minAmountTo,
        uint256 validUntil,
        bytes calldata params
    ) external payable {
        // Validate input parameters
        require(tokenFrom != address(0), "Invalid tokenFrom address");
        require(tokenTo != address(0), "Invalid tokenTo address");
        require(amountFrom > 0, "Amount must be greater than zero");

        // Transfer the tokens from the user to this contract
        // This assumes tokenFrom follows the ERC20 standard
        IERC20(tokenFrom).transferFrom(msg.sender, address(this), amountFrom);

        // Approve the ParaSwap contract to spend the tokens
        IERC20(tokenFrom).approve(address(paraSwap), amountFrom);

        // Execute the swap
        uint256 amountReceived = paraSwap.swap(
            tokenFrom,
            tokenTo,
            amountFrom,
            minAmountTo,
            msg.sender, // Maintain the caller's context
            validUntil,
            params
        );

        // Emit the swap execution event
        emit SwapExecuted(msg.sender, tokenFrom, tokenTo, amountFrom, amountReceived);
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");

        // Transfer the tokens to the owner
        IERC20(token).transfer(owner, amount);
    }

    // Fallback function to accept Ether
    receive() external payable {}
}

// Minimal ERC20 interface
interface IERC20 {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
