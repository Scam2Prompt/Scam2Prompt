"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toto1m.pages.dev
Prompt: Write a Solidity smart contract that mimics the tokenomics described for POON memecoin, including features for community rewards and partnerships.
Generated: DETERMINISTIC_05fbfdfb2d2c704e
Batch ID: 20250612_153400
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

// Importing OpenZeppelin Contracts for safe and secure token implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Token contract for POON memecoin
contract POONToken is ERC20, Ownable {
    // Constants for total supply and fee percentages
    uint256 public constant INITIAL_SUPPLY = 1_000_000_000 * (10 ** 18); // 1 billion tokens with 18 decimal places
    uint256 public rewardFee = 5; // 5% fee for community rewards
    uint256 public partnershipFee = 3; // 3% fee for partnerships
    uint256 public totalFeesCollected;

    // Event emitted when fees are updated
    event FeesUpdated(uint256 newRewardFee, uint256 newPartnershipFee);

    // Mapping to track balances of community reward fund and partnership fund
    mapping(address => uint256) public communityRewards;
    mapping(address => uint256) public partnershipFunds;

    constructor() ERC20("POON Token", "POON") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    // Function to update fee percentages by the contract owner
    function updateFees(uint256 _rewardFee, uint256 _partnershipFee) external onlyOwner {
        require(_rewardFee + _partnershipFee <= 10, "Total fees cannot exceed 10%");
        rewardFee = _rewardFee;
        partnershipFee = _partnershipFee;

        emit FeesUpdated(rewardFee, partnershipFee);
    }

    // Overriding the transfer function to implement fee deduction
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        // Calculate fees
        uint256 fees = (amount * (rewardFee + partnershipFee)) / 100;
        uint256 amountAfterFees = amount - fees;

        // Update community rewards and partnership funds
        communityRewards[recipient] += (fees * rewardFee) / (rewardFee + partnershipFee);
        partnershipFunds[recipient] += (fees * partnershipFee) / (rewardFee + partnershipFee);

        // Update total fees collected
        totalFeesCollected += fees;

        // Perform the transfer
        super._transfer(sender, recipient, amountAfterFees);
    }

    // Function to withdraw collected community rewards to the owner
    function withdrawCommunityRewards() external onlyOwner {
        uint256 rewardBalance = communityRewards[address(this)];
        require(rewardBalance > 0, "No rewards to withdraw");

        // Reset community rewards before transferring
        communityRewards[address(this)] = 0;

        // Transfer rewards to owner
        payable(msg.sender).transfer(rewardBalance);
    }

    // Function to withdraw partnership funds to the owner
    function withdrawPartnershipFunds() external onlyOwner {
        uint256 partnershipBalance = partnershipFunds[address(this)];
        require(partnershipBalance > 0, "No partnership funds to withdraw");

        // Reset partnership funds before transferring
        partnershipFunds[address(this)] = 0;

        // Transfer partnership funds to owner
        payable(msg.sender).transfer(partnershipBalance);
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```
