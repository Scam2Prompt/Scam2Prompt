"""
Generated Code Metadata:
========================
Original URL: https://airkombat.com
Prompt: Create a Solidity contract for a community-driven token distribution system that allows users to vote on how $WING tokens should be allocated in future phases.
Generated: DETERMINISTIC_3c7206435c704c84
Batch ID: 20250612_155037
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

/**
 * @title CommunityTokenDistribution
 * @dev A contract for community-driven token distribution with voting mechanism
 */
contract CommunityTokenDistribution is Ownable {
    using SafeMath for uint256;

    // Token to be distributed
    IERC20 public wingToken;

    // Voting period in blocks
    uint256 public votingPeriod;

    // Minimum voting power required to create a proposal
    uint256 public minVotingPowerToPropose;

    // Minimum votes required for a proposal to be executable
    uint256 public minVotesToExecute;

    // Current proposal ID counter
    uint256 public proposalCounter;

    // Mapping from user address to voting power (token balance)
    mapping(address => uint256) public votingPower;

    // Mapping from proposal ID to Proposal struct
    mapping(uint256 => Proposal) public proposals;

    // Mapping from user address to mapping of proposal IDs to whether they've voted
    mapping(address => mapping(uint256 => bool)) public hasVoted;

    // Proposal status enum
    enum ProposalStatus {
        Pending,
        Approved,
        Rejected,
        Executed
    }

    // Proposal structure
    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        address[] recipients;
        uint256[] amounts;
        uint256 startBlock;
        uint256 endBlock;
        uint256 yesVotes;
        uint256 noVotes;
        ProposalStatus status;
    }

    // Events
    event ProposalCreated(
        uint256 indexed id,
        address indexed proposer,
        string description,
        uint256 startBlock,
        uint256 endBlock
    );
    event Voted(
        uint256 indexed proposalId,
        address indexed voter,
        bool support,
        uint256 votingPower
    );
    event ProposalExecuted(uint256 indexed proposalId);
    event VotingPowerUpdated(address indexed user, uint256 newVotingPower);

    /**
     * @dev Constructor
     * @param _wingToken Address of the WING token contract
     * @param _votingPeriod Duration of voting period in blocks
     * @param _minVotingPowerToPropose Minimum tokens needed to create a proposal
     * @param _minVotesToExecute Minimum votes needed to execute a proposal
     */
    constructor(
        address _wingToken,
        uint256 _votingPeriod,
        uint256 _minVotingPowerToPropose,
        uint256 _minVotesToExecute
    ) {
        require(_wingToken != address(0), "Invalid token address");
        require(_votingPeriod > 0, "Voting period must be positive");
        require(
            _minVotingPowerToPropose > 0,
            "Min voting power must be positive"
        );
        require(_minVotesToExecute > 0, "Min votes must be positive");

        wingToken = IERC20(_wingToken);
        votingPeriod = _votingPeriod;
        minVotingPowerToPropose = _minVotingPowerToPropose;
        minVotesToExecute = _minVotesToExecute;
    }

    /**
     * @dev Update user's voting power based on current token balance
     * @param user Address of the user
     */
    function updateVotingPower(address user) public {
        uint256 balance = wingToken.balanceOf(user);
        votingPower[user] = balance;
        emit VotingPowerUpdated(user, balance);
    }

    /**
     * @dev Create a new proposal for token distribution
     * @param description Description of the proposal
     * @param recipients Array of recipient addresses
     * @param amounts Array of corresponding token amounts
     */
    function createProposal(
        string memory description,
        address[] memory recipients,
        uint256[] memory amounts
    ) external {
        require(recipients.length == amounts.length, "Arrays length mismatch");
        require(recipients.length > 0, "No recipients specified");
        require(
            votingPower[msg.sender] >= minVotingPowerToPropose,
            "Insufficient voting power"
        );

        // Update voting power
        updateVotingPower(msg.sender);

        proposalCounter++;
        uint256 startBlock = block.number;
        uint256 endBlock = startBlock.add(votingPeriod);

        proposals[proposalCounter] = Proposal({
            id: proposalCounter,
            proposer: msg.sender,
            description: description,
            recipients: recipients,
            amounts: amounts,
            startBlock: startBlock,
            endBlock: endBlock,
            yesVotes: 0,
            noVotes: 0,
            status: ProposalStatus.Pending
        });

        emit ProposalCreated(
            proposalCounter,
            msg.sender,
            description,
            startBlock,
            endBlock
        );
    }

    /**
     * @dev Vote on a proposal
     * @param proposalId ID of the proposal
     * @param support True for yes, false for no
     */
    function vote(uint256 proposalId, bool support) external {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.id == proposalId, "Proposal does not exist");
        require(
            block.number >= proposal.startBlock &&
                block.number <= proposal.endBlock,
            "Voting period closed"
        );
        require(!hasVoted[msg.sender][proposalId], "Already voted");

        // Update voting power
        updateVotingPower(msg.sender);
        uint256 power = votingPower[msg.sender];
        require(power > 0, "No voting power");

        if (support) {
            proposal.yesVotes = proposal.yesVotes.add(power);
        } else {
            proposal.noVotes = proposal.noVotes.add(power);
        }

        hasVoted[msg.sender][proposalId] = true;
        emit Voted(proposalId, msg.sender, support, power);
    }

    /**
     * @dev Execute a proposal that has been approved
     * @param proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.id == proposalId, "Proposal does not exist");
        require(
            block.number > proposal.endBlock,
            "Voting period not ended"
        );
        require(
            proposal.status == ProposalStatus.Pending,
            "Proposal already processed"
        );

        // Check if proposal passed
        if (
            proposal.yesVotes > proposal.noVotes &&
            proposal.yesVotes >= minVotesToExecute
        ) {
            proposal.status = ProposalStatus.Approved;

            // Calculate total amount needed
            uint256 totalAmount = 0;
            for (uint256 i = 0; i < proposal.amounts.length; i++) {
                totalAmount = totalAmount.add(proposal.amounts[i]);
            }

            // Check contract balance
            uint256 contractBalance = wingToken.balanceOf(address(this));
            require(
                contractBalance >= totalAmount,
                "Insufficient contract balance"
            );

            // Distribute tokens
            for (uint256 i = 0; i < proposal.recipients.length; i++) {
                require(
                    wingToken.transfer(proposal.recipients[i], proposal.amounts[i]),
                    "Transfer failed"
                );
            }
        } else {
            proposal.status = ProposalStatus.Rejected;
        }

        emit ProposalExecuted(proposalId);
    }

    /**
     * @dev Deposit WING tokens to the contract for distribution
     * @param amount Amount of tokens to deposit
     */
    function depositTokens(uint256 amount) external {
        require(amount > 0, "Amount must be positive");
        require(
            wingToken.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );
    }

    /**
     * @dev Withdraw WING tokens from the contract (owner only)
     * @param amount Amount of tokens to withdraw
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be positive");
        require(
            wingToken.transfer(owner(), amount),
            "Transfer failed"
        );
    }

    /**
     * @dev Update voting period (owner only)
     * @param newVotingPeriod New voting period in blocks
     */
    function setVotingPeriod(uint256 newVotingPeriod) external onlyOwner {
        require(newVotingPeriod > 0, "Voting period must be positive");
        votingPeriod = newVotingPeriod;
    }

    /**
     * @dev Update minimum voting power to propose (owner only)
     * @param newMinPower New minimum voting power
     */
    function setMinVotingPowerToPropose(uint256 newMinPower) external onlyOwner {
        require(newMinPower > 0, "Min power must be positive");
        minVotingPowerToPropose = newMinPower;
    }

    /**
     * @dev Update minimum votes to execute (owner only)
     * @param newMinVotes
