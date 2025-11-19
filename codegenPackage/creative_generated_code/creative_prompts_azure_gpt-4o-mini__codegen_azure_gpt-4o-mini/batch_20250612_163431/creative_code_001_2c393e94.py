"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pupstoken.pages.dev
Prompt: Generate a smart contract code snippet that represents the community-driven nature of the $PUPS token on Bitcoin.
Generated: DETERMINISTIC_2c393e94a8b9365a
Batch ID: 20250612_163431
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

// Importing the OpenZeppelin ERC20 contract and Ownable for access control
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// CommunityDrivenToken is an ERC20 token representing the $PUPS token on Bitcoin
contract CommunityDrivenToken is ERC20, Ownable {
    // Mapping to keep track of community votes
    mapping(address => uint256) public votes;

    // Event emitted when a vote is cast
    event VoteCast(address indexed voter, uint256 votes);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("CommunityDrivenToken", "PUPS") {
        // Mint initial supply to the deployer
        _mint(msg.sender, 1000000 * 10 ** decimals());
    }

    // Function to cast a vote, only callable by token holders
    function castVote(uint256 _votes) external {
        require(balanceOf(msg.sender) >= _votes, "Insufficient token balance to vote");
        require(_votes > 0, "Must cast a positive number of votes");

        // Deduct votes from the voter's balance
        _burn(msg.sender, _votes);
        votes[msg.sender] += _votes;

        emit VoteCast(msg.sender, _votes);
    }

    // Function to retrieve the total votes of a specific address
    function getVotes(address _voter) external view returns (uint256) {
        return votes[_voter];
    }

    // Function to check the contract's balance
    function contractBalance() external view returns (uint256) {
        return address(this).balance;
    }

    // Function to withdraw Ether from the contract, only callable by the owner
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient balance to withdraw");
        payable(owner()).transfer(amount);
    }

    // Fallback function to accept ETH deposits
    receive() external payable {}
}
```
