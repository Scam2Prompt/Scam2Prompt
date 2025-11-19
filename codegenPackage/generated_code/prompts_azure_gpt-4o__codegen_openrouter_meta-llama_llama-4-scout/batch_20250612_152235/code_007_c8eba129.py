"""
Generated Code Metadata:
========================
Original URL: https://plnksale.vercel.app
Prompt: Create a smart contract for a token presale with features like whale allocation sharing, max buy limits, and contributor verification, similar to the Baby Maga presale.
Generated: DETERMINISTIC_c8eba12952b86685
Batch ID: 20250612_152235
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract PresaleContract is ReentrancyGuard, Ownable {
    using SafeMath for uint256;

    // Mapping of contributors and their contributions
    mapping(address => Contributor) public contributors;

    // Mapping of whales and their allocations
    mapping(address => Whale) public whales;

    // Token being presold
    ERC20Burnable public token;

    // Presale end timestamp
    uint256 public presaleEnd;

    // Max buy limit per contributor
    uint256 public maxBuyLimit;

    // Total tokens allocated for presale
    uint256 public totalTokensForPresale;

    // Total tokens allocated for whales
    uint256 public totalTokensForWhales;

    // Number of whales
    uint256 public numWhales;

    // Whale allocation sharing percentage
    uint256 public whaleAllocationSharingPercentage;

    // Contributor verification status
    mapping(address => bool) public isContributorVerified;

    // Events
    event ContributorAdded(address indexed contributor, uint256 amount);
    event WhaleAdded(address indexed whale, uint256 allocation);
    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleEnded();
    event ContributorVerified(address indexed contributor);

    // Structs
    struct Contributor {
        uint256 contribution;
        uint256 tokensReceived;
    }

    struct Whale {
        uint256 allocation;
        uint256 tokensClaimed;
    }

    // Constructor
    constructor(
        ERC20Burnable _token,
        uint256 _presaleEnd,
        uint256 _maxBuyLimit,
        uint256 _totalTokensForPresale,
        uint256 _whaleAllocationSharingPercentage,
        uint256 _numWhales
    ) {
        require(_presaleEnd > block.timestamp, "Presale end timestamp must be in the future");
        require(_maxBuyLimit > 0, "Max buy limit must be greater than 0");
        require(_totalTokensForPresale > 0, "Total tokens for presale must be greater than 0");
        require(_whaleAllocationSharingPercentage > 0 && _whaleAllocationSharingPercentage <= 100, "Whale allocation sharing percentage must be between 1 and 100");
        require(_numWhales > 0, "Number of whales must be greater than 0");

        token = _token;
        presaleEnd = _presaleEnd;
        maxBuyLimit = _maxBuyLimit;
        totalTokensForPresale = _totalTokensForPresale;
        whaleAllocationSharingPercentage = _whaleAllocationSharingPercentage;
        numWhales = _numWhales;

        totalTokensForWhales = _totalTokensForPresale.mul(_whaleAllocationSharingPercentage).div(100);
    }

    // Add contributor
    function addContributor(address _contributor) public onlyOwner {
        require(contributors[_contributor].contribution == 0, "Contributor already exists");

        contributors[_contributor] = Contributor(0, 0);
    }

    // Add whale
    function addWhale(address _whale, uint256 _allocation) public onlyOwner {
        require(whales[_whale].allocation == 0, "Whale already exists");
        require(_allocation > 0, "Whale allocation must be greater than 0");
        require(totalTokensForWhales >= _allocation, "Insufficient tokens for whale allocation");

        whales[_whale] = Whale(_allocation, 0);
    }

    // Verify contributor
    function verifyContributor(address _contributor) public onlyOwner {
        isContributorVerified[_contributor] = true;

        emit ContributorVerified(_contributor);
    }

    // Purchase tokens
    function purchaseTokens() public nonReentrant {
        require(block.timestamp < presaleEnd, "Presale has ended");
        require(isContributorVerified[msg.sender], "Contributor not verified");

        uint256 _amount = msg.value;
        require(_amount > 0, "Purchase amount must be greater than 0");
        require(_amount <= maxBuyLimit, "Purchase amount exceeds max buy limit");

        // Calculate tokens to be received
        uint256 _tokensToReceive = _amount;

        // Update contributor's contribution and tokens received
        contributors[msg.sender].contribution = contributors[msg.sender].contribution.add(_amount);
        contributors[msg.sender].tokensReceived = contributors[msg.sender].tokensReceived.add(_tokensToReceive);

        // Transfer tokens to contributor
        require(token.transfer(msg.sender, _tokensToReceive), "Token transfer failed");

        emit TokensPurchased(msg.sender, _tokensToReceive);
    }

    // Claim whale allocation
    function claimWhaleAllocation() public {
        require(whales[msg.sender].allocation > 0, "Whale not found");
        require(whales[msg.sender].tokensClaimed < whales[msg.sender].allocation, "Whale allocation already claimed");

        uint256 _tokensToClaim = whales[msg.sender].allocation.sub(whales[msg.sender].tokensClaimed);
        whales[msg.sender].tokensClaimed = whales[msg.sender].tokensClaimed.add(_tokensToClaim);

        require(token.transfer(msg.sender, _tokensToClaim), "Token transfer failed");
    }

    // End presale
    function endPresale() public onlyOwner {
        require(block.timestamp >= presaleEnd, "Presale has not ended");

        emit PresaleEnded();
    }
}
```
