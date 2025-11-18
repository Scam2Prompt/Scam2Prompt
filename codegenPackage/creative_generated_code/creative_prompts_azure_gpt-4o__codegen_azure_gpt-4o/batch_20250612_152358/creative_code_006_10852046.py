"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeihj3zbaoidqg3cnaolz6v7im45zqz4q7wuxzepq5xid72xeotioua.ipfs.dweb.link
Prompt: Develop a smart contract that interacts with Layer3's treasury pool allocation system to distribute $L3 tokens based on predefined criteria.
Generated: DETERMINISTIC_10852046d88f754e
Batch ID: 20250612_152358
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
 * @title Layer3TokenDistributor
 * @dev Smart contract to distribute $L3 tokens based on predefined criteria.
 */
contract Layer3TokenDistributor {
    // Address of the Layer3 Treasury Pool
    address public treasuryPool;

    // Address of the $L3 token contract
    IERC20 public l3Token;

    // Owner of the contract
    address public owner;

    // Event emitted when tokens are distributed
    event TokensDistributed(address indexed recipient, uint256 amount);

    // Mapping to store predefined criteria (e.g., eligibility of recipients and distribution amounts)
    mapping(address => uint256) public allocationCriteria;

    /**
     * @dev Modifier to restrict function access to the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to set the initial state of the contract.
     * @param _treasuryPool Address of the Layer3 Treasury Pool.
     * @param _l3Token Address of the $L3 token contract.
     */
    constructor(address _treasuryPool, address _l3Token) {
        require(_treasuryPool != address(0), "Invalid treasury pool address");
        require(_l3Token != address(0), "Invalid token address");

        treasuryPool = _treasuryPool;
        l3Token = IERC20(_l3Token);
        owner = msg.sender;
    }

    /**
     * @dev Function to set allocation criteria for recipients.
     * @param recipients Array of recipient addresses.
     * @param amounts Array of token amounts.
     */
    function setAllocationCriteria(address[] calldata recipients, uint256[] calldata amounts)
        external
        onlyOwner
    {
        require(recipients.length == amounts.length, "Mismatched array lengths");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Invalid recipient address");
            require(amounts[i] > 0, "Invalid allocation amount");

            allocationCriteria[recipients[i]] = amounts[i];
        }
    }

    /**
     * @dev Function to distribute tokens based on predefined criteria.
     *      This function pulls tokens from the treasury pool and distributes them to recipients.
     */
    function distributeTokens() external onlyOwner {
        for (uint256 i = 0; i < recipients.length; i++) {
            address recipient = recipients[i];
            uint256 amount = allocationCriteria[recipient];

            require(amount > 0, "No allocation for this recipient");

            // Transfer tokens from the treasury pool to the recipient
            require(
                l3Token.transferFrom(treasuryPool, recipient, amount),
                "Token transfer failed"
            );

            // Emit event for successful distribution
            emit TokensDistributed(recipient, amount);

            // Reset allocation for the recipient to avoid duplicate distributions
            allocationCriteria[recipient] = 0;
        }
    }

    /**
     * @dev Function to withdraw any tokens accidentally sent to this contract.
     * @param tokenAddress Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        require(amount > 0, "Invalid withdrawal amount");

        IERC20 token = IERC20(tokenAddress);
        require(token.transfer(owner, amount), "Token withdrawal failed");
    }

    /**
     * @dev Function to transfer ownership of the contract to a new owner.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        owner = newOwner;
    }
}

/**
 * @dev Interface for ERC20 token interactions.
 */
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
