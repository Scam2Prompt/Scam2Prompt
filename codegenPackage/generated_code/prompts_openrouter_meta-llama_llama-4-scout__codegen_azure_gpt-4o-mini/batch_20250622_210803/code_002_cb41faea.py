"""
Generated Code Metadata:
========================
Original URL: https://merlion.pages.dev
Prompt: Generate a smart contract code for a new token launchpad on MerlinSwap, incorporating features from Merlin's Spellbook.
Generated: DETERMINISTIC_cb41faeab8c04464
Batch ID: 20250622_210803
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the MerlinSwap Router
interface IMerlinSwapRouter {
    function addLiquidity(
        address tokenA,
        address tokenB,
        uint amountADesired,
        uint amountBDesired,
        uint amountAMin,
        uint amountBMin,
        address to,
        uint deadline
    ) external returns (uint amountA, uint amountB, uint liquidity);
}

// TokenLaunchpad contract for launching new tokens on MerlinSwap
contract TokenLaunchpad is Ownable {
    using SafeMath for uint256;

    // State variables
    IMerlinSwapRouter public merlinSwapRouter;
    address public merlinToken; // Address of the Merlin token
    mapping(address => bool) public isTokenLaunched; // Track launched tokens

    // Event emitted when a new token is launched
    event TokenLaunched(address indexed token, uint256 amountA, uint256 amountB);

    // Constructor to set the MerlinSwap router and token address
    constructor(address _merlinSwapRouter, address _merlinToken) {
        merlinSwapRouter = IMerlinSwapRouter(_merlinSwapRouter);
        merlinToken = _merlinToken;
    }

    // Function to launch a new token
    function launchToken(
        address tokenAddress,
        uint256 amountADesired,
        uint256 amountBDesired,
        uint256 amountAMin,
        uint256 amountBMin
    ) external onlyOwner {
        require(!isTokenLaunched[tokenAddress], "Token already launched");
        
        // Transfer tokens from the owner to this contract
        IERC20(tokenAddress).transferFrom(msg.sender, address(this), amountADesired);
        IERC20(merlinToken).transferFrom(msg.sender, address(this), amountBDesired);

        // Approve the router to spend the tokens
        IERC20(tokenAddress).approve(address(merlinSwapRouter), amountADesired);
        IERC20(merlinToken).approve(address(merlinSwapRouter), amountBDesired);

        // Add liquidity to the MerlinSwap
        (uint256 amountA, uint256 amountB, uint256 liquidity) = merlinSwapRouter.addLiquidity(
            tokenAddress,
            merlinToken,
            amountADesired,
            amountBDesired,
            amountAMin,
            amountBMin,
            address(this),
            block.timestamp
        );

        // Mark the token as launched
        isTokenLaunched[tokenAddress] = true;

        // Emit the TokenLaunched event
        emit TokenLaunched(tokenAddress, amountA, amountB);
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }

    // Function to withdraw Ether from the contract
    function withdrawEther(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        payable(msg.sender).transfer(amount);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
