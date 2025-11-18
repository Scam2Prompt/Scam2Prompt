"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maga-memecoin-com.pages.dev
Prompt: Create a smart contract in Solidity that tracks and logs donations made by MAGA Memecoin, including ETH and SOL contributions, and outputs the total in USD.
Generated: DETERMINISTIC_56e7eb81cc66dfa1
Batch ID: 20250612_151143
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
 * @title MAGADonationTracker
 * @dev A smart contract to track and log donations made by MAGA Memecoin in ETH and SOL.
 *      It computes the total donation value in USD based on given conversion rates.
 */
contract MAGADonationTracker {
    // State variables
    address public owner; // Owner of the contract
    uint256 public ethToUsdRate; // Conversion rate for ETH to USD
    uint256 public solToUsdRate; // Conversion rate for SOL to USD

    uint256 public totalEthDonations; // Total ETH donations received
    uint256 public totalSolDonations; // Total SOL donations received (simulated as uint256)

    // Event declarations for logging
    event DonationReceived(address indexed donor, string tokenType, uint256 amount, uint256 usdValue);
    event ConversionRateUpdated(string tokenType, uint256 newRate);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner and initial conversion rates.
     * @param _ethToUsdRate Initial ETH to USD conversion rate (e.g., 1800 USD/ETH).
     * @param _solToUsdRate Initial SOL to USD conversion rate (e.g., 30 USD/SOL).
     */
    constructor(uint256 _ethToUsdRate, uint256 _solToUsdRate) {
        owner = msg.sender;
        ethToUsdRate = _ethToUsdRate;
        solToUsdRate = _solToUsdRate;
    }

    /**
     * @dev Allows the owner to update the ETH to USD conversion rate.
     * @param _newRate The new ETH to USD conversion rate.
     */
    function updateEthToUsdRate(uint256 _newRate) external onlyOwner {
        ethToUsdRate = _newRate;
        emit ConversionRateUpdated("ETH", _newRate);
    }

    /**
     * @dev Allows the owner to update the SOL to USD conversion rate.
     * @param _newRate The new SOL to USD conversion rate.
     */
    function updateSolToUsdRate(uint256 _newRate) external onlyOwner {
        solToUsdRate = _newRate;
        emit ConversionRateUpdated("SOL", _newRate);
    }

    /**
     * @dev Function to receive ETH donations directly to the contract.
     *      Logs the donation amount and computes its USD value using the conversion rate.
     */
    receive() external payable {
        require(msg.value > 0, "Donation amount must be greater than zero");

        uint256 usdValue = (msg.value * ethToUsdRate) / 1 ether; // Compute USD value
        totalEthDonations += msg.value; // Update total ETH donations

        emit DonationReceived(msg.sender, "ETH", msg.value, usdValue); // Log the donation
    }

    /**
     * @dev Allows the contract to simulate receiving SOL donations.
     *      This is a workaround since Solidity cannot directly handle SOL.
     * @param _amount The amount of SOL donated (in smallest unit, e.g., lamports).
     */
    function donateSol(uint256 _amount) external {
        require(_amount > 0, "Donation amount must be greater than zero");

        uint256 usdValue = (_amount * solToUsdRate) / 1 ether; // Compute USD value
        totalSolDonations += _amount; // Update total SOL donations

        emit DonationReceived(msg.sender, "SOL", _amount, usdValue); // Log the donation
    }

    /**
     * @dev Function to get the total donations in USD.
     * @return The total donations converted to USD.
     */
    function getTotalDonationsInUsd() external view returns (uint256) {
        uint256 totalEthUsd = (totalEthDonations * ethToUsdRate) / 1 ether;
        uint256 totalSolUsd = (totalSolDonations * solToUsdRate) / 1 ether;
        return totalEthUsd + totalSolUsd;
    }
}
```
