"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-claim.pages.dev
Prompt: Generate code for an airdrop system that distributes tokens to presale participants at the conclusion of the presale, ensuring no fees are required for claiming tokens.
Generated: DETERMINISTIC_169e68d0c3e666aa
Batch ID: 20250612_145923
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
 * @title AirdropSystem
 * @dev This contract handles the distribution of tokens to presale participants after the presale concludes.
 *      Participants can claim their tokens without any fees.
 */
contract AirdropSystem {
    // ERC20 token interface
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    address public owner; // Contract owner
    IERC20 public token; // ERC20 token to be airdropped
    bool public presaleEnded; // Tracks if the presale has ended
    mapping(address => uint256) public allocations; // Stores allocations for participants

    event TokensClaimed(address indexed participant, uint256 amount);
    event AllocationsSet(address indexed participant, uint256 amount);
    event PresaleEnded();
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier presaleMustBeEnded() {
        require(presaleEnded, "Presale has not ended yet");
        _;
    }

    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        owner = msg.sender; // Set the contract deployer as the owner
        token = IERC20(_tokenAddress); // Set the token address
    }

    /**
     * @dev Allows the owner to set token allocations for presale participants.
     * @param participants List of participant addresses.
     * @param amounts List of token amounts corresponding to each participant.
     */
    function setAllocations(address[] calldata participants, uint256[] calldata amounts) external onlyOwner {
        require(participants.length == amounts.length, "Participants and amounts length mismatch");

        for (uint256 i = 0; i < participants.length; i++) {
            require(participants[i] != address(0), "Invalid participant address");
            allocations[participants[i]] = amounts[i];
            emit AllocationsSet(participants[i], amounts[i]);
        }
    }

    /**
     * @dev Ends the presale. Tokens can be claimed only after this is called.
     */
    function endPresale() external onlyOwner {
        presaleEnded = true;
        emit PresaleEnded();
    }

    /**
     * @dev Allows presale participants to claim their allocated tokens after the presale ends.
     */
    function claimTokens() external presaleMustBeEnded {
        uint256 amount = allocations[msg.sender];
        require(amount > 0, "No tokens allocated or already claimed");
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract token balance");

        allocations[msg.sender] = 0; // Prevent re-entrancy
        require(token.transfer(msg.sender, amount), "Token transfer failed");

        emit TokensClaimed(msg.sender, amount);
    }

    /**
     * @dev Transfers ownership of the contract to a new address.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner is the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Allows the owner to withdraw any remaining tokens in the contract after the presale ends.
     */
    function withdrawRemainingTokens() external onlyOwner presaleMustBeEnded {
        uint256 remainingBalance = token.balanceOf(address(this));
        require(remainingBalance > 0, "No tokens left in the contract");
        require(token.transfer(owner, remainingBalance), "Token transfer failed");
    }

    // Fallback function to prevent accidental Ether transfers
    fallback() external {
        revert("Ether transfers not allowed");
    }

    receive() external payable {
        revert("Ether transfers not allowed");
    }
}
```
