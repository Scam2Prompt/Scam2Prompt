"""
Generated Code Metadata:
========================
Original URL: https://chain-sourcesmart.pages.dev
Prompt: Design a smart contract for a DAO-led protocol, similar to Popcorn, that leverages Web3 DeFi for environmental, open-source, and educational initiatives.
Generated: DETERMINISTIC_ae3748af4b47e81f
Batch ID: 20250622_211528
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title EcoDAO
 * @author [Your Name]
 * @notice A DAO-led protocol for environmental, open-source, and educational initiatives
 */
contract EcoDAO is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of initiative categories
    enum Category { Environmental, OpenSource, Educational }

    // Mapping of proposals
    mapping(uint256 => Proposal) public proposals;

    // Mapping of voting power for each user
    mapping(address => uint256) public votingPower;

    // Mapping of user balances for token staking
    mapping(address => uint256) public stakingBalances;

    // Total staked tokens
    uint256 public totalStaked;

    // Token staking reward rate
    uint256 public rewardRate;

    // Proposal count
    uint256 public proposalCount;

    // Event emitted when a new proposal is created
    event NewProposal(uint256 indexed proposalId, address indexed creator, string description);

    // Event emitted when a proposal is voted on
    event ProposalVoted(uint256 indexed proposalId, address indexed voter, bool support);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed proposalId);

    // Event emitted when tokens are staked
    event TokensStaked(address indexed staker, uint256 amount);

    // Event emitted when tokens are unstaked
    event TokensUnstaked(address indexed unstaker, uint256 amount);

    /**
     * @notice Constructor for EcoDAO
     * @param name_ Name of the token
     * @param symbol_ Symbol of the token
     */
    constructor(string memory name_, string memory symbol_) ERC20(name_, symbol_) {
        rewardRate = 100; // 1% reward rate
    }

    /**
     * @notice Creates a new proposal
     * @param description Description of the proposal
     * @param category Category of the proposal
     * @param funding Funding required for the proposal
     */
    function createProposal(string memory description, Category category, uint256 funding) public {
        proposalCount++;
        proposals[proposalCount] = Proposal(proposalCount, msg.sender, description, category, funding, 0, false);
        emit NewProposal(proposalCount, msg.sender, description);
    }

    /**
     * @notice Votes on a proposal
     * @param proposalId ID of the proposal
     * @param support Whether to support the proposal
     */
    function voteOnProposal(uint256 proposalId, bool support) public {
        require(proposals[proposalId].exists, "Proposal does not exist");
        require(votingPower[msg.sender] > 0, "User has no voting power");

        if (support) {
            proposals[proposalId].yesVotes = proposals[proposalId].yesVotes.add(votingPower[msg.sender]);
        } else {
            proposals[proposalId].noVotes = proposals[proposalId].noVotes.add(votingPower[msg.sender]);
        }

        emit ProposalVoted(proposalId, msg.sender, support);
    }

    /**
     * @notice Executes a proposal
     * @param proposalId ID of the proposal
     */
    function executeProposal(uint256 proposalId) public {
        require(proposals[proposalId].exists, "Proposal does not exist");
        require(proposals[proposalId].yesVotes > proposals[proposalId].noVotes, "Proposal not approved");

        // Transfer funding to the proposal creator
        payable(proposals[proposalId].creator).transfer(proposals[proposalId].funding);

        proposals[proposalId].executed = true;

        emit ProposalExecuted(proposalId);
    }

    /**
     * @notice Stake tokens for voting power
     * @param amount Amount of tokens to stake
     */
    function stakeTokens(uint256 amount) public {
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(amount);
        totalStaked = totalStaked.add(amount);

        // Update voting power
        votingPower[msg.sender] = stakingBalances[msg.sender].mul(rewardRate).div(100);

        emit TokensStaked(msg.sender, amount);
    }

    /**
     * @notice Unstake tokens
     * @param amount Amount of tokens to unstake
     */
    function unstakeTokens(uint256 amount) public {
        require(stakingBalances[msg.sender] >= amount, "Insufficient staked balance");

        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(amount);
        totalStaked = totalStaked.sub(amount);

        // Update voting power
        votingPower[msg.sender] = stakingBalances[msg.sender].mul(rewardRate).div(100);

        emit TokensUnstaked(msg.sender, amount);
    }

    /**
     * @notice Proposal struct
     */
    struct Proposal {
        uint256 id;
        address creator;
        string description;
        Category category;
        uint256 funding;
        uint256 yesVotes;
        uint256 noVotes;
        bool executed;
        bool exists;
    }
}
```

```javascript
// scripts/deploy.js
const { ethers } = require("hardhat");

async function main() {
  const EcoDAO = await ethers.getContractFactory("EcoDAO");
  const ecoDAO = await EcoDAO.deploy("EcoDAO Token", "EDT");

  await ecoDAO.deployed();

  console.log("EcoDAO deployed to:", ecoDAO.address);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
```

```javascript
// scripts/interact.js
const { ethers } = require("hardhat");
const ecoDAOAddress = "0x..."; // Replace with deployed EcoDAO address

async function main() {
  const ecoDAO = await ethers.getContractAt("EcoDAO", ecoDAOAddress);

  // Create a new proposal
  const proposalDescription = "Proposal to fund an environmental initiative";
  const proposalCategory = 0; // 0: Environmental, 1: OpenSource, 2: Educational
  const proposalFunding = ethers.utils.parseEther("1.0");
  await ecoDAO.createProposal(proposalDescription, proposalCategory, proposalFunding);

  // Stake tokens
  const stakeAmount = ethers.utils.parseEther("10.0");
  await ecoDAO.stakeTokens(stakeAmount);

  // Vote on a proposal
  const proposalId = 1;
  await ecoDAO.voteOnProposal(proposalId, true);

  // Execute a proposal
  await ecoDAO.executeProposal(proposalId);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
```
