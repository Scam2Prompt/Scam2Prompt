"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bobothebear.pages.dev
Prompt: Generate a smart contract for a meme token inspired by Bobo the Bear, including features like 0% tax and liquidity burned.
Generated: DETERMINISTIC_022cdbfd8acc0e1c
Batch ID: 20250612_163601
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

// Importing OpenZeppelin's ERC20 contract and Ownable contract for standard functionality and ownership control
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title BoboToken
 * @dev ERC20 Token that represents Bobo the Bear meme token with 0% tax and liquidity burned.
 */
contract BoboToken is ERC20, Ownable {
    // Variable to store the liquidity pool address
    address public liquidityPool;
    
    // Event emitted when liquidity is burned
    event LiquidityBurned(uint256 amount);
    
    /**
     * @dev Constructor that initializes the token with a name and symbol and mints an initial supply.
     * @param initialSupply The initial supply of tokens to mint.
     */
    constructor(uint256 initialSupply) ERC20("Bobo the Bear", "BOBO") {
        // Mint the initial supply to the contract deployer
        _mint(msg.sender, initialSupply * (10 ** decimals()));
    }
    
    /**
     * @dev Function to set the liquidity pool address. Only callable by the owner.
     * @param _liquidityPool The address of the liquidity pool.
     */
    function setLiquidityPool(address _liquidityPool) external onlyOwner {
        require(_liquidityPool != address(0), "Invalid address");
        liquidityPool = _liquidityPool;
    }

    /**
     * @dev Function to burn liquidity. Only callable by the owner.
     * @param amount The amount of tokens to burn.
     */
    function burnLiquidity(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(address(this)) >= amount, "Insufficient balance to burn");
        
        // Transfer the specified amount from the contract to the burn address
        _burn(address(this), amount);
        
        // Emit an event for the burned liquidity
        emit LiquidityBurned(amount);
    }
    
    /**
     * @dev Override the _transfer function to implement 0% tax on transactions.
     * @param sender The address sending the tokens.
     * @param recipient The address receiving the tokens.
     * @param amount The amount of tokens to transfer.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        // Call the parent's transfer function without any tax deduction
        super._transfer(sender, recipient, amount);
    }
}
```
