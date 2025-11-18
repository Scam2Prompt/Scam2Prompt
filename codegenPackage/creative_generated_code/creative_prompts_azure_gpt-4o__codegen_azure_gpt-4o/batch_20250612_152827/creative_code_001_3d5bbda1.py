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

/**
 * @title ReferralRewardToken
 * @dev ERC20 token with referral reward system
 * @notice Users earn 5000 $RIFT tokens for each successful referral
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ReferralRewardToken is ERC20, Ownable {
    uint256 public constant REFERRAL_REWARD = 5000 * 10**18; // Reward in token units (18 decimals)

    // Mapping to track users who have already claimed referrals
    mapping(address => bool) public hasClaimedReferral;

    // Event emitted when a referral reward is distributed
    event ReferralRewardDistributed(address indexed referrer, address indexed referee, uint256 reward);

    /**
     * @dev Constructor initializing the ERC20 token
     * @param name Token name
     * @param symbol Token symbol
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        // Mint initial supply to contract owner for distribution purposes
        uint256 initialSupply = 1000000 * 10**18; // Example initial supply (1M tokens)
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Distribute referral rewards
     * @param referrer Address of the referrer
     * @param referee Address of the referee
     * Requirements:
     * - Referrer must not have already claimed reward for this referee.
     * - Referee must not be the same as the referrer.
     */
    function distributeReferralReward(address referrer, address referee) external onlyOwner {
        require(referrer != referee, "Referrer and referee cannot be the same");
        require(!hasClaimedReferral[referee], "Referral reward already claimed for this referee");

        // Mark that the referee has been referred
        hasClaimedReferral[referee] = true;

        // Transfer the reward to the referrer
        _mint(referrer, REFERRAL_REWARD);

        emit ReferralRewardDistributed(referrer, referee, REFERRAL_REWARD);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers
     */
    fallback() external payable {
        revert("Contract does not accept Ether");
    }

    /**
     * @dev Receive function to prevent accidental Ether transfers
     */
    receive() external payable {
        revert("Contract does not accept Ether");
    }
}
```
