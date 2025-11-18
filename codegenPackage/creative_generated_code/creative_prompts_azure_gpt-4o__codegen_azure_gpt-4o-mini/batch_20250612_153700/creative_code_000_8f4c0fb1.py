"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://internetmoney-4rq.pages.dev
Prompt: Write a smart contract function in Solidity that integrates with the Internet Money (IM) token to calculate and display the total burned supply percentage, similar to the "Total Burned (0.225% OF TOTAL SUPPLY)" feature described on the website.
Generated: DETERMINISTIC_8f4c0fb118b4067d
Batch ID: 20250612_153700
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

// Interface for the Internet Money (IM) Token
interface IIMToken {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
}

contract BurnedSupplyCalculator {
    // The address of the Internet Money (IM) token contract
    address public imTokenAddress;

    // Constructor to set the IM token address
    constructor(address _imTokenAddress) {
        require(_imTokenAddress != address(0), "Invalid token address");
        imTokenAddress = _imTokenAddress;
    }

    // Function to calculate the total burned supply percentage
    function calculateBurnedSupplyPercentage() public view returns (string memory) {
        // Create an instance of the IM token
        IIMToken imToken = IIMToken(imTokenAddress);

        // Get the total supply of the token
        uint256 totalSupply = imToken.totalSupply();
        require(totalSupply > 0, "Total supply must be greater than zero");

        // Calculate the total burned supply
        uint256 burnedSupply = totalSupply - imToken.balanceOf(address(this));

        // Calculate burned supply percentage
        uint256 burnedPercentage = (burnedSupply * 10000) / totalSupply; // Use 10000 for percentage with two decimal places

        // Format the result as a string
        return string(abi.encodePacked("Total Burned (", uint2str(burnedPercentage / 100), ".", uint2str(burnedPercentage % 100), "% OF TOTAL SUPPLY)"));
    }

    // Helper function to convert uint256 to string
    function uint2str(uint256 _i) internal pure returns (string memory str) {
        if (_i == 0) {
            return "0";
        }
        uint256 j = _i;
        uint256 len;
        while (j != 0) {
            len++;
            j /= 10;
        }
        bytes memory bstr = new bytes(len);
        uint256 k = len;
        while (_i != 0) {
            k = k - 1;
            bstr[k] = bytes1(uint8(48 + _i % 10));
            _i /= 10;
        }
        return string(bstr);
    }
}
```
