"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://richpepe.vercel.app
Prompt: Create a Solidity contract for a lottery system tied to a meme-based cryptocurrency token, referencing the "Rich Pepe" special meme lottery concept.
Generated: DETERMINISTIC_0906640f2cb9e6eb
Batch ID: 20250612_153420
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

/**
 * @title Rich Pepe Meme Lottery
 * @dev A lottery system tied to a meme-based cryptocurrency token.
 * Participants use the 'Rich Pepe' token to enter the lottery, and winners are drawn periodically.
 */
contract RichPepeLottery {
    // Owner of the contract
    address public owner;

    // Token interface for Rich Pepe cryptocurrency
    IERC20 public richPepeToken;

    // Entry fee for the lottery (in Rich Pepe tokens)
    uint256 public entryFee;

    // Array of participants
    address[] public participants;

    // Event to notify when a participant enters the lottery
    event LotteryEntered(address indexed participant);

    // Event to notify when a winner is drawn
    event WinnerDrawn(address indexed winner, uint256 prizeAmount);

    /**
     * @dev Modifier to ensure only the owner can call specific functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the Rich Pepe token address and entry fee.
     * @param _richPepeTokenAddress Address of the Rich Pepe token contract.
     * @param _entryFee Amount of Rich Pepe tokens required to enter the lottery.
     */
    constructor(address _richPepeTokenAddress, uint256 _entryFee) {
        require(_richPepeTokenAddress != address(0), "Invalid token address");
        require(_entryFee > 0, "Entry fee must be greater than zero");

        owner = msg.sender;
        richPepeToken = IERC20(_richPepeTokenAddress);
        entryFee = _entryFee;
    }

    /**
     * @dev Function to enter the lottery by transferring the entry fee in Rich Pepe tokens.
     */
    function enterLottery() external {
        // Check if the sender has enough tokens
        require(
            richPepeToken.balanceOf(msg.sender) >= entryFee,
            "Insufficient Rich Pepe tokens for entry"
        );

        // Transfer Rich Pepe tokens to the contract
        require(
            richPepeToken.transferFrom(msg.sender, address(this), entryFee),
            "Token transfer failed"
        );

        // Add the participant to the list
        participants.push(msg.sender);

        // Emit the event
        emit LotteryEntered(msg.sender);
    }

    /**
     * @dev Function to draw the winner randomly. Can only be called by the contract owner.
     */
    function drawWinner() external onlyOwner {
        require(participants.length > 0, "No participants in the lottery");

        // Generate a pseudo-random index based on block properties
        uint256 winnerIndex = uint256(
            keccak256(
                abi.encodePacked(
                    block.timestamp,
                    block.difficulty,
                    participants.length
                )
            )
        ) % participants.length;

        // Get the winner's address
        address winner = participants[winnerIndex];

        // Calculate the prize amount (entire contract balance)
        uint256 prizeAmount = richPepeToken.balanceOf(address(this));

        // Transfer the prize to the winner
        require(
            richPepeToken.transfer(winner, prizeAmount),
            "Prize transfer failed"
        );

        // Emit the event
        emit WinnerDrawn(winner, prizeAmount);

        // Reset the participants list
        delete participants;
    }

    /**
     * @dev Function to update the entry fee. Can only be called by the contract owner.
     * @param _newEntryFee New entry fee for the lottery.
     */
    function updateEntryFee(uint256 _newEntryFee) external onlyOwner {
        require(_newEntryFee > 0, "Entry fee must be greater than zero");
        entryFee = _newEntryFee;
    }

    /**
     * @dev Function to withdraw any accidentally sent Ether. Can only be called by the contract owner.
     */
    function withdrawEther() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        payable(owner).transfer(balance);
    }

    /**
     * @dev Function to check the current list of participants in the lottery.
     * @return An array of addresses of participants.
     */
    function getParticipants() external view returns (address[] memory) {
        return participants;
    }
}

/**
 * @dev Interface for ERC20 token interactions.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
