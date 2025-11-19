"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoindogsclub-en.pages.dev
Prompt: Develop a smart contract for the $0DOG token that includes features for claiming tokens after the presale ends.
Generated: DETERMINISTIC_94795b2de18db24b
Batch ID: 20250612_161617
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

// Importing the OpenZeppelin ERC20 contract for token standards
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/// @title $0DOG Token Contract
/// @notice This contract implements the $0DOG token with presale claiming functionality
contract DogToken is ERC20, Ownable {
    using SafeMath for uint256;

    // State variables
    uint256 public presaleEndTime; // Timestamp indicating the end of the presale
    mapping(address => uint256) private _claims; // Tracks claims for each address
    bool public presaleEnded; // Indicates if the presale has ended

    /// @notice Event emitted when tokens are claimed
    event TokensClaimed(address indexed claimant, uint256 amount);

    /// @param _name The name of the token
    /// @param _symbol The symbol of the token
    /// @param _initialSupply The initial supply of tokens to be minted
    constructor(string memory _name, string memory _symbol, uint256 _initialSupply) 
        ERC20(_name, _symbol) 
    {
        // Mint the initial supply to the contract owner
        _mint(msg.sender, _initialSupply * (10 ** decimals()));
    }

    /// @notice Starts the presale by defining the end time
    /// @param duration Duration of the presale in seconds
    function startPresale(uint256 duration) external onlyOwner {
        require(!presaleEnded, "Presale has already ended");
        presaleEndTime = block.timestamp.add(duration);
    }

    /// @notice Ends the presale
    function endPresale() external onlyOwner {
        require(!presaleEnded, "Presale has already ended");
        require(block.timestamp >= presaleEndTime, "Presale can't be ended before the end time");

        presaleEnded = true;
    }

    /// @notice Allows users to claim their tokens after the presale has ended
    function claimTokens() external {
        require(presaleEnded, "Presale has not ended yet");
        require(_claims[msg.sender] > 0, "No tokens to claim");

        uint256 amount = _claims[msg.sender];
        _claims[msg.sender] = 0;

        // Transfer the tokens to the claimant
        _transfer(address(this), msg.sender, amount);
        emit TokensClaimed(msg.sender, amount);
    }

    /// @notice Allows the owner to set claimable tokens for a user
    /// @param claimant The address of the user claiming tokens
    /// @param amount The amount of tokens that can be claimed
    function setClaimableTokens(address claimant, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        _claims[claimant] = amount;
    }

    /// @notice Returns the claimable tokens for a user
    /// @param claimant The address of the user
    /// @return The amount of claimable tokens
    function claimableTokens(address claimant) external view returns (uint256) {
        return _claims[claimant];
    }
}
```
