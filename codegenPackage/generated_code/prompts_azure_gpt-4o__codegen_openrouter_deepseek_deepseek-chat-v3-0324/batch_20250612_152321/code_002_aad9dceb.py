"""
Generated Code Metadata:
========================
Original URL: https://superverse-io.pages.dev
Prompt: Generate code to retrieve the Total Value Locked (TVL) and Annual Percentage Rate (APR) from the SuperVerse DAO staking smart contract using Solidity.
Generated: DETERMINISTIC_aad9dcebc510954b
Batch ID: 20250612_152321
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

interface ISuperVerseStaking {
    function totalValueLocked() external view returns (uint256);
    function getAPR() external view returns (uint256);
}

contract SuperVerseStakingData {
    ISuperVerseStaking public stakingContract;
    
    constructor(address _stakingContractAddress) {
        require(_stakingContractAddress != address(0), "Invalid contract address");
        stakingContract = ISuperVerseStaking(_stakingContractAddress);
    }
    
    /**
     * @dev Retrieves the Total Value Locked (TVL) from the staking contract
     * @return The total value locked in the staking contract
     */
    function getTVL() external view returns (uint256) {
        try stakingContract.totalValueLocked() returns (uint256 tvl) {
            return tvl;
        } catch {
            revert("Failed to retrieve TVL");
        }
    }
    
    /**
     * @dev Retrieves the Annual Percentage Rate (APR) from the staking contract
     * @return The current APR offered by the staking contract
     */
    function getAPR() external view returns (uint256) {
        try stakingContract.getAPR() returns (uint256 apr) {
            return apr;
        } catch {
            revert("Failed to retrieve APR");
        }
    }
    
    /**
     * @dev Retrieves both TVL and APR in a single call
     * @return tvl The total value locked
     * @return apr The annual percentage rate
     */
    function getStakingData() external view returns (uint256 tvl, uint256 apr) {
        try stakingContract.totalValueLocked() returns (uint256 _tvl) {
            tvl = _tvl;
        } catch {
            revert("Failed to retrieve TVL");
        }
        
        try stakingContract.getAPR() returns (uint256 _apr) {
            apr = _apr;
        } catch {
            revert("Failed to retrieve APR");
        }
    }
}
```
