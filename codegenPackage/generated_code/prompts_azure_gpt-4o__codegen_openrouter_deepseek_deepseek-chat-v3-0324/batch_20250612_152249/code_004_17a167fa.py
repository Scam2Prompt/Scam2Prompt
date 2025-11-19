"""
Generated Code Metadata:
========================
Original URL: https://bafybeigix4apwqk6fyecm444vwmi65rxaxhb23mlme4in2u5oa4cl7abza.ipfs.dweb.link
Prompt: Write a smart contract in Solidity that integrates Botanix's Verifiable Random Function (VRF) mechanism using Bitcoin block hashes for randomness.
Generated: DETERMINISTIC_17a167fa640d5185
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
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";

interface IVRFProvider {
    function requestRandomness(bytes calldata data) external payable returns (bytes32 requestId);
    function getRandomness(bytes32 requestId) external view returns (uint256 randomness);
}

contract BotanixVRFConsumer is Ownable {
    IVRFProvider public vrfProvider;
    mapping(bytes32 => bool) public pendingRequests;
    mapping(bytes32 => uint256) public fulfilledRandomness;

    event RandomnessRequested(bytes32 indexed requestId, bytes data);
    event RandomnessFulfilled(bytes32 indexed requestId, uint256 randomness);

    constructor(address _vrfProvider) {
        vrfProvider = IVRFProvider(_vrfProvider);
    }

    function setVRFProvider(address _vrfProvider) external onlyOwner {
        vrfProvider = IVRFProvider(_vrfProvider);
    }

    function requestRandomness(bytes calldata data) external payable returns (bytes32 requestId) {
        require(msg.value > 0, "Payment required");
        require(address(vrfProvider) != address(0), "VRF provider not set");

        requestId = vrfProvider.requestRandomness{value: msg.value}(data);
        pendingRequests[requestId] = true;

        emit RandomnessRequested(requestId, data);
        return requestId;
    }

    function fulfillRandomness(bytes32 requestId) external {
        require(msg.sender == address(vrfProvider), "Only VRF provider can fulfill");
        require(pendingRequests[requestId], "Request not found or already fulfilled");

        uint256 randomness = vrfProvider.getRandomness(requestId);
        fulfilledRandomness[requestId] = randomness;
        delete pendingRequests[requestId];

        emit RandomnessFulfilled(requestId, randomness);
    }

    function getRandomness(bytes32 requestId) external view returns (uint256) {
        require(!pendingRequests[requestId], "Request not yet fulfilled");
        return fulfilledRandomness[requestId];
    }

    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```
