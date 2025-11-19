"""
Generated Code Metadata:
========================
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: Describe how to verify off-chain reserves for tokenized assets using Chainlink's Proof of Reserve and provide a coding example.
Generated: DETERMINISTIC_6d0f40b652366102
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "@chainlink/contracts/src/v0.8/interfaces/ProofOfReserveInterface.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TokenizedAssetReserveVerifier
 * @dev A contract to verify off-chain reserves for tokenized assets using Chainlink's Proof of Reserve
 */
contract TokenizedAssetReserveVerifier is Ownable {
    // Chainlink Proof of Reserve feed address
    address public proofOfReserveFeed;
    
    // Minimum required reserve ratio (1e18 = 100%)
    uint256 public minReserveRatio;
    
    // Last verified reserve amount
    uint256 public lastVerifiedReserve;
    
    // Last verification timestamp
    uint256 public lastVerificationTime;
    
    // Event emitted when reserves are verified
    event ReserveVerified(
        uint256 reserveAmount,
        uint256 timestamp,
        bool meetsRequirement
    );
    
    /**
     * @dev Constructor to initialize the contract
     * @param _proofOfReserveFeed Address of the Chainlink Proof of Reserve feed
     * @param _minReserveRatio Minimum reserve ratio required (1e18 = 100%)
     */
    constructor(address _proofOfReserveFeed, uint256 _minReserveRatio) {
        require(_proofOfReserveFeed != address(0), "Invalid feed address");
        require(_minReserveRatio > 0, "Invalid reserve ratio");
        
        proofOfReserveFeed = _proofOfReserveFeed;
        minReserveRatio = _minReserveRatio;
    }
    
    /**
     * @dev Verifies the current reserve against the minimum required ratio
     * @return reserveAmount The current reserve amount
     * @return meetsRequirement Whether the reserve meets the minimum requirement
     */
    function verifyReserves() public returns (uint256 reserveAmount, bool meetsRequirement) {
        // Get latest reserve data from Chainlink
        ProofOfReserveInterface por = ProofOfReserveInterface(proofOfReserveFeed);
        (reserveAmount, ) = por.latestRoundData();
        
        // Get the total supply of the tokenized asset
        uint256 totalSupply = por.getTotalSupply();
        
        // Calculate reserve ratio (reserveAmount / totalSupply)
        uint256 reserveRatio = (reserveAmount * 1e18) / totalSupply;
        
        // Check if reserve meets minimum requirement
        meetsRequirement = reserveRatio >= minReserveRatio;
        
        // Update state
        lastVerifiedReserve = reserveAmount;
        lastVerificationTime = block.timestamp;
        
        emit ReserveVerified(reserveAmount, block.timestamp, meetsRequirement);
        
        return (reserveAmount, meetsRequirement);
    }
    
    /**
     * @dev Updates the Proof of Reserve feed address
     * @param newFeed The new feed address
     */
    function updateProofOfReserveFeed(address newFeed) external onlyOwner {
        require(newFeed != address(0), "Invalid feed address");
        proofOfReserveFeed = newFeed;
    }
    
    /**
     * @dev Updates the minimum reserve ratio
     * @param newRatio The new minimum reserve ratio (1e18 = 100%)
     */
    function updateMinReserveRatio(uint256 newRatio) external onlyOwner {
        require(newRatio > 0, "Invalid reserve ratio");
        minReserveRatio = newRatio;
    }
    
    /**
     * @dev Returns the current reserve data from Chainlink
     * @return reserveAmount The current reserve amount
     * @return timestamp The timestamp of the latest update
     */
    function getLatestReserveData() public view returns (uint256 reserveAmount, uint256 timestamp) {
        ProofOfReserveInterface por = ProofOfReserveInterface(proofOfReserveFeed);
        (reserveAmount, timestamp) = por.latestRoundData();
        return (reserveAmount, timestamp);
    }
    
    /**
     * @dev Returns the total supply of the tokenized asset
     * @return totalSupply The total supply
     */
    function getTotalSupply() public view returns (uint256 totalSupply) {
        ProofOfReserveInterface por = ProofOfReserveInterface(proofOfReserveFeed);
        return por.getTotalSupply();
    }
    
    /**
     * @dev Returns the current reserve ratio (1e18 = 100%)
     * @return reserveRatio The current reserve ratio
     */
    function getCurrentReserveRatio() public view returns (uint256 reserveRatio) {
        (uint256 reserveAmount, ) = getLatestReserveData();
        uint256 totalSupply = getTotalSupply();
        if (totalSupply == 0) return 0;
        return (reserveAmount * 1e18) / totalSupply;
    }
}
```
