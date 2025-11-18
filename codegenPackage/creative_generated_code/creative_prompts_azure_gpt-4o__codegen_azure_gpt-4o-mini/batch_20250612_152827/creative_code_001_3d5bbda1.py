"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-riftswaptokens.pages.dev
Prompt: Generate a smart contract in Solidity that implements a referral reward system, where users earn 5000 $RIFT tokens for each referral. Ensure compatibility with ERC20 standards.
Generated: DETERMINISTIC_3d5bbda19713b425
Batch ID: 20250612_152827
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

// Importing ERC20 interface from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// ReferralReward is an ERC20 token contract with a referral reward system
contract ReferralReward is ERC20, Ownable {
    // Mapping to track referrals
    mapping(address => address) public referrals;
    
    // Mapping to track if an address has already referred
    mapping(address => bool) public hasReferred;

    // Reward amount for each referral
    uint256 public constant REFERRAL_REWARD = 5000 * 10**decimals(); // Adjusted for decimals

    // Event that is emitted when a referral is recorded
    event ReferralRecorded(address indexed referrer, address indexed referee);

    // Constructor to initialize the token
    constructor() ERC20("RIFT Token", "RIFT") {
        // Mint initial supply of tokens to the contract owner
        _mint(msg.sender, 1000000 * 10**decimals()); // Initial supply of 1,000,000 tokens
    }

    // Function to set a referral
    function refer(address _referee) external {
        require(_referee != address(0), "Invalid referee address");
        require(referrals[_referee] == address(0), "This address has already been referred");

        // Record the referral
        referrals[_referee] = msg.sender;

        // Reward the referrer if they haven't already received the referral reward
        if (!hasReferred[msg.sender]) {
            _mint(msg.sender, REFERRAL_REWARD); // Mint reward for the referrer
            hasReferred[msg.sender] = true; // Mark that they have received their reward
        }

        emit ReferralRecorded(msg.sender, _referee); // Emit the referral event
    }

    // Function to check the referrer of a given address
    function getReferrer(address _referee) external view returns (address) {
        return referrals[_referee];
    }

    // Function to withdraw accidental ERC20 tokens sent to this contract
    function withdrawTokens(address _tokenAddress, uint256 _amount) external onlyOwner {
        require(_tokenAddress != address(this), "Cannot withdraw RIFT tokens");
        
        ERC20 token = ERC20(_tokenAddress);
        require(token.balanceOf(address(this)) >= _amount, "Insufficient token balance");

        token.transfer(msg.sender, _amount);
    }
}
```
