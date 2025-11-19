"""
Generated Code Metadata:
========================
Original URL: https://good-games-guild.gitbook.io
Prompt: Create a Solidity smart contract for implementing the HighTable Secret Deal Program, using the key features described in the Good Games Guild documentation.
Generated: DETERMINISTIC_18003293dc81789d
Batch ID: 20250612_153820
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title HighTable Secret Deal Program
 * @author [Your Name]
 * @notice Implementation of the HighTable Secret Deal Program as per Good Games Guild documentation
 */
contract HighTableSecretDealProgram {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of users to their deal info
    mapping(address => DealInfo) public userDeals;

    // Mapping of deal IDs to their info
    mapping(uint256 => DealInfo) public dealInfos;

    // ERC20 token used for deals
    IERC20 public token;

    // Unique deal ID counter
    uint256 public dealIdCounter;

    // Event emitted when a new deal is created
    event NewDeal(address indexed user, uint256 dealId);

    // Event emitted when a deal is claimed
    event DealClaimed(address indexed user, uint256 dealId);

    // Event emitted when a deal is expired
    event DealExpired(uint256 dealId);

    // Struct to hold deal information
    struct DealInfo {
        uint256 dealId;
        address user;
        uint256 amount;
        uint256 expirationTime;
        bool isClaimed;
    }

    /**
     * @notice Constructor
     * @param _token ERC20 token address
     */
    constructor(IERC20 _token) {
        token = _token;
        dealIdCounter = 0;
    }

    /**
     * @notice Create a new deal
     * @param _amount Deal amount
     * @param _expirationTime Deal expiration time in seconds
     */
    function createDeal(uint256 _amount, uint256 _expirationTime) public {
        require(_amount > 0, "Deal amount must be greater than 0");
        require(_expirationTime > block.timestamp, "Expiration time must be in the future");

        DealInfo memory dealInfo;
        dealInfo.dealId = dealIdCounter++;
        dealInfo.user = msg.sender;
        dealInfo.amount = _amount;
        dealInfo.expirationTime = _expirationTime;
        dealInfo.isClaimed = false;

        userDeals[msg.sender] = dealInfo;
        dealInfos[dealInfo.dealId] = dealInfo;

        emit NewDeal(msg.sender, dealInfo.dealId);
    }

    /**
     * @notice Claim a deal
     * @param _dealId Deal ID
     */
    function claimDeal(uint256 _dealId) public {
        DealInfo storage dealInfo = dealInfos[_dealId];
        require(dealInfo.dealId == _dealId, "Deal not found");
        require(dealInfo.user != address(0), "Deal user not found");
        require(!dealInfo.isClaimed, "Deal already claimed");
        require(block.timestamp < dealInfo.expirationTime, "Deal has expired");

        dealInfo.isClaimed = true;
        token.safeTransfer(msg.sender, dealInfo.amount);

        emit DealClaimed(dealInfo.user, _dealId);
    }

    /**
     * @notice Expire a deal
     * @param _dealId Deal ID
     */
    function expireDeal(uint256 _dealId) public {
        DealInfo storage dealInfo = dealInfos[_dealId];
        require(dealInfo.dealId == _dealId, "Deal not found");
        require(block.timestamp >= dealInfo.expirationTime, "Deal has not expired yet");

        emit DealExpired(_dealId);
    }

    /**
     * @notice Get deal info
     * @param _dealId Deal ID
     * @return DealInfo
     */
    function getDealInfo(uint256 _dealId) public view returns (DealInfo memory) {
        return dealInfos[_dealId];
    }
}
```
