"""
Generated Code Metadata:
========================
Original URL: https://internetmoney-4rq.pages.dev
Prompt: Write a smart contract function in Solidity that integrates with the Internet Money (IM) token to calculate and display the total burned supply percentage, similar to the "Total Burned (0.225% OF TOTAL SUPPLY)" feature described on the website.
Generated: DETERMINISTIC_8f4c0fb118b4067d
Batch ID: 20250612_153700
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

interface IIMToken {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function burnAddress() external view returns (address);
}

contract BurnedSupplyCalculator {
    IIMToken public imToken;

    constructor(address _imTokenAddress) {
        require(_imTokenAddress != address(0), "Invalid token address");
        imToken = IIMToken(_imTokenAddress);
    }

    /**
     * @dev Calculates the total burned supply of IM tokens
     * @return burnedAmount The total amount of burned tokens
     * @return burnedPercentage The percentage of total supply that has been burned (with 18 decimal precision)
     */
    function getBurnedSupplyData() public view returns (uint256 burnedAmount, uint256 burnedPercentage) {
        address burnAddress = imToken.burnAddress();
        require(burnAddress != address(0), "Burn address not set");

        uint256 totalSupply = imToken.totalSupply();
        uint256 burnedBalance = imToken.balanceOf(burnAddress);

        burnedAmount = burnedBalance;
        burnedPercentage = (burnedBalance * 1e18) / totalSupply; // 18 decimal precision

        return (burnedAmount, burnedPercentage);
    }

    /**
     * @dev Returns a formatted string of the burned supply percentage
     * @return A string in the format "Total Burned (X.XXX% OF TOTAL SUPPLY)"
     */
    function getFormattedBurnedPercentage() external view returns (string memory) {
        (, uint256 burnedPercentage) = getBurnedSupplyData();
        
        // Convert percentage to 3 decimal places
        uint256 percentageWith3Decimals = (burnedPercentage * 1000) / 1e18;
        
        uint256 integerPart = percentageWith3Decimals / 1000;
        uint256 fractionalPart = percentageWith3Decimals % 1000;
        
        return string(abi.encodePacked(
            "Total Burned (",
            uintToString(integerPart),
            ".",
            formatFractionalPart(fractionalPart),
            "% OF TOTAL SUPPLY)"
        ));
    }

    /**
     * @dev Helper function to convert uint to string
     */
    function uintToString(uint256 value) internal pure returns (string memory) {
        if (value == 0) {
            return "0";
        }
        
        uint256 temp = value;
        uint256 digits;
        while (temp != 0) {
            digits++;
            temp /= 10;
        }
        
        bytes memory buffer = new bytes(digits);
        while (value != 0) {
            digits -= 1;
            buffer[digits] = bytes1(uint8(48 + uint256(value % 10)));
            value /= 10;
        }
        
        return string(buffer);
    }

    /**
     * @dev Helper function to format fractional part with leading zeros
     */
    function formatFractionalPart(uint256 value) internal pure returns (string memory) {
        if (value < 10) {
            return string(abi.encodePacked("00", uintToString(value)));
        } else if (value < 100) {
            return string(abi.encodePacked("0", uintToString(value)));
        } else {
            return uintToString(value);
        }
    }
}
```
