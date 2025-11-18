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

/**
 * @title MetaklashAirdrop
 * @dev A contract for distributing tokens to eligible wallets as per the airdrop rules.
 * Excludes exchange wallets and wallets from prohibited countries.
 */
contract MetaklashAirdrop {
    // Owner of the contract
    address public owner;

    // Mapping for whitelisted wallets eligible for airdrop
    mapping(address => bool) public eligibleWallets;

    // Mapping for prohibited countries based on ISO country codes
    mapping(string => bool) public prohibitedCountries;

    // Mapping for known exchange wallets
    mapping(address => bool) public exchangeWallets;

    // Event emitted when tokens are distributed
    event TokensDistributed(address indexed wallet, uint256 amount);

    // Event emitted when wallet eligibility is updated
    event WalletEligibilityUpdated(address indexed wallet, bool isEligible);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Add or remove a wallet from the eligibility list
     * @param wallet Address of the wallet to update
     * @param isEligible Boolean indicating eligibility
     */
    function updateWalletEligibility(address wallet, bool isEligible) external onlyOwner {
        eligibleWallets[wallet] = isEligible;
        emit WalletEligibilityUpdated(wallet, isEligible);
    }

    /**
     * @dev Add or remove a country from the prohibited list
     * @param countryCode ISO country code to update
     * @param isProhibited Boolean indicating prohibition
     */
    function updateProhibitedCountries(string calldata countryCode, bool isProhibited) external onlyOwner {
        prohibitedCountries[countryCode] = isProhibited;
    }

    /**
     * @dev Add or remove a wallet from the exchange wallet list
     * @param wallet Address of the wallet to update
     * @param isExchange Boolean indicating whether it's an exchange wallet
     */
    function updateExchangeWallets(address wallet, bool isExchange) external onlyOwner {
        exchangeWallets[wallet] = isExchange;
    }

    /**
     * @dev Distribute tokens to an eligible wallet
     * @param wallet Address of the wallet to distribute tokens to
     * @param countryCode ISO country code of the wallet owner
     * @param amount Number of tokens to distribute
     */
    function distributeTokens(address wallet, string calldata countryCode, uint256 amount) external onlyOwner {
        // Check wallet eligibility
        require(eligibleWallets[wallet], "Wallet not eligible for airdrop");

        // Check if the wallet is not an exchange wallet
        require(!exchangeWallets[wallet], "Exchange wallets are not eligible");

        // Check if the country is not prohibited
        require(!prohibitedCountries[countryCode], "Wallet belongs to a prohibited country");

        // Distribute the tokens (assuming native transfer function)
        // In a real-world scenario, replace this with actual token transfer logic
        payable(wallet).transfer(amount);

        emit TokensDistributed(wallet, amount);
    }

    /**
     * @dev Fallback function to allow the contract to receive funds
     */
    receive() external payable {}

    /**
     * @dev Allows the owner to withdraw funds from the contract
     * @param amount Amount to withdraw
     */
    function withdrawFunds(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient contract balance");
        payable(owner).transfer(amount);
    }
}
```
