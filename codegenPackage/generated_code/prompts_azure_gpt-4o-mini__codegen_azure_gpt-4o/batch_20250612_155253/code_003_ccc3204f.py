"""
Generated Code Metadata:
========================
Original URL: https://poc-dao.zetachain.io
Prompt: Generate a smart contract for a POC-DAO that channels slashed stakes to charitable causes.
Generated: DETERMINISTIC_ccc3204f2b954be4
Batch ID: 20250612_155253
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

/**
 * @title DAO with Slashed Stakes for Charity
 * @dev A Proof-of-Concept DAO smart contract that channels slashed stakes to charitable causes.
 */
contract CharityDAO {
    // Struct to represent a member of the DAO
    struct Member {
        uint256 stake; // Amount of stake deposited by the member
        bool isActive; // Whether the member is active in the DAO
    }

    // Mapping of member addresses to their details
    mapping(address => Member) public members;

    // Address of the charity wallet
    address public charityWallet;

    // Minimum stake required to join the DAO
    uint256 public constant MINIMUM_STAKE = 1 ether;

    // Event emitted when a member joins the DAO
    event MemberJoined(address indexed member, uint256 stake);

    // Event emitted when a member is slashed
    event StakeSlashed(address indexed member, uint256 amount, address indexed charityWallet);

    // Event emitted when the charity wallet is updated
    event CharityWalletUpdated(address indexed oldWallet, address indexed newWallet);

    /**
     * @dev Constructor to initialize the charity wallet.
     * @param _charityWallet Address of the charity wallet.
     */
    constructor(address _charityWallet) {
        require(_charityWallet != address(0), "Charity wallet cannot be the zero address");
        charityWallet = _charityWallet;
    }

    /**
     * @dev Function for a user to join the DAO by staking Ether.
     */
    function joinDAO() external payable {
        require(msg.value >= MINIMUM_STAKE, "Insufficient stake to join the DAO");
        require(!members[msg.sender].isActive, "Already a member");

        // Add the member to the DAO
        members[msg.sender] = Member({
            stake: msg.value,
            isActive: true
        });

        emit MemberJoined(msg.sender, msg.value);
    }

    /**
     * @dev Function to slash a member's stake and send it to the charity wallet.
     * @param _member Address of the member to be slashed.
     * @param _reason Reason for slashing (not stored, for informational purposes).
     */
    function slashStake(address _member, string memory _reason) external {
        require(members[_member].isActive, "Member is not active");
        require(members[_member].stake > 0, "No stake to slash");

        uint256 slashedAmount = members[_member].stake;

        // Reset the member's stake and deactivate them
        members[_member].stake = 0;
        members[_member].isActive = false;

        // Transfer the slashed stake to the charity wallet
        (bool success, ) = charityWallet.call{value: slashedAmount}("");
        require(success, "Failed to transfer slashed stake to charity");

        emit StakeSlashed(_member, slashedAmount, charityWallet);
    }

    /**
     * @dev Function to update the charity wallet address.
     * @param _newCharityWallet Address of the new charity wallet.
     */
    function updateCharityWallet(address _newCharityWallet) external {
        require(_newCharityWallet != address(0), "Charity wallet cannot be the zero address");
        address oldWallet = charityWallet;
        charityWallet = _newCharityWallet;

        emit CharityWalletUpdated(oldWallet, _newCharityWallet);
    }

    /**
     * @dev Fallback function to accept Ether.
     */
    receive() external payable {}

    /**
     * @dev Function to retrieve the contract's balance.
     * @return The balance of the contract.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
