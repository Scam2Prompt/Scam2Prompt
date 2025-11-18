"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://frax-finances.pages.dev
Prompt: Write a Solidity contract that utilizes Frax Price Index (FPI) as a stablecoin pegged to a basket of consumer goods (CPI). Include functionality to calculate and display the peg properties.
Generated: DETERMINISTIC_67ef289a89c25d4f
Batch ID: 20250612_150327
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
 * @title FPIStablecoin
 * @dev A stablecoin pegged to the Frax Price Index (FPI), which represents a basket of consumer goods.
 */
contract FPIStablecoin {
    // Stablecoin details
    string public constant name = "Frax Price Index Stablecoin";
    string public constant symbol = "FPI";
    uint8 public constant decimals = 18;
    
    // Total supply of FPI tokens
    uint256 public totalSupply;

    // Mapping to track balances of each address
    mapping(address => uint256) private balances;

    // Owner of the contract
    address public owner;

    // Placeholder for the Consumer Price Index (CPI) basket peg value
    uint256 public cpiPegValue;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event PegUpdated(uint256 newPegValue);

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Access restricted to owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with an owner and initial peg value.
     */
    constructor(uint256 initialPegValue) {
        require(initialPegValue > 0, "Initial peg value must be greater than zero");
        owner = msg.sender;
        cpiPegValue = initialPegValue;
    }

    /**
     * @dev Function to mint new FPI tokens. Restricted to the owner.
     * @param to Address to receive the minted tokens.
     * @param amount Number of tokens to mint.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to zero address");
        require(amount > 0, "Mint amount must be greater than zero");

        balances[to] += amount;
        totalSupply += amount;

        emit Transfer(address(0), to, amount);
    }

    /**
     * @dev Function to transfer tokens between addresses.
     * @param to Recipient address.
     * @param amount Number of tokens to transfer.
     */
    function transfer(address to, uint256 amount) external returns (bool) {
        require(to != address(0), "Cannot transfer to zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[to] += amount;

        emit Transfer(msg.sender, to, amount);
        return true;
    }

    /**
     * @dev Function to get the balance of a specific address.
     * @param account Address whose balance is to be checked.
     * @return Balance of the account.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Function to update the CPI peg value. Restricted to the owner.
     * @param newPegValue Updated peg value.
     */
    function updatePegValue(uint256 newPegValue) external onlyOwner {
        require(newPegValue > 0, "Peg value must be greater than zero");
        cpiPegValue = newPegValue;

        emit PegUpdated(newPegValue);
    }

    /**
     * @dev Function to get the current CPI peg value.
     * @return Current CPI peg value.
     */
    function getPegValue() external view returns (uint256) {
        return cpiPegValue;
    }
}
```
