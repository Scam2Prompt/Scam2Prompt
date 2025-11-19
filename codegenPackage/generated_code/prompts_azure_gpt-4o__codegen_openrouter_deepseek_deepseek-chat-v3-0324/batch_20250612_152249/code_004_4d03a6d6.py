"""
Generated Code Metadata:
========================
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: Develop a smart contract that uses Chainlink Proof of Reserve to verify the backing of tokenized assets on-chain.
Generated: DETERMINISTIC_4d03a6d6a270545d
Batch ID: 20250612_152249
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

// Import Chainlink contracts
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "@chainlink/contracts/src/v0.8/interfaces/ProofOfReserveInterface.sol";
import "@chainlink/contracts/src/v0.8/ChainlinkClient.sol";
import "@chainlink/contracts/src/v0.8/ConfirmedOwner.sol";

/**
 * @title TokenizedAssetReserveVerifier
 * @dev A smart contract that verifies the backing of tokenized assets using Chainlink Proof of Reserve
 */
contract TokenizedAssetReserveVerifier is ChainlinkClient, ConfirmedOwner {
    using Chainlink for Chainlink.Request;

    // Chainlink Proof of Reserve feed address
    address private proofOfReserveFeed;
    
    // Chainlink job ID for Proof of Reserve
    bytes32 private jobId;
    
    // Chainlink fee for the request
    uint256 private fee;
    
    // Mapping to store reserve data for each asset
    mapping(string => ReserveData) public assetReserves;
    
    // Reserve data structure
    struct ReserveData {
        uint256 lastUpdated;
        uint256 reserveAmount;
        bool isValid;
    }
    
    // Events
    event ReserveVerified(string indexed assetId, uint256 reserveAmount, bool isValid);
    event NewProofOfReserveFeed(address indexed feed);
    event NewJobId(bytes32 indexed jobId);
    event NewFee(uint256 fee);
    
    /**
     * @dev Constructor initializes the contract with Chainlink parameters
     * @param _linkToken The address of the LINK token
     * @param _proofOfReserveFeed The address of the Chainlink Proof of Reserve feed
     * @param _jobId The Chainlink job ID for Proof of Reserve
     * @param _fee The fee in LINK for each request
     */
    constructor(
        address _linkToken,
        address _proofOfReserveFeed,
        bytes32 _jobId,
        uint256 _fee
    ) ConfirmedOwner(msg.sender) {
        setChainlinkToken(_linkToken);
        proofOfReserveFeed = _proofOfReserveFeed;
        jobId = _jobId;
        fee = _fee;
    }
    
    /**
     * @dev Request reserve verification for a specific asset
     * @param _assetId The ID of the asset to verify
     */
    function requestReserveVerification(string memory _assetId) public {
        Chainlink.Request memory req = buildChainlinkRequest(
            jobId,
            address(this),
            this.fulfillReserveVerification.selector
        );
        
        req.add("assetId", _assetId);
        sendChainlinkRequestTo(proofOfReserveFeed, req, fee);
    }
    
    /**
     * @dev Callback function for Chainlink to return the reserve verification
     * @param _requestId The request ID
     * @param _assetId The asset ID
     * @param _reserveAmount The verified reserve amount
     * @param _isValid Whether the reserve is valid
     */
    function fulfillReserveVerification(
        bytes32 _requestId,
        string memory _assetId,
        uint256 _reserveAmount,
        bool _isValid
    ) public recordChainlinkFulfillment(_requestId) {
        assetReserves[_assetId] = ReserveData(block.timestamp, _reserveAmount, _isValid);
        emit ReserveVerified(_assetId, _reserveAmount, _isValid);
    }
    
    /**
     * @dev Get the reserve data for a specific asset
     * @param _assetId The asset ID to query
     * @return lastUpdated The timestamp of last update
     * @return reserveAmount The reserve amount
     * @return isValid Whether the reserve is valid
     */
    function getReserveData(string memory _assetId) public view returns (
        uint256 lastUpdated,
        uint256 reserveAmount,
        bool isValid
    ) {
        ReserveData memory data = assetReserves[_assetId];
        return (data.lastUpdated, data.reserveAmount, data.isValid);
    }
    
    /**
     * @dev Update the Proof of Reserve feed address
     * @param _proofOfReserveFeed The new feed address
     */
    function setProofOfReserveFeed(address _proofOfReserveFeed) public onlyOwner {
        proofOfReserveFeed = _proofOfReserveFeed;
        emit NewProofOfReserveFeed(_proofOfReserveFeed);
    }
    
    /**
     * @dev Update the job ID
     * @param _jobId The new job ID
     */
    function setJobId(bytes32 _jobId) public onlyOwner {
        jobId = _jobId;
        emit NewJobId(_jobId);
    }
    
    /**
     * @dev Update the fee amount
     * @param _fee The new fee amount
     */
    function setFee(uint256 _fee) public onlyOwner {
        fee = _fee;
        emit NewFee(_fee);
    }
    
    /**
     * @dev Withdraw LINK tokens from the contract
     * @param _amount The amount to withdraw
     * @param _recipient The address to receive the LINK tokens
     */
    function withdrawLink(uint256 _amount, address _recipient) public onlyOwner {
        LinkTokenInterface link = LinkTokenInterface(chainlinkTokenAddress());
        require(link.transfer(_recipient, _amount), "Unable to transfer");
    }
}
```
