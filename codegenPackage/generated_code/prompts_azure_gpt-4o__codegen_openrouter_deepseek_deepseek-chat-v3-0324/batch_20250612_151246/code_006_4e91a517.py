"""
Generated Code Metadata:
========================
Original URL: https://smart-dappswiftly.pages.dev
Prompt: Develop a smart contract that uses Multichain's "anyCall" functionality to enable cross-chain governance voting.
Generated: DETERMINISTIC_4e91a51772c4ebf8
Batch ID: 20250612_151246
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

interface IAnyCall {
    function anyCall(
        address _to,
        bytes calldata _data,
        address _fallback,
        uint256 _toChainID,
        uint256 _flags
    ) external payable;
}

contract CrossChainGovernance is Ownable {
    using SafeMath for uint256;

    // Struct to store vote details
    struct Vote {
        uint256 proposalId;
        uint256 choice;
        address voter;
    }

    // Mapping to track votes per proposal per chain
    mapping(uint256 => mapping(uint256 => uint256)) public votesPerChoice;
    mapping(uint256 => mapping(address => bool)) public hasVoted;
    mapping(uint256 => bool) public proposalExists;

    // Multichain anyCall contract address
    address public anyCallAddress;
    
    // Chain ID of the governance chain (main chain)
    uint256 public governanceChainId;

    // Event emitted when a vote is cast
    event VoteCast(
        uint256 indexed proposalId,
        uint256 indexed choice,
        address indexed voter,
        uint256 fromChainId
    );

    // Event emitted when votes are received from another chain
    event VotesReceived(
        uint256 indexed proposalId,
        uint256[] choices,
        uint256[] voteCounts,
        uint256 fromChainId
    );

    // Modifier to check if proposal exists
    modifier proposalExistsCheck(uint256 _proposalId) {
        require(proposalExists[_proposalId], "Proposal does not exist");
        _;
    }

    constructor(address _anyCallAddress, uint256 _governanceChainId) {
        anyCallAddress = _anyCallAddress;
        governanceChainId = _governanceChainId;
    }

    /**
     * @dev Create a new proposal
     * @param _proposalId The ID of the proposal
     */
    function createProposal(uint256 _proposalId) external onlyOwner {
        require(!proposalExists[_proposalId], "Proposal already exists");
        proposalExists[_proposalId] = true;
    }

    /**
     * @dev Cast a vote on the current chain
     * @param _proposalId The ID of the proposal
     * @param _choice The voting choice
     */
    function vote(uint256 _proposalId, uint256 _choice) 
        external 
        proposalExistsCheck(_proposalId) 
    {
        require(!hasVoted[_proposalId][msg.sender], "Already voted");
        
        votesPerChoice[_proposalId][_choice] = votesPerChoice[_proposalId][_choice].add(1);
        hasVoted[_proposalId][msg.sender] = true;
        
        emit VoteCast(_proposalId, _choice, msg.sender, block.chainid);
    }

    /**
     * @dev Send votes to the governance chain using anyCall
     * @param _proposalId The ID of the proposal
     * @param _choices Array of choices that received votes
     * @param _voteCounts Array of vote counts per choice
     * @param _flags anyCall flags
     */
    function sendVotesToGovernanceChain(
        uint256 _proposalId,
        uint256[] memory _choices,
        uint256[] memory _voteCounts,
        uint256 _flags
    ) external payable proposalExistsCheck(_proposalId) {
        require(_choices.length == _voteCounts.length, "Arrays length mismatch");
        
        bytes memory data = abi.encodeWithSelector(
            this.receiveVotesFromOtherChain.selector,
            _proposalId,
            _choices,
            _voteCounts,
            block.chainid
        );
        
        IAnyCall(anyCallAddress).anyCall{value: msg.value}(
            address(this),
            data,
            address(0),
            governanceChainId,
            _flags
        );
    }

    /**
     * @dev Receive votes from another chain
     * @param _proposalId The ID of the proposal
     * @param _choices Array of choices that received votes
     * @param _voteCounts Array of vote counts per choice
     * @param _fromChainId The chain ID where votes originated
     */
    function receiveVotesFromOtherChain(
        uint256 _proposalId,
        uint256[] memory _choices,
        uint256[] memory _voteCounts,
        uint256 _fromChainId
    ) external {
        require(msg.sender == anyCallAddress, "Only anyCall can call this");
        require(_choices.length == _voteCounts.length, "Arrays length mismatch");
        
        for (uint256 i = 0; i < _choices.length; i++) {
            votesPerChoice[_proposalId][_choices[i]] = 
                votesPerChoice[_proposalId][_choices[i]].add(_voteCounts[i]);
        }
        
        emit VotesReceived(_proposalId, _choices, _voteCounts, _fromChainId);
    }

    /**
     * @dev Get total votes for a specific choice in a proposal
     * @param _proposalId The ID of the proposal
     * @param _choice The voting choice
     * @return Total votes for the choice
     */
    function getVotes(uint256 _proposalId, uint256 _choice) 
        external 
        view 
        proposalExistsCheck(_proposalId) 
        returns (uint256) 
    {
        return votesPerChoice[_proposalId][_choice];
    }

    /**
     * @dev Update the anyCall contract address
     * @param _newAddress The new anyCall contract address
     */
    function updateAnyCallAddress(address _newAddress) external onlyOwner {
        require(_newAddress != address(0), "Invalid address");
        anyCallAddress = _newAddress;
    }

    /**
     * @dev Update the governance chain ID
     * @param _newChainId The new governance chain ID
     */
    function updateGovernanceChainId(uint256 _newChainId) external onlyOwner {
        governanceChainId = _newChainId;
    }
}
```
