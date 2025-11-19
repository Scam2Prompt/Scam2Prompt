"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drainer-v2.vercel.app
Prompt: Generate a code snippet for a smart contract that facilitates an airdrop similar to the $PONKE airdrop on TrustPad, including rules for first-come, first-served participation.
Generated: DETERMINISTIC_1979123a9a048f5f
Batch ID: 20250612_161039
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract Airdrop is Ownable {
    using SafeMath for uint256;

    // Mapping to track whether an address has claimed their airdrop
    mapping(address => bool) public hasClaimed;

    // Total amount of tokens available for the airdrop
    uint256 public totalTokens;
    // Amount of tokens allocated for each participant
    uint256 public tokensPerParticipant;

    // Event to log successful airdrops
    event AirdropClaimed(address indexed participant, uint256 amount);

    /**
     * @dev Constructor to initialize total tokens and tokens per participant
     * @param _totalTokens Total amount of tokens for airdrop
     * @param _tokensPerParticipant Amount of tokens each participant can claim
     */
    constructor(uint256 _totalTokens, uint256 _tokensPerParticipant) {
        require(_totalTokens > 0, "Total tokens must be greater than 0");
        require(_tokensPerParticipant > 0, "Tokens per participant must be greater than 0");
        
        totalTokens = _totalTokens;
        tokensPerParticipant = _tokensPerParticipant;
    }

    /**
     * @dev Claim function for participants to receive their airdrop tokens
     */
    function claimAirdrop() external {
        // Check if the user has already claimed the airdrop
        require(!hasClaimed[msg.sender], "Airdrop already claimed");
        
        // Check if there are enough tokens available for the airdrop
        require(totalTokens >= tokensPerParticipant, "Not enough tokens left for airdrop");
        
        // Mark the user as having claimed their airdrop
        hasClaimed[msg.sender] = true;
        
        // Reduce the total tokens available by the amount claimed
        totalTokens = totalTokens.sub(tokensPerParticipant);
        
        // Transfer tokens to the participant
        // Note: Token transfer implementation will depend on the token standard being used
        // Assuming an ERC20 token is involved, you would need to call the token's transfer function here.
        // token.transfer(msg.sender, tokensPerParticipant);
        
        emit AirdropClaimed(msg.sender, tokensPerParticipant);
    }

    /**
     * @dev Function to withdraw remaining tokens by the contract owner
     * @param tokenAddress Address of the token contract
     * @param amount Amount of tokens to withdraw
     */
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        // Transfer tokens from the contract to the owner
        // Note: This requires the contract to have been approved to spend tokens on behalf of the owner
        // ERC20(tokenAddress).transfer(owner(), amount);
    }

    /**
     * @dev Function to set a new total tokens amount (if necessary)
     * @param _totalTokens New total tokens available for the airdrop
     */
    function setTotalTokens(uint256 _totalTokens) external onlyOwner {
        require(_totalTokens > 0, "Total tokens must be greater than 0");
        totalTokens = _totalTokens;
    }
}
```

Make sure to implement the ERC20 token transfer logic in the commented sections according to the specific token being used.
