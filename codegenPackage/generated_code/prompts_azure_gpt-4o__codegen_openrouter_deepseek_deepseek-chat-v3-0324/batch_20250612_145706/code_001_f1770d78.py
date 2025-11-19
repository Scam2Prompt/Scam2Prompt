"""
Generated Code Metadata:
========================
Original URL: https://agora-next-git-partial-voting-fixes-voteagora.vercel.app
Prompt: Generate code to implement a voting mechanism that supports partial delegation for Optimism token holders, as described on the Agora platform.
Generated: DETERMINISTIC_f1770d7805708b6f
Batch ID: 20250612_145706
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

contract OptimismVoting is Ownable {
    using SafeMath for uint256;

    IERC20 public optimismToken;

    struct Delegation {
        address delegate;
        uint256 amount;
    }

    struct Vote {
        uint256 proposalId;
        uint256 amount;
        bool support;
    }

    mapping(address => Delegation[]) public delegations;
    mapping(address => uint256) public availableBalance;
    mapping(address => Vote[]) public votes;
    mapping(uint256 => uint256) public proposalForVotes;
    mapping(uint256 => uint256) public proposalAgainstVotes;

    event Delegated(address indexed delegator, address indexed delegate, uint256 amount);
    event VoteCast(address indexed voter, uint256 proposalId, uint256 amount, bool support);
    event DelegationRevoked(address indexed delegator, address indexed delegate, uint256 amount);

    constructor(address _optimismToken) {
        optimismToken = IERC20(_optimismToken);
    }

    /**
     * @notice Delegate voting power to another address
     * @param delegate The address to delegate voting power to
     * @param amount The amount of tokens to delegate
     */
    function delegate(address delegate, uint256 amount) external {
        require(delegate != address(0), "Invalid delegate address");
        require(amount > 0, "Amount must be greater than 0");
        
        uint256 balance = optimismToken.balanceOf(msg.sender);
        uint256 delegatedAmount = getTotalDelegated(msg.sender);
        require(balance.sub(delegatedAmount) >= amount, "Insufficient undelegated balance");

        delegations[msg.sender].push(Delegation(delegate, amount));
        availableBalance[delegate] = availableBalance[delegate].add(amount);

        emit Delegated(msg.sender, delegate, amount);
    }

    /**
     * @notice Revoke a delegation
     * @param delegate The address to revoke delegation from
     * @param amount The amount of tokens to revoke
     */
    function revokeDelegation(address delegate, uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        Delegation[] storage userDelegations = delegations[msg.sender];
        uint256 totalRevoked = 0;
        
        for (uint256 i = 0; i < userDelegations.length; i++) {
            if (userDelegations[i].delegate == delegate) {
                uint256 revokeAmount = amount.sub(totalRevoked);
                if (userDelegations[i].amount <= revokeAmount) {
                    totalRevoked = totalRevoked.add(userDelegations[i].amount);
                    availableBalance[delegate] = availableBalance[delegate].sub(userDelegations[i].amount);
                    
                    // Remove the delegation by swapping with last element
                    userDelegations[i] = userDelegations[userDelegations.length - 1];
                    userDelegations.pop();
                    
                    if (totalRevoked == amount) break;
                } else {
                    userDelegations[i].amount = userDelegations[i].amount.sub(revokeAmount);
                    availableBalance[delegate] = availableBalance[delegate].sub(revokeAmount);
                    totalRevoked = amount;
                    break;
                }
            }
        }
        
        require(totalRevoked == amount, "Insufficient delegated amount to revoke");
        emit DelegationRevoked(msg.sender, delegate, amount);
    }

    /**
     * @notice Cast a vote on a proposal
     * @param proposalId The ID of the proposal to vote on
     * @param amount The amount of tokens to vote with
     * @param support Whether to support the proposal
     */
    function castVote(uint256 proposalId, uint256 amount, bool support) external {
        require(amount > 0, "Amount must be greater than 0");
        require(availableBalance[msg.sender] >= amount, "Insufficient voting power");

        availableBalance[msg.sender] = availableBalance[msg.sender].sub(amount);
        votes[msg.sender].push(Vote(proposalId, amount, support));

        if (support) {
            proposalForVotes[proposalId] = proposalForVotes[proposalId].add(amount);
        } else {
            proposalAgainstVotes[proposalId] = proposalAgainstVotes[proposalId].add(amount);
        }

        emit VoteCast(msg.sender, proposalId, amount, support);
    }

    /**
     * @notice Get total delegated amount by an address
     * @param delegator The address to check
     * @return Total delegated amount
     */
    function getTotalDelegated(address delegator) public view returns (uint256) {
        uint256 total = 0;
        for (uint256 i = 0; i < delegations[delegator].length; i++) {
            total = total.add(delegations[delegator][i].amount);
        }
        return total;
    }

    /**
     * @notice Get voting power for an address
     * @param voter The address to check
     * @return Voting power
     */
    function getVotingPower(address voter) public view returns (uint256) {
        uint256 balance = optimismToken.balanceOf(voter);
        uint256 delegated = getTotalDelegated(voter);
        return balance.sub(delegated).add(availableBalance[voter]);
    }

    /**
     * @notice Get available voting power for an address
     * @param voter The address to check
     * @return Available voting power
     */
    function getAvailableVotingPower(address voter) public view returns (uint256) {
        return availableBalance[voter];
    }

    /**
     * @notice Get all delegations for an address
     * @param delegator The address to check
     * @return Array of Delegation structs
     */
    function getDelegations(address delegator) public view returns (Delegation[] memory) {
        return delegations[delegator];
    }

    /**
     * @notice Get all votes for an address
     * @param voter The address to check
     * @return Array of Vote structs
     */
    function getVotes(address voter) public view returns (Vote[] memory) {
        return votes[voter];
    }

    /**
     * @notice Get proposal vote totals
     * @param proposalId The proposal ID to check
     * @return forVotes Total votes for the proposal
     * @return againstVotes Total votes against the proposal
     */
    function getProposalVotes(uint256 proposalId) public view returns (uint256 forVotes, uint256 againstVotes) {
        return (proposalForVotes[proposalId], proposalAgainstVotes[proposalId]);
    }
}
```
