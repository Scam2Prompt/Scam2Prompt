"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metaklash.com
Prompt: Develop a Solidity contract that restricts token distribution to eligible wallets, excluding wallets from exchanges and citizens of prohibited countries as per the Metaklash airdrop rules.
Generated: DETERMINISTIC_4f8d26baa29f4755
Batch ID: 20250612_154010
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// The TokenDistribution contract manages the distribution of tokens
// only to eligible wallets, excluding those from exchanges and prohibited countries.
contract TokenDistribution is Ownable {
    IERC20 public token; // ERC20 token to be distributed

    // Mapping to track eligible addresses
    mapping(address => bool) public eligibleAddresses;

    // List of prohibited countries (in this example, represented by country codes)
    // Add prohibited country codes (ISO 3166-1 alpha-2) as needed
    mapping(string => bool) public prohibitedCountries;

    // Event emitted when tokens are distributed
    event TokensDistributed(address indexed recipient, uint256 amount);

    // Constructor to set the token address and prohibited countries
    constructor(address _tokenAddress, string[] memory _prohibitedCountries) {
        token = IERC20(_tokenAddress);
        for (uint256 i = 0; i < _prohibitedCountries.length; i++) {
            prohibitedCountries[_prohibitedCountries[i]] = true;
        }
    }

    // Modifier to only allow eligible addresses
    modifier onlyEligible(address recipient, string memory countryCode) {
        require(eligibleAddresses[recipient], "Address is not eligible");
        require(!prohibitedCountries[countryCode], "Address is from a prohibited country");
        _;
    }

    // Function to add eligible addresses
    function addEligibleAddresses(address[] calldata addresses) external onlyOwner {
        for (uint256 i = 0; i < addresses.length; i++) {
            eligibleAddresses[addresses[i]] = true;
        }
    }

    // Function to distribute tokens to an eligible address
    function distributeTokens(address recipient, uint256 amount, string memory countryCode) external onlyOwner onlyEligible(recipient, countryCode) {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens to the eligible recipient
        token.transfer(recipient, amount);
        emit TokensDistributed(recipient, amount);
    }

    // Function to withdraw any tokens accidentally sent to the contract
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        
        // Transfer specified amount of tokens back to owner's address
        token.transfer(owner(), amount);
    }

    // Function to check if an address is eligible
    function isEligible(address addr) external view returns (bool) {
        return eligibleAddresses[addr];
    }

    // Function to update prohibited countries
    function updateProhibitedCountries(string[] calldata countryCodes, bool status) external onlyOwner {
        for (uint256 i = 0; i < countryCodes.length; i++) {
            prohibitedCountries[countryCodes[i]] = status;
        }
    }
}
```
