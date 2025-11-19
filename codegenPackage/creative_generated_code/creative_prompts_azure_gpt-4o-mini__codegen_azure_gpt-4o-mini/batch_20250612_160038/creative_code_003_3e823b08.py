"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://singularity-finance.pages.dev
Prompt: Provide an example of a smart contract that allows users to contribute data for monetization in the AI economy on the Singularity Finance platform.
Generated: DETERMINISTIC_3e823b088364b887
Batch ID: 20250612_160038
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

/// @title Data Contribution Smart Contract
/// @notice This contract allows users to contribute data for monetization in the AI economy
/// @dev The contract manages data submissions and rewards for contributions
contract DataContribution {

    // Events
    event DataSubmitted(address indexed contributor, uint256 dataId, string dataUri);
    event RewardClaimed(address indexed contributor, uint256 amount);

    // Struct to hold data information
    struct DataInfo {
        address contributor;
        string dataUri;
        uint256 reward;
        bool claimed;
    }

    // Mapping from data ID to DataInfo
    mapping(uint256 => DataInfo) public dataRecords;
    uint256 public dataCount;

    // Reward rate per data submission in wei
    uint256 public rewardRate;

    // Owner of the contract
    address public owner;

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    modifier onlyContributor(uint256 dataId) {
        require(msg.sender == dataRecords[dataId].contributor, "Not the original contributor");
        _;
    }

    // Constructor to set the initial reward rate
    constructor(uint256 _rewardRate) {
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    /// @notice Allows users to submit data for monetization
    /// @param dataUri URI of the data being contributed
    /// @return dataId The ID assigned to the submitted data
    function submitData(string memory dataUri) external returns (uint256 dataId) {
        require(bytes(dataUri).length > 0, "Data URI cannot be empty");
        
        // Increment data count to generate unique ID
        dataCount++;
        dataId = dataCount;

        // Store data information
        dataRecords[dataId] = DataInfo({
            contributor: msg.sender,
            dataUri: dataUri,
            reward: rewardRate,
            claimed: false
        });

        emit DataSubmitted(msg.sender, dataId, dataUri);
    }

    /// @notice Allows contributors to claim their rewards
    /// @param dataId The ID of the data for which the reward is claimed
    function claimReward(uint256 dataId) external onlyContributor(dataId) {
        DataInfo storage dataInfo = dataRecords[dataId];
        require(!dataInfo.claimed, "Reward already claimed");

        // Mark the reward as claimed
        dataInfo.claimed = true;

        // Transfer the reward
        payable(msg.sender).transfer(dataInfo.reward);
        emit RewardClaimed(msg.sender, dataInfo.reward);
    }

    /// @notice Function to withdraw contract's balance by the owner
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");

        payable(owner).transfer(balance);
    }

    /// @notice Fallback function to accept ether
    receive() external payable {}
}
```
