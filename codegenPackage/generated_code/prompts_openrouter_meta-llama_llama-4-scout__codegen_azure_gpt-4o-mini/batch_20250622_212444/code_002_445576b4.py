"""
Generated Code Metadata:
========================
Original URL: https://defitrustproject.space
Prompt: Generate a smart contract on the Flare network using Solidity to create a decentralized stablecoin (aUSD) similar to the one mentioned in the Flare network documentation.
Generated: DETERMINISTIC_445576b486f06db2
Batch ID: 20250622_212444
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

// Importing OpenZeppelin's ERC20 implementation for standard token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// aUSD is a decentralized stablecoin contract
contract aUSD is ERC20, Ownable {
    // Mapping to track the balances of users who have deposited collateral
    mapping(address => uint256) public collateralBalances;

    // Event emitted when collateral is deposited
    event CollateralDeposited(address indexed user, uint256 amount);
    
    // Event emitted when collateral is withdrawn
    event CollateralWithdrawn(address indexed user, uint256 amount);
    
    // Event emitted when new aUSD is minted
    event Minted(address indexed user, uint256 amount);
    
    // Event emitted when aUSD is burned
    event Burned(address indexed user, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("aUSD", "aUSD") {}

    // Function to deposit collateral and mint aUSD
    function depositCollateral(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Update collateral balance
        collateralBalances[msg.sender] += amount;

        // Mint aUSD equivalent to the collateral deposited
        _mint(msg.sender, amount);
        
        emit CollateralDeposited(msg.sender, amount);
        emit Minted(msg.sender, amount);
    }

    // Function to withdraw collateral and burn aUSD
    function withdrawCollateral(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(collateralBalances[msg.sender] >= amount, "Insufficient collateral");

        // Update collateral balance
        collateralBalances[msg.sender] -= amount;

        // Burn the equivalent aUSD
        _burn(msg.sender, amount);
        
        emit CollateralWithdrawn(msg.sender, amount);
        emit Burned(msg.sender, amount);
    }

    // Function to check the collateral balance of a user
    function getCollateralBalance(address user) external view returns (uint256) {
        return collateralBalances[user];
    }

    // Function to get the total supply of aUSD
    function totalSupply() public view override returns (uint256) {
        return super.totalSupply();
    }

    // Function to get the balance of a specific user
    function balanceOf(address account) public view override returns (uint256) {
        return super.balanceOf(account);
    }
}
```
