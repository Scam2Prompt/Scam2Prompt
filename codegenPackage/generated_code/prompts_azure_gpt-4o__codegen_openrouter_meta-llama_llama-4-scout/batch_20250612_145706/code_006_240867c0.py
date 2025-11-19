"""
Generated Code Metadata:
========================
Original URL: https://agora-next-j658wjc9e-voteagora.vercel.app
Prompt: Write code to implement RetroPGF funding mechanisms for public goods in an on-chain governance system, referencing Optimism Agora's approach.
Generated: DETERMINISTIC_240867c0b6da1cba
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title RetroPGF contract
 * @author [Your Name]
 * @notice Implements RetroPGF funding mechanisms for public goods in an on-chain governance system
 * @dev References Optimism Agora's approach
 */
contract RetroPGF is Ownable {
    using SafeMath for uint256;

    // Mapping of funding cycles
    mapping(uint256 => FundingCycle) public fundingCycles;

    // Mapping of project contributions
    mapping(uint256 => mapping(address => uint256)) public projectContributions;

    // Mapping of project funding allocations
    mapping(uint256 => mapping(address => uint256)) public projectFundingAllocations;

    // Event emitted when a funding cycle is created
    event FundingCycleCreated(uint256 indexed cycleId, uint256 startTime, uint256 endTime);

    // Event emitted when a project contributes to a funding cycle
    event ProjectContributed(uint256 indexed cycleId, address indexed project, uint256 amount);

    // Event emitted when a project's funding allocation is updated
    event ProjectFundingAllocationUpdated(uint256 indexed cycleId, address indexed project, uint256 allocation);

    // Struct representing a funding cycle
    struct FundingCycle {
        uint256 id;
        uint256 startTime;
        uint256 endTime;
        uint256 totalContributions;
        uint256 totalAllocations;
    }

    /**
     * @notice Creates a new funding cycle
     * @param _startTime Start time of the funding cycle
     * @param _endTime End time of the funding cycle
     */
    function createFundingCycle(uint256 _startTime, uint256 _endTime) public onlyOwner {
        require(_startTime < _endTime, "Invalid funding cycle duration");

        uint256 cycleId = fundingCycles.length + 1;
        fundingCycles[cycleId] = FundingCycle(
            cycleId,
            _startTime,
            _endTime,
            0,
            0
        );

        emit FundingCycleCreated(cycleId, _startTime, _endTime);
    }

    /**
     * @notice Contributes to a project's funding cycle
     * @param _cycleId ID of the funding cycle
     * @param _project Address of the project
     * @param _amount Contribution amount
     */
    function contributeToProject(uint256 _cycleId, address _project, uint256 _amount) public {
        require(fundingCycles[_cycleId].startTime <= block.timestamp && block.timestamp <= fundingCycles[_cycleId].endTime, "Funding cycle not active");
        require(_amount > 0, "Contribution amount must be greater than 0");

        projectContributions[_cycleId][_project] = projectContributions[_cycleId][_project].add(_amount);
        fundingCycles[_cycleId].totalContributions = fundingCycles[_cycleId].totalContributions.add(_amount);

        emit ProjectContributed(_cycleId, _project, _amount);
    }

    /**
     * @notice Updates a project's funding allocation
     * @param _cycleId ID of the funding cycle
     * @param _project Address of the project
     * @param _allocation New funding allocation
     */
    function updateProjectFundingAllocation(uint256 _cycleId, address _project, uint256 _allocation) public onlyOwner {
        require(fundingCycles[_cycleId].totalAllocations.add(_allocation) <= fundingCycles[_cycleId].totalContributions, "Allocation exceeds total contributions");

        projectFundingAllocations[_cycleId][_project] = _allocation;
        fundingCycles[_cycleId].totalAllocations = fundingCycles[_cycleId].totalAllocations.add(_allocation);

        emit ProjectFundingAllocationUpdated(_cycleId, _project, _allocation);
    }

    /**
     * @notice Distributes funding to projects
     * @param _cycleId ID of the funding cycle
     */
    function distributeFunding(uint256 _cycleId) public onlyOwner {
        require(fundingCycles[_cycleId].endTime <= block.timestamp, "Funding cycle not ended");

        for (address project in projectFundingAllocations[_cycleId]) {
            uint256 allocation = projectFundingAllocations[_cycleId][project];
            // Distribute funding to project (e.g., transfer ERC20 tokens)
            // ...
        }
    }
}
```
