"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://client-website1.pages.dev
Prompt: Write a smart contract in Solidity that facilitates transparent and long-term relationships between crypto-native funds and project founders, inspired by Innodapter ApS's values.
Generated: DETERMINISTIC_25057a2b683eaed9
Batch ID: 20250612_151207
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
 * @title Transparent Partnership Smart Contract
 * @dev Facilitates transparent and long-term relationships between crypto-native funds and project founders
 */
contract TransparentPartnership {

    // Represents a partnership agreement
    struct Agreement {
        uint256 fundsAllocated;
        uint256 milestoneAmount;
        uint256 milestonesCompleted;
        uint256 totalMilestones;
        bool isActive;
        bool isTerminated;
        address funder;
        address founder;
    }

    // Mapping of agreements by ID
    mapping(uint256 => Agreement) public agreements;

    // Counter to track agreement IDs
    uint256 public agreementCounter;

    // Events
    event AgreementCreated(uint256 indexed agreementId, address indexed funder, address indexed founder);
    event FundsDisbursed(uint256 indexed agreementId, uint256 amount);
    event AgreementTerminated(uint256 indexed agreementId);

    // Modifier to ensure that only the funder can call certain functions
    modifier onlyFunder(uint256 agreementId) {
        require(msg.sender == agreements[agreementId].funder, "Caller is not the funder");
        _;
    }

    // Modifier to ensure that only the founder can call certain functions
    modifier onlyFounder(uint256 agreementId) {
        require(msg.sender == agreements[agreementId].founder, "Caller is not the founder");
        _;
    }

    // Modifier to check if the agreement is active
    modifier isAgreementActive(uint256 agreementId) {
        require(agreements[agreementId].isActive, "Agreement is not active");
        _;
    }

    /**
     * @dev Creates a new partnership agreement
     * @param _funder Address of the funder
     * @param _founder Address of the founder
     * @param _fundsAllocated Total funds allocated for the agreement
     * @param _milestoneAmount Amount to be released per milestone
     * @param _totalMilestones Total number of milestones in the agreement
     */
    function createAgreement(
        address _funder,
        address _founder,
        uint256 _fundsAllocated,
        uint256 _milestoneAmount,
        uint256 _totalMilestones
    ) external returns (uint256) {
        require(_funder != address(0), "Invalid funder address");
        require(_founder != address(0), "Invalid founder address");
        require(_fundsAllocated > 0, "Funds allocated must be greater than zero");
        require(_milestoneAmount > 0, "Milestone amount must be greater than zero");
        require(_totalMilestones > 0, "Total milestones must be greater than zero");

        // Increment agreement counter
        agreementCounter++;

        // Create a new agreement
        agreements[agreementCounter] = Agreement({
            fundsAllocated: _fundsAllocated,
            milestoneAmount: _milestoneAmount,
            milestonesCompleted: 0,
            totalMilestones: _totalMilestones,
            isActive: true,
            isTerminated: false,
            funder: _funder,
            founder: _founder
        });

        emit AgreementCreated(agreementCounter, _funder, _founder);
        return agreementCounter;
    }

    /**
     * @dev Disburses funds for a completed milestone
     * @param agreementId ID of the agreement
     */
    function disburseFunds(uint256 agreementId) external onlyFunder(agreementId) isAgreementActive(agreementId) {
        Agreement storage agreement = agreements[agreementId];

        require(agreement.milestonesCompleted < agreement.totalMilestones, "All milestones completed");
        
        uint256 fundsToDisburse = agreement.milestoneAmount;
        require(fundsToDisburse <= agreement.fundsAllocated, "Insufficient allocated funds");

        agreement.milestonesCompleted++;
        agreement.fundsAllocated -= fundsToDisburse;

        // Transfer funds to the founder
        (bool sent, ) = agreement.founder.call{value: fundsToDisburse}("");
        require(sent, "Failed to disburse funds");

        emit FundsDisbursed(agreementId, fundsToDisburse);
    }

    /**
     * @dev Terminates an agreement
     * @param agreementId ID of the agreement
     */
    function terminateAgreement(uint256 agreementId) external onlyFunder(agreementId) isAgreementActive(agreementId) {
        Agreement storage agreement = agreements[agreementId];

        agreement.isTerminated = true;
        agreement.isActive = false;

        emit AgreementTerminated(agreementId);
    }

    /**
     * @dev Allows the founder to mark the agreement as inactive (optional safeguard mechanism)
     * @param agreementId ID of the agreement
     */
    function deactivateAgreement(uint256 agreementId) external onlyFounder(agreementId) isAgreementActive(agreementId) {
        Agreement storage agreement = agreements[agreementId];

        agreement.isActive = false;

        emit AgreementTerminated(agreementId);
    }

    // Fallback function to accept ETH
    receive() external payable {}

    // Get details of an agreement
    function getAgreementDetails(uint256 agreementId) external view returns (Agreement memory) {
        return agreements[agreementId];
    }
}
```
