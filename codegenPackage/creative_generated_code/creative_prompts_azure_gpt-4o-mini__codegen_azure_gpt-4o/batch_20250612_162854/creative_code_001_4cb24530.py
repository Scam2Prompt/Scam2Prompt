"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.community
Prompt: Write a smart contract that integrates with the Moxie Protocol to automate shared payouts for rewards earned on Farcaster.
Generated: DETERMINISTIC_4cb24530a6957c39
Batch ID: 20250612_162854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the clean, well-commented, and production-ready smart contract code for the given request. It is written in Solidity, assuming that the Moxie Protocol is an external contract, and the shared payouts functionality is implemented securely.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title SharedRewardsPayout
 * @dev This contract integrates with the Moxie Protocol to automate shared payouts
 *      for rewards earned on Farcaster.
 */
contract SharedRewardsPayout {
    // Moxie Protocol interface
    interface IMoxieProtocol {
        function claimRewards(address recipient) external returns (uint256);
    }

    // Address of the Moxie Protocol contract
    address public moxieProtocolAddress;

    // Event emitted when a payout is successfully distributed
    event PayoutDistributed(address indexed recipient, uint256 amount);

    // Struct to define a participant and their share
    struct Participant {
        address walletAddress;
        uint256 sharePercentage; // Share percentage (out of 100)
    }

    // Array to store participants
    Participant[] public participants;

    // Total share percentage (should always sum to 100)
    uint256 public totalSharePercentage;

    // Modifier to ensure only the contract owner can execute certain functions
    address public owner;
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the Moxie Protocol address.
     * @param _moxieProtocolAddress Address of the Moxie Protocol contract.
     */
    constructor(address _moxieProtocolAddress) {
        require(_moxieProtocolAddress != address(0), "Invalid Moxie Protocol address");
        moxieProtocolAddress = _moxieProtocolAddress;
        owner = msg.sender; // Set the contract deployer as the owner
    }

    /**
     * @dev Adds a new participant to the payout pool.
     * @param _walletAddress Address of the participant's wallet.
     * @param _sharePercentage Percentage share of the rewards for the participant.
     */
    function addParticipant(address _walletAddress, uint256 _sharePercentage) external onlyOwner {
        require(_walletAddress != address(0), "Invalid wallet address");
        require(_sharePercentage > 0, "Share percentage must be greater than zero");
        require(totalSharePercentage + _sharePercentage <= 100, "Total share percentage exceeds 100");

        participants.push(Participant({
            walletAddress: _walletAddress,
            sharePercentage: _sharePercentage
        }));

        totalSharePercentage += _sharePercentage;
    }

    /**
     * @dev Removes all participants. Can only be called by the contract owner.
     */
    function resetParticipants() external onlyOwner {
        delete participants;
        totalSharePercentage = 0;
    }

    /**
     * @dev Distributes the rewards earned via the Moxie Protocol based on participant shares.
     */
    function distributeRewards() external {
        // Ensure participants are configured correctly
        require(participants.length > 0, "No participants to distribute rewards to");
        require(totalSharePercentage == 100, "Total share percentage must equal 100");

        // Interact with the Moxie Protocol to claim rewards
        IMoxieProtocol moxieProtocol = IMoxieProtocol(moxieProtocolAddress);
        uint256 totalRewards = moxieProtocol.claimRewards(address(this));
        require(totalRewards > 0, "No rewards available for distribution");

        // Distribute rewards among participants
        for (uint256 i = 0; i < participants.length; i++) {
            Participant memory participant = participants[i];
            uint256 payoutAmount = (totalRewards * participant.sharePercentage) / 100;

            // Transfer payout to the participant
            (bool success,) = participant.walletAddress.call{value: payoutAmount}("");
            require(success, "Failed to transfer payout");

            emit PayoutDistributed(participant.walletAddress, payoutAmount);
        }
    }

    /**
     * @dev Allows the owner to update the Moxie Protocol address in case of contract migration.
     * @param _newMoxieProtocolAddress New address of the Moxie Protocol contract.
     */
    function updateMoxieProtocolAddress(address _newMoxieProtocolAddress) external onlyOwner {
        require(_newMoxieProtocolAddress != address(0), "Invalid Moxie Protocol address");
        moxieProtocolAddress = _newMoxieProtocolAddress;
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {}

    /**
     * @dev Function to withdraw any leftover Ether in the contract.
     * @param _recipient Address where the leftover Ether should be sent.
     */
    function withdrawEther(address _recipient) external onlyOwner {
        require(_recipient != address(0), "Invalid recipient address");
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No Ether to withdraw");

        (bool success,) = _recipient.call{value: contractBalance}("");
        require(success, "Failed to withdraw Ether");
    }
}
```
