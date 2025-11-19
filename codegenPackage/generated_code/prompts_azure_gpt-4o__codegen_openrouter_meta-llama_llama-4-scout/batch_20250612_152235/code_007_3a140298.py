"""
Generated Code Metadata:
========================
Original URL: https://bafybeiexkodjd2izwx6r53x5g4q54yhqmiifywanhuecvkkdn2yyxq3rpu.ipfs.dweb.link
Prompt: Write a function in Solidity that enforces the total token supply limit of 100,000,000 ALIEN during the presale, ensuring no additional tokens are minted beyond this limit.
Generated: DETERMINISTIC_3a140298792c088f
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
pragma solidity ^0.8.0;

/**
 * @title ALIEN Presale Contract
 * @author [Your Name]
 * @notice This contract enforces the total token supply limit of 100,000,000 ALIEN during the presale.
 */
contract ALIENPresale {
    // Total token supply limit
    uint256 public constant TOTAL_SUPPLY_LIMIT = 100_000_000 ether;

    // Current total supply
    uint256 public totalSupply;

    // Mapping of token balances
    mapping(address => uint256) public balances;

    /**
     * @notice Initializes the contract with an initial supply.
     * @param initialSupply The initial supply of tokens.
     */
    constructor(uint256 initialSupply) {
        // Ensure initial supply does not exceed the total supply limit
        require(initialSupply <= TOTAL_SUPPLY_LIMIT, "Initial supply exceeds the total supply limit.");

        totalSupply = initialSupply;
        balances[msg.sender] = initialSupply;
    }

    /**
     * @notice Mints tokens to the specified address during the presale.
     * @param to The address to mint tokens to.
     * @param amount The amount of tokens to mint.
     */
    function mint(address to, uint256 amount) public {
        // Ensure the total supply does not exceed the limit
        require(totalSupply + amount <= TOTAL_SUPPLY_LIMIT, "Minting exceeds the total supply limit.");

        totalSupply += amount;
        balances[to] += amount;
    }

    /**
     * @notice Transfers tokens from the sender to the specified address.
     * @param to The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     */
    function transfer(address to, uint256 amount) public {
        require(balances[msg.sender] >= amount, "Insufficient balance.");
        balances[msg.sender] -= amount;
        balances[to] += amount;
    }

    /**
     * @notice Returns the balance of the specified address.
     * @param owner The address to retrieve the balance for.
     * @return The balance of the specified address.
     */
    function balanceOf(address owner) public view returns (uint256) {
        return balances[owner];
    }
}
```
