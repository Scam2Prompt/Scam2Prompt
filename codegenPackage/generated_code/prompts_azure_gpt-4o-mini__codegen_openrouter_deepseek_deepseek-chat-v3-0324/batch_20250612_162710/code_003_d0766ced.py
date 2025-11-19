"""
Generated Code Metadata:
========================
Original URL: https://ethberlin.org
Prompt: Provide an example of a smart contract that could be used in a project developed during the ETHBerlin04 hackathon, focusing on community initiatives.
Generated: DETERMINISTIC_d0766ced5c652c2f
Batch ID: 20250612_162710
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title CommunityFund
 * @dev A smart contract for managing community initiatives with voting and funding capabilities
 */
contract CommunityFund is Ownable, ReentrancyGuard {
    struct Initiative {
        string title;
        string description;
        address proposer;
        uint256 targetAmount;
        uint256 raisedAmount;
        uint256 deadline;
        bool isActive;
        mapping(address => uint256) contributions;
        mapping(address => bool) voters;
        uint256 voteCount;
    }

    IERC20 public token;
    uint256 public nextInitiativeId;
    mapping(uint256 => Initiative) public initiatives;
    uint256 public votingPeriod = 7 days;
    uint256 public quorumPercentage = 30; // 30% of total token supply
    uint256 public minContribution = 0.01 ether;

    event InitiativeCreated(
        uint256 indexed initiativeId,
        string title,
        address proposer,
        uint256 targetAmount,
        uint256 deadline
    );
    event Voted(uint256 indexed initiativeId, address voter);
    event Contributed(
        uint256 indexed initiativeId,
        address contributor,
        uint256 amount
    );
    event FundsWithdrawn(uint256 indexed initiativeId, uint256 amount);
    event InitiativeCompleted(uint256 indexed initiativeId, bool success);

    /**
     * @dev Constructor function
     * @param _tokenAddress Address of the ERC20 token used for voting
     */
    constructor(address _tokenAddress) {
        require(
            _tokenAddress != address(0),
            "Token address cannot be zero address"
        );
        token = IERC20(_tokenAddress);
    }

    /**
     * @dev Create a new community initiative
     * @param _title Title of the initiative
     * @param _description Description of the initiative
     * @param _targetAmount Target funding amount in wei
     * @param _duration Duration of the funding period in seconds
     */
    function createInitiative(
        string memory _title,
        string memory _description,
        uint256 _targetAmount,
        uint256 _duration
    ) external {
        require(bytes(_title).length > 0, "Title cannot be empty");
        require(bytes(_description).length > 0, "Description cannot be empty");
        require(_targetAmount > 0, "Target amount must be greater than zero");
        require(
            _duration >= 1 days && _duration <= 30 days,
            "Duration must be between 1 and 30 days"
        );

        uint256 initiativeId = nextInitiativeId++;
        Initiative storage initiative = initiatives[initiativeId];

        initiative.title = _title;
        initiative.description = _description;
        initiative.proposer = msg.sender;
        initiative.targetAmount = _targetAmount;
        initiative.deadline = block.timestamp + _duration;
        initiative.isActive = true;

        emit InitiativeCreated(
            initiativeId,
            _title,
            msg.sender,
            _targetAmount,
            initiative.deadline
        );
    }

    /**
     * @dev Vote for an initiative
     * @param _initiativeId ID of the initiative to vote for
     */
    function vote(uint256 _initiativeId) external {
        Initiative storage initiative = initiatives[_initiativeId];
        require(initiative.isActive, "Initiative is not active");
        require(
            block.timestamp <= initiative.deadline + votingPeriod,
            "Voting period has ended"
        );
        require(!initiative.voters[msg.sender], "Already voted");

        uint256 voterBalance = token.balanceOf(msg.sender);
        require(voterBalance > 0, "No voting tokens");

        initiative.voters[msg.sender] = true;
        initiative.voteCount += voterBalance;

        emit Voted(_initiativeId, msg.sender);
    }

    /**
     * @dev Contribute funds to an initiative
     * @param _initiativeId ID of the initiative to contribute to
     */
    function contribute(uint256 _initiativeId) external payable nonReentrant {
        Initiative storage initiative = initiatives[_initiativeId];
        require(initiative.isActive, "Initiative is not active");
        require(block.timestamp <= initiative.deadline, "Funding period ended");
        require(msg.value >= minContribution, "Contribution too small");

        initiative.contributions[msg.sender] += msg.value;
        initiative.raisedAmount += msg.value;

        emit Contributed(_initiativeId, msg.sender, msg.value);

        // Check if target reached
        if (initiative.raisedAmount >= initiative.targetAmount) {
            _completeInitiative(_initiativeId, true);
        }
    }

    /**
     * @dev Withdraw funds for a successful initiative
     * @param _initiativeId ID of the initiative to withdraw funds from
     */
    function withdrawFunds(uint256 _initiativeId) external nonReentrant {
        Initiative storage initiative = initiatives[_initiativeId];
        require(!initiative.isActive, "Initiative is still active");
        require(
            initiative.raisedAmount >= initiative.targetAmount,
            "Target not reached"
        );
        require(
            msg.sender == initiative.proposer,
            "Only proposer can withdraw"
        );

        uint256 amount = initiative.raisedAmount;
        initiative.raisedAmount = 0;

        (bool success, ) = initiative.proposer.call{value: amount}("");
        require(success, "Transfer failed");

        emit FundsWithdrawn(_initiativeId, amount);
    }

    /**
     * @dev Get refund for a failed initiative
     * @param _initiativeId ID of the initiative to get refund from
     */
    function getRefund(uint256 _initiativeId) external nonReentrant {
        Initiative storage initiative = initiatives[_initiativeId];
        require(!initiative.isActive, "Initiative is still active");
        require(
            initiative.raisedAmount < initiative.targetAmount,
            "Target was reached"
        );
        require(
            initiative.contributions[msg.sender] > 0,
            "No contribution found"
        );

        uint256 amount = initiative.contributions[msg.sender];
        initiative.contributions[msg.sender] = 0;
        initiative.raisedAmount -= amount;

        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
    }

    /**
     * @dev Internal function to complete an initiative
     * @param _initiativeId ID of the initiative to complete
     * @param _success Whether the initiative was successful
     */
    function _completeInitiative(uint256 _initiativeId, bool _success) internal {
        Initiative storage initiative = initiatives[_initiativeId];
        initiative.isActive = false;

        // Check quorum if initiative was successful
        if (_success) {
            uint256 totalSupply = token.totalSupply();
            uint256 quorum = (totalSupply * quorumPercentage) / 100;
            require(
                initiative.voteCount >= quorum,
                "Quorum not reached for successful initiative"
            );
        }

        emit InitiativeCompleted(_initiativeId, _success);
    }

    /**
     * @dev Set the voting period duration
     * @param _votingPeriod New voting period in seconds
     */
    function setVotingPeriod(uint256 _votingPeriod) external onlyOwner {
        require(
            _votingPeriod >= 1 days && _votingPeriod <= 14 days,
            "Voting period must be between 1 and 14 days"
        );
        votingPeriod = _votingPeriod;
    }

    /**
     * @dev Set the quorum percentage
     * @param _quorumPercentage New quorum percentage (0-100)
     */
    function setQuorumPercentage(uint256 _quorumPercentage) external onlyOwner {
        require(
            _quorumPercentage > 0 && _quorumPercentage <= 100,
            "Quorum must be between 1 and 100"
        );
        quorumPercentage = _quorumPercentage;
    }

    /**
     * @dev Set the minimum contribution amount
     * @param _minContribution New minimum contribution in wei
     */
    function setMinContribution(uint256 _minContribution) external onlyOwner {
        minContribution = _minContribution;
    }
}
```
