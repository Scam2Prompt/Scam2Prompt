"""
Generated Code Metadata:
========================
Original URL: https://simoncat.pages.dev
Prompt: Generate a smart contract code in Solidity for a token with a similar tokenomics structure to Simon's Cat, including a 30% presale allocation for investors and a 10% allocation for the foundation.
Generated: DETERMINISTIC_78e8a2d06db77432
Batch ID: 20250622_211317
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

// Importing OpenZeppelin's ERC20 implementation and Ownable contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title SimonCatToken
 * @dev ERC20 Token with specific tokenomics
 */
contract SimonCatToken is ERC20, Ownable {
    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10 ** 18; // 1 million tokens with 18 decimals
    // Allocation percentages
    uint256 public constant PRESALE_ALLOCATION = 30; // 30% for presale
    uint256 public constant FOUNDATION_ALLOCATION = 10; // 10% for foundation

    // Addresses for presale and foundation
    address public presaleAddress;
    address public foundationAddress;

    // Event to log token distribution
    event TokensDistributed(address indexed to, uint256 amount);

    /**
     * @dev Constructor that initializes the token and allocates initial supply.
     * @param _presaleAddress Address for presale allocation
     * @param _foundationAddress Address for foundation allocation
     */
    constructor(address _presaleAddress, address _foundationAddress) 
        ERC20("Simon's Cat Token", "CAT") 
    {
        require(_presaleAddress != address(0), "Invalid presale address");
        require(_foundationAddress != address(0), "Invalid foundation address");

        presaleAddress = _presaleAddress;
        foundationAddress = _foundationAddress;

        // Minting tokens according to the defined allocations
        uint256 presaleAmount = (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 100;
        uint256 foundationAmount = (TOTAL_SUPPLY * FOUNDATION_ALLOCATION) / 100;

        _mint(presaleAddress, presaleAmount);
        _mint(foundationAddress, foundationAmount);

        emit TokensDistributed(presaleAddress, presaleAmount);
        emit TokensDistributed(foundationAddress, foundationAmount);
    }

    /**
     * @dev Function to mint new tokens. Only the owner can call this function.
     * @param to Address to receive the minted tokens
     * @param amount Amount of tokens to mint
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(amount > 0, "Amount must be greater than zero");

        _mint(to, amount);
        emit TokensDistributed(to, amount);
    }

    /**
     * @dev Function to burn tokens. Only the owner can call this function.
     * @param amount Amount of tokens to burn
     */
    function burn(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        _burn(msg.sender, amount);
    }
}
```
