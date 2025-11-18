"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raffle-front-beige.vercel.app
Prompt: Develop a smart contract in Solidity that supports raffles with SOL and USDC as entry tokens.
Generated: DETERMINISTIC_2b77512046eeb911
Batch ID: 20250612_153648
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
 * @title Raffle Smart Contract
 * @dev This contract allows users to enter a raffle using SOL or USDC as entry tokens.
 */
contract Raffle {
    // Address of the contract owner
    address public owner;

    // Accepted ERC20 token (USDC) address
    address public usdcToken;

    // Raffle entry fee (in wei for SOL, and in smallest USDC units for USDC)
    uint256 public entryFeeSOL;
    uint256 public entryFeeUSDC;

    // Array to hold participants
    address[] public participants;

    // Mapping to track participants' payment method
    mapping(address => bool) public isPaidWithSOL;

    // Events
    event RaffleEntered(address indexed participant, bool paidWithSOL);
    event WinnerSelected(address indexed winner);

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize contract owner, USDC token address, and entry fees.
     * @param _usdcToken Address of the USDC token contract.
     * @param _entryFeeSOL Entry fee in wei for SOL.
     * @param _entryFeeUSDC Entry fee in smallest USDC units.
     */
    constructor(address _usdcToken, uint256 _entryFeeSOL, uint256 _entryFeeUSDC) {
        require(_usdcToken != address(0), "Invalid USDC token address");
        owner = msg.sender;
        usdcToken = _usdcToken;
        entryFeeSOL = _entryFeeSOL;
        entryFeeUSDC = _entryFeeUSDC;
    }

    /**
     * @dev Function to enter the raffle by paying with SOL.
     * Requires the exact entry fee to be sent along with the transaction.
     */
    function enterWithSOL() external payable {
        require(msg.value == entryFeeSOL, "Incorrect SOL entry fee");

        // Add the participant to the list
        participants.push(msg.sender);
        isPaidWithSOL[msg.sender] = true;

        emit RaffleEntered(msg.sender, true);
    }

    /**
     * @dev Function to enter the raffle by paying with USDC.
     * USDC tokens must be approved for transfer before calling this function.
     */
    function enterWithUSDC() external {
        require(entryFeeUSDC > 0, "USDC entry fee not set");

        // Transfer USDC tokens from the participant to the contract
        bool success = IERC20(usdcToken).transferFrom(msg.sender, address(this), entryFeeUSDC);
        require(success, "USDC transfer failed");

        // Add the participant to the list
        participants.push(msg.sender);
        isPaidWithSOL[msg.sender] = false;

        emit RaffleEntered(msg.sender, false);
    }

    /**
     * @dev Function to select a random winner from the participants.
     * Can only be called by the contract owner.
     */
    function selectWinner() external onlyOwner {
        require(participants.length > 0, "No participants in the raffle");

        // Generate a random index
        uint256 randomIndex = uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty, participants))) % participants.length;

        // Select the winner
        address winner = participants[randomIndex];

        // Clear participants for the next raffle
        delete participants;

        emit WinnerSelected(winner);
    }

    /**
     * @dev Function to withdraw the contract's SOL balance.
     * Can only be called by the contract owner.
     */
    function withdrawSOL() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No SOL balance to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "SOL withdrawal failed");
    }

    /**
     * @dev Function to withdraw the contract's USDC balance.
     * Can only be called by the contract owner.
     */
    function withdrawUSDC() external onlyOwner {
        uint256 balance = IERC20(usdcToken).balanceOf(address(this));
        require(balance > 0, "No USDC balance to withdraw");

        bool success = IERC20(usdcToken).transfer(owner, balance);
        require(success, "USDC withdrawal failed");
    }

    /**
     * @dev Interface for interacting with ERC20 tokens.
     */
    interface IERC20 {
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }
}
```
