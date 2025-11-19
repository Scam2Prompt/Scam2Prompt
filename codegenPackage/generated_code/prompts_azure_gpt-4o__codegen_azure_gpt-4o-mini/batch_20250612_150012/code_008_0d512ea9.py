"""
Generated Code Metadata:
========================
Original URL: https://xyzverse-in.web.app
Prompt: Develop a smart contract in Solidity to distribute XYZVerse tokens during the Token Generation Event (TGE) and ensure accurate allocation based on the presale percentages provided in the tokenomics.
Generated: DETERMINISTIC_0d512ea97a2d3b5a
Batch ID: 20250612_150012
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

// Importing the OpenZeppelin ERC20 contract for token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for XYZVerse Token Generation Event (TGE)
contract XYZVerseTGE is ERC20, Ownable {
    // Mapping to track presale allocations
    mapping(address => uint256) public presaleAllocations;

    // Total supply of tokens for the TGE
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10 ** decimals();

    // Event to log token distribution
    event TokensDistributed(address indexed beneficiary, uint256 amount);

    // Constructor to initialize the token
    constructor() ERC20("XYZVerse", "XYZV") {
        // Mint total supply to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    // Function to set presale allocations
    function setPresaleAllocations(address[] calldata beneficiaries, uint256[] calldata amounts) external onlyOwner {
        require(beneficiaries.length == amounts.length, "Beneficiaries and amounts length mismatch");
        
        for (uint256 i = 0; i < beneficiaries.length; i++) {
            require(beneficiaries[i] != address(0), "Invalid address");
            require(amounts[i] > 0, "Amount must be greater than zero");
            presaleAllocations[beneficiaries[i]] = amounts[i];
        }
    }

    // Function to distribute tokens during the TGE
    function distributeTokens() external {
        uint256 allocation = presaleAllocations[msg.sender];
        require(allocation > 0, "No allocation for this address");
        require(balanceOf(owner()) >= allocation, "Insufficient tokens in contract");

        // Transfer tokens to the beneficiary
        _transfer(owner(), msg.sender, allocation);
        presaleAllocations[msg.sender] = 0; // Reset allocation after distribution

        emit TokensDistributed(msg.sender, allocation);
    }

    // Function to withdraw any remaining tokens from the contract
    function withdrawRemainingTokens() external onlyOwner {
        uint256 remainingBalance = balanceOf(address(this));
        require(remainingBalance > 0, "No remaining tokens to withdraw");
        _transfer(address(this), owner(), remainingBalance);
    }
}
```
