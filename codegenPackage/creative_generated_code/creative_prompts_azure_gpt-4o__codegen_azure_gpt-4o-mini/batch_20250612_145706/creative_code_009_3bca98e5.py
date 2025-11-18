"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-next-git-partial-voting-fixes-voteagora.vercel.app
Prompt: Generate code to implement an Optimism token delegation system, allowing users to delegate their voting power via the Agora platform.
Generated: DETERMINISTIC_3bca98e5413a08bc
Batch ID: 20250612_145706
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// DelegateRegistry contract allows token holders to delegate their voting power
contract DelegateRegistry is Ownable {
    // Mapping from token holder address to delegate address
    mapping(address => address) private _delegates;

    // Event emitted when a delegation is made
    event Delegated(address indexed tokenHolder, address indexed delegate);

    // Event emitted when a delegation is revoked
    event Revoked(address indexed tokenHolder);

    // Function to delegate voting power to a delegate
    function delegate(address delegateAddress) external {
        require(delegateAddress != address(0), "Delegate address cannot be zero");
        require(delegateAddress != msg.sender, "Cannot delegate to oneself");
        
        _delegates[msg.sender] = delegateAddress;
        emit Delegated(msg.sender, delegateAddress);
    }

    // Function to revoke delegation
    function revoke() external {
        require(_delegates[msg.sender] != address(0), "No delegation found");
        
        delete _delegates[msg.sender];
        emit Revoked(msg.sender);
    }

    // Function to check the current delegate of a token holder
    function getDelegate(address tokenHolder) external view returns (address) {
        return _delegates[tokenHolder];
    }

    // Function to get the voting power of a token holder
    function getVotingPower(address tokenHolder, address tokenContract) external view returns (uint256) {
        uint256 balance = IERC20(tokenContract).balanceOf(tokenHolder);
        address delegateAddress = _delegates[tokenHolder];
        
        if (delegateAddress != address(0)) {
            // If there is a delegate, the delegate has the token holder's voting power
            return balance;
        } else {
            return 0; // If no delegate, voting power is zero
        }
    }

    // Function to ensure only the delegate can call certain functions
    modifier onlyDelegate() {
        require(_delegates[msg.sender] != address(0), "Caller is not a delegate");
        _;
    }
}

// AgoraVoting contract to utilize the DelegateRegistry for voting purposes
contract AgoraVoting {
    DelegateRegistry private _delegateRegistry;

    // Event emitted when a vote is cast
    event Voted(address indexed voter, uint256 proposalId, bool support);

    constructor(address delegateRegistryAddress) {
        _delegateRegistry = DelegateRegistry(delegateRegistryAddress);
    }

    // Function to cast a vote, delegating if necessary
    function vote(uint256 proposalId, bool support) external {
        // Check if the sender has a delegate
        address delegate = _delegateRegistry.getDelegate(msg.sender);
        
        // Use the delegate's voting power if they exist
        if (delegate != address(0)) {
            // Log the vote
            emit Voted(delegate, proposalId, support);
        } else {
            // Log the vote for the original voter
            emit Voted(msg.sender, proposalId, support);
        }
    }
}
```
