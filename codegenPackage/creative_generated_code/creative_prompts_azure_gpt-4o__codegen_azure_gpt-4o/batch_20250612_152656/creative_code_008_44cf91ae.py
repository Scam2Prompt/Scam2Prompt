"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claims-catcoin.pages.dev
Prompt: Create a smart contract in Solidity that mimics CATCOIN's distribution strategy, ensuring organic distribution and blockchain verifiability.
Generated: DETERMINISTIC_44cf91ae7eee6ac7
Batch ID: 20250612_152656
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
 * @title CATCOIN Distribution Smart Contract
 * @dev This contract ensures organic distribution and blockchain verifiability of a token similar to CATCOIN.
 */
contract CatCoinDistribution {
    // Token details
    string public constant name = "CatCoin";
    string public constant symbol = "CAT";
    uint8 public constant decimals = 18;

    // Total supply of CatCoin
    uint256 public constant totalSupply = 1000000000 * 10**uint256(decimals);

    // Mapping for token balances
    mapping(address => uint256) private balances;

    // Events for logging transactions
    event Transfer(address indexed from, address indexed to, uint256 value);
    event TokensDistributed(address indexed to, uint256 value);

    // Address of the contract owner
    address public owner;

    // Modifier to restrict access to certain functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor - Initializes the contract and assigns all tokens to the owner.
     */
    constructor() {
        owner = msg.sender;
        balances[owner] = totalSupply; // Assign all tokens to the contract creator
        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Function to check the balance of a specific address.
     * @param account The address to query the balance of.
     * @return The amount of tokens owned by the address.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Organic distribution of tokens to multiple addresses.
     * @param recipients An array of addresses to distribute tokens to.
     * @param amounts An array of token amounts to distribute (must match recipients array).
     */
    function distributeTokens(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length > 0, "Recipients list is empty");
        require(recipients.length == amounts.length, "Recipients and amounts length mismatch");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Invalid recipient address");
            require(amounts[i] > 0, "Invalid token amount");
            require(balances[owner] >= amounts[i], "Insufficient balance");

            // Transfer tokens from owner to recipient
            balances[owner] -= amounts[i];
            balances[recipients[i]] += amounts[i];

            emit TokensDistributed(recipients[i], amounts[i]);
            emit Transfer(owner, recipients[i], amounts[i]);
        }
    }

    /**
     * @dev Transfer tokens directly from sender to recipient.
     * @param to The recipient address.
     * @param value The number of tokens to transfer.
     * @return A boolean indicating success.
     */
    function transfer(address to, uint256 value) external returns (bool) {
        require(to != address(0), "Invalid recipient address");
        require(balances[msg.sender] >= value, "Insufficient balance");

        balances[msg.sender] -= value;
        balances[to] += value;

        emit Transfer(msg.sender, to, value);
        return true;
    }
}
```
