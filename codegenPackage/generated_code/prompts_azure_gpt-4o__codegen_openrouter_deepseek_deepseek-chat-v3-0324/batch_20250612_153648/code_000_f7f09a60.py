"""
Generated Code Metadata:
========================
Original URL: https://dogodoges.pages.dev
Prompt: Write a smart contract in Solidity for an ERC-20 token similar to $DOGO, including features for staking and governance as described in the Dogodoge ecosystem.
Generated: DETERMINISTIC_f7f09a60c420b2fa
Batch ID: 20250612_153648
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Votes.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract DogoToken is ERC20, ERC20Votes, Ownable {
    using SafeMath for uint256;

    // Staking variables
    struct Stake {
        uint256 amount;
        uint256 stakedAt;
    }

    mapping(address => Stake) public stakes;
    uint256 public stakingRewardRate = 10; // 10% annual reward
    uint256 public minStakeDuration = 30 days;

    // Governance variables
    uint256 public proposalCount;
    mapping(uint256 => Proposal) public proposals;
    mapping(uint256 => mapping(address => bool)) public votes;

    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        uint256 startTime;
        uint256 endTime;
        bool executed;
    }

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event RewardClaimed(address indexed user, uint256 reward);
    event ProposalCreated(uint256 indexed id, string description);
    event Voted(uint256 indexed proposalId, address indexed voter);
    event ProposalExecuted(uint256 indexed id);

    constructor() ERC20("DogoToken", "DOGO") ERC20Permit("DogoToken") {
        _mint(msg.sender, 1000000000 * 10 ** decimals()); // 1 billion tokens
    }

    // Staking functions
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        if (stakes[msg.sender].amount > 0) {
            claimReward();
        }

        _transfer(msg.sender, address(this), amount);
        stakes[msg.sender] = Stake({
            amount: stakes[msg.sender].amount.add(amount),
            stakedAt: block.timestamp
        });

        emit Staked(msg.sender, amount);
    }

    function unstake() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake found");
        require(
            block.timestamp >= userStake.stakedAt.add(minStakeDuration),
            "Minimum stake duration not reached"
        );

        uint256 reward = calculateReward(msg.sender);
        uint256 totalAmount = userStake.amount.add(reward);

        _transfer(address(this), msg.sender, userStake.amount);
        _mint(msg.sender, reward);

        delete stakes[msg.sender];
        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    function claimReward() public {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake found");

        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No reward to claim");

        stakes[msg.sender].stakedAt = block.timestamp;
        _mint(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    function calculateReward(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        uint256 stakingDuration = block.timestamp.sub(userStake.stakedAt);
        uint256 annualReward = userStake.amount.mul(stakingRewardRate).div(100);
        return annualReward.mul(stakingDuration).div(365 days);
    }

    // Governance functions
    function createProposal(string memory description, uint256 duration) external onlyOwner {
        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: description,
            voteCount: 0,
            startTime: block.timestamp,
            endTime: block.timestamp.add(duration),
            executed: false
        });

        emit ProposalCreated(proposalCount, description);
    }

    function vote(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.id != 0, "Proposal does not exist");
        require(block.timestamp >= proposal.startTime, "Voting not started");
        require(block.timestamp <= proposal.endTime, "Voting ended");
        require(!votes[proposalId][msg.sender], "Already voted");

        uint256 votingPower = balanceOf(msg.sender).add(stakes[msg.sender].amount);
        require(votingPower > 0, "No voting power");

        votes[proposalId][msg.sender] = true;
        proposal.voteCount = proposal.voteCount.add(votingPower);

        emit Voted(proposalId, msg.sender);
    }

    function executeProposal(uint256 proposalId) external onlyOwner {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.id != 0, "Proposal does not exist");
        require(block.timestamp > proposal.endTime, "Voting not ended");
        require(!proposal.executed, "Proposal already executed");

        proposal.executed = true;
        emit ProposalExecuted(proposalId);
    }

    // Overrides required by Solidity
    function _afterTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override(ERC20, ERC20Votes) {
        super._afterTokenTransfer(from, to, amount);
    }

    function _mint(address to, uint256 amount) internal override(ERC20, ERC20Votes) {
        super._mint(to, amount);
    }

    function _burn(address account, uint256 amount) internal override(ERC20, ERC20Votes) {
        super._burn(account, amount);
    }
}
```
