"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereum.com.tr
Prompt: Generate Solidity code for a decentralized application (ĐApp) that utilizes Ethereum's "kripto yakıt" concept to manage energy credits, inspired by the analogy of Ethereum as "petrol" from ethereum.com.tr.
Generated: DETERMINISTIC_1d19e4371bce1f92
Batch ID: 20250612_151308
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

/**
 * @title EnergyCreditsManager
 * @notice A decentralized application (ĐApp) to manage energy credits ("kripto yakıt").
 * Inspired by Ethereum's analogy of being "petrol" for the blockchain economy.
 */
contract EnergyCreditsManager {
    // Struct to represent an energy credit holder
    struct Holder {
        uint256 balance; // Balance of energy credits
        bool exists;     // Indicates if the holder exists
    }

    // State variable to store the address of the contract owner
    address public owner;

    // Mapping to store holders and their energy credits
    mapping(address => Holder) public holders;

    // Total supply of energy credits
    uint256 public totalSupply;

    // Events to notify when important actions are performed
    event EnergyCreditsMinted(address indexed to, uint256 amount);
    event EnergyCreditsTransferred(address indexed from, address indexed to, uint256 amount);
    event EnergyCreditsBurned(address indexed from, uint256 amount);

    /**
     * @dev Modifier to enforce that only the contract owner can call certain functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function.");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * Sets the message sender as the owner of the contract.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @notice Mint new energy credits to a specific address.
     * @param to The address to receive the new energy credits.
     * @param amount The amount of energy credits to mint.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address.");
        require(amount > 0, "Mint amount must be greater than zero.");
        
        // Create a holder if they don't exist already
        if (!holders[to].exists) {
            holders[to] = Holder({ balance: 0, exists: true });
        }
        
        holders[to].balance += amount;
        totalSupply += amount;

        emit EnergyCreditsMinted(to, amount);
    }

    /**
     * @notice Transfer energy credits from one address to another.
     * @param to The recipient address.
     * @param amount The amount of energy credits to transfer.
     */
    function transfer(address to, uint256 amount) external {
        require(to != address(0), "Cannot transfer to the zero address.");
        require(holders[msg.sender].balance >= amount, "Insufficient balance.");
        require(amount > 0, "Transfer amount must be greater than zero.");
        
        // Ensure the recipient exists
        if (!holders[to].exists) {
            holders[to] = Holder({ balance: 0, exists: true });
        }

        holders[msg.sender].balance -= amount;
        holders[to].balance += amount;

        emit EnergyCreditsTransferred(msg.sender, to, amount);
    }

    /**
     * @notice Burn energy credits from the sender's account.
     * @param amount The amount of energy credits to burn.
     */
    function burn(uint256 amount) external {
        require(holders[msg.sender].balance >= amount, "Insufficient balance.");
        require(amount > 0, "Burn amount must be greater than zero.");

        holders[msg.sender].balance -= amount;
        totalSupply -= amount;

        emit EnergyCreditsBurned(msg.sender, amount);
    }

    /**
     * @notice Retrieve the balance of energy credits for a specific address.
     * @param account The address whose balance is being queried.
     * @return The balance of energy credits for the specified address.
     */
    function balanceOf(address account) external view returns (uint256) {
        require(account != address(0), "Zero address is invalid.");
        return holders[account].balance;
    }
}
```
