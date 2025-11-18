"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://roost-ch9.pages.dev
Prompt: Provide an example of a Solidity smart contract that could be used for distributing $ROOST tokens according to the tokenomics breakdown provided on the website.
Generated: DETERMINISTIC_d7e22caa99ba82c1
Batch ID: 20250612_152710
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

// Import the OpenZeppelin ERC20 token standard for creating the $ROOST token
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// The ROOSTToken contract manages the $ROOST token distribution
contract ROOSTToken is ERC20, Ownable {
    // Token distribution percentages
    uint256 private constant TEAM_ALLOCATION = 20; // 20%
    uint256 private constant MARKETING_ALLOCATION = 15; // 15%
    uint256 private constant DEVELOPMENT_ALLOCATION = 25; // 25%
    uint256 private constant COMMUNITY_ALLOCATION = 40; // 40%
    
    // Total supply of the token
    uint256 private constant TOTAL_SUPPLY = 1_000_000 * 10**18; // 1 million tokens

    // Addresses for distribution
    address public teamAddress;
    address public marketingAddress;
    address public developmentAddress;
    address public communityAddress;

    // Events
    event TokensDistributed(address indexed to, uint256 amount);

    // Constructor to initialize the token and allocate initial distributions
    constructor(
        address _teamAddress,
        address _marketingAddress,
        address _developmentAddress,
        address _communityAddress
    ) ERC20("ROOST Token", "ROOST") {
        // Set the distribution addresses
        teamAddress = _teamAddress;
        marketingAddress = _marketingAddress;
        developmentAddress = _developmentAddress;
        communityAddress = _communityAddress;

        // Mint the total supply and distribute according to allocations
        _mint(teamAddress, (TOTAL_SUPPLY * TEAM_ALLOCATION) / 100);
        _mint(marketingAddress, (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 100);
        _mint(developmentAddress, (TOTAL_SUPPLY * DEVELOPMENT_ALLOCATION) / 100);
        _mint(communityAddress, (TOTAL_SUPPLY * COMMUNITY_ALLOCATION) / 100);
    }

    // Function to distribute additional tokens (if needed) to the community
    function distributeCommunityTokens(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(communityAddress) >= amount, "Insufficient balance in community allocation");

        // Transfer tokens to the specified address
        _transfer(communityAddress, to, amount);
        emit TokensDistributed(to, amount);
    }

    // Function to retrieve the balance of the specified address
    function getBalance(address account) external view returns (uint256) {
        return balanceOf(account);
    }

    // Function to allow the owner to withdraw any ERC20 tokens mistakenly sent to the contract
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(this), "Cannot withdraw own token");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
