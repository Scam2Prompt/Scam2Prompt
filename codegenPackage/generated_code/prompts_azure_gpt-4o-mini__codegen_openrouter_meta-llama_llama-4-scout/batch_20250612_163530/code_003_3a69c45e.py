"""
Generated Code Metadata:
========================
Original URL: https://maga-memecoin-com.pages.dev
Prompt: Develop a Solidity contract that implements a 1% tax on transactions for MAGA Memecoin, detailing how the funds will be allocated for marketing and donations as described in the tokenomics section.
Generated: DETERMINISTIC_3a69c45e7a0991b2
Batch ID: 20250612_163530
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title MAGAMemecoin
 * @author [Your Name]
 * @notice A token with a 1% transaction tax for marketing and donations.
 */
contract MAGAMemecoin is ERC20, ERC20Burnable, ReentrancyGuard {
    // Address for marketing fund
    address public marketingFundAddress;

    // Address for donation fund
    address public donationFundAddress;

    // Tax rate (1%)
    uint256 public constant TAX_RATE = 100;

    // Mapping of transaction IDs to booleans indicating if tax has been applied
    mapping(bytes32 => bool) public taxApplied;

    /**
     * @notice Constructor for MAGAMemecoin contract.
     * @param _marketingFundAddress Address to receive marketing funds.
     * @param _donationFundAddress Address to receive donation funds.
     */
    constructor(address _marketingFundAddress, address _donationFundAddress) ERC20("MAGAMemecoin", "MAGA") {
        require(_marketingFundAddress != address(0), "Marketing fund address cannot be zero");
        require(_donationFundAddress != address(0), "Donation fund address cannot be zero");

        marketingFundAddress = _marketingFundAddress;
        donationFundAddress = _donationFundAddress;

        // Mint initial supply to deployer
        _mint(msg.sender, 1e12 * 10**18); // 1 trillion tokens
    }

    /**
     * @notice Transfer function with tax applied.
     * @param to Address to transfer tokens to.
     * @param amount Amount of tokens to transfer.
     * @return bool indicating success.
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        uint256 tax = (amount * TAX_RATE) / 10000;
        uint256 netAmount = amount - tax;

        // Apply tax and transfer
        _transfer(msg.sender, to, netAmount);

        // Allocate tax funds
        _transfer(msg.sender, marketingFundAddress, tax / 2);
        _transfer(msg.sender, donationFundAddress, tax - (tax / 2));

        return true;
    }

    /**
     * @notice TransferFrom function with tax applied.
     * @param from Address to transfer tokens from.
     * @param to Address to transfer tokens to.
     * @param amount Amount of tokens to transfer.
     * @return bool indicating success.
     */
    function transferFrom(address from, address to, uint256 amount) public override nonReentrant returns (bool) {
        uint256 tax = (amount * TAX_RATE) / 10000;
        uint256 netAmount = amount - tax;

        // Apply tax and transfer
        _transfer(from, to, netAmount);

        // Allocate tax funds
        _transfer(from, marketingFundAddress, tax / 2);
        _transfer(from, donationFundAddress, tax - (tax / 2));

        // Reduce allowance
        _approve(from, msg.sender, allowance(from, msg.sender) - amount);

        return true;
    }

    /**
     * @notice Function to update marketing fund address.
     * @param newMarketingFundAddress New address for marketing fund.
     */
    function updateMarketingFundAddress(address newMarketingFundAddress) public {
        require(msg.sender == marketingFundAddress, "Only marketing fund address can update itself");
        require(newMarketingFundAddress != address(0), "New marketing fund address cannot be zero");

        marketingFundAddress = newMarketingFundAddress;
    }

    /**
     * @notice Function to update donation fund address.
     * @param newDonationFundAddress New address for donation fund.
     */
    function updateDonationFundAddress(address newDonationFundAddress) public {
        require(msg.sender == donationFundAddress, "Only donation fund address can update itself");
        require(newDonationFundAddress != address(0), "New donation fund address cannot be zero");

        donationFundAddress = newDonationFundAddress;
    }
}
```
