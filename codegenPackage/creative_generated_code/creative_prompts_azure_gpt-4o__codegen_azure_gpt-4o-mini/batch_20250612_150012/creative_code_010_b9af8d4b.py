"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xyzverse-in.web.app
Prompt: Write a Solidity contract for integrating XYZVerse tokens into a sponsorship program for influencers, as mentioned in the roadmap for Q4.
Generated: DETERMINISTIC_b9af8d4ba93c908c
Batch ID: 20250612_150012
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing the interface for ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for sponsoring influencers with XYZVerse tokens
contract SponsorshipProgram is Ownable {
    // Event to log sponsorship details
    event SponsorshipCreated(address indexed influencer, uint256 amount, uint256 duration);
    event SponsorshipCanceled(address indexed influencer);
    
    // Struct to hold sponsorship details
    struct Sponsorship {
        uint256 amount;        // Amount of tokens sponsored
        uint256 endTime;       // Time until the sponsorship ends
        bool active;           // Sponsorship status
    }

    // Mapping of influencers to their sponsorship details
    mapping(address => Sponsorship) public sponsorships;

    // Token used for sponsorships
    IERC20 public xyzVerseToken;

    // Constructor to set the token address
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        xyzVerseToken = IERC20(_tokenAddress);
    }

    // Function to create a sponsorship
    function createSponsorship(address influencer, uint256 amount, uint256 duration) external onlyOwner {
        require(influencer != address(0), "Invalid influencer address");
        require(amount > 0, "Amount must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");

        // Transfer tokens from the contract owner to the influencer
        xyzVerseToken.transferFrom(msg.sender, influencer, amount);

        // Create sponsorship details
        sponsorships[influencer] = Sponsorship({
            amount: amount,
            endTime: block.timestamp + duration,
            active: true
        });

        emit SponsorshipCreated(influencer, amount, duration);
    }

    // Function to cancel an active sponsorship
    function cancelSponsorship(address influencer) external onlyOwner {
        require(sponsorships[influencer].active, "No active sponsorship found");

        // Mark sponsorship as inactive
        sponsorships[influencer].active = false;

        emit SponsorshipCanceled(influencer);
    }

    // Function to get the details of a sponsorship
    function getSponsorshipDetails(address influencer) external view returns (Sponsorship memory) {
        return sponsorships[influencer];
    }

    // Function for the contract owner to withdraw tokens in case of emergency
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(xyzVerseToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer tokens to the owner
        xyzVerseToken.transfer(msg.sender, amount);
    }
}
```
