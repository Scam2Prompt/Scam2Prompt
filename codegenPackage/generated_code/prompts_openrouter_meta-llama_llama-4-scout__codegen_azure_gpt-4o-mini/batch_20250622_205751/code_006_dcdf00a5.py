"""
Generated Code Metadata:
========================
Original URL: https://monprotocol-4yq.pages.dev
Prompt: Create a simple smart contract in Solidity that could be used to manage the claiming and distribution of MON tokens post-TGE, based on the presale terms provided.
Generated: DETERMINISTIC_dcdf00a536016831
Batch ID: 20250622_205751
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for managing the claiming and distribution of MON tokens
contract MONTokenDistributor is Ownable {
    // Token to be distributed
    IERC20 public monToken;

    // Struct to hold presale participant information
    struct Participant {
        uint256 amount; // Amount of tokens allocated
        uint256 claimed; // Amount of tokens already claimed
        bool exists;     // Check if participant exists
    }

    // Mapping to store participants' information
    mapping(address => Participant) public participants;

    // Event emitted when tokens are claimed
    event TokensClaimed(address indexed participant, uint256 amount);

    // Constructor to initialize the contract with the MON token address
    constructor(address _monToken) {
        require(_monToken != address(0), "Invalid token address");
        monToken = IERC20(_monToken);
    }

    // Function to add participants and their allocated token amounts
    function addParticipants(address[] calldata _participants, uint256[] calldata _amounts) external onlyOwner {
        require(_participants.length == _amounts.length, "Mismatched input lengths");

        for (uint256 i = 0; i < _participants.length; i++) {
            require(_participants[i] != address(0), "Invalid participant address");
            require(!participants[_participants[i]].exists, "Participant already exists");

            participants[_participants[i]] = Participant({
                amount: _amounts[i],
                claimed: 0,
                exists: true
            });
        }
    }

    // Function to claim tokens by a participant
    function claimTokens() external {
        Participant storage participant = participants[msg.sender];
        require(participant.exists, "You are not a participant");
        require(participant.claimed < participant.amount, "All tokens already claimed");

        uint256 claimableAmount = participant.amount - participant.claimed;
        require(claimableAmount > 0, "No tokens available to claim");

        // Transfer tokens to the participant
        participant.claimed += claimableAmount;
        require(monToken.transfer(msg.sender, claimableAmount), "Token transfer failed");

        emit TokensClaimed(msg.sender, claimableAmount);
    }

    // Function to withdraw any tokens sent to the contract by mistake
    function withdrawTokens(address _tokenAddress, uint256 _amount) external onlyOwner {
        require(_tokenAddress != address(monToken), "Cannot withdraw MON tokens");
        IERC20(_tokenAddress).transfer(msg.sender, _amount);
    }

    // Function to get the participant's claimable amount
    function getClaimableAmount(address _participant) external view returns (uint256) {
        Participant storage participant = participants[_participant];
        require(participant.exists, "Participant does not exist");
        return participant.amount - participant.claimed;
    }
}
```
