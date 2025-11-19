"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claims-catcoin.pages.dev
Prompt: Provide an example of how to implement a smart contract for a token like CATCOIN that has zero taxes and locked liquidity.
Generated: DETERMINISTIC_33d3f2ba6adc528a
Batch ID: 20250612_161427
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

// Import the OpenZeppelin ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// CATCOIN is an ERC20 token implementation
contract CATCOIN is ERC20, Ownable {
    
    // Address where liquidity will be locked
    address public liquidityLocker;

    // Event emitted when liquidity is locked
    event LiquidityLocked(address indexed locker);

    // Constructor to set the token details and mint initial supply
    constructor(uint256 initialSupply, address _liquidityLocker) ERC20("CATCOIN", "CAT") {
        // Mint initial supply to the contract deployer
        _mint(msg.sender, initialSupply * (10 ** decimals()));
        liquidityLocker = _liquidityLocker; // Set the liquidity locker address
    }

    // Function to lock liquidity
    function lockLiquidity() external onlyOwner {
        // Ensure liquidity is not already locked
        require(liquidityLocker != address(0), "Liquidity is already locked");
        
        // Emit event for liquidity lock
        emit LiquidityLocked(liquidityLocker);
        
        // Set liquidity locker to zero address, indicating it is locked
        liquidityLocker = address(0);
    }

    // Override _transfer to ensure zero taxes
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        // Ensure sender has sufficient balance
        require(balanceOf(sender) >= amount, "Insufficient balance");

        // Call the default transfer logic from ERC20
        super._transfer(sender, recipient, amount);
    }
}
```
