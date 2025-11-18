"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeidlrlbotyuulbnias66uqhqkoy7f4px26fibleghikvgo24hd7tje.ipfs.dweb.link
Prompt: Write a smart contract in Solidity that integrates Moonwell's lending protocol for supplying assets and earning interest, ensuring compatibility with Moonbeam and Moonriver networks.
Generated: DETERMINISTIC_be0d47a0070c875d
Batch ID: 20250612_152358
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for Moonwell's lending protocol
interface IMoonwell {
    function supply(address asset, uint256 amount) external;
    function withdraw(address asset, uint256 amount) external;
    function getSupplyRate(address asset) external view returns (uint256);
}

contract MoonwellLending is Ownable {
    // State variables
    IMoonwell public moonwell; // Moonwell lending protocol instance
    mapping(address => uint256) public userBalances; // User balances

    // Events
    event Supplied(address indexed user, address indexed asset, uint256 amount);
    event Withdrawn(address indexed user, address indexed asset, uint256 amount);

    // Constructor to set the Moonwell contract address
    constructor(address _moonwell) {
        require(_moonwell != address(0), "Invalid Moonwell address");
        moonwell = IMoonwell(_moonwell);
    }

    // Function to supply assets to Moonwell
    function supplyAssets(address asset, uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(asset).transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Approve the Moonwell contract to spend the asset
        IERC20(asset).approve(address(moonwell), amount);

        // Supply assets to Moonwell
        moonwell.supply(asset, amount);

        // Update user balance
        userBalances[msg.sender] += amount;

        emit Supplied(msg.sender, asset, amount);
    }

    // Function to withdraw assets from Moonwell
    function withdrawAssets(address asset, uint256 amount) external {
        require(userBalances[msg.sender] >= amount, "Insufficient balance");

        // Withdraw assets from Moonwell
        moonwell.withdraw(asset, amount);

        // Update user balance
        userBalances[msg.sender] -= amount;

        // Transfer the asset back to the user
        require(IERC20(asset).transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(msg.sender, asset, amount);
    }

    // Function to check the supply rate of an asset
    function getSupplyRate(address asset) external view returns (uint256) {
        return moonwell.getSupplyRate(asset);
    }

    // Function to set a new Moonwell contract address (only by owner)
    function setMoonwellAddress(address _moonwell) external onlyOwner {
        require(_moonwell != address(0), "Invalid Moonwell address");
        moonwell = IMoonwell(_moonwell);
    }
}
```
