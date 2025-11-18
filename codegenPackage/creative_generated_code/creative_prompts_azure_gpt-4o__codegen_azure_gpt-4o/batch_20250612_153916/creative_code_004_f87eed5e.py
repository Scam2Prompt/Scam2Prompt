"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fishersclubs.com
Prompt: Write a Solidity function that integrates Spark's savings protocol to allow users to withdraw their stablecoin deposits into USDC, USDS, or DAI with zero slippage.
Generated: DETERMINISTIC_f87eed5e8b6631c4
Batch ID: 20250612_153916
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

// Importing necessary interfaces for Spark's savings protocol and ERC20 tokens
interface ISparkSavingsProtocol {
    function withdraw(address token, uint256 amount) external returns (uint256);
}

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract StablecoinWithdraw {

    // Address of Spark's savings protocol
    ISparkSavingsProtocol private sparkSavingsProtocol;

    // Constructor to initialize Spark's savings protocol
    constructor(address _sparkSavingsProtocol) {
        require(_sparkSavingsProtocol != address(0), "Invalid protocol address");
        sparkSavingsProtocol = ISparkSavingsProtocol(_sparkSavingsProtocol);
    }

    /**
     * @notice Withdraws stablecoin deposits from Spark's savings protocol with zero slippage
     * @param token Address of the stablecoin to withdraw (e.g., USDC, USDS, DAI)
     * @param amount Amount of tokens to withdraw
     */
    function withdrawStablecoin(address token, uint256 amount) external {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Withdrawal amount must be greater than zero");

        // Check the balance of the sender in Spark's savings protocol
        uint256 preBalance = IERC20(token).balanceOf(msg.sender);

        // Perform the withdrawal from Spark's savings protocol
        uint256 withdrawnAmount = sparkSavingsProtocol.withdraw(token, amount);
        require(withdrawnAmount == amount, "Withdrawal failed or slippage occurred"); // Ensure zero slippage

        // Transfer the withdrawn tokens to the sender
        bool success = IERC20(token).transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        // Post-withdrawal balance check
        uint256 postBalance = IERC20(token).balanceOf(msg.sender);
        require(postBalance == preBalance + amount, "Balance mismatch after withdrawal");
    }
}
```
