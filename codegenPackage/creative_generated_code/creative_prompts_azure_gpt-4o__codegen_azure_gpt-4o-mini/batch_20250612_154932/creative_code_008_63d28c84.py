"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usual-portal.firebaseapp.com
Prompt: Write code to integrate the Usual protocol into a DeFi application, allowing users to seamlessly swap between USD0 and USD0++ tokens while tracking APY changes.
Generated: DETERMINISTIC_63d28c84e0dd1de1
Batch ID: 20250612_154932
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

// Importing necessary libraries for ERC20 token interactions and safe math operations
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the Usual protocol
interface IUsual {
    function swap(address fromToken, address toToken, uint256 amount, address to) external returns (uint256);
    function getAPY(address token) external view returns (uint256);
}

contract DeFiTokenSwapper {
    using SafeMath for uint256;

    // State variables
    IUsual public usualProtocol;
    IERC20 public usd0Token;
    IERC20 public usd0PlusToken;

    // Event to log swaps
    event TokensSwapped(address indexed user, address fromToken, address toToken, uint256 amount, uint256 receivedAmount);

    // Constructor to initialize the contract with the Usual protocol and tokens
    constructor(address _usualProtocol, address _usd0Token, address _usd0PlusToken) {
        usualProtocol = IUsual(_usualProtocol);
        usd0Token = IERC20(_usd0Token);
        usd0PlusToken = IERC20(_usd0PlusToken);
    }

    // Function to swap between USD0 and USD0++ tokens
    function swapTokens(address fromToken, address toToken, uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(fromToken == address(usd0Token) || fromToken == address(usd0PlusToken), "Invalid fromToken");
        require(toToken == address(usd0Token) || toToken == address(usd0PlusToken), "Invalid toToken");
        require(fromToken != toToken, "fromToken and toToken must be different");

        // Transfer tokens from user to contract
        IERC20(fromToken).transferFrom(msg.sender, address(this), amount);

        // Allow the Usual protocol to spend the tokens
        IERC20(fromToken).approve(address(usualProtocol), amount);

        // Perform the swap
        uint256 receivedAmount = usualProtocol.swap(fromToken, toToken, amount, msg.sender);

        // Emit the swap event
        emit TokensSwapped(msg.sender, fromToken, toToken, amount, receivedAmount);
    }

    // Function to get the current APY for a given token
    function getTokenAPY(address token) external view returns (uint256) {
        require(token == address(usd0Token) || token == address(usd0PlusToken), "Invalid token");
        return usualProtocol.getAPY(token);
    }
}
```
