"""
Generated Code Metadata:
========================
Original URL: https://agora-next-k675d77o0-voteagora.vercel.app
Prompt: Develop a smart contract that implements the quorum calculation for Optimism governance proposals, ensuring it aligns with the values provided on the Agora platform.
Generated: DETERMINISTIC_bd2ecb3143b1fea0
Batch ID: 20250612_145706
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title QuorumCalculator
 * @dev Smart contract to calculate quorum for governance proposals on the Optimism platform.
 */
contract QuorumCalculator is Ownable {
    using SafeMath for uint256;

    // Total supply of tokens used for governance
    uint256 public totalSupply;

    // Minimum percentage required for quorum (in basis points, e.g., 500 = 5%)
    uint256 public quorumPercentage;

    // Event emitted when quorum is calculated
    event QuorumCalculated(uint256 quorum);

    /**
     * @dev Constructor to initialize the contract with total supply and quorum percentage.
     * @param _totalSupply Total supply of governance tokens.
     * @param _quorumPercentage Minimum percentage required for quorum.
     */
    constructor(uint256 _totalSupply, uint256 _quorumPercentage) {
        require(_totalSupply > 0, "Total supply must be greater than zero");
        require(_quorumPercentage > 0 && _quorumPercentage <= 10000, "Quorum percentage must be between 0 and 10000");

        totalSupply = _totalSupply;
        quorumPercentage = _quorumPercentage;
    }

    /**
     * @dev Calculate the quorum based on the total supply and quorum percentage.
     * @return uint256 The calculated quorum.
     */
    function calculateQuorum() public view returns (uint256) {
        uint256 quorum = totalSupply.mul(quorumPercentage).div(10000);
        emit QuorumCalculated(quorum);
        return quorum;
    }

    /**
     * @dev Update the total supply of governance tokens.
     * @param _totalSupply New total supply of governance tokens.
     */
    function updateTotalSupply(uint256 _totalSupply) external onlyOwner {
        require(_totalSupply > 0, "Total supply must be greater than zero");
        totalSupply = _totalSupply;
    }

    /**
     * @dev Update the quorum percentage.
     * @param _quorumPercentage New quorum percentage.
     */
    function updateQuorumPercentage(uint256 _quorumPercentage) external onlyOwner {
        require(_quorumPercentage > 0 && _quorumPercentage <= 10000, "Quorum percentage must be between 0 and 10000");
        quorumPercentage = _quorumPercentage;
    }
}
```
