"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tenderize.xyz
Prompt: Write a tutorial for integrating ERC-20 compliant tenderized tokens into a DeFi lending protocol, allowing users to leverage their staked assets.
Generated: DETERMINISTIC_81ab68781f6eff0f
Batch ID: 20250612_145913
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

// Import interfaces for ERC20 and the lending protocol
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the DeFi lending protocol
interface IDeFiLendingProtocol {
    function deposit(address asset, uint256 amount) external;
    function withdraw(address asset, uint256 amount) external;
}

/**
 * @title TenderizedToken
 * @dev ERC20 compliant token representing the tenderized version of staked assets
 */
contract TenderizedToken is ERC20, Ownable {
    // Address of the DeFi lending protocol
    IDeFiLendingProtocol public lendingProtocol;

    // Mapping to track user deposits
    mapping(address => uint256) public userDeposits;

    // Event emitted when assets are deposited
    event AssetsDeposited(address indexed user, uint256 amount);
    
    // Event emitted when assets are withdrawn
    event AssetsWithdrawn(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the token and lending protocol
     * @param name The name of the token
     * @param symbol The symbol of the token
     * @param _lendingProtocol The address of the DeFi lending protocol
     */
    constructor(string memory name, string memory symbol, address _lendingProtocol) 
        ERC20(name, symbol) 
    {
        require(_lendingProtocol != address(0), "Invalid lending protocol address");
        lendingProtocol = IDeFiLendingProtocol(_lendingProtocol);
    }

    /**
     * @dev Deposit staked assets into the lending protocol
     * @param amount The amount of tokens to deposit
     */
    function deposit(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer the tokens to this contract
        transfer(address(this), amount);

        // Update user deposits
        userDeposits[msg.sender] += amount;

        // Deposit into the lending protocol
        lendingProtocol.deposit(address(this), amount);

        emit AssetsDeposited(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked assets from the lending protocol
     * @param amount The amount of tokens to withdraw
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(userDeposits[msg.sender] >= amount, "Insufficient deposit balance");

        // Withdraw from the lending protocol
        lendingProtocol.withdraw(address(this), amount);

        // Update user deposits
        userDeposits[msg.sender] -= amount;

        // Transfer the tokens back to the user
        transfer(msg.sender, amount);

        emit AssetsWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Allow the owner to update the lending protocol address
     * @param newLendingProtocol The new lending protocol address
     */
    function updateLendingProtocol(address newLendingProtocol) external onlyOwner {
        require(newLendingProtocol != address(0), "Invalid lending protocol address");
        lendingProtocol = IDeFiLendingProtocol(newLendingProtocol);
    }
}
```

This code is a complete implementation of a tenderized token that integrates with a DeFi lending protocol, allowing users to leverage their staked assets. It includes comments to explain each part of the code and follows best practices for Solidity development.
