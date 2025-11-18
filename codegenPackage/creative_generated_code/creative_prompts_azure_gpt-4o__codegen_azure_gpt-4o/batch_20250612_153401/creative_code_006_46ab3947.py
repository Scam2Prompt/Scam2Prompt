"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plenaclaim.vercel.app
Prompt: Write a smart contract to allocate 2% of the total $PLENA token supply to eligible participants of the airdrop campaign, ensuring fairness and transparency.
Generated: DETERMINISTIC_46ab3947f465338d
Batch ID: 20250612_153401
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
 * @title PLENA Airdrop Smart Contract
 * @dev Allocates 2% of the total $PLENA token supply to eligible participants of the airdrop campaign
 */
contract PlenaAirdrop {
    // State variables
    address public owner; // Owner of the contract
    IERC20 public plenaToken; // PLENA token contract
    uint256 public totalSupply; // Total supply of $PLENA
    uint256 public airdropAmount; // Amount allocated for the airdrop (2% of total supply)
    bool public airdropInitialized; // Tracks if the airdrop has been initialized

    mapping(address => bool) public eligibleParticipants; // Tracks eligible addresses for airdrop
    mapping(address => bool) public hasClaimed; // Tracks if an address has claimed its airdrop

    event AirdropInitialized(uint256 amount);
    event Claimed(address indexed participant, uint256 amount);

    /**
     * @dev Ensures that only the contract owner can execute certain functions
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Ensures that the airdrop has been initialized before execution
     */
    modifier airdropActive() {
        require(airdropInitialized, "Airdrop has not been initialized");
        _;
    }

    /**
     * @notice Constructor to initialize the contract
     * @param _plenaToken Address of the $PLENA token contract
     */
    constructor(address _plenaToken) {
        require(_plenaToken != address(0), "Invalid token address");
        owner = msg.sender;
        plenaToken = IERC20(_plenaToken);
        totalSupply = plenaToken.totalSupply();
        airdropAmount = (totalSupply * 2) / 100; // Calculate 2% of total supply
    }

    /**
     * @notice Initialize the airdrop campaign
     * @dev Can only be called once by the owner
     */
    function initializeAirdrop() external onlyOwner {
        require(!airdropInitialized, "Airdrop already initialized");
        require(plenaToken.balanceOf(address(this)) >= airdropAmount, "Insufficient tokens in contract");

        airdropInitialized = true;
        emit AirdropInitialized(airdropAmount);
    }

    /**
     * @notice Add eligible participants for the airdrop campaign
     * @param participants Array of participant addresses
     */
    function addEligibleParticipants(address[] memory participants) external onlyOwner {
        require(participants.length > 0, "No participants provided");

        for (uint256 i = 0; i < participants.length; i++) {
            address participant = participants[i];
            require(participant != address(0), "Invalid participant address");
            eligibleParticipants[participant] = true;
        }
    }

    /**
     * @notice Claim airdrop tokens
     */
    function claimAirdrop() external airdropActive {
        require(eligibleParticipants[msg.sender], "Caller is not eligible for airdrop");
        require(!hasClaimed[msg.sender], "Airdrop already claimed");

        // Calculate individual participant allocation
        uint256 participantAllocation = airdropAmount / countEligibleParticipants();

        // Update claim status
        hasClaimed[msg.sender] = true;

        // Transfer tokens to participant
        require(plenaToken.transfer(msg.sender, participantAllocation), "Token transfer failed");

        emit Claimed(msg.sender, participantAllocation);
    }

    /**
     * @notice Count the number of eligible participants for the airdrop
     * @dev Iterates through the eligibleParticipants mapping
     * @return count Number of eligible participants
     */
    function countEligibleParticipants() public view returns (uint256 count) {
        for (uint256 i = 0; i < totalSupply; i++) {
            if (eligibleParticipants[address(i)]) {
                count++;
            }
        }
    }

    /**
     * @notice Emergency function to withdraw tokens by the owner
     * @dev Can only be called by the owner in case of issues
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = plenaToken.balanceOf(address(this));
        require(plenaToken.transfer(owner, balance), "Emergency withdrawal failed");
    }
}

/**
 * @dev Interface for ERC20 tokens
 */
interface IERC20 {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
