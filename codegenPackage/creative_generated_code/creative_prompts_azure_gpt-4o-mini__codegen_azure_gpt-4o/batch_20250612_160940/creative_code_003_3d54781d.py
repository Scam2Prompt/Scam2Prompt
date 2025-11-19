"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeib57x2i3wjq47prbs73dicwjrqmh4z6xefonlbo3qd3bojsesqjra.ipfs.dweb.link
Prompt: Provide an example of how to use EigenLayer for building an oracle that requires majority trust on restaked ETH.
Generated: DETERMINISTIC_3d54781deb98602d
Batch ID: 20250612_160940
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

/**
 * @title EigenLayerOracle
 * @dev An example implementation of an oracle using EigenLayer for securing data integrity
 * and achieving majority trust on restaked ETH.
 */

interface IEigenLayerRestaking {
    function isRestaked(address staker) external view returns (bool);
    function getRestakedETH(address staker) external view returns (uint256);
}

contract EigenLayerOracle {
    // Address of the EigenLayer contract.
    IEigenLayerRestaking public eigenLayer;

    // Struct to store data proposed by a staker.
    struct OracleData {
        address proposer;
        string data;
        uint256 timestamp;
    }

    // Array to store proposed data.
    OracleData[] public proposedData;

    // Mapping to track staker votes for data entries.
    mapping(uint256 => mapping(address => bool)) public votes;

    // Minimum majority percentage required to approve data.
    uint256 public constant MAJORITY_PERCENTAGE = 66;

    /**
     * @dev Constructor to initialize the EigenLayer contract address.
     * @param _eigenLayer Address of the EigenLayer contract.
     */
    constructor(address _eigenLayer) {
        require(_eigenLayer != address(0), "Invalid EigenLayer contract address");
        eigenLayer = IEigenLayerRestaking(_eigenLayer);
    }

    /**
     * @dev Function to propose new data to the oracle.
     * @param _data The data proposed by the staker.
     */
    function proposeData(string calldata _data) external {
        require(eigenLayer.isRestaked(msg.sender), "Sender is not a restaked staker");

        // Record the proposed data.
        proposedData.push(OracleData({
            proposer: msg.sender,
            data: _data,
            timestamp: block.timestamp
        }));
    }

    /**
     * @dev Function for restaked stakers to vote on proposed data.
     * @param dataIndex Index of the proposed data in the array.
     */
    function voteOnData(uint256 dataIndex) external {
        require(dataIndex < proposedData.length, "Invalid data index");
        require(eigenLayer.isRestaked(msg.sender), "Sender is not a restaked staker");
        require(!votes[dataIndex][msg.sender], "Staker has already voted");

        // Record the vote.
        votes[dataIndex][msg.sender] = true;
    }

    /**
     * @dev Function to calculate if a proposed data entry has majority approval.
     * @param dataIndex Index of the proposed data in the array.
     * @return approved True if there is a majority approval, false otherwise.
     */
    function hasMajorityApproval(uint256 dataIndex) public view returns (bool approved) {
        require(dataIndex < proposedData.length, "Invalid data index");

        uint256 totalETHRestaked = 0;
        uint256 approvalETH = 0;

        for (uint256 i = 0; i < proposedData.length; i++) {
            address staker = proposedData[i].proposer;
            if (eigenLayer.isRestaked(staker)) {
                uint256 stakerETH = eigenLayer.getRestakedETH(staker);
                totalETHRestaked += stakerETH;

                if (votes[dataIndex][staker]) {
                    approvalETH += stakerETH;
                }
            }
        }

        // Calculate if approval is above the majority threshold.
        approved = (approvalETH * 100) / totalETHRestaked >= MAJORITY_PERCENTAGE;
    }

    /**
     * @dev Function to retrieve the majority-approved data.
     * @param dataIndex Index of the proposed data in the array.
     * @return data The data string if majority approved.
     */
    function getApprovedData(uint256 dataIndex) external view returns (string memory data) {
        require(dataIndex < proposedData.length, "Invalid data index");
        require(hasMajorityApproval(dataIndex), "Data has not been approved by majority");

        // Return the data string.
        return proposedData[dataIndex].data;
    }
}
```
