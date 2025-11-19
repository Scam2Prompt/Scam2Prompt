"""
Generated Code Metadata:
========================
Original URL: https://taiyoil.web.app
Prompt: Develop a function in Solidity that calculates the number of Taiyo Pilots a user should receive based on the amount of Taiyo Oil they mint, following the rules outlined on the Taiyo Oil webpage.
Generated: DETERMINISTIC_8b670c74c3693e11
Batch ID: 20250612_151611
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

/**
 * @title TaiyoPilotCalculator
 * @dev Calculates the number of Taiyo Pilots based on Taiyo Oil minted
 */
contract TaiyoPilotCalculator {
    /**
     * @dev Calculates the number of Taiyo Pilots based on Taiyo Oil minted
     * @param oilAmount The amount of Taiyo Oil minted
     * @return pilots The number of Taiyo Pilots to receive
     */
    function calculatePilots(uint256 oilAmount) public pure returns (uint256 pilots) {
        require(oilAmount > 0, "Oil amount must be greater than 0");
        
        if (oilAmount < 1000 ether) {
            pilots = 0;
        } else if (oilAmount < 5000 ether) {
            pilots = 1;
        } else if (oilAmount < 10000 ether) {
            pilots = 2;
        } else if (oilAmount < 20000 ether) {
            pilots = 3;
        } else if (oilAmount < 50000 ether) {
            pilots = 4;
        } else if (oilAmount < 100000 ether) {
            pilots = 5;
        } else if (oilAmount < 200000 ether) {
            pilots = 6;
        } else if (oilAmount < 500000 ether) {
            pilots = 7;
        } else if (oilAmount < 1000000 ether) {
            pilots = 8;
        } else if (oilAmount < 2000000 ether) {
            pilots = 9;
        } else {
            pilots = 10;
        }
        
        return pilots;
    }
}
```
