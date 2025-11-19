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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

contract HighTableSecretDeal is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    struct Deal {
        address creator;
        address token;
        uint256 totalAmount;
        uint256 claimedAmount;
        uint256 startTime;
        uint256 endTime;
        uint256 cliffDuration;
        uint256 vestingDuration;
        bool isActive;
        mapping(address => uint256) allocations;
        mapping(address => uint256) claimed;
    }

    uint256 public dealCounter;
    mapping(uint256 => Deal) public deals;
    mapping(address => bool) public whitelistedTokens;

    event DealCreated(
        uint256 indexed dealId,
        address indexed creator,
        address indexed token,
        uint256 totalAmount,
        uint256 startTime,
        uint256 endTime,
        uint256 cliffDuration,
        uint256 vestingDuration
    );
    event DealCancelled(uint256 indexed dealId);
    event TokensAllocated(
        uint256 indexed dealId,
        address indexed participant,
        uint256 amount
    );
    event TokensClaimed(
        uint256 indexed dealId,
        address indexed participant,
        uint256 amount
    );
    event TokenWhitelisted(address indexed token);
    event TokenRemovedFromWhitelist(address indexed token);

    modifier onlyDealCreator(uint256 dealId) {
        require(
            deals[dealId].creator == msg.sender,
            "Only deal creator can perform this action"
        );
        _;
    }

    modifier validDeal(uint256 dealId) {
        require(deals[dealId].isActive, "Deal does not exist or is inactive");
        _;
    }

    constructor() {
        dealCounter = 1;
    }

    function createDeal(
        address token,
        uint256 totalAmount,
        uint256 startTime,
        uint256 endTime,
        uint256 cliffDuration,
        uint256 vestingDuration
    ) external onlyOwner {
        require(
            whitelistedTokens[token],
            "Token is not whitelisted for deals"
        );
        require(totalAmount > 0, "Total amount must be greater than 0");
        require(
            startTime >= block.timestamp,
            "Start time must be in the future"
        );
        require(endTime > startTime, "End time must be after start time");
        require(
            cliffDuration <= vestingDuration,
            "Cliff duration must be less than or equal to vesting duration"
        );

        Deal storage newDeal = deals[dealCounter];
        newDeal.creator = msg.sender;
        newDeal.token = token;
        newDeal.totalAmount = totalAmount;
        newDeal.claimedAmount = 0;
        newDeal.startTime = startTime;
        newDeal.endTime = endTime;
        newDeal.cliffDuration = cliffDuration;
        newDeal.vestingDuration = vestingDuration;
        newDeal.isActive = true;

        IERC20(token).safeTransferFrom(
            msg.sender,
            address(this),
            totalAmount
        );

        emit DealCreated(
            dealCounter,
            msg.sender,
            token,
            totalAmount,
            startTime,
            endTime,
            cliffDuration,
            vestingDuration
        );

        dealCounter++;
    }

    function cancelDeal(uint256 dealId)
        external
        onlyDealCreator(dealId)
        validDeal(dealId)
    {
        Deal storage deal = deals[dealId];
        deal.isActive = false;

        uint256 remainingAmount = deal.totalAmount - deal.claimedAmount;
        if (remainingAmount > 0) {
            IERC20(deal.token).safeTransfer(deal.creator, remainingAmount);
        }

        emit DealCancelled(dealId);
    }

    function allocateTokens(
        uint256 dealId,
        address[] calldata participants,
        uint256[] calldata amounts
    ) external onlyDealCreator(dealId) validDeal(dealId) {
        require(
            participants.length == amounts.length,
            "Participants and amounts length mismatch"
        );

        Deal storage deal = deals[dealId];
        uint256 totalAllocated = 0;

        for (uint256 i = 0; i < participants.length; i++) {
            require(
                participants[i] != address(0),
                "Invalid participant address"
            );
            require(amounts[i] > 0, "Allocation amount must be greater than 0");

            deal.allocations[participants[i]] = amounts[i];
            totalAllocated += amounts[i];

            emit TokensAllocated(dealId, participants[i], amounts[i]);
        }

        require(
            totalAllocated <= deal.totalAmount - deal.claimedAmount,
            "Total allocations exceed remaining deal amount"
        );
    }

    function claimTokens(uint256 dealId) external nonReentrant validDeal(dealId) {
        Deal storage deal = deals[dealId];
        require(
            deal.allocations[msg.sender] > 0,
            "No allocation for this address"
        );
        require(
            block.timestamp >= deal.startTime,
            "Deal has not started yet"
        );

        uint256 claimableAmount = calculateClaimableAmount(dealId, msg.sender);
        require(claimableAmount > 0, "No tokens available to claim");

        deal.claimed[msg.sender] += claimableAmount;
        deal.claimedAmount += claimableAmount;

        IERC20(deal.token).safeTransfer(msg.sender, claimableAmount);

        emit TokensClaimed(dealId, msg.sender, claimableAmount);
    }

    function calculateClaimableAmount(uint256 dealId, address participant)
        public
        view
        validDeal(dealId)
        returns (uint256)
    {
        Deal storage deal = deals[dealId];
        uint256 allocation = deal.allocations[participant];
        uint256 alreadyClaimed = deal.claimed[participant];

        if (block.timestamp < deal.startTime + deal.cliffDuration) {
            return 0;
        }

        if (block.timestamp >= deal.endTime) {
            return allocation - alreadyClaimed;
        }

        uint256 elapsedTime = block.timestamp - deal.startTime;
        uint256 vestedAmount = (allocation * elapsedTime) / deal.vestingDuration;

        if (vestedAmount > allocation) {
            vestedAmount = allocation;
        }

        return vestedAmount - alreadyClaimed;
    }

    function whitelistToken(address token) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(!whitelistedTokens[token], "Token already whitelisted");

        whitelistedTokens[token] = true;
        emit TokenWhitelisted(token);
    }

    function removeTokenFromWhitelist(address token) external onlyOwner {
        require(whitelistedTokens[token], "Token not whitelisted");

        whitelistedTokens[token] = false;
        emit TokenRemovedFromWhitelist(token);
    }

    function getDealInfo(uint256 dealId)
        external
        view
        returns (
            address creator,
            address token,
            uint256 totalAmount,
            uint256 claimedAmount,
            uint256 startTime,
            uint256 endTime,
            uint256 cliffDuration,
            uint256 vestingDuration,
            bool isActive
        )
    {
        Deal storage deal = deals[dealId];
        return (
            deal.creator,
            deal.token,
            deal.totalAmount,
            deal.claimedAmount,
            deal.startTime,
            deal.endTime,
            deal.cliffDuration,
            deal.vestingDuration,
            deal.isActive
        );
    }

    function getAllocation(uint256 dealId, address participant)
        external
        view
        returns (uint256)
    {
        return deals[dealId].allocations[participant];
    }

    function getClaimedAmount(uint256 dealId, address participant)
        external
        view
        returns (uint256)
    {
        return deals[dealId].claimed[participant];
    }
}
```
