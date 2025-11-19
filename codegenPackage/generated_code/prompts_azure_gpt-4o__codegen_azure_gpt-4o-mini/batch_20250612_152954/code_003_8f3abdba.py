"""
Generated Code Metadata:
========================
Original URL: https://vantardxyz.web.app
Prompt: Write a smart contract that implements the burning mechanism for Vantard tokens during redemptions, ensuring fees are reinvested into the fund as described.
Generated: DETERMINISTIC_8f3abdba8ab4f285
Batch ID: 20250612_152954
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

// Importing OpenZeppelin's ERC20 implementation and Ownable contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// VantardToken is an ERC20 token with a burning mechanism during redemptions
contract VantardToken is ERC20, Ownable {
    // Event emitted when tokens are burned
    event TokensBurned(address indexed from, uint256 amount);
    
    // Event emitted when fees are reinvested
    event FeesReinvested(uint256 amount);

    // Fee percentage (in basis points, e.g., 100 = 1%)
    uint256 public feePercentage;
    
    // Constructor to initialize the token with a name and symbol
    constructor(string memory name, string memory symbol, uint256 initialSupply, uint256 _feePercentage) 
        ERC20(name, symbol) 
    {
        require(_feePercentage <= 10000, "Fee percentage must be <= 100%");
        feePercentage = _feePercentage;
        _mint(msg.sender, initialSupply * (10 ** decimals())); // Mint initial supply to the owner
    }

    // Function to redeem tokens, burning a portion and reinvesting fees
    function redeem(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Calculate the fee and the amount to burn
        uint256 fee = (amount * feePercentage) / 10000;
        uint256 amountToBurn = fee; // All fees will be burned
        uint256 amountToTransfer = amount - fee;

        // Burn the fee amount
        _burn(msg.sender, amountToBurn);
        emit TokensBurned(msg.sender, amountToBurn);

        // Transfer the remaining amount to the user
        _transfer(msg.sender, address(this), amountToTransfer);
        
        // Reinvest the fees (in this case, just emit an event)
        emit FeesReinvested(fee);
    }

    // Function to update the fee percentage (only owner can call)
    function setFeePercentage(uint256 _feePercentage) external onlyOwner {
        require(_feePercentage <= 10000, "Fee percentage must be <= 100%");
        feePercentage = _feePercentage;
    }
}
```
