"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-ai.pages.dev
Prompt: Develop a presale token distribution system in Solidity for a platform like Pushd, ensuring tokens are airdropped to users at the conclusion of the presale without requiring additional fees.
Generated: DETERMINISTIC_436f15e9dbf012a7
Batch ID: 20250612_152249
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
 * @title PresaleTokenDistributor
 * @dev A contract to manage presale token distribution and automated airdrops post presale.
 */
contract PresaleTokenDistributor {
    // Token interface
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // Token being distributed
    IERC20 public immutable token;

    // Address of the owner (contract administrator)
    address public owner;

    // Presale participants and their allocated token amounts
    mapping(address => uint256) public allocations;

    // Presale status
    bool public presaleActive;

    /**
     * @dev Modifier to restrict function access to the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Modifier to ensure presale is active.
     */
    modifier presaleIsActive() {
        require(presaleActive, "Presale is not active");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _token Address of the token to be distributed.
     */
    constructor(address _token) {
        require(_token != address(0), "Token address cannot be zero");
        token = IERC20(_token);
        owner = msg.sender;
        presaleActive = true;
    }

    /**
     * @dev Function to allocate tokens to a participant during presale.
     * @param participant Address of the participant.
     * @param amount Amount of tokens allocated.
     */
    function allocateTokens(address participant, uint256 amount) external onlyOwner presaleIsActive {
        require(participant != address(0), "Invalid participant address");
        require(amount > 0, "Allocation amount must be greater than zero");

        allocations[participant] += amount;
    }

    /**
     * @dev Function to deactivate the presale.
     */
    function endPresale() external onlyOwner {
        presaleActive = false;
    }

    /**
     * @dev Function to airdrop tokens to all participants post presale.
     * @param participants Array of participant addresses.
     */
    function airdropTokens(address[] calldata participants) external onlyOwner {
        require(!presaleActive, "Presale must be ended before airdrop");
        require(participants.length > 0, "Participants array cannot be empty");

        for (uint256 i = 0; i < participants.length; i++) {
            address participant = participants[i];
            uint256 amount = allocations[participant];

            if (amount > 0) {
                allocations[participant] = 0; // Reset allocation
                require(token.transfer(participant, amount), "Token transfer failed");
            }
        }
    }

    /**
     * @dev Function to withdraw any leftover tokens in the contract (post airdrop).
     * @param recipient Address to receive the leftover tokens.
     */
    function withdrawRemainingTokens(address recipient) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");

        uint256 remainingBalance = token.balanceOf(address(this));
        require(remainingBalance > 0, "No tokens to withdraw");

        require(token.transfer(recipient, remainingBalance), "Token transfer failed");
    }
}
```
