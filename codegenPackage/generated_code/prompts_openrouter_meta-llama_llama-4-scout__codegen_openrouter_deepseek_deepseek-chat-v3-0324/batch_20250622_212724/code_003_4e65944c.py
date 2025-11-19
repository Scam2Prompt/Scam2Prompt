"""
Generated Code Metadata:
========================
Original URL: https://bitcoin-pepe.xyz
Prompt: "Design a smart contract for a weekly $BPEP token giveaway, where 1,000,000 tokens are randomly distributed to active community members."
Generated: DETERMINISTIC_4e65944c6bc3b212
Batch ID: 20250622_212724
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
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

contract BPEPGiveaway is Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;

    IERC20 public bpepToken;
    uint256 public constant WEEKLY_GIVEAWAY_AMOUNT = 1_000_000 * 10**18; // Assuming 18 decimals
    uint256 public lastDistributionTime;
    uint256 public distributionInterval = 7 days;

    EnumerableSet.AddressSet private activeMembers;

    event MemberAdded(address indexed member);
    event MemberRemoved(address indexed member);
    event TokensDistributed(address[] recipients, uint256[] amounts);

    constructor(address _bpepTokenAddress) {
        bpepToken = IERC20(_bpepTokenAddress);
        lastDistributionTime = block.timestamp;
    }

    modifier onlyWhenReady() {
        require(
            block.timestamp >= lastDistributionTime + distributionInterval,
            "Giveaway: Distribution interval not reached"
        );
        _;
    }

    function addMember(address _member) external onlyOwner {
        require(_member != address(0), "Giveaway: Invalid address");
        require(activeMembers.add(_member), "Giveaway: Member already exists");
        emit MemberAdded(_member);
    }

    function removeMember(address _member) external onlyOwner {
        require(activeMembers.remove(_member), "Giveaway: Member not found");
        emit MemberRemoved(_member);
    }

    function isMemberActive(address _member) external view returns (bool) {
        return activeMembers.contains(_member);
    }

    function getActiveMemberCount() external view returns (uint256) {
        return activeMembers.length();
    }

    function distributeTokens() external onlyOwner onlyWhenReady {
        require(
            bpepToken.balanceOf(address(this)) >= WEEKLY_GIVEAWAY_AMOUNT,
            "Giveaway: Insufficient token balance"
        );

        uint256 memberCount = activeMembers.length();
        require(memberCount > 0, "Giveaway: No active members");

        address[] memory recipients = new address[](memberCount);
        uint256[] memory amounts = new uint256[](memberCount);
        uint256 remainingAmount = WEEKLY_GIVEAWAY_AMOUNT;

        // Generate pseudo-random numbers using block data
        bytes32 seed = keccak256(
            abi.encodePacked(
                block.timestamp,
                block.difficulty,
                block.coinbase,
                block.number
            )
        );

        for (uint256 i = 0; i < memberCount; i++) {
            recipients[i] = activeMembers.at(i);
            
            // Distribute random amount (1-10% of remaining) to each member
            uint256 maxPercent = (i == memberCount - 1) ? 100 : 10;
            uint256 randomPercent = uint256(keccak256(abi.encodePacked(seed, i))) % maxPercent + 1;
            
            uint256 amount = (remainingAmount * randomPercent) / 100;
            amounts[i] = amount;
            remainingAmount -= amount;
        }

        // Perform actual token transfers
        for (uint256 i = 0; i < memberCount; i++) {
            require(
                bpepToken.transfer(recipients[i], amounts[i]),
                "Giveaway: Transfer failed"
            );
        }

        lastDistributionTime = block.timestamp;
        emit TokensDistributed(recipients, amounts);
    }

    function withdrawTokens() external onlyOwner {
        uint256 balance = bpepToken.balanceOf(address(this));
        require(balance > 0, "Giveaway: No tokens to withdraw");
        require(
            bpepToken.transfer(owner(), balance),
            "Giveaway: Withdrawal failed"
        );
    }

    function setDistributionInterval(uint256 _interval) external onlyOwner {
        require(_interval > 0, "Giveaway: Interval must be > 0");
        distributionInterval = _interval;
    }
}
```
