"""
Generated Code Metadata:
========================
Original URL: https://iqratechpoint.pages.dev
Prompt: Generate a sample smart contract for managing scholarships and grants using IQRA Token on the Binance Smart Chain.
Generated: DETERMINISTIC_1bc5bb618d3296a1
Batch ID: 20250612_163659
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
 * @title ScholarshipAndGrantManager
 * @dev A smart contract for managing scholarships and grants using IQRA Token on Binance Smart Chain.
 */
contract ScholarshipAndGrantManager {
    // Address of the IQRA Token contract
    address public iqraTokenAddress;

    // Owner of the contract
    address public owner;

    // Struct to represent a scholarship or grant
    struct ScholarshipOrGrant {
        uint256 id;
        string name;
        uint256 amount;
        address recipient;
        bool isClaimed;
    }

    // Mapping to store scholarships and grants by ID
    mapping(uint256 => ScholarshipOrGrant) public scholarshipsAndGrants;

    // Counter for scholarship and grant IDs
    uint256 public nextId;

    // Events
    event ScholarshipOrGrantCreated(uint256 id, string name, uint256 amount, address recipient);
    event ScholarshipOrGrantClaimed(uint256 id, address recipient);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _iqraTokenAddress Address of the IQRA Token contract.
     */
    constructor(address _iqraTokenAddress) {
        require(_iqraTokenAddress != address(0), "Invalid IQRA Token address");
        iqraTokenAddress = _iqraTokenAddress;
        owner = msg.sender;
    }

    /**
     * @dev Function to create a new scholarship or grant.
     * @param _name Name of the scholarship or grant.
     * @param _amount Amount of IQRA Tokens to allocate.
     * @param _recipient Address of the recipient.
     */
    function createScholarshipOrGrant(
        string memory _name,
        uint256 _amount,
        address _recipient
    ) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(_recipient != address(0), "Invalid recipient address");

        scholarshipsAndGrants[nextId] = ScholarshipOrGrant({
            id: nextId,
            name: _name,
            amount: _amount,
            recipient: _recipient,
            isClaimed: false
        });

        emit ScholarshipOrGrantCreated(nextId, _name, _amount, _recipient);
        nextId++;
    }

    /**
     * @dev Function to claim a scholarship or grant.
     * @param _id ID of the scholarship or grant to claim.
     */
    function claimScholarshipOrGrant(uint256 _id) external {
        ScholarshipOrGrant storage scholarshipOrGrant = scholarshipsAndGrants[_id];

        require(scholarshipOrGrant.id == _id, "Scholarship or grant does not exist");
        require(scholarshipOrGrant.recipient == msg.sender, "You are not the recipient");
        require(!scholarshipOrGrant.isClaimed, "Scholarship or grant already claimed");

        scholarshipOrGrant.isClaimed = true;

        // Transfer IQRA Tokens to the recipient
        require(
            IERC20(iqraTokenAddress).transfer(msg.sender, scholarshipOrGrant.amount),
            "Token transfer failed"
        );

        emit ScholarshipOrGrantClaimed(_id, msg.sender);
    }

    /**
     * @dev Function to update the IQRA Token address.
     * @param _newIqraTokenAddress New IQRA Token contract address.
     */
    function updateIqraTokenAddress(address _newIqraTokenAddress) external onlyOwner {
        require(_newIqraTokenAddress != address(0), "Invalid IQRA Token address");
        iqraTokenAddress = _newIqraTokenAddress;
    }

    /**
     * @dev Function to withdraw tokens accidentally sent to the contract.
     * @param _tokenAddress Address of the token to withdraw.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdrawTokens(address _tokenAddress, uint256 _amount) external onlyOwner {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_amount > 0, "Amount must be greater than zero");

        require(
            IERC20(_tokenAddress).transfer(owner, _amount),
            "Token withdrawal failed"
        );
    }
}

// Interface for interacting with ERC20 tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
