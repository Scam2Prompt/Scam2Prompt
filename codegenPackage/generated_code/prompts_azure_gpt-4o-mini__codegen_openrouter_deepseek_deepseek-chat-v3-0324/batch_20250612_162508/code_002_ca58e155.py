"""
Generated Code Metadata:
========================
Original URL: https://metalcoin.vercel.app
Prompt: Create a smart contract in Solidity that implements the Proof of Hilarity mechanism for the METAL token, allowing miners to submit memes for rewards.
Generated: DETERMINISTIC_ca58e155dfd101d5
Batch ID: 20250612_162508
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract METAL is ERC20, Ownable {
    using Counters for Counters.Counter;

    // Struct to represent a meme submission
    struct MemeSubmission {
        address submitter;
        string memeHash; // IPFS or Arweave hash of the meme
        uint256 timestamp;
        uint256 upvotes;
        bool isApproved;
    }

    // Constants
    uint256 public constant REWARD_AMOUNT = 100 * 10**18; // 100 METAL tokens
    uint256 public constant APPROVAL_THRESHOLD = 5; // Minimum upvotes for approval
    uint256 public constant SUBMISSION_COOLDOWN = 1 days;

    // State variables
    Counters.Counter private _submissionIds;
    mapping(uint256 => MemeSubmission) public submissions;
    mapping(address => uint256) public lastSubmissionTime;
    mapping(address => mapping(uint256 => bool)) public hasUpvoted;

    // Events
    event MemeSubmitted(uint256 indexed submissionId, address indexed submitter, string memeHash);
    event MemeApproved(uint256 indexed submissionId, address indexed submitter, uint256 reward);
    event MemeUpvoted(uint256 indexed submissionId, address indexed upvoter);

    constructor() ERC20("METAL", "METAL") {
        _mint(msg.sender, 1000000 * 10**18); // Initial supply: 1,000,000 METAL
    }

    /**
     * @dev Submit a meme for Proof of Hilarity
     * @param memeHash The IPFS/Arweave hash of the meme
     */
    function submitMeme(string memory memeHash) external {
        require(bytes(memeHash).length > 0, "Empty meme hash");
        require(
            block.timestamp >= lastSubmissionTime[msg.sender] + SUBMISSION_COOLDOWN,
            "Submission cooldown active"
        );

        _submissionIds.increment();
        uint256 newSubmissionId = _submissionIds.current();

        submissions[newSubmissionId] = MemeSubmission({
            submitter: msg.sender,
            memeHash: memeHash,
            timestamp: block.timestamp,
            upvotes: 0,
            isApproved: false
        });

        lastSubmissionTime[msg.sender] = block.timestamp;
        emit MemeSubmitted(newSubmissionId, msg.sender, memeHash);
    }

    /**
     * @dev Upvote a meme submission
     * @param submissionId The ID of the submission to upvote
     */
    function upvoteMeme(uint256 submissionId) external {
        require(submissionId > 0 && submissionId <= _submissionIds.current(), "Invalid submission ID");
        require(!hasUpvoted[msg.sender][submissionId], "Already upvoted");
        require(!submissions[submissionId].isApproved, "Submission already approved");

        MemeSubmission storage submission = submissions[submissionId];
        submission.upvotes += 1;
        hasUpvoted[msg.sender][submissionId] = true;

        emit MemeUpvoted(submissionId, msg.sender);

        // Check if submission meets approval threshold
        if (submission.upvotes >= APPROVAL_THRESHOLD && !submission.isApproved) {
            submission.isApproved = true;
            _mint(submission.submitter, REWARD_AMOUNT);
            emit MemeApproved(submissionId, submission.submitter, REWARD_AMOUNT);
        }
    }

    /**
     * @dev Get details of a submission
     * @param submissionId The ID of the submission
     * @return MemeSubmission details
     */
    function getSubmission(uint256 submissionId) external view returns (MemeSubmission memory) {
        require(submissionId > 0 && submissionId <= _submissionIds.current(), "Invalid submission ID");
        return submissions[submissionId];
    }

    /**
     * @dev Get total number of submissions
     * @return uint256 total submissions count
     */
    function getTotalSubmissions() external view returns (uint256) {
        return _submissionIds.current();
    }
}
```
