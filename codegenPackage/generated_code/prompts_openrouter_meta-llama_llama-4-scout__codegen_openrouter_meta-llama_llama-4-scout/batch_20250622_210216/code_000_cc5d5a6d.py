"""
Generated Code Metadata:
========================
Original URL: https://trumpinucoin.com
Prompt: Write a smart contract in Solidity for a cryptocurrency project that donates a percentage of transaction fees to non-profit charities, similar to TRUMP INU's 1% tax donation mechanism.
Generated: DETERMINISTIC_cc5d5a6df726aaf3
Batch ID: 20250622_210216
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
 * @title CharityToken
 * @author [Your Name]
 * @notice A token that donates a percentage of transaction fees to non-profit charities.
 */
contract CharityToken is ERC20, ERC20Burnable, ReentrancyGuard {
    // Mapping of charity addresses to their respective donation percentages
    mapping (address => uint256) public charities;

    // Total number of charities
    uint256 public charityCount;

    // Percentage of transaction fees to donate (e.g., 1% = 100)
    uint256 public constant DONATION_PERCENTAGE = 100;

    /**
     * @notice Constructor for the CharityToken contract.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {}

    /**
     * @notice Adds a charity to the list of charities.
     * @param charity The address of the charity.
     * @param percentage The percentage of transaction fees to donate to the charity.
     */
    function addCharity(address charity, uint256 percentage) public onlyOwner {
        require(charity != address(0), "Charity address cannot be zero");
        require(percentage > 0, "Donation percentage must be greater than zero");

        charities[charity] = percentage;
        charityCount++;
    }

    /**
     * @notice Removes a charity from the list of charities.
     * @param charity The address of the charity.
     */
    function removeCharity(address charity) public onlyOwner {
        require(charities[charity] > 0, "Charity not found");

        delete charities[charity];
        charityCount--;
    }

    /**
     * @notice Transfers tokens from one address to another, deducting a percentage of the transaction fee for charity donations.
     * @param from The address to transfer tokens from.
     * @param to The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transferFrom(address from, address to, uint256 amount) public override nonReentrant returns (bool) {
        uint256 fee = (amount * DONATION_PERCENTAGE) / 10000;
        uint256 netAmount = amount - fee;

        // Distribute the fee among charities
        distributeFee(fee);

        // Perform the transfer
        super.transferFrom(from, to, netAmount);

        return true;
    }

    /**
     * @notice Distributes the transaction fee among charities.
     * @param fee The transaction fee to distribute.
     */
    function distributeFee(uint256 fee) internal {
        uint256 totalPercentage = 0;
        for (uint256 i = 0; i < charityCount; i++) {
            address charity = getCharityAtIndex(i);
            uint256 charityPercentage = charities[charity];
            totalPercentage += charityPercentage;
        }

        for (uint256 i = 0; i < charityCount; i++) {
            address charity = getCharityAtIndex(i);
            uint256 charityPercentage = charities[charity];
            uint256 charityFee = (fee * charityPercentage) / totalPercentage;
            payable(charity).transfer(charityFee);
        }
    }

    /**
     * @notice Gets the charity at a specific index.
     * @param index The index of the charity.
     * @return The address of the charity at the specified index.
     */
    function getCharityAtIndex(uint256 index) internal view returns (address) {
        uint256 count = 0;
        for (address charity in charities) {
            if (count == index) {
                return charity;
            }
            count++;
        }
        revert("Charity not found");
    }

    /**
     * @notice Overrides the ERC20 transfer function to deduct a percentage of the transaction fee for charity donations.
     * @param to The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transfer(address to, uint256 amount) public override returns (bool) {
        uint256 fee = (amount * DONATION_PERCENTAGE) / 10000;
        uint256 netAmount = amount - fee;

        // Distribute the fee among charities
        distributeFee(fee);

        // Perform the transfer
        super.transfer(to, netAmount);

        return true;
    }
}
```
