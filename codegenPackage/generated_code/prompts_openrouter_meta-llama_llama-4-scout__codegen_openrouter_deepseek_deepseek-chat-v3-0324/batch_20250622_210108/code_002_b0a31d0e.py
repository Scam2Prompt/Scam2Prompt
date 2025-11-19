"""
Generated Code Metadata:
========================
Original URL: https://floki.icu
Prompt: Generate a smart contract code snippet for a token airdrop distribution similar to the FLOKI INU reward system.
Generated: DETERMINISTIC_b0a31d0ec7021c36
Batch ID: 20250622_210108
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract TokenAirdrop is Ownable {
    using SafeMath for uint256;

    IERC20 public token;
    uint256 public totalAirdropped;
    uint256 public totalRecipients;
    uint256 public claimPeriodEnd;

    mapping(address => bool) public hasClaimed;
    mapping(address => uint256) public claimableAmounts;

    event AirdropClaimed(address indexed recipient, uint256 amount);
    event AirdropFunded(uint256 totalAmount, uint256 totalRecipients);
    event ClaimPeriodExtended(uint256 newEndTime);

    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        token = IERC20(_tokenAddress);
    }

    function fundAirdrop(
        address[] calldata recipients,
        uint256[] calldata amounts
    ) external onlyOwner {
        require(recipients.length == amounts.length, "Arrays must be equal length");
        require(recipients.length > 0, "No recipients provided");

        uint256 totalAmount = 0;

        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Invalid recipient address");
            require(amounts[i] > 0, "Amount must be greater than zero");
            
            if (claimableAmounts[recipients[i]] == 0) {
                totalRecipients = totalRecipients.add(1);
            }
            
            claimableAmounts[recipients[i]] = claimableAmounts[recipients[i]].add(amounts[i]);
            totalAmount = totalAmount.add(amounts[i]);
        }

        require(
            token.transferFrom(msg.sender, address(this), totalAmount),
            "Token transfer failed"
        );

        totalAirdropped = totalAirdropped.add(totalAmount);
        emit AirdropFunded(totalAmount, recipients.length);
    }

    function claim() external {
        require(block.timestamp <= claimPeriodEnd, "Claim period has ended");
        require(!hasClaimed[msg.sender], "Already claimed");
        require(claimableAmounts[msg.sender] > 0, "No tokens to claim");

        uint256 amount = claimableAmounts[msg.sender];
        hasClaimed[msg.sender] = true;

        require(
            token.transfer(msg.sender, amount),
            "Token transfer failed"
        );

        emit AirdropClaimed(msg.sender, amount);
    }

    function setClaimPeriodEnd(uint256 _endTime) external onlyOwner {
        require(_endTime > block.timestamp, "End time must be in the future");
        claimPeriodEnd = _endTime;
        emit ClaimPeriodExtended(_endTime);
    }

    function withdrawUnclaimedTokens() external onlyOwner {
        require(block.timestamp > claimPeriodEnd, "Claim period not ended");
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No unclaimed tokens");
        
        require(
            token.transfer(owner(), balance),
            "Token transfer failed"
        );
    }

    function getClaimableAmount(address _user) external view returns (uint256) {
        return hasClaimed[_user] ? 0 : claimableAmounts[_user];
    }
}
```
