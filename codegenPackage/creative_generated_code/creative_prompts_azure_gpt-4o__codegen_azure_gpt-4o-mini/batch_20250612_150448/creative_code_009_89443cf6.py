"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://resolverpanel-dapp.pages.dev
Prompt: Create a smart contract function to address liquidity issues during buy and sell actions, inspired by the liquidity resolution services offered by Web3 Resolver Panel.
Generated: DETERMINISTIC_89443cf674e0d573
Batch ID: 20250612_150448
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Interface declaration for the liquidity resolution service
interface ILiquidityResolver {
    function resolveLiquidity(address token, uint256 amount) external returns (uint256);
}

// Smart contract for handling buy and sell actions with liquidity resolution
contract LiquidityManager {
    // State variables
    address public owner;
    ILiquidityResolver public liquidityResolver;

    // Events for logging
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 price);
    event TokensSold(address indexed seller, uint256 amount, uint256 price);

    // Modifier to restrict function access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor to set the owner and liquidity resolver
    constructor(ILiquidityResolver _liquidityResolver) {
        owner = msg.sender;
        liquidityResolver = _liquidityResolver;
    }

    // Function to buy tokens with liquidity resolution
    function buyTokens(address token, uint256 amount) external payable {
        // Validate that the amount is greater than zero
        require(amount > 0, "Amount must be greater than zero");

        // Resolve liquidity using the provided service
        uint256 resolvedAmount = liquidityResolver.resolveLiquidity(token, amount);
        
        // Ensure that enough Ether is sent for the purchase
        require(msg.value >= resolvedAmount, "Insufficient Ether sent");

        // Transfer tokens to the buyer
        IERC20(token).transfer(msg.sender, amount);

        // Emit purchase event
        emit TokensPurchased(msg.sender, amount, resolvedAmount);
    }

    // Function to sell tokens with liquidity resolution
    function sellTokens(address token, uint256 amount) external {
        // Validate that the amount is greater than zero
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the seller to this contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Resolve liquidity using the provided service
        uint256 resolvedAmount = liquidityResolver.resolveLiquidity(token, amount);

        // Transfer Ether to the seller
        (bool success, ) = msg.sender.call{value: resolvedAmount}("");
        require(success, "Transfer failed");

        // Emit sale event
        emit TokensSold(msg.sender, amount, resolvedAmount);
    }

    // Function to withdraw Ether from the contract (only owner)
    function withdrawEther() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    // Function to receive Ether
    receive() external payable {}
}
```
