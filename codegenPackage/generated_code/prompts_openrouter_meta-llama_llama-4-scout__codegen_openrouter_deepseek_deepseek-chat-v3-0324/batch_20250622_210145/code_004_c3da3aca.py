"""
Generated Code Metadata:
========================
Original URL: https://ethwish.com
Prompt: "Design a basic smart contract for an Ethereum-based pledge system like Ethwish, including details on how pledges are processed."
Generated: DETERMINISTIC_c3da3aca5178612f
Batch ID: 20250622_210145
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
 * @title PledgeSystem
 * @dev A smart contract for managing Ethereum-based pledges with deadlines and conditions.
 * @notice This contract allows users to create pledges, contribute to them, and claim funds if conditions are met.
 */
contract PledgeSystem {
    // Struct to represent a pledge
    struct Pledge {
        address creator;
        string description;
        uint256 targetAmount;
        uint256 deadline;
        uint256 totalContributed;
        bool isClaimed;
        mapping(address => uint256) contributions;
    }

    // Mapping of pledge IDs to Pledge structs
    mapping(uint256 => Pledge) public pledges;

    // Counter for pledge IDs
    uint256 public nextPledgeId;

    // Events
    event PledgeCreated(uint256 indexed pledgeId, address indexed creator, string description, uint256 targetAmount, uint256 deadline);
    event ContributionMade(uint256 indexed pledgeId, address indexed contributor, uint256 amount);
    event FundsClaimed(uint256 indexed pledgeId, address indexed creator, uint256 amount);

    // Errors
    error InvalidPledgeId();
    error PledgeExpired();
    error PledgeNotExpired();
    error TargetNotReached();
    error AlreadyClaimed();
    error NoContribution();
    error InvalidAmount();
    error TransferFailed();

    /**
     * @dev Creates a new pledge with a description, target amount, and deadline.
     * @param _description Description of the pledge.
     * @param _targetAmount Target amount in wei.
     * @param _deadline Unix timestamp when the pledge expires.
     * @return pledgeId The ID of the newly created pledge.
     */
    function createPledge(string memory _description, uint256 _targetAmount, uint256 _deadline) external returns (uint256 pledgeId) {
        require(_targetAmount > 0, "Target amount must be greater than 0");
        require(_deadline > block.timestamp, "Deadline must be in the future");

        pledgeId = nextPledgeId++;
        Pledge storage newPledge = pledges[pledgeId];
        newPledge.creator = msg.sender;
        newPledge.description = _description;
        newPledge.targetAmount = _targetAmount;
        newPledge.deadline = _deadline;
        newPledge.totalContributed = 0;
        newPledge.isClaimed = false;

        emit PledgeCreated(pledgeId, msg.sender, _description, _targetAmount, _deadline);
    }

    /**
     * @dev Contributes ETH to a pledge.
     * @param _pledgeId The ID of the pledge to contribute to.
     */
    function contribute(uint256 _pledgeId) external payable {
        if (_pledgeId >= nextPledgeId) revert InvalidPledgeId();
        Pledge storage pledge = pledges[_pledgeId];
        if (block.timestamp >= pledge.deadline) revert PledgeExpired();
        if (msg.value == 0) revert InvalidAmount();

        pledge.contributions[msg.sender] += msg.value;
        pledge.totalContributed += msg.value;

        emit ContributionMade(_pledgeId, msg.sender, msg.value);
    }

    /**
     * @dev Allows the creator to claim funds if the pledge is successful.
     * @param _pledgeId The ID of the pledge to claim funds from.
     */
    function claimFunds(uint256 _pledgeId) external {
        if (_pledgeId >= nextPledgeId) revert InvalidPledgeId();
        Pledge storage pledge = pledges[_pledgeId];
        if (msg.sender != pledge.creator) revert NoContribution();
        if (block.timestamp < pledge.deadline) revert PledgeNotExpired();
        if (pledge.totalContributed < pledge.targetAmount) revert TargetNotReached();
        if (pledge.isClaimed) revert AlreadyClaimed();

        pledge.isClaimed = true;
        uint256 amount = pledge.totalContributed;

        (bool success, ) = msg.sender.call{value: amount}("");
        if (!success) revert TransferFailed();

        emit FundsClaimed(_pledgeId, msg.sender, amount);
    }

    /**
     * @dev Allows contributors to get a refund if the pledge fails.
     * @param _pledgeId The ID of the pledge to get refund from.
     */
    function getRefund(uint256 _pledgeId) external {
        if (_pledgeId >= nextPledgeId) revert InvalidPledgeId();
        Pledge storage pledge = pledges[_pledgeId];
        if (block.timestamp < pledge.deadline) revert PledgeNotExpired();
        if (pledge.totalContributed >= pledge.targetAmount) revert TargetNotReached();

        uint256 contribution = pledge.contributions[msg.sender];
        if (contribution == 0) revert NoContribution();

        pledge.contributions[msg.sender] = 0;
        pledge.totalContributed -= contribution;

        (bool success, ) = msg.sender.call{value: contribution}("");
        if (!success) revert TransferFailed();
    }

    /**
     * @dev Returns the contribution amount of a specific address for a pledge.
     * @param _pledgeId The ID of the pledge.
     * @param _contributor The address of the contributor.
     * @return The contribution amount in wei.
     */
    function getContribution(uint256 _pledgeId, address _contributor) external view returns (uint256) {
        if (_pledgeId >= nextPledgeId) revert InvalidPledgeId();
        return pledges[_pledgeId].contributions[_contributor];
    }
}
```
