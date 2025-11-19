"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://godcandle404-en.web.app
Prompt: Explain how to implement a referral bonus system for the God Candle NFT project using ERC-20 tokens.
Generated: DETERMINISTIC_a77c64f721d6d1d8
Batch ID: 20250612_160804
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

// Import OpenZeppelin's ERC20 implementation for reusable token logic
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// ReferralBonus is an ERC20 token that also implements a referral bonus system
contract ReferralBonus is ERC20, Ownable {
    // Mapping of addresses to their referred addresses
    mapping(address => address) public referrals;
    // Mapping to track if an address has already claimed their referral bonus
    mapping(address => bool) public hasClaimedBonus;

    // Bonus amount for each successful referral
    uint256 public constant REFERRAL_BONUS = 10 * 10 ** 18; // 10 tokens

    // Event emitted when a new referral is made
    event ReferralMade(address indexed referrer, address indexed referee);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("GodCandleToken", "GCT") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 10000 * 10 ** 18); // Initial supply: 10,000 tokens
    }

    /**
     * @dev Allows a user to refer another user to the system.
     * @param _referee The address of the new user being referred.
     */
    function refer(address _referee) external {
        require(_referee != address(0), "Invalid referee address");
        require(referrals[_referee] == address(0), "Referee already referred");

        // Set the referrer for this referee
        referrals[_referee] = msg.sender;
        
        // Emit an event for the referral
        emit ReferralMade(msg.sender, _referee);
    }

    /**
     * @dev Allows the referrer to claim the referral bonus.
     */
    function claimReferralBonus() external {
        // Ensure the user has a referral
        address referrer = referrals[msg.sender];
        require(referrer != address(0), "No referral found");
        require(!hasClaimedBonus[referrer], "Bonus already claimed");

        // Mark that the bonus has been claimed
        hasClaimedBonus[referrer] = true;

        // Transfer referral bonus to the referrer
        _transfer(address(this), referrer, REFERRAL_BONUS);
    }

    /**
     * @dev Allows the owner to withdraw tokens from the contract.
     * @param _amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(balanceOf(address(this)) >= _amount, "Insufficient balance");
        _transfer(address(this), msg.sender, _amount);
    }

    /**
     * @dev Fallback function to prevent accidental ether transfers.
     */
    receive() external payable {
        revert("Ether not accepted");
    }
}
```
