"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seedify-cs6.pages.dev
Prompt: Write a Solidity contract that integrates with Seedify's blockchain-based lending protocol "SOIL" to enable lending and borrowing of stablecoins.
Generated: DETERMINISTIC_946cdc2edb81c105
Batch ID: 20250612_152000
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

// Import required interfaces and contracts
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for interacting with the SOIL lending protocol
interface ISOIL {
    function lend(uint256 amount) external;
    function borrow(uint256 amount) external;
    function repay(uint256 amount) external;
    function withdraw(uint256 amount) external;
}

// Contract to facilitate lending and borrowing on Seedify's SOIL protocol
contract SeedifyLending is Ownable {
    // Stablecoin token to be used for lending and borrowing
    IERC20 public stablecoin;
    // SOIL lending protocol interface
    ISOIL public soil;

    // Events to log actions
    event Lent(address indexed user, uint256 amount);
    event Borrowed(address indexed user, uint256 amount);
    event Repaid(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to initialize the contract with stablecoin and SOIL protocol address
    constructor(address _stablecoin, address _soil) {
        require(_stablecoin != address(0), "Stablecoin address cannot be zero");
        require(_soil != address(0), "SOIL address cannot be zero");
        
        stablecoin = IERC20(_stablecoin);
        soil = ISOIL(_soil);
    }

    // Function to lend stablecoins to the SOIL protocol
    function lend(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer stablecoins from user to this contract
        stablecoin.transferFrom(msg.sender, address(this), amount);

        // Approve the SOIL contract to spend the stablecoins
        stablecoin.approve(address(soil), amount);

        // Lend the stablecoins to the SOIL protocol
        soil.lend(amount);

        emit Lent(msg.sender, amount);
    }

    // Function to borrow stablecoins from the SOIL protocol
    function borrow(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Borrow the stablecoins from the SOIL protocol
        soil.borrow(amount);

        // Transfer the borrowed stablecoins to the user
        stablecoin.transfer(msg.sender, amount);

        emit Borrowed(msg.sender, amount);
    }

    // Function to repay borrowed stablecoins to the SOIL protocol
    function repay(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer stablecoins from user to this contract
        stablecoin.transferFrom(msg.sender, address(this), amount);

        // Approve the SOIL contract to spend the stablecoins
        stablecoin.approve(address(soil), amount);

        // Repay the borrowed amount to the SOIL protocol
        soil.repay(amount);

        emit Repaid(msg.sender, amount);
    }

    // Function to withdraw lent stablecoins from the SOIL protocol
    function withdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");

        // Withdraw the stablecoins from the SOIL protocol
        soil.withdraw(amount);

        // Transfer the withdrawn stablecoins to the owner
        stablecoin.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Function to check the balance of stablecoins held by this contract
    function balance() external view returns (uint256) {
        return stablecoin.balanceOf(address(this));
    }
}
```
