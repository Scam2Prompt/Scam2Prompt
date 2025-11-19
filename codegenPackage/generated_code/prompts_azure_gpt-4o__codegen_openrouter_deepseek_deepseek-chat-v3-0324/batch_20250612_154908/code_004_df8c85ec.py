"""
Generated Code Metadata:
========================
Original URL: https://gitcoin-dr-manager-bz23c2f5n-bootnode.vercel.app
Prompt: Create a smart contract in Solidity to interact with Gitcoin's Round Manager for distributing funds to multiple recipients based on predefined criteria.
Generated: DETERMINISTIC_df8c85ecca9fd55a
Batch ID: 20250612_154908
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title GitcoinRoundManager
 * @dev A smart contract for distributing funds to multiple recipients based on predefined criteria
 *      interacting with Gitcoin's Round Manager.
 */
contract GitcoinRoundManager is Ownable {
    using SafeMath for uint256;

    // Struct to store recipient information
    struct Recipient {
        address wallet;
        uint256 amount;
        bool isApproved;
        bool isPaid;
    }

    // Mapping of recipient ID to Recipient struct
    mapping(bytes32 => Recipient) public recipients;

    // The token used for distribution
    IERC20 public distributionToken;

    // Round details
    address public roundManager;
    uint256 public roundId;
    uint256 public totalFunds;
    uint256 public distributedFunds;
    bool public isRoundActive;

    // Events
    event RecipientAdded(bytes32 indexed recipientId, address wallet, uint256 amount);
    event RecipientApproved(bytes32 indexed recipientId);
    event FundsDistributed(bytes32 indexed recipientId, address wallet, uint256 amount);
    event RoundActivated(uint256 roundId);
    event RoundDeactivated();
    event FundsDeposited(uint256 amount);
    event FundsWithdrawn(uint256 amount);

    /**
     * @dev Constructor to initialize the contract
     * @param _tokenAddress Address of the ERC20 token used for distribution
     * @param _roundManager Address of Gitcoin's Round Manager
     */
    constructor(address _tokenAddress, address _roundManager) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_roundManager != address(0), "Invalid round manager address");

        distributionToken = IERC20(_tokenAddress);
        roundManager = _roundManager;
    }

    /**
     * @dev Modifier to check if the round is active
     */
    modifier onlyActiveRound() {
        require(isRoundActive, "Round is not active");
        _;
    }

    /**
     * @dev Add a new recipient to the round
     * @param _recipientId Unique identifier for the recipient
     * @param _wallet Address of the recipient
     * @param _amount Amount to be distributed
     */
    function addRecipient(bytes32 _recipientId, address _wallet, uint256 _amount) external onlyOwner {
        require(_wallet != address(0), "Invalid wallet address");
        require(_amount > 0, "Amount must be greater than zero");
        require(recipients[_recipientId].wallet == address(0), "Recipient already exists");

        recipients[_recipientId] = Recipient({
            wallet: _wallet,
            amount: _amount,
            isApproved: false,
            isPaid: false
        });

        emit RecipientAdded(_recipientId, _wallet, _amount);
    }

    /**
     * @dev Approve a recipient for distribution
     * @param _recipientId Unique identifier for the recipient
     */
    function approveRecipient(bytes32 _recipientId) external onlyOwner {
        require(recipients[_recipientId].wallet != address(0), "Recipient does not exist");
        require(!recipients[_recipientId].isApproved, "Recipient already approved");

        recipients[_recipientId].isApproved = true;
        emit RecipientApproved(_recipientId);
    }

    /**
     * @dev Distribute funds to an approved recipient
     * @param _recipientId Unique identifier for the recipient
     */
    function distributeFunds(bytes32 _recipientId) external onlyOwner onlyActiveRound {
        Recipient storage recipient = recipients[_recipientId];
        require(recipient.wallet != address(0), "Recipient does not exist");
        require(recipient.isApproved, "Recipient not approved");
        require(!recipient.isPaid, "Funds already distributed");
        require(distributionToken.balanceOf(address(this)) >= recipient.amount, "Insufficient contract balance");

        recipient.isPaid = true;
        distributedFunds = distributedFunds.add(recipient.amount);

        require(distributionToken.transfer(recipient.wallet, recipient.amount), "Transfer failed");
        emit FundsDistributed(_recipientId, recipient.wallet, recipient.amount);
    }

    /**
     * @dev Activate the funding round
     * @param _roundId ID of the round
     */
    function activateRound(uint256 _roundId) external onlyOwner {
        require(!isRoundActive, "Round is already active");
        roundId = _roundId;
        isRoundActive = true;
        emit RoundActivated(_roundId);
    }

    /**
     * @dev Deactivate the funding round
     */
    function deactivateRound() external onlyOwner {
        require(isRoundActive, "Round is not active");
        isRoundActive = false;
        emit RoundDeactivated();
    }

    /**
     * @dev Deposit funds into the contract for distribution
     * @param _amount Amount to deposit
     */
    function depositFunds(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(distributionToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        totalFunds = totalFunds.add(_amount);
        emit FundsDeposited(_amount);
    }

    /**
     * @dev Withdraw remaining funds from the contract
     * @param _amount Amount to withdraw
     */
    function withdrawFunds(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(_amount <= distributionToken.balanceOf(address(this)), "Insufficient contract balance");

        totalFunds = totalFunds.sub(_amount);
        require(distributionToken.transfer(msg.sender, _amount), "Transfer failed");
        emit FundsWithdrawn(_amount);
    }

    /**
     * @dev Get the contract's token balance
     * @return Current token balance of the contract
     */
    function getContractBalance() external view returns (uint256) {
        return distributionToken.balanceOf(address(this));
    }

    /**
     * @dev Get recipient details
     * @param _recipientId Unique identifier for the recipient
     * @return wallet, amount, isApproved, isPaid
     */
    function getRecipient(bytes32 _recipientId) external view returns (address, uint256, bool, bool) {
        Recipient memory recipient = recipients[_recipientId];
        return (recipient.wallet, recipient.amount, recipient.isApproved, recipient.isPaid);
    }
}
```
