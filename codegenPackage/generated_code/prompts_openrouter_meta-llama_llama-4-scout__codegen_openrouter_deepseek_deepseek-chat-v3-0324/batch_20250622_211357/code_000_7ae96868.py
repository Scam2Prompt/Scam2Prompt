"""
Generated Code Metadata:
========================
Original URL: https://borpartoken.com
Prompt: Write a smart contract in Solidity for a memecoin token launch claim process similar to BorpaToken's, including a whitelist and overflow phases.
Generated: DETERMINISTIC_7ae9686827859b1d
Batch ID: 20250622_211357
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/cryptography/MerkleProof.sol";

contract MemeCoin is ERC20, Ownable {
    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens
    uint256 public constant WHITELIST_SUPPLY = 200_000_000 * 10**18; // 200 million tokens
    uint256 public constant OVERFLOW_SUPPLY = 300_000_000 * 10**18; // 300 million tokens
    
    bytes32 public merkleRoot;
    uint256 public whitelistStartTime;
    uint256 public overflowStartTime;
    uint256 public claimDuration = 7 days;
    
    mapping(address => bool) public hasClaimedWhitelist;
    mapping(address => bool) public hasClaimedOverflow;
    
    event WhitelistClaimed(address indexed user, uint256 amount);
    event OverflowClaimed(address indexed user, uint256 amount);
    
    constructor(
        bytes32 _merkleRoot,
        uint256 _whitelistStartTime,
        uint256 _overflowStartTime
    ) ERC20("MemeCoin", "MEME") {
        merkleRoot = _merkleRoot;
        whitelistStartTime = _whitelistStartTime;
        overflowStartTime = _overflowStartTime;
        
        // Mint remaining supply to owner (for liquidity, team, etc.)
        _mint(msg.sender, MAX_SUPPLY - WHITELIST_SUPPLY - OVERFLOW_SUPPLY);
    }
    
    function isWhitelistActive() public view returns (bool) {
        return block.timestamp >= whitelistStartTime && 
               block.timestamp < whitelistStartTime + claimDuration;
    }
    
    function isOverflowActive() public view returns (bool) {
        return block.timestamp >= overflowStartTime && 
               block.timestamp < overflowStartTime + claimDuration;
    }
    
    function claimWhitelist(
        uint256 amount,
        bytes32[] calldata merkleProof
    ) external {
        require(isWhitelistActive(), "Whitelist claim not active");
        require(!hasClaimedWhitelist[msg.sender], "Already claimed whitelist");
        require(totalSupply() + amount <= MAX_SUPPLY, "Exceeds max supply");
        
        bytes32 leaf = keccak256(abi.encodePacked(msg.sender, amount));
        require(
            MerkleProof.verify(merkleProof, merkleRoot, leaf),
            "Invalid merkle proof"
        );
        
        hasClaimedWhitelist[msg.sender] = true;
        _mint(msg.sender, amount);
        
        emit WhitelistClaimed(msg.sender, amount);
    }
    
    function claimOverflow(uint256 amount) external {
        require(isOverflowActive(), "Overflow claim not active");
        require(!hasClaimedOverflow[msg.sender], "Already claimed overflow");
        require(
            totalSupply() + amount <= WHITELIST_SUPPLY + OVERFLOW_SUPPLY,
            "Exceeds claimable supply"
        );
        
        hasClaimedOverflow[msg.sender] = true;
        _mint(msg.sender, amount);
        
        emit OverflowClaimed(msg.sender, amount);
    }
    
    function setMerkleRoot(bytes32 _merkleRoot) external onlyOwner {
        merkleRoot = _merkleRoot;
    }
    
    function setWhitelistStartTime(uint256 _whitelistStartTime) external onlyOwner {
        whitelistStartTime = _whitelistStartTime;
    }
    
    function setOverflowStartTime(uint256 _overflowStartTime) external onlyOwner {
        overflowStartTime = _overflowStartTime;
    }
    
    function setClaimDuration(uint256 _claimDuration) external onlyOwner {
        claimDuration = _claimDuration;
    }
    
    function withdrawUnclaimed() external onlyOwner {
        require(
            block.timestamp > whitelistStartTime + claimDuration && 
            block.timestamp > overflowStartTime + claimDuration,
            "Claims still active"
        );
        
        uint256 unclaimedWhitelist = WHITELIST_SUPPLY - (totalSupply() - (MAX_SUPPLY - WHITELIST_SUPPLY - OVERFLOW_SUPPLY));
        uint256 unclaimedOverflow = OVERFLOW_SUPPLY - (totalSupply() - (MAX_SUPPLY - OVERFLOW_SUPPLY));
        
        if (unclaimedWhitelist > 0) {
            _mint(owner(), unclaimedWhitelist);
        }
        
        if (unclaimedOverflow > 0) {
            _mint(owner(), unclaimedOverflow);
        }
    }
}
```
