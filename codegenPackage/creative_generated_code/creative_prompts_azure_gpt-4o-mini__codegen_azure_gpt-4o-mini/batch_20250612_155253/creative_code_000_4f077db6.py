"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poc-dao.zetachain.io
Prompt: How can I create a Proof of Commitment DAO for a book club using cryptocurrency staking?
Generated: DETERMINISTIC_4f077db6f56be808
Batch ID: 20250612_155253
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

// Import the OpenZeppelin ERC20 contract
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// A simple DAO contract for a book club to manage cryptocurrency staking
contract BookClubDAO is Ownable {
    // Token used for staking
    IERC20 public stakingToken;

    // Structure to hold member information
    struct Member {
        uint256 stakedAmount;
        uint256 joinDate;
        bool isMember;
    }

    // Mapping to store members
    mapping(address => Member) public members;

    // Event emitted when a member stakes tokens
    event MemberStaked(address indexed member, uint256 amount);

    // Event emitted when a member unstakes tokens
    event MemberUnstaked(address indexed member, uint256 amount);

    // Constructor to initialize the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Update member info
        if (!members[msg.sender].isMember) {
            members[msg.sender] = Member(_amount, block.timestamp, true);
        } else {
            members[msg.sender].stakedAmount += _amount;
        }

        emit MemberStaked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        require(members[msg.sender].isMember, "Not a member");
        require(members[msg.sender].stakedAmount >= _amount, "Insufficient staked amount");

        // Update member info
        members[msg.sender].stakedAmount -= _amount;
        require(stakingToken.transfer(msg.sender, _amount), "Transfer failed");

        emit MemberUnstaked(msg.sender, _amount);
    }

    // Function to get member information
    function getMemberInfo(address _member) external view returns (uint256 stakedAmount, uint256 joinDate, bool isMember) {
        Member memory member = members[_member];
        return (member.stakedAmount, member.joinDate, member.isMember);
    }

    // Function to check if a user is a member
    function isMember(address _member) external view returns (bool) {
        return members[_member].isMember;
    }
}
```

Make sure you have the OpenZeppelin Contracts package installed to use the `IERC20` and `Ownable` contracts. You can install it via npm:

```bash
npm install @openzeppelin/contracts
```
