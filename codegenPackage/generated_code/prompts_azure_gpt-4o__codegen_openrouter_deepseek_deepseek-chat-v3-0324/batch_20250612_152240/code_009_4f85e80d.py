"""
Generated Code Metadata:
========================
Original URL: https://bafybeifq4glolowymafy6kuniwbsh4kspbnetu3fgelnegknbnkai2ahje.ipfs.dweb.link
Prompt: Generate code to implement trust and reputation systems on Linea's network using its zkSNARK-based cryptographic infrastructure.
Generated: DETERMINISTIC_4f85e80d8e048db3
Batch ID: 20250612_152240
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

import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "./IVerifier.sol"; // Interface for zkSNARK verifier

/**
 * @title LineaTrustReputationSystem
 * @dev A trust and reputation system using zkSNARKs on Linea network
 */
contract LineaTrustReputationSystem is Ownable {
    using Counters for Counters.Counter;

    // Struct to store reputation data
    struct Reputation {
        uint256 score;
        uint256 lastUpdate;
        uint256 positiveCount;
        uint256 negativeCount;
    }

    // Struct for zkSNARK proof
    struct Proof {
        uint256[2] a;
        uint256[2][2] b;
        uint256[2] c;
    }

    // Events
    event ReputationUpdated(address indexed user, uint256 newScore);
    event FeedbackSubmitted(address indexed from, address indexed to, bool isPositive);

    // State variables
    Counters.Counter private _feedbackNonce;
    IVerifier private verifier;
    mapping(address => Reputation) public reputations;
    mapping(bytes32 => bool) private _usedNullifiers;

    // Constants
    uint256 public constant MAX_SCORE = 1000;
    uint256 public constant MIN_SCORE = 0;
    uint256 public constant SCORE_DECAY_PERIOD = 30 days;
    uint256 public constant SCORE_DECAY_AMOUNT = 10;

    /**
     * @dev Constructor
     * @param _verifierAddress Address of the zkSNARK verifier contract
     */
    constructor(address _verifierAddress) {
        verifier = IVerifier(_verifierAddress);
    }

    /**
     * @dev Submit feedback with zkSNARK proof
     * @param _to Address receiving feedback
     * @param _isPositive Whether feedback is positive
     * @param _proof zkSNARK proof
     * @param _nullifierHash Unique hash to prevent double spending
     * @param _signal Signal containing feedback data
     */
    function submitFeedback(
        address _to,
        bool _isPositive,
        Proof memory _proof,
        uint256 _nullifierHash,
        uint256 _signal
    ) external {
        require(_to != address(0), "Invalid recipient address");
        require(!_usedNullifiers[bytes32(_nullifierHash)], "Proof already used");

        // Verify the zkSNARK proof
        require(
            verifier.verifyProof(
                _proof.a,
                _proof.b,
                _proof.c,
                [_nullifierHash, _signal]
            ),
            "Invalid proof"
        );

        _usedNullifiers[bytes32(_nullifierHash)] = true;
        _processFeedback(_to, _isPositive);
    }

    /**
     * @dev Internal function to process feedback and update reputation
     * @param _to Address receiving feedback
     * @param _isPositive Whether feedback is positive
     */
    function _processFeedback(address _to, bool _isPositive) internal {
        Reputation storage rep = reputations[_to];

        // Apply score decay if needed
        _applyDecay(_to);

        // Update reputation
        if (_isPositive) {
            rep.score = (rep.score + 10) > MAX_SCORE ? MAX_SCORE : rep.score + 10;
            rep.positiveCount += 1;
        } else {
            rep.score = (rep.score < 10 + MIN_SCORE) ? MIN_SCORE : rep.score - 10;
            rep.negativeCount += 1;
        }

        rep.lastUpdate = block.timestamp;
        emit FeedbackSubmitted(msg.sender, _to, _isPositive);
        emit ReputationUpdated(_to, rep.score);
    }

    /**
     * @dev Apply score decay if the last update was too long ago
     * @param _user Address of the user to check
     */
    function _applyDecay(address _user) internal {
        Reputation storage rep = reputations[_user];
        if (rep.lastUpdate == 0) {
            rep.lastUpdate = block.timestamp;
            return;
        }

        uint256 timePassed = block.timestamp - rep.lastUpdate;
        if (timePassed > SCORE_DECAY_PERIOD) {
            uint256 decayCycles = timePassed / SCORE_DECAY_PERIOD;
            uint256 decayAmount = decayCycles * SCORE_DECAY_AMOUNT;
            
            if (rep.score > decayAmount) {
                rep.score -= decayAmount;
            } else {
                rep.score = MIN_SCORE;
            }
            
            rep.lastUpdate = block.timestamp;
        }
    }

    /**
     * @dev Get reputation score for a user
     * @param _user Address of the user
     * @return Current reputation score
     */
    function getReputationScore(address _user) external view returns (uint256) {
        return reputations[_user].score;
    }

    /**
     * @dev Get reputation details for a user
     * @param _user Address of the user
     * @return score Current reputation score
     * @return lastUpdate Timestamp of last update
     * @return positiveCount Total positive feedback count
     * @return negativeCount Total negative feedback count
     */
    function getReputationDetails(address _user) external view returns (
        uint256 score,
        uint256 lastUpdate,
        uint256 positiveCount,
        uint256 negativeCount
    ) {
        Reputation memory rep = reputations[_user];
        return (rep.score, rep.lastUpdate, rep.positiveCount, rep.negativeCount);
    }

    /**
     * @dev Update verifier contract (only owner)
     * @param _newVerifier Address of the new verifier contract
     */
    function updateVerifier(address _newVerifier) external onlyOwner {
        require(_newVerifier != address(0), "Invalid verifier address");
        verifier = IVerifier(_newVerifier);
    }
}
```

```solidity
// IVerifier.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IVerifier {
    function verifyProof(
        uint256[2] memory a,
        uint256[2][2] memory b,
        uint256[2] memory c,
        uint256[2] memory input
    ) external view returns (bool);
}
```
