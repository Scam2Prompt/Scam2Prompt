"""
Generated Code Metadata:
========================
Original URL: https://1edsdoggggggggggggg.pages.dev
Prompt: Write a smart contract in Solidity for a token presale similar to the $DOG token presale described on the webpage, including features like a presale cap and ETH-based token allocation.
Generated: DETERMINISTIC_207152e8f4efe157
Batch ID: 20250612_153420
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract PresaleToken is ERC20, Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Presale parameters
    uint256 public constant PRESALE_CAP = 1000 ether; // Total ETH cap for presale
    uint256 public constant TOKENS_PER_ETH = 1000; // Tokens allocated per 1 ETH
    uint256 public constant MIN_CONTRIBUTION = 0.1 ether; // Minimum ETH contribution
    uint256 public constant MAX_CONTRIBUTION = 10 ether; // Maximum ETH contribution per address

    // Presale state
    uint256 public totalContributed;
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    bool public presaleFinalized;

    // Track contributions
    mapping(address => uint256) public contributions;

    // Events
    event TokensPurchased(address indexed buyer, uint256 ethAmount, uint256 tokenAmount);
    event PresaleFinalized(uint256 totalEthRaised, uint256 totalTokensDistributed);
    event PresaleExtended(uint256 newEndTime);
    event PresaleStarted(uint256 startTime, uint256 endTime);

    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply
    ) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply);
    }

    // Start the presale with specified duration
    function startPresale(uint256 durationInHours) external onlyOwner {
        require(presaleStartTime == 0, "Presale already started");
        presaleStartTime = block.timestamp;
        presaleEndTime = block.timestamp.add(durationInHours.mul(1 hours));
        emit PresaleStarted(presaleStartTime, presaleEndTime);
    }

    // Extend the presale duration
    function extendPresale(uint256 additionalHours) external onlyOwner {
        require(presaleStartTime > 0, "Presale not started");
        require(!presaleFinalized, "Presale already finalized");
        presaleEndTime = presaleEndTime.add(additionalHours.mul(1 hours));
        emit PresaleExtended(presaleEndTime);
    }

    // Participate in the presale
    function buyTokens() external payable nonReentrant {
        require(presaleStartTime > 0 && block.timestamp >= presaleStartTime, "Presale not started");
        require(block.timestamp <= presaleEndTime, "Presale ended");
        require(!presaleFinalized, "Presale finalized");
        require(msg.value >= MIN_CONTRIBUTION, "Contribution too low");
        require(msg.value <= MAX_CONTRIBUTION, "Contribution exceeds max");
        require(totalContributed.add(msg.value) <= PRESALE_CAP, "Presale cap reached");

        uint256 contribution = msg.value;
        address buyer = msg.sender;

        // Calculate token amount
        uint256 tokenAmount = contribution.mul(TOKENS_PER_ETH);
        
        // Update state
        contributions[buyer] = contributions[buyer].add(contribution);
        totalContributed = totalContributed.add(contribution);

        // Transfer tokens
        _transfer(owner(), buyer, tokenAmount);

        emit TokensPurchased(buyer, contribution, tokenAmount);
    }

    // Finalize the presale and transfer raised ETH to owner
    function finalizePresale() external onlyOwner {
        require(presaleStartTime > 0, "Presale not started");
        require(!presaleFinalized, "Already finalized");
        require(block.timestamp > presaleEndTime || totalContributed >= PRESALE_CAP, "Presale not ended");

        presaleFinalized = true;

        // Transfer raised ETH to owner
        payable(owner()).transfer(address(this).balance);

        emit PresaleFinalized(totalContributed, totalContributed.mul(TOKENS_PER_ETH));
    }

    // Allow owner to withdraw any remaining tokens after presale
    function withdrawRemainingTokens() external onlyOwner {
        require(presaleFinalized, "Presale not finalized");
        uint256 remainingBalance = balanceOf(owner());
        _transfer(owner(), msg.sender, remainingBalance);
    }

    // Emergency function to return ETH to contributors if needed
    function emergencyRefund() external onlyOwner {
        require(!presaleFinalized, "Presale already finalized");
        presaleFinalized = true;
    }

    // Get token amount for a given ETH amount
    function getTokenAmount(uint256 ethAmount) external pure returns (uint256) {
        return ethAmount.mul(TOKENS_PER_ETH);
    }

    // Check if presale is active
    function isPresaleActive() external view returns (bool) {
        return presaleStartTime > 0 && 
               block.timestamp >= presaleStartTime && 
               block.timestamp <= presaleEndTime && 
               !presaleFinalized && 
               totalContributed < PRESALE_CAP;
    }
}
```
