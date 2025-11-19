"""
Generated Code Metadata:
========================
Original URL: https://singularity-finance.pages.dev
Prompt: Provide an example of a smart contract that allows users to contribute data for monetization in the AI economy on the Singularity Finance platform.
Generated: DETERMINISTIC_3e823b088364b887
Batch ID: 20250612_160038
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
 * @title AI Data Contribution Contract
 * @dev Allows users to contribute data for monetization in the AI economy
 */
contract AIDataContribution is Ownable, ReentrancyGuard {
    // Struct to store data contribution details
    struct Contribution {
        address contributor;
        string dataHash;
        uint256 timestamp;
        uint256 value;
        bool isVerified;
    }

    // Platform token for payments
    IERC20 public platformToken;

    // Contribution details mapping
    mapping(uint256 => Contribution) public contributions;
    uint256 public contributionCount;

    // Contributor balances
    mapping(address => uint256) public contributorBalances;

    // Verification threshold (percentage of contributors who must verify)
    uint256 public verificationThreshold = 70;

    // Verification votes
    mapping(uint256 => mapping(address => bool)) public verifications;
    mapping(uint256 => uint256) public verificationCounts;

    // Events
    event DataContributed(uint256 indexed id, address indexed contributor, string dataHash, uint256 value);
    event DataVerified(uint256 indexed id, address indexed verifier);
    event Withdrawal(address indexed contributor, uint256 amount);
    event VerificationThresholdUpdated(uint256 newThreshold);

    /**
     * @dev Constructor
     * @param _tokenAddress Address of the platform token
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        platformToken = IERC20(_tokenAddress);
    }

    /**
     * @dev Contribute data to the platform
     * @param _dataHash IPFS hash of the contributed data
     * @param _value Value of the contribution in platform tokens
     */
    function contributeData(string memory _dataHash, uint256 _value) external nonReentrant {
        require(bytes(_dataHash).length > 0, "Data hash cannot be empty");
        require(_value > 0, "Value must be greater than zero");

        // Transfer tokens from contributor to contract
        require(
            platformToken.transferFrom(msg.sender, address(this), _value),
            "Token transfer failed"
        );

        // Create new contribution
        contributionCount++;
        contributions[contributionCount] = Contribution({
            contributor: msg.sender,
            dataHash: _dataHash,
            timestamp: block.timestamp,
            value: _value,
            isVerified: false
        });

        emit DataContributed(contributionCount, msg.sender, _dataHash, _value);
    }

    /**
     * @dev Verify a data contribution
     * @param _contributionId ID of the contribution to verify
     */
    function verifyContribution(uint256 _contributionId) external {
        require(_contributionId > 0 && _contributionId <= contributionCount, "Invalid contribution ID");
        require(!contributions[_contributionId].isVerified, "Already verified");
        require(!verifications[_contributionId][msg.sender], "Already verified by this address");
        require(msg.sender != contributions[_contributionId].contributor, "Cannot verify own contribution");

        verifications[_contributionId][msg.sender] = true;
        verificationCounts[_contributionId]++;

        emit DataVerified(_contributionId, msg.sender);

        // Check if verification threshold is met
        if (verificationCounts[_contributionId] * 100 >= verificationThreshold) {
            contributions[_contributionId].isVerified = true;
            contributorBalances[contributions[_contributionId].contributor] += contributions[_contributionId].value;
        }
    }

    /**
     * @dev Withdraw accumulated balance
     */
    function withdraw() external nonReentrant {
        uint256 balance = contributorBalances[msg.sender];
        require(balance > 0, "No balance to withdraw");

        contributorBalances[msg.sender] = 0;
        require(platformToken.transfer(msg.sender, balance), "Token transfer failed");

        emit Withdrawal(msg.sender, balance);
    }

    /**
     * @dev Update verification threshold (owner only)
     * @param _newThreshold New verification threshold percentage
     */
    function setVerificationThreshold(uint256 _newThreshold) external onlyOwner {
        require(_newThreshold > 0 && _newThreshold <= 100, "Invalid threshold");
        verificationThreshold = _newThreshold;
        emit VerificationThresholdUpdated(_newThreshold);
    }

    /**
     * @dev Get contribution details
     * @param _contributionId ID of the contribution
     * @return Contribution details
     */
    function getContribution(uint256 _contributionId) external view returns (Contribution memory) {
        require(_contributionId > 0 && _contributionId <= contributionCount, "Invalid contribution ID");
        return contributions[_contributionId];
    }

    /**
     * @dev Get verification status for a contribution
     * @param _contributionId ID of the contribution
     * @param _verifier Address of the verifier
     * @return True if verified by the address
     */
    function isVerifiedBy(uint256 _contributionId, address _verifier) external view returns (bool) {
        require(_contributionId > 0 && _contributionId <= contributionCount, "Invalid contribution ID");
        return verifications[_contributionId][_verifier];
    }
}
```
