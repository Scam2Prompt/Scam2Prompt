"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kayenferno.pages.dev
Prompt: Create a smart contract function to supply liquidity to the USDT-CHZ pool and calculate bonus points earned for the KAYEN League.
Generated: DETERMINISTIC_e8cd7395054c2aa2
Batch ID: 20250612_153547
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

// Importing necessary interfaces from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the liquidity pool (assumed to be an ERC20 token compliant)
interface ILiquidityPool {
    function supplyLiquidity(address token, uint256 amount) external;
}

contract LiquidityProvider is Ownable {
    // State variables
    IERC20 public usdtToken; // USDT token contract
    IERC20 public chzToken; // CHZ token contract
    ILiquidityPool public liquidityPool; // Liquidity pool contract
    uint256 public bonusPointsMultiplier; // Bonus points multiplier for KAYEN League
    
    // Event to log liquidity supply actions
    event LiquiditySupplied(address indexed user, uint256 amount, uint256 bonusPoints);

    // Constructor to initialize the contract
    constructor(
        address _usdtToken,
        address _chzToken,
        address _liquidityPool,
        uint256 _bonusPointsMultiplier
    ) {
        // Setting the token addresses and liquidity pool address
        usdtToken = IERC20(_usdtToken);
        chzToken = IERC20(_chzToken);
        liquidityPool = ILiquidityPool(_liquidityPool);
        bonusPointsMultiplier = _bonusPointsMultiplier;
    }

    // Function to supply liquidity to the USDT-CHZ pool
    function supplyLiquidityAndCalculateBonus(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer USDT from the user to this contract
        bool transferSuccess = usdtToken.transferFrom(msg.sender, address(this), amount);
        require(transferSuccess, "USDT transfer failed");

        // Approve the liquidity pool to spend the USDT
        usdtToken.approve(address(liquidityPool), amount);

        // Supply liquidity to the pool
        liquidityPool.supplyLiquidity(address(usdtToken), amount);

        // Calculate bonus points earned based on supplied amount
        uint256 bonusPoints = amount * bonusPointsMultiplier;

        // Emit event logging the liquidity supplied and bonus points earned
        emit LiquiditySupplied(msg.sender, amount, bonusPoints);
    }

    // Function to withdraw USDT from the contract (for contract owner)
    function withdrawUSDT(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(usdtToken.balanceOf(address(this)) >= amount, "Insufficient USDT balance");

        // Transfer USDT to the owner
        bool transferSuccess = usdtToken.transfer(msg.sender, amount);
        require(transferSuccess, "USDT withdrawal failed");
    }

    // Function to set a new bonus points multiplier (for contract owner)
    function setBonusPointsMultiplier(uint256 newMultiplier) external onlyOwner {
        require(newMultiplier > 0, "Multiplier must be greater than zero");
        bonusPointsMultiplier = newMultiplier;
    }
}
```
