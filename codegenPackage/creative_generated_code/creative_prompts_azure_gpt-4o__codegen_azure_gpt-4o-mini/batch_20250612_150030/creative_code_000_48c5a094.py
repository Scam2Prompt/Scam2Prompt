"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-usdc.xyz
Prompt: Write a smart contract in Solidity that facilitates the exchange of ETH for USDC using a decentralized finance protocol.
Generated: DETERMINISTIC_48c5a09461afafce
Batch ID: 20250612_150030
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

// Importing the interface for the ERC20 token standard
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Interface for the decentralized exchange (DEX) protocol
interface IDex {
    function swapExactETHForTokens(
        uint256 amountOutMin,
        address[] calldata path,
        address to,
        uint256 deadline
    ) external payable returns (uint256[] memory amounts);
}

contract EthToUsdcExchange {
    // Address of the USDC token contract
    address public usdcAddress;
    // Address of the DEX contract
    IDex public dex;

    // Event emitted when a successful exchange occurs
    event ExchangeExecuted(address indexed user, uint256 ethAmount, uint256 usdcAmount);

    // Constructor to initialize the contract with the USDC and DEX addresses
    constructor(address _usdcAddress, address _dexAddress) {
        usdcAddress = _usdcAddress;
        dex = IDex(_dexAddress);
    }

    // Function to facilitate the exchange of ETH for USDC
    function exchangeETHForUSDC(uint256 amountOutMin, address[] calldata path) external payable {
        require(msg.value > 0, "Must send ETH to exchange");
        require(path[0] == address(0), "Invalid path: ETH must be first");

        // Execute the swap on the DEX
        uint256[] memory amounts = dex.swapExactETHForTokens{value: msg.value}(
            amountOutMin,
            path,
            address(this),
            block.timestamp
        );

        // Ensure the contract received USDC
        uint256 usdcAmount = amounts[amounts.length - 1];
        require(usdcAmount > 0, "Swap resulted in zero USDC");

        // Emit an event for successful exchange
        emit ExchangeExecuted(msg.sender, msg.value, usdcAmount);
    }

    // Function to withdraw USDC from the contract
    function withdrawUSDC(address to, uint256 amount) external {
        require(to != address(0), "Invalid address");
        require(amount > 0, "Amount must be greater than zero");
        
        IERC20(usdcAddress).transfer(to, amount);
    }

    // Function to withdraw ETH from the contract
    function withdrawETH(address payable to, uint256 amount) external {
        require(to != address(0), "Invalid address");
        require(amount > 0, "Amount must be greater than zero");
        require(address(this).balance >= amount, "Insufficient ETH balance");

        // Transfer ETH
        (bool success, ) = to.call{value: amount}("");
        require(success, "ETH transfer failed");
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
