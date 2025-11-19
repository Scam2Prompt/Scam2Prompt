"""
Generated Code Metadata:
========================
Original URL: https://lightchain-dapp.web.app
Prompt: Write a Solidity contract to facilitate the rollout of Lightchain AI’s testnet, incorporating performance optimization and feedback integration features.
Generated: DETERMINISTIC_b0c96026efdcda8e
Batch ID: 20250612_154820
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";

/**
 * @title Lightchain AI Testnet Contract
 * @author [Your Name]
 * @notice This contract facilitates the rollout of Lightchain AI's testnet,
 *          incorporating performance optimization and feedback integration features.
 */
contract LightchainAI {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user addresses to their respective testnet participant IDs
    mapping(address => uint256) public participantIds;

    // Mapping of testnet participant IDs to their respective performance scores
    mapping(uint256 => uint256) public performanceScores;

    // Mapping of testnet participant IDs to their respective feedback
    mapping(uint256 => string) public feedback;

    // IERC20 token used for testnet incentives
    IERC20 public incentiveToken;

    // Address of the testnet administrator
    address public admin;

    // Event emitted when a new participant joins the testnet
    event NewParticipant(address indexed participant, uint256 indexed participantId);

    // Event emitted when a participant's performance score is updated
    event PerformanceScoreUpdated(uint256 indexed participantId, uint256 newScore);

    // Event emitted when a participant submits feedback
    event FeedbackSubmitted(uint256 indexed participantId, string feedback);

    /**
     * @dev Initializes the contract with the incentive token and administrator address
     * @param _incentiveToken Address of the IERC20 token used for testnet incentives
     * @param _admin Address of the testnet administrator
     */
    constructor(IERC20 _incentiveToken, address _admin) public {
        require(_admin != address(0), "Admin address cannot be zero");
        incentiveToken = _incentiveToken;
        admin = _admin;
    }

    /**
     * @dev Allows the administrator to add a new participant to the testnet
     * @param _participant Address of the new participant
     */
    function addParticipant(address _participant) public {
        require(msg.sender == admin, "Only the administrator can add participants");
        require(participantIds[_participant] == 0, "Participant already exists");

        uint256 participantId = uint256(keccak256(abi.encodePacked(_participant))) % (2**256 - 1);
        participantIds[_participant] = participantId;
        emit NewParticipant(_participant, participantId);
    }

    /**
     * @dev Updates a participant's performance score
     * @param _participantId ID of the participant
     * @param _newScore New performance score
     */
    function updatePerformanceScore(uint256 _participantId, uint256 _newScore) public {
        require(participantIds[msg.sender] == _participantId, "Only the participant can update their score");
        performanceScores[_participantId] = _newScore;
        emit PerformanceScoreUpdated(_participantId, _newScore);
    }

    /**
     * @dev Allows a participant to submit feedback
     * @param _feedback Feedback string
     */
    function submitFeedback(string memory _feedback) public {
        uint256 participantId = participantIds[msg.sender];
        require(participantId != 0, "Participant does not exist");
        feedback[participantId] = _feedback;
        emit FeedbackSubmitted(participantId, _feedback);
    }

    /**
     * @dev Allows the administrator to distribute incentives to participants
     * @param _participantIds Array of participant IDs
     * @param _amounts Array of incentive amounts
     */
    function distributeIncentives(uint256[] memory _participantIds, uint256[] memory _amounts) public {
        require(msg.sender == admin, "Only the administrator can distribute incentives");
        require(_participantIds.length == _amounts.length, "Participant IDs and amounts arrays must be the same length");

        for (uint256 i = 0; i < _participantIds.length; i++) {
            uint256 participantId = _participantIds[i];
            uint256 amount = _amounts[i];
            address participantAddress = getParticipantAddress(participantId);
            require(participantAddress != address(0), "Participant does not exist");
            incentiveToken.safeTransfer(participantAddress, amount);
        }
    }

    /**
     * @dev Retrieves the address of a participant given their ID
     * @param _participantId ID of the participant
     * @return Address of the participant
     */
    function getParticipantAddress(uint256 _participantId) internal view returns (address) {
        for (address participant in participantIds) {
            if (participantIds[participant] == _participantId) {
                return participant;
            }
        }
        return address(0);
    }
}
```
