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

/**
 * @title SimonsCatToken
 * @dev ERC20 Token with tokenomics similar to Simon's Cat.
 *      Includes presale allocation (30%) and foundation allocation (10%).
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract SimonsCatToken is ERC20, Ownable {
    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens

    // Allocation percentages
    uint256 public constant PRESALE_ALLOCATION = (TOTAL_SUPPLY * 30) / 100; // 30% for presale
    uint256 public constant FOUNDATION_ALLOCATION = (TOTAL_SUPPLY * 10) / 100; // 10% for foundation

    // Addresses for allocations
    address public presaleWallet;
    address public foundationWallet;

    /**
     * @dev Constructor to initialize the token and allocate initial supply.
     * @param _presaleWallet Address for presale allocation.
     * @param _foundationWallet Address for foundation allocation.
     */
    constructor(address _presaleWallet, address _foundationWallet) ERC20("SimonsCatToken", "SCT") {
        require(_presaleWallet != address(0), "Presale wallet address cannot be zero");
        require(_foundationWallet != address(0), "Foundation wallet address cannot be zero");

        presaleWallet = _presaleWallet;
        foundationWallet = _foundationWallet;

        // Mint tokens to presale wallet
        _mint(presaleWallet, PRESALE_ALLOCATION);

        // Mint tokens to foundation wallet
        _mint(foundationWallet, FOUNDATION_ALLOCATION);

        // Mint remaining tokens to contract owner
        uint256 remainingSupply = TOTAL_SUPPLY - PRESALE_ALLOCATION - FOUNDATION_ALLOCATION;
        _mint(owner(), remainingSupply);
    }

    /**
     * @dev Function to update the presale wallet address.
     * @param _newPresaleWallet New address for presale allocation.
     */
    function updatePresaleWallet(address _newPresaleWallet) external onlyOwner {
        require(_newPresaleWallet != address(0), "New presale wallet address cannot be zero");
        presaleWallet = _newPresaleWallet;
    }

    /**
     * @dev Function to update the foundation wallet address.
     * @param _newFoundationWallet New address for foundation allocation.
     */
    function updateFoundationWallet(address _newFoundationWallet) external onlyOwner {
        require(_newFoundationWallet != address(0), "New foundation wallet address cannot be zero");
        foundationWallet = _newFoundationWallet;
    }
}
```
