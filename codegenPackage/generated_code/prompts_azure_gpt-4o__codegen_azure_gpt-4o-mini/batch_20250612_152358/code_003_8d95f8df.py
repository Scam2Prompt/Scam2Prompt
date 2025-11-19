"""
Generated Code Metadata:
========================
Original URL: https://bafybeidfgwggshi5syqnklufswynx2u6rumuvgp4jl6n4lbqsolbeshdga.ipfs.dweb.link
Prompt: Create a Solidity function that implements a disinflationary issuance mechanism for the $USUAL token, ensuring non-dilutive features and alignment with user interests.
Generated: DETERMINISTIC_8d95f8df68f067ef
Batch ID: 20250612_152358
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title USUAL Token
 * @dev ERC20 Token with a disinflationary issuance mechanism
 */
contract USUAL is ERC20, Ownable {
    // Total supply cap for the token
    uint256 public constant MAX_SUPPLY = 1_000_000 * 10 ** decimals();
    
    // Current issuance rate (in basis points)
    uint256 public issuanceRate; // e.g., 100 = 1%
    
    // Event emitted when the issuance rate is updated
    event IssuanceRateUpdated(uint256 newRate);
    
    // Event emitted when tokens are minted
    event TokensMinted(address indexed to, uint256 amount);

    /**
     * @dev Constructor to initialize the token with a name and symbol.
     * @param _name Name of the token
     * @param _symbol Symbol of the token
     * @param _initialIssuanceRate Initial issuance rate in basis points
     */
    constructor(string memory _name, string memory _symbol, uint256 _initialIssuanceRate) 
        ERC20(_name, _symbol) 
    {
        require(_initialIssuanceRate <= 10000, "Issuance rate must be <= 100%");
        issuanceRate = _initialIssuanceRate;
    }

    /**
     * @dev Function to mint new tokens based on the current issuance rate.
     * @param to Address to receive the minted tokens
     * @return success Indicates if the minting was successful
     */
    function mintTokens(address to) external onlyOwner returns (bool success) {
        require(to != address(0), "Cannot mint to the zero address");
        
        // Calculate the amount to mint based on the current supply and issuance rate
        uint256 currentSupply = totalSupply();
        uint256 amountToMint = (currentSupply * issuanceRate) / 10000;

        // Ensure that minting does not exceed the maximum supply
        require(currentSupply + amountToMint <= MAX_SUPPLY, "Minting exceeds max supply");

        // Mint the tokens
        _mint(to, amountToMint);
        
        emit TokensMinted(to, amountToMint);
        return true;
    }

    /**
     * @dev Function to update the issuance rate.
     * @param newRate New issuance rate in basis points
     */
    function updateIssuanceRate(uint256 newRate) external onlyOwner {
        require(newRate <= 10000, "Issuance rate must be <= 100%");
        issuanceRate = newRate;
        emit IssuanceRateUpdated(newRate);
    }
}
```
