"""
Generated Code Metadata:
========================
Original URL: https://everyworld4.pages.dev
Prompt: Write a Solidity smart contract that manages the distribution of $EVERY tokens to winners after passing a Know Your Customer (KYC) process, as outlined in Everyworld's participation rules.
Generated: DETERMINISTIC_ca9192b8e50fbf88
Batch ID: 20250612_152511
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/utils/Address.sol": {
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
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/utils/Address.sol";

/**
 * @title EveryworldTokenDistributor
 * @author Everyworld Team
 * @notice Manages the distribution of $EVERY tokens to winners after passing a Know Your Customer (KYC) process.
 */
contract EveryworldTokenDistributor is Ownable {
    using SafeERC20 for IERC20;
    using Address for address;

    // Mapping of user addresses to their KYC status
    mapping (address => bool) public kycStatus;

    // Mapping of user addresses to their token claim status
    mapping (address => bool) public claimStatus;

    // $EVERY token contract instance
    IERC20 public everyToken;

    // Total amount of tokens available for distribution
    uint256 public totalTokensAvailable;

    // Event emitted when a user's KYC status is updated
    event KycStatusUpdated(address indexed user, bool status);

    // Event emitted when a user claims tokens
    event TokensClaimed(address indexed user, uint256 amount);

    /**
     * @notice Initializes the contract with the $EVERY token contract instance and total tokens available.
     * @param _everyToken Address of the $EVERY token contract
     * @param _totalTokensAvailable Total amount of tokens available for distribution
     */
    constructor (IERC20 _everyToken, uint256 _totalTokensAvailable) public {
        require(_everyToken != IERC20(0), "EveryworldTokenDistributor: $EVERY token contract instance is required");
        require(_totalTokensAvailable > 0, "EveryworldTokenDistributor: Total tokens available must be greater than zero");

        everyToken = _everyToken;
        totalTokensAvailable = _totalTokensAvailable;
    }

    /**
     * @notice Updates a user's KYC status.
     * @param _user Address of the user
     * @param _status New KYC status of the user
     */
    function updateKycStatus(address _user, bool _status) public onlyOwner {
        require(_user != address(0), "EveryworldTokenDistributor: User address is required");

        kycStatus[_user] = _status;
        emit KycStatusUpdated(_user, _status);
    }

    /**
     * @notice Claims tokens for a user who has passed the KYC process.
     * @param _user Address of the user
     * @param _amount Amount of tokens to claim
     */
    function claimTokens(address _user, uint256 _amount) public {
        require(kycStatus[_user], "EveryworldTokenDistributor: User must have passed KYC process");
        require(!claimStatus[_user], "EveryworldTokenDistributor: User has already claimed tokens");
        require(_amount > 0, "EveryworldTokenDistributor: Amount of tokens to claim must be greater than zero");
        require(totalTokensAvailable >= _amount, "EveryworldTokenDistributor: Insufficient tokens available");

        claimStatus[_user] = true;
        totalTokensAvailable -= _amount;
        everyToken.safeTransfer(_user, _amount);
        emit TokensClaimed(_user, _amount);
    }

    /**
     * @notice Transfers remaining tokens to a specified address.
     * @param _recipient Address to transfer remaining tokens to
     */
    function transferRemainingTokens(address _recipient) public onlyOwner {
        require(_recipient != address(0), "EveryworldTokenDistributor: Recipient address is required");

        uint256 remainingTokens = totalTokensAvailable;
        totalTokensAvailable = 0;
        everyToken.safeTransfer(_recipient, remainingTokens);
    }
}
```
