"""
Generated Code Metadata:
========================
Original URL: https://enter-eigenxyz.pages.dev
Prompt: Write a smart contract that utilizes OpenOracle (built on EigenLayer AVS) to validate exotic data feeds and perform fast on-chain data verification.
Generated: DETERMINISTIC_d56426622f1566e9
Batch ID: 20250612_150622
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

interface IOpenOracle {
    function getDataFeed(bytes32 feedId) external view returns (bytes memory, uint256);
    function verifyData(bytes32 feedId, bytes memory data, bytes memory signature) external view returns (bool);
}

contract ExoticDataVerifier is Ownable {
    using SafeMath for uint256;

    IOpenOracle public openOracle;
    
    // Mapping of supported feed IDs to their respective verification thresholds
    mapping(bytes32 => uint256) public feedVerificationThresholds;
    
    // Mapping of feed IDs to their last verified timestamps
    mapping(bytes32 => uint256) public lastVerifiedTimestamps;
    
    // Mapping of feed IDs to their last verified values
    mapping(bytes32 => bytes) public lastVerifiedValues;
    
    // Events
    event FeedAdded(bytes32 indexed feedId, uint256 verificationThreshold);
    event FeedRemoved(bytes32 indexed feedId);
    event DataVerified(bytes32 indexed feedId, bytes data, uint256 timestamp);
    event VerificationThresholdUpdated(bytes32 indexed feedId, uint256 newThreshold);
    
    // Errors
    error FeedNotSupported(bytes32 feedId);
    error VerificationFailed(bytes32 feedId);
    error StaleData(bytes32 feedId, uint256 currentTimestamp, uint256 requiredTimestamp);
    
    /**
     * @dev Constructor that sets the OpenOracle contract address
     * @param _openOracleAddress Address of the OpenOracle contract
     */
    constructor(address _openOracleAddress) {
        require(_openOracleAddress != address(0), "Invalid OpenOracle address");
        openOracle = IOpenOracle(_openOracleAddress);
    }
    
    /**
     * @dev Add a new supported data feed with verification threshold
     * @param feedId The ID of the data feed to support
     * @param verificationThreshold Minimum time between verifications (in seconds)
     */
    function addFeed(bytes32 feedId, uint256 verificationThreshold) external onlyOwner {
        require(feedVerificationThresholds[feedId] == 0, "Feed already exists");
        feedVerificationThresholds[feedId] = verificationThreshold;
        emit FeedAdded(feedId, verificationThreshold);
    }
    
    /**
     * @dev Remove a supported data feed
     * @param feedId The ID of the data feed to remove
     */
    function removeFeed(bytes32 feedId) external onlyOwner {
        require(feedVerificationThresholds[feedId] != 0, "Feed does not exist");
        delete feedVerificationThresholds[feedId];
        delete lastVerifiedTimestamps[feedId];
        delete lastVerifiedValues[feedId];
        emit FeedRemoved(feedId);
    }
    
    /**
     * @dev Update verification threshold for a feed
     * @param feedId The ID of the data feed
     * @param newThreshold New verification threshold (in seconds)
     */
    function updateVerificationThreshold(bytes32 feedId, uint256 newThreshold) external onlyOwner {
        require(feedVerificationThresholds[feedId] != 0, "Feed does not exist");
        feedVerificationThresholds[feedId] = newThreshold;
        emit VerificationThresholdUpdated(feedId, newThreshold);
    }
    
    /**
     * @dev Verify data from OpenOracle and store if valid
     * @param feedId The ID of the data feed to verify
     * @param data The data to verify
     * @param signature The signature to verify against
     */
    function verifyAndStoreData(
        bytes32 feedId,
        bytes memory data,
        bytes memory signature
    ) external {
        // Check if feed is supported
        if (feedVerificationThresholds[feedId] == 0) {
            revert FeedNotSupported(feedId);
        }
        
        // Verify the data with OpenOracle
        bool isValid = openOracle.verifyData(feedId, data, signature);
        if (!isValid) {
            revert VerificationFailed(feedId);
        }
        
        // Check if data is fresh enough
        (bytes memory oracleData, uint256 oracleTimestamp) = openOracle.getDataFeed(feedId);
        require(keccak256(data) == keccak256(oracleData), "Data mismatch with oracle");
        
        uint256 currentTimestamp = block.timestamp;
        uint256 lastVerified = lastVerifiedTimestamps[feedId];
        
        if (lastVerified != 0 && currentTimestamp < lastVerified.add(feedVerificationThresholds[feedId])) {
            revert StaleData(feedId, currentTimestamp, lastVerified.add(feedVerificationThresholds[feedId]));
        }
        
        // Store the verified data
        lastVerifiedValues[feedId] = data;
        lastVerifiedTimestamps[feedId] = oracleTimestamp;
        
        emit DataVerified(feedId, data, oracleTimestamp);
    }
    
    /**
     * @dev Get the latest verified data for a feed
     * @param feedId The ID of the data feed
     * @return data The latest verified data
     * @return timestamp The timestamp of the verification
     */
    function getVerifiedData(bytes32 feedId) external view returns (bytes memory data, uint256 timestamp) {
        if (feedVerificationThresholds[feedId] == 0) {
            revert FeedNotSupported(feedId);
        }
        return (lastVerifiedValues[feedId], lastVerifiedTimestamps[feedId]);
    }
    
    /**
     * @dev Check if data needs verification (stale or never verified)
     * @param feedId The ID of the data feed
     * @return needsVerification True if data needs verification
     */
    function needsVerification(bytes32 feedId) external view returns (bool) {
        if (feedVerificationThresholds[feedId] == 0) {
            revert FeedNotSupported(feedId);
        }
        
        uint256 lastVerified = lastVerifiedTimestamps[feedId];
        if (lastVerified == 0) {
            return true;
        }
        
        return block.timestamp >= lastVerified.add(feedVerificationThresholds[feedId]);
    }
}
```
