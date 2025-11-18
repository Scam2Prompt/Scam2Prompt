"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethena-fi.us
Prompt: Create a smart contract in Solidity that mirrors Ethena.fi’s approach to transparency and security in stablecoin transactions.
Generated: DETERMINISTIC_cbf2157492d8631c
Batch ID: 20250612_153925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title Transparent Stablecoin Contract
 * @dev This contract implements a simple stablecoin functionality with transparency and security.
 */
contract TransparentStablecoin {
    // Mapping to hold balances of each account
    mapping(address => uint256) private balances;

    // Total supply of the stablecoin
    uint256 private _totalSupply;

    // Address of the contract owner
    address public owner;

    // Events to provide transparency in all transactions
    event Mint(address indexed to, uint256 amount);
    event Burn(address indexed from, uint256 amount);
    event Transfer(address indexed from, address indexed to, uint256 amount);

    /**
     * @dev Modifier to restrict access to certain functions
     *      to the contract owner only.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the contract owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to mint new stablecoins.
     * @param to The address to receive the minted stablecoins.
     * @param amount The amount of stablecoins to mint.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Mint amount must be greater than zero");

        balances[to] += amount;
        _totalSupply += amount;

        emit Mint(to, amount);
    }

    /**
     * @dev Function to burn stablecoins from an account.
     * @param from The address from which stablecoins are burned.
     * @param amount The amount of stablecoins to burn.
     */
    function burn(address from, uint256 amount) external onlyOwner {
        require(from != address(0), "Cannot burn from the zero address");
        require(amount > 0, "Burn amount must be greater than zero");
        require(balances[from] >= amount, "Insufficient balance to burn");

        balances[from] -= amount;
        _totalSupply -= amount;

        emit Burn(from, amount);
    }

    /**
     * @dev Function to transfer stablecoins between accounts.
     * @param to The recipient address.
     * @param amount The amount of stablecoins to transfer.
     */
    function transfer(address to, uint256 amount) external {
        require(to != address(0), "Cannot transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[to] += amount;

        emit Transfer(msg.sender, to, amount);
    }

    /**
     * @dev Function to get the balance of an account.
     * @param account The address of the account.
     * @return The balance of the account.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Function to get the total supply of the stablecoin.
     * @return The total supply of the stablecoin.
     */
    function totalSupply() external view returns (uint256) {
        return _totalSupply;
    }
}
```
