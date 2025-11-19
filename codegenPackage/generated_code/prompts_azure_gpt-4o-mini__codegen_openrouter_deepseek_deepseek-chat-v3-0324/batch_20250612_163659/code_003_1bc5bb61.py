"""
Generated Code Metadata:
========================
Original URL: https://iqratechpoint.pages.dev
Prompt: Generate a sample smart contract for managing scholarships and grants using IQRA Token on the Binance Smart Chain.
Generated: DETERMINISTIC_1bc5bb618d3296a1
Batch ID: 20250612_163659
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title IQRA Scholarship and Grant Manager
 * @dev A smart contract for managing scholarships and grants using IQRA Token
 * on the Binance Smart Chain. Supports creating funds, applying, and disbursing awards.
 */
contract IQRAFundManager is Ownable, ReentrancyGuard {
    IERC20 public iqraToken;

    // Struct to represent a fund
    struct Fund {
        address creator;
        string name;
        string description;
        uint256 totalAmount;
        uint256 disbursedAmount;
        uint256 maxApplicants;
        uint256 applicationDeadline;
        bool isActive;
        mapping(address => bool) applicants;
        mapping(address => bool) awardees;
    }

    // Mapping of fund ID to Fund
    mapping(uint256 => Fund) public funds;
    uint256 public fundCount;

    // Events
    event FundCreated(
        uint256 fundId,
        address creator,
        string name,
        uint256 totalAmount,
        uint256 applicationDeadline
    );
    event ApplicationSubmitted(uint256 fundId, address applicant);
    event AwardDisbursed(uint256 fundId, address awardee, uint256 amount);
    event FundStatusChanged(uint256 fundId, bool isActive);
    event FundsWithdrawn(uint256 fundId, address creator, uint256 amount);

    /**
     * @dev Constructor initializes the contract with the IQRA Token address
     * @param _iqraTokenAddress Address of the IQRA Token contract
     */
    constructor(address _iqraTokenAddress) {
        require(
            _iqraTokenAddress != address(0),
            "IQRA token address cannot be zero"
        );
        iqraToken = IERC20(_iqraTokenAddress);
    }

    /**
     * @dev Creates a new scholarship/grant fund
     * @param _name Name of the fund
     * @param _description Description of the fund
     * @param _totalAmount Total IQRA tokens to be allocated
     * @param _maxApplicants Maximum number of applicants
     * @param _applicationDeadline Deadline for applications (UNIX timestamp)
     */
    function createFund(
        string memory _name,
        string memory _description,
        uint256 _totalAmount,
        uint256 _maxApplicants,
        uint256 _applicationDeadline
    ) external {
        require(bytes(_name).length > 0, "Name cannot be empty");
        require(bytes(_description).length > 0, "Description cannot be empty");
        require(_totalAmount > 0, "Amount must be greater than zero");
        require(
            _applicationDeadline > block.timestamp,
            "Deadline must be in the future"
        );

        // Transfer tokens from creator to this contract
        require(
            iqraToken.transferFrom(msg.sender, address(this), _totalAmount),
            "Token transfer failed"
        );

        uint256 fundId = fundCount++;
        Fund storage newFund = funds[fundId];
        newFund.creator = msg.sender;
        newFund.name = _name;
        newFund.description = _description;
        newFund.totalAmount = _totalAmount;
        newFund.maxApplicants = _maxApplicants;
        newFund.applicationDeadline = _applicationDeadline;
        newFund.isActive = true;

        emit FundCreated(
            fundId,
            msg.sender,
            _name,
            _totalAmount,
            _applicationDeadline
        );
    }

    /**
     * @dev Apply for a fund
     * @param _fundId ID of the fund to apply for
     */
    function applyForFund(uint256 _fundId) external {
        require(_fundId < fundCount, "Invalid fund ID");
        Fund storage fund = funds[_fundId];

        require(fund.isActive, "Fund is not active");
        require(
            block.timestamp <= fund.applicationDeadline,
            "Application deadline passed"
        );
        require(!fund.applicants[msg.sender], "Already applied");
        require(
            fund.maxApplicants == 0 ||
                getApplicantCount(_fundId) < fund.maxApplicants,
            "Maximum applicants reached"
        );

        fund.applicants[msg.sender] = true;
        emit ApplicationSubmitted(_fundId, msg.sender);
    }

    /**
     * @dev Disburse award to selected applicant
     * @param _fundId ID of the fund
     * @param _awardee Address of the awardee
     * @param _amount Amount to disburse
     */
    function disburseAward(
        uint256 _fundId,
        address _awardee,
        uint256 _amount
    ) external nonReentrant {
        require(_fundId < fundCount, "Invalid fund ID");
        Fund storage fund = funds[_fundId];

        require(msg.sender == fund.creator, "Only creator can disburse");
        require(fund.isActive, "Fund is not active");
        require(fund.applicants[_awardee], "Not an applicant");
        require(!fund.awardees[_awardee], "Already awarded");
        require(
            fund.disbursedAmount + _amount <= fund.totalAmount,
            "Insufficient funds"
        );

        fund.awardees[_awardee] = true;
        fund.disbursedAmount += _amount;

        require(
            iqraToken.transfer(_awardee, _amount),
            "Token transfer failed"
        );

        emit AwardDisbursed(_fundId, _awardee, _amount);
    }

    /**
     * @dev Toggle fund active status (only by creator)
     * @param _fundId ID of the fund
     * @param _isActive New status
     */
    function setFundActive(uint256 _fundId, bool _isActive) external {
        require(_fundId < fundCount, "Invalid fund ID");
        Fund storage fund = funds[_fundId];

        require(msg.sender == fund.creator, "Only creator can modify");
        require(fund.isActive != _isActive, "Status already set");

        fund.isActive = _isActive;
        emit FundStatusChanged(_fundId, _isActive);
    }

    /**
     * @dev Withdraw remaining funds after deadline (only by creator)
     * @param _fundId ID of the fund
     */
    function withdrawRemainingFunds(uint256 _fundId) external nonReentrant {
        require(_fundId < fundCount, "Invalid fund ID");
        Fund storage fund = funds[_fundId];

        require(msg.sender == fund.creator, "Only creator can withdraw");
        require(
            block.timestamp > fund.applicationDeadline,
            "Deadline not passed"
        );

        uint256 remainingAmount = fund.totalAmount - fund.disbursedAmount;
        require(remainingAmount > 0, "No funds to withdraw");

        fund.totalAmount = fund.disbursedAmount; // Mark all as disbursed

        require(
            iqraToken.transfer(msg.sender, remainingAmount),
            "Token transfer failed"
        );

        emit FundsWithdrawn(_fundId, msg.sender, remainingAmount);
    }

    /**
     * @dev Get applicant count for a fund
     * @param _fundId ID of the fund
     * @return count Number of applicants
     */
    function getApplicantCount(uint256 _fundId) public view returns (uint256) {
        require(_fundId < fundCount, "Invalid fund ID");
        Fund storage fund = funds[_fundId];

        uint256 count = 0;
        // Note: In production, you might want to maintain a separate counter
        // as this approach is gas-intensive for large numbers of applicants
        for (uint256 i = 0; i < fundCount; i++) {
            if (fund.applicants[address(uint160(i))]) {
                count++;
            }
        }
        return count;
    }

    /**
     * @dev Check if address is an applicant for a fund
     * @param _fundId ID of the fund
     * @param _applicant Address to check
     * @return isApplicant True if address is an applicant
     */
    function isApplicant(uint256 _fundId, address _applicant)
        public
        view
        returns (bool)
    {
        require(_fundId < fundCount, "Invalid fund ID");
        return funds[_fundId].applicants[_applicant];
    }

    /**
     * @dev Check if address is an awardee for a fund
     * @param _fundId ID of the fund
     * @param _awardee Address to check
     * @return isAwardee True if address is an awardee
     */
    function isAwardee(uint256 _fundId, address _awardee)
        public
        view
        returns (bool)
    {
        require(_fundId < fundCount, "Invalid fund ID");
        return funds[_fundId].awardees[_awardee];
    }
