"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://on-oeth.pages.dev
Prompt: Write a Solidity contract that integrates with the Origin vault to calculate the proportional mix of stablecoins received when redeeming OUSD, as described in the documentation.
Generated: DETERMINISTIC_eb65555a126cbcf7
Batch ID: 20250612_150613
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

// Importing interfaces and libraries for OUSD and Origin Vault interactions.
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Interface for the Origin Vault contract
interface IOriginVault {
    function redeem(uint256 amount) external returns (uint256, uint256);
    function getStablecoinBalances() external view returns (uint256[] memory);
}

/**
 * @title OUSDRedemption
 * @dev This contract allows users to calculate the proportional mix of stablecoins
 * when redeeming OUSD from the Origin Vault.
 */
contract OUSDRedemption is Ownable {
    // Instance of the Origin Vault contract
    IOriginVault public originVault;

    // Event emitted when redemption is calculated
    event RedemptionCalculated(address indexed user, uint256[] stablecoinAmounts);

    /**
     * @dev Sets the Origin Vault contract address.
     * @param _originVault Address of the Origin Vault contract
     */
    constructor(address _originVault) {
        require(_originVault != address(0), "Invalid vault address");
        originVault = IOriginVault(_originVault);
    }

    /**
     * @dev Calculate the proportional mix of stablecoins received upon redeeming OUSD.
     * @param amount The amount of OUSD to redeem
     * @return stablecoinAmounts An array of amounts of each stablecoin received
     */
    function calculateRedemption(uint256 amount) external returns (uint256[] memory stablecoinAmounts) {
        require(amount > 0, "Amount must be greater than zero");

        // Call the redeem function from the Origin Vault
        (uint256 totalStablecoins, ) = originVault.redeem(amount);

        // Get the current balances of stablecoins in the vault
        uint256[] memory balances = originVault.getStablecoinBalances();
        uint256 totalSupply = 0;

        // Calculate total supply of stablecoins
        for (uint256 i = 0; i < balances.length; i++) {
            totalSupply += balances[i];
        }

        // Calculate the proportional mix of stablecoins to be received
        stablecoinAmounts = new uint256[](balances.length);
        for (uint256 i = 0; i < balances.length; i++) {
            if (totalSupply > 0) {
                stablecoinAmounts[i] = (balances[i] * totalStablecoins) / totalSupply;
            } else {
                stablecoinAmounts[i] = 0; // Avoid division by zero
            }
        }

        // Emit an event with the results
        emit RedemptionCalculated(msg.sender, stablecoinAmounts);
    }
}
```
