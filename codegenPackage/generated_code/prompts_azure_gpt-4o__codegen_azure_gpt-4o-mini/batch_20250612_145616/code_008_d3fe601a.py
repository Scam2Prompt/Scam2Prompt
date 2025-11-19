"""
Generated Code Metadata:
========================
Original URL: https://airdropneiro-xyz.pages.dev
Prompt: Write a smart contract in Solidity that facilitates the claiming of $NEIRO tokens, ensuring referral tracking and reward distribution.
Generated: DETERMINISTIC_d3fe601aa63fa0f8
Batch ID: 20250612_145616
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for claiming NEIRO tokens with referral tracking
contract NeiroTokenClaim is Ownable {
    // State variables
    IERC20 public neiroToken; // The NEIRO token contract
    mapping(address => address) public referrals; // Mapping of user addresses to their referrers
    mapping(address => uint256) public claimedAmount; // Tracking claimed amounts per address
    uint256 public constant CLAIM_AMOUNT = 100 * 10**18; // Amount of NEIRO tokens to claim
    uint256 public constant REFERRAL_REWARD = 10 * 10**18; // Referral reward amount

    // Events
    event Claimed(address indexed claimant, address indexed referrer);
    event ReferralRewarded(address indexed referrer, uint256 amount);

    // Constructor to set the NEIRO token address
    constructor(address _neiroToken) {
        require(_neiroToken != address(0), "Invalid token address");
        neiroToken = IERC20(_neiroToken);
    }

    // Function to claim NEIRO tokens
    function claimTokens(address referrer) external {
        require(claimedAmount[msg.sender] == 0, "Tokens already claimed");
        require(referrer != msg.sender, "Cannot refer yourself");
        require(referrals[msg.sender] == address(0), "Referral already set");

        // Set the referrer
        referrals[msg.sender] = referrer;

        // Update claimed amount
        claimedAmount[msg.sender] = CLAIM_AMOUNT;

        // Transfer tokens to the claimant
        require(neiroToken.balanceOf(address(this)) >= CLAIM_AMOUNT, "Insufficient contract balance");
        neiroToken.transfer(msg.sender, CLAIM_AMOUNT);

        // Reward the referrer
        if (referrer != address(0)) {
            require(neiroToken.balanceOf(address(this)) >= REFERRAL_REWARD, "Insufficient contract balance for referral reward");
            neiroToken.transfer(referrer, REFERRAL_REWARD);
            emit ReferralRewarded(referrer, REFERRAL_REWARD);
        }

        emit Claimed(msg.sender, referrer);
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(neiroToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        neiroToken.transfer(msg.sender, amount);
    }

    // Function to check the claimed amount for an address
    function getClaimedAmount(address claimant) external view returns (uint256) {
        return claimedAmount[claimant];
    }

    // Function to check the referrer for an address
    function getReferrer(address claimant) external view returns (address) {
        return referrals[claimant];
    }
}
```
