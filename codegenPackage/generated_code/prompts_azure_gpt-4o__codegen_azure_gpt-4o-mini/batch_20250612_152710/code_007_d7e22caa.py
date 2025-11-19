"""
Generated Code Metadata:
========================
Original URL: https://roost-ch9.pages.dev
Prompt: Provide an example of a Solidity smart contract that could be used for distributing $ROOST tokens according to the tokenomics breakdown provided on the website.
Generated: DETERMINISTIC_d7e22caa99ba82c1
Batch ID: 20250612_152710
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

// Importing OpenZeppelin's ERC20 implementation for token standards
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for the $ROOST token
contract RoostToken is ERC20, Ownable {
    // Tokenomics breakdown
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10 ** 18; // Total supply of 1 million tokens
    uint256 public constant TEAM_ALLOCATION = (TOTAL_SUPPLY * 20) / 100; // 20% for the team
    uint256 public constant MARKETING_ALLOCATION = (TOTAL_SUPPLY * 15) / 100; // 15% for marketing
    uint256 public constant DEVELOPMENT_ALLOCATION = (TOTAL_SUPPLY * 25) / 100; // 25% for development
    uint256 public constant COMMUNITY_ALLOCATION = (TOTAL_SUPPLY * 40) / 100; // 40% for community

    // Addresses for allocations
    address public teamAddress;
    address public marketingAddress;
    address public developmentAddress;
    address public communityAddress;

    // Constructor to initialize the token and allocate initial supply
    constructor(
        address _teamAddress,
        address _marketingAddress,
        address _developmentAddress,
        address _communityAddress
    ) ERC20("Roost Token", "$ROOST") {
        // Set allocation addresses
        teamAddress = _teamAddress;
        marketingAddress = _marketingAddress;
        developmentAddress = _developmentAddress;
        communityAddress = _communityAddress;

        // Minting the total supply to the contract owner
        _mint(address(this), TOTAL_SUPPLY);
    }

    // Function to distribute tokens according to the tokenomics
    function distributeTokens() external onlyOwner {
        // Ensure tokens are not already distributed
        require(balanceOf(address(this)) >= TOTAL_SUPPLY, "Insufficient tokens to distribute");

        // Distributing tokens to respective addresses
        _transfer(address(this), teamAddress, TEAM_ALLOCATION);
        _transfer(address(this), marketingAddress, MARKETING_ALLOCATION);
        _transfer(address(this), developmentAddress, DEVELOPMENT_ALLOCATION);
        _transfer(address(this), communityAddress, COMMUNITY_ALLOCATION);
    }

    // Function to withdraw any ERC20 tokens sent to this contract by mistake
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(this), "Cannot withdraw $ROOST tokens");
        require(IERC20(tokenAddress).transfer(msg.sender, amount), "Transfer failed");
    }
}
```
