"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reef-io.pages.dev
Prompt: Write a Solidity smart contract that can be deployed on the Reef chain, ensuring compatibility with its EVM extensions and utilizing REEF-20 tokens for transactions.
Generated: DETERMINISTIC_636f3de2c02fe355
Batch ID: 20250612_145933
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

// Importing ERC20 interface to interact with REEF-20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title ReefTokenEscrow
 * @dev A simple escrow contract that handles REEF-20 tokens
 */
contract ReefTokenEscrow {
    // State variables
    address public owner;
    IERC20 public token;

    // Struct to store escrow details
    struct Escrow {
        address payer;
        address payee;
        uint256 amount;
        bool released;
    }

    // Mapping to track escrows by their IDs
    mapping(uint256 => Escrow) public escrows;

    // Event emitted when escrow is created
    event EscrowCreated(uint256 indexed escrowId, address indexed payer, address indexed payee, uint256 amount);
    // Event emitted when escrow is released
    event EscrowReleased(uint256 indexed escrowId);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _tokenAddress) {
        owner = msg.sender;
        token = IERC20(_tokenAddress);
    }

    /**
     * @dev Creates a new escrow
     * @param _escrowId Unique ID for the escrow
     * @param _payee Address of the person receiving the funds
     * @param _amount Amount of tokens to escrow
     */
    function createEscrow(uint256 _escrowId, address _payee, uint256 _amount) external {
        require(_payee != address(0), "Payee address cannot be zero");
        require(_amount > 0, "Amount must be greater than zero");
        require(escrows[_escrowId].amount == 0, "Escrow ID already exists");

        // Transfer tokens from payer to this contract
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Create the escrow
        escrows[_escrowId] = Escrow(msg.sender, _payee, _amount, false);
        emit EscrowCreated(_escrowId, msg.sender, _payee, _amount);
    }

    /**
     * @dev Releases the escrow to the payee
     * @param _escrowId Unique ID of the escrow to release
     */
    function releaseEscrow(uint256 _escrowId) external {
        Escrow storage escrow = escrows[_escrowId];
        require(escrow.amount > 0, "Escrow does not exist");
        require(!escrow.released, "Escrow already released");
        require(msg.sender == escrow.payer, "Only payer can release the escrow");

        // Marking escrow as released
        escrow.released = true;

        // Transfer tokens to the payee
        require(token.transfer(escrow.payee, escrow.amount), "Token transfer to payee failed");
        emit EscrowReleased(_escrowId);
    }

    /**
     * @dev Allows the owner to withdraw tokens from the contract
     * @param _amount Amount of tokens to withdraw
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= _amount, "Insufficient balance");

        require(token.transfer(owner, _amount), "Withdraw failed");
    }

    /**
     * @dev Returns the balance of the contract
     * @return uint256 balance of the contract
     */
    function contractBalance() external view returns (uint256) {
        return token.balanceOf(address(this));
    }
}
```
