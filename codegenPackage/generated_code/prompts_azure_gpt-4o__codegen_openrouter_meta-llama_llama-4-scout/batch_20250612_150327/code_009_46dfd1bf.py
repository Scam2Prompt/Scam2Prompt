"""
Generated Code Metadata:
========================
Original URL: https://frax-finances.pages.dev
Prompt: Create a Solidity contract that integrates Frax Governance tokens (FXS and FPIS) for voting on ecosystem proposals. Include staking mechanisms for veFXS and veFPIS.
Generated: DETERMINISTIC_46dfd1bf6f083d4d
Batch ID: 20250612_150327
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/Math.sol";

contract FraxGovernanceContract is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of token addresses to their respective staking pools
    mapping(address => StakingPool) public stakingPools;

    // Mapping of proposal IDs to their respective voting results
    mapping(uint256 => Proposal) public proposals;

    // Mapping of user addresses to their respective voting powers
    mapping(address => UserVotingPower) public userVotingPowers;

    // Event emitted when a new proposal is created
    event NewProposal(uint256 proposalId, string proposalDescription);

    // Event emitted when a user votes on a proposal
    event VoteCast(uint256 proposalId, address user, bool support);

    // Event emitted when a user stakes tokens
    event TokensStaked(address indexed user, address indexed token, uint256 amount);

    // Event emitted when a user unstakes tokens
    event TokensUnstaked(address indexed user, address indexed token, uint256 amount);

    // FXS and FPIS token addresses
    address public constant FXS_TOKEN_ADDRESS = 0x3432F6AF6C708A7E7E5C0E80A9E4F6fC3bD2c9C;
    address public constant FPIS_TOKEN_ADDRESS = 0x5Ca981bA31B95759C4B7cCfb8cB7A0C1d46F7f2;

    // veFXS and veFPIS token addresses
    address public constant VEFXS_TOKEN_ADDRESS = 0xA0a3E5B9B2B65588A563E5372574f7E319C1cC;
    address public constant VEFPIS_TOKEN_ADDRESS = 0x8A0a3E5B9B2B65588A563E5372574f7E319C1cD;

    // Constructor
    constructor() public {}

    // Function to create a new staking pool for a given token
    function createStakingPool(address token) public onlyOwner {
        require(stakingPools[token].poolExists == false, "Staking pool already exists for this token");

        stakingPools[token] = StakingPool(true, token, 0);
    }

    // Function to stake tokens
    function stakeTokens(address token, uint256 amount) public {
        require(stakingPools[token].poolExists == true, "Staking pool does not exist for this token");
        require(IERC20(token).balanceOf(msg.sender) >= amount, "Insufficient token balance");

        IERC20(token).safeTransferFrom(msg.sender, address(this), amount);
        stakingPools[token].totalStaked = stakingPools[token].totalStaked.add(amount);

        // Calculate and update user's voting power
        uint256 votingPower = calculateVotingPower(token, amount);
        userVotingPowers[msg.sender].votingPower = userVotingPowers[msg.sender].votingPower.add(votingPower);

        emit TokensStaked(msg.sender, token, amount);
    }

    // Function to unstake tokens
    function unstakeTokens(address token, uint256 amount) public {
        require(stakingPools[token].poolExists == true, "Staking pool does not exist for this token");
        require(stakingPools[token].totalStaked >= amount, "Insufficient staked tokens");

        stakingPools[token].totalStaked = stakingPools[token].totalStaked.sub(amount);

        // Calculate and update user's voting power
        uint256 votingPower = calculateVotingPower(token, amount);
        userVotingPowers[msg.sender].votingPower = userVotingPowers[msg.sender].votingPower.sub(votingPower);

        IERC20(token).safeTransfer(msg.sender, amount);

        emit TokensUnstaked(msg.sender, token, amount);
    }

    // Function to create a new proposal
    function createProposal(string memory proposalDescription) public {
        uint256 proposalId = proposals.length;
        proposals[proposalId] = Proposal(proposalId, proposalDescription, 0, 0);

        emit NewProposal(proposalId, proposalDescription);
    }

    // Function to vote on a proposal
    function voteOnProposal(uint256 proposalId, bool support) public {
        require(proposals[proposalId].exists == true, "Proposal does not exist");

        // Update proposal voting results
        if (support) {
            proposals[proposalId].yesVotes = proposals[proposalId].yesVotes.add(userVotingPowers[msg.sender].votingPower);
        } else {
            proposals[proposalId].noVotes = proposals[proposalId].noVotes.add(userVotingPowers[msg.sender].votingPower);
        }

        emit VoteCast(proposalId, msg.sender, support);
    }

    // Function to calculate voting power based on staked tokens
    function calculateVotingPower(address token, uint256 amount) internal view returns (uint256) {
        // For simplicity, assume 1:1 voting power to staked tokens ratio
        // In a real-world scenario, this would be a more complex calculation
        // based on the specific requirements of the Frax Governance tokens
        return amount;
    }

    // Struct to represent a staking pool
    struct StakingPool {
        bool poolExists;
        address token;
        uint256 totalStaked;
    }

    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        string description;
        bool exists;
        uint256 yesVotes;
        uint256 noVotes;
    }

    // Struct to represent a user's voting power
    struct UserVotingPower {
        uint256 votingPower;
    }
}
```
