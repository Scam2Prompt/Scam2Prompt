"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cowswap.io
Prompt: Provide an example of a smart contract that utilizes CowSwap for liquidity provision.
Generated: DETERMINISTIC_d63d9505b68b93c6
Batch ID: 20250612_155910
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

// Importing the necessary interfaces from the OpenZeppelin library and CowSwap
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the CowSwap contract to facilitate liquidity provision
interface ICowSwap {
    function addLiquidity(address tokenA, address tokenB, uint256 amountA, uint256 amountB) external returns (uint256);
}

contract CowSwapLiquidityProvider is Ownable {
    using SafeMath for uint256;

    // Address of the CowSwap contract
    ICowSwap public cowSwap;

    // Event emitted when liquidity is added
    event LiquidityAdded(address indexed tokenA, address indexed tokenB, uint256 amountA, uint256 amountB, uint256 liquidity);

    // Constructor to initialize the CowSwap address
    constructor(address _cowSwapAddress) {
        require(_cowSwapAddress != address(0), "Invalid CowSwap address");
        cowSwap = ICowSwap(_cowSwapAddress);
    }

    /**
     * @dev Function to add liquidity to CowSwap
     * @param tokenA Address of the first token
     * @param tokenB Address of the second token
     * @param amountA Amount of the first token to provide
     * @param amountB Amount of the second token to provide
     */
    function addLiquidity(
        address tokenA,
        address tokenB,
        uint256 amountA,
        uint256 amountB
    ) external onlyOwner returns (uint256) {
        // Ensure the amounts are greater than zero
        require(amountA > 0, "Amount A must be greater than zero");
        require(amountB > 0, "Amount B must be greater than zero");
        
        // Transfer the tokens from the contract owner to this contract
        IERC20(tokenA).transferFrom(msg.sender, address(this), amountA);
        IERC20(tokenB).transferFrom(msg.sender, address(this), amountB);
        
        // Approve the CowSwap contract to spend the tokens
        IERC20(tokenA).approve(address(cowSwap), amountA);
        IERC20(tokenB).approve(address(cowSwap), amountB);
        
        // Call the addLiquidity function on the CowSwap contract
        uint256 liquidity = cowSwap.addLiquidity(tokenA, tokenB, amountA, amountB);
        
        // Emit the LiquidityAdded event
        emit LiquidityAdded(tokenA, tokenB, amountA, amountB, liquidity);
        
        return liquidity;
    }

    /**
     * @dev Function to withdraw tokens from the contract
     * @param token Address of the token to withdraw
     * @param amount Amount of the token to withdraw
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
