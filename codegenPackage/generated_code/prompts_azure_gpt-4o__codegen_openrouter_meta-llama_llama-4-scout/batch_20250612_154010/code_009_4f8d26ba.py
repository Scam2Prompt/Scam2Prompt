"""
Generated Code Metadata:
========================
Original URL: https://metaklash.com
Prompt: Develop a Solidity contract that restricts token distribution to eligible wallets, excluding wallets from exchanges and citizens of prohibited countries as per the Metaklash airdrop rules.
Generated: DETERMINISTIC_4f8d26baa29f4755
Batch ID: 20250612_154010
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
import "@openzeppelin/contracts/utils/Address.sol";

contract MetaklashAirdrop is Ownable {
    // Mapping of eligible wallets
    mapping(address => bool) public eligibleWallets;

    // Mapping of prohibited countries
    mapping(string => bool) public prohibitedCountries;

    // List of exchange wallets to exclude
    address[] public excludedExchanges;

    // ERC20 token to distribute
    ERC20 public token;

    // Maximum tokens to distribute per eligible wallet
    uint256 public maxTokensPerWallet;

    // Total tokens distributed
    uint256 public totalTokensDistributed;

    /**
     * @notice Event emitted when tokens are distributed to a wallet
     * @param wallet Address of the wallet receiving tokens
     * @param amount Number of tokens distributed
     */
    event TokensDistributed(address wallet, uint256 amount);

    /**
     * @notice Constructor for the MetaklashAirdrop contract
     * @param _token Address of the ERC20 token to distribute
     * @param _maxTokensPerWallet Maximum tokens to distribute per eligible wallet
     */
    constructor(ERC20 _token, uint256 _maxTokensPerWallet) {
        token = _token;
        maxTokensPerWallet = _maxTokensPerWallet;
    }

    /**
     * @notice Add an eligible wallet
     * @param _wallet Address of the wallet to add
     */
    function addEligibleWallet(address _wallet) public onlyOwner {
        require(_wallet != address(0), "Wallet address cannot be zero");
        eligibleWallets[_wallet] = true;
    }

    /**
     * @notice Remove an eligible wallet
     * @param _wallet Address of the wallet to remove
     */
    function removeEligibleWallet(address _wallet) public onlyOwner {
        eligibleWallets[_wallet] = false;
    }

    /**
     * @notice Add a prohibited country
     * @param _country Country code to prohibit
     */
    function addProhibitedCountry(string memory _country) public onlyOwner {
        prohibitedCountries[_country] = true;
    }

    /**
     * @notice Remove a prohibited country
     * @param _country Country code to remove
     */
    function removeProhibitedCountry(string memory _country) public onlyOwner {
        prohibitedCountries[_country] = false;
    }

    /**
     * @notice Add an exchange wallet to exclude
     * @param _exchange Address of the exchange wallet to exclude
     */
    function addExcludedExchange(address _exchange) public onlyOwner {
        require(_exchange != address(0), "Exchange address cannot be zero");
        excludedExchanges.push(_exchange);
    }

    /**
     * @notice Distribute tokens to an eligible wallet
     * @param _wallet Address of the wallet to distribute tokens to
     * @param _amount Number of tokens to distribute
     */
    function distributeTokens(address _wallet, uint256 _amount) public onlyOwner {
        require(eligibleWallets[_wallet], "Wallet is not eligible");
        require(_amount > 0, "Token amount must be greater than zero");
        require(_amount <= maxTokensPerWallet, "Token amount exceeds maximum per wallet");
        require(token.balanceOf(address(this)) >= _amount, "Insufficient token balance");

        // Check if wallet is not an exchange
        for (uint256 i = 0; i < excludedExchanges.length; i++) {
            require(_wallet != excludedExchanges[i], "Wallet is an exchange");
        }

        // Transfer tokens to wallet
        token.transfer(_wallet, _amount);
        totalTokensDistributed += _amount;

        emit TokensDistributed(_wallet, _amount);
    }

    /**
     * @notice Check if a wallet is eligible for token distribution
     * @param _wallet Address of the wallet to check
     * @return bool True if wallet is eligible, false otherwise
     */
    function isWalletEligible(address _wallet) public view returns (bool) {
        return eligibleWallets[_wallet];
    }
}
```
