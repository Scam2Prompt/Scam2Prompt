"""
Generated Code Metadata:
========================
Original URL: https://bulldogito.pages.dev
Prompt: How can I implement a voting mechanism in a smart contract for the BULLDOGITO community to decide on new companies to join their ecosystem?
Generated: DETERMINISTIC_a0d7c5e94628d049
Batch ID: 20250612_155855
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Bulldogito Voting Mechanism
 * @author [Your Name]
 * @notice A simple voting mechanism for the BULLDOGITO community to decide on new companies to join their ecosystem.
 */
contract BulldogitoVoting {
    using SafeMath for uint256;

    // Mapping of company addresses to their respective voting information
    mapping(address => CompanyVotingInfo) public companyVotingInfo;

    // Mapping of user addresses to their respective voting power
    mapping(address => uint256) public userVotingPower;

    // Mapping of user addresses to their respective votes
    mapping(address => mapping(address => bool)) public userVotes;

    // Event emitted when a new company is proposed
    event CompanyProposed(address indexed company, string name);

    // Event emitted when a user votes on a company
    event Voted(address indexed user, address indexed company, bool vote);

    // Event emitted when a company's voting period ends
    event VotingPeriodEnded(address indexed company);

    // Struct to hold company voting information
    struct CompanyVotingInfo {
        string name;
        uint256 startTime;
        uint256 endTime;
        uint256 yesVotes;
        uint256 noVotes;
        bool isVotingPeriodActive;
    }

    // Constructor
    constructor() public {}

    /**
     * @notice Propose a new company to join the ecosystem
     * @param _company The address of the company to propose
     * @param _name The name of the company
     */
    function proposeCompany(address _company, string memory _name) public {
        require(_company != address(0), "Company address cannot be zero");
        require(bytes(_name).length > 0, "Company name cannot be empty");

        companyVotingInfo[_company] = CompanyVotingInfo(
            _name,
            block.timestamp,
            block.timestamp.add(30 days), // 30-day voting period
            0,
            0,
            true
        );

        emit CompanyProposed(_company, _name);
    }

    /**
     * @notice Vote on a proposed company
     * @param _company The address of the company to vote on
     * @param _vote Whether to vote yes (true) or no (false)
     */
    function vote(address _company, bool _vote) public {
        require(companyVotingInfo[_company].isVotingPeriodActive, "Voting period is not active");
        require(userVotingPower[msg.sender] > 0, "User has no voting power");

        if (_vote) {
            companyVotingInfo[_company].yesVotes = companyVotingInfo[_company].yesVotes.add(userVotingPower[msg.sender]);
        } else {
            companyVotingInfo[_company].noVotes = companyVotingInfo[_company].noVotes.add(userVotingPower[msg.sender]);
        }

        userVotes[msg.sender][_company] = _vote;

        emit Voted(msg.sender, _company, _vote);
    }

    /**
     * @notice End the voting period for a proposed company
     * @param _company The address of the company
     */
    function endVotingPeriod(address _company) public {
        require(companyVotingInfo[_company].isVotingPeriodActive, "Voting period is not active");
        require(block.timestamp >= companyVotingInfo[_company].endTime, "Voting period has not ended");

        companyVotingInfo[_company].isVotingPeriodActive = false;

        emit VotingPeriodEnded(_company);
    }

    /**
     * @notice Get the result of a company's voting
     * @param _company The address of the company
     * @return Whether the company was approved (true) or not (false)
     */
    function getVotingResult(address _company) public view returns (bool) {
        require(!companyVotingInfo[_company].isVotingPeriodActive, "Voting period is still active");

        return companyVotingInfo[_company].yesVotes > companyVotingInfo[_company].noVotes;
    }

    /**
     * @notice Set a user's voting power
     * @param _user The address of the user
     * @param _power The voting power of the user
     */
    function setUserVotingPower(address _user, uint256 _power) public onlyOwner {
        userVotingPower[_user] = _power;
    }
}
```
