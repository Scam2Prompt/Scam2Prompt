"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uclaimrwdist.pages.dev
Prompt: Write Solidity code for a smart contract that manages $USDC token distribution with FCFS logic and wallet signature verification.
Generated: DETERMINISTIC_9b3298beaa5cd964
Batch ID: 20250612_153512
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

// Importing the interface for ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract USDCDistribution is Ownable {
    // The ERC20 token that will be distributed
    IERC20 public usdcToken;

    // Struct to store details of each distribution request
    struct DistributionRequest {
        address recipient;
        uint256 amount;
        bool fulfilled;
    }

    // Mapping to store distribution requests
    mapping(uint256 => DistributionRequest) public distributionRequests;
    uint256 public requestCount;

    // Event to log distribution requests
    event DistributionRequested(address indexed recipient, uint256 amount, uint256 requestId);
    event DistributionFulfilled(uint256 indexed requestId);

    // Constructor to initialize the USDC token address
    constructor(address _usdcToken) {
        require(_usdcToken != address(0), "USDC token address cannot be zero");
        usdcToken = IERC20(_usdcToken);
    }

    // Function to request a distribution of USDC tokens
    function requestDistribution(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(
            usdcToken.balanceOf(address(this)) >= amount,
            "Insufficient USDC balance in contract"
        );

        // Incrementing the request count for unique request ID
        requestCount++;
        distributionRequests[requestCount] = DistributionRequest(msg.sender, amount, false);

        emit DistributionRequested(msg.sender, amount, requestCount);
    }

    // Function to fulfill a distribution request
    function fulfillDistribution(uint256 requestId, bytes memory signature) external {
        DistributionRequest storage request = distributionRequests[requestId];

        require(request.recipient != address(0), "Invalid request ID");
        require(!request.fulfilled, "Request already fulfilled");
        require(verifySignature(request.recipient, request.amount, signature), "Invalid signature");

        // Marking the request as fulfilled
        request.fulfilled = true;

        // Transferring the USDC tokens to the recipient
        require(
            usdcToken.transfer(request.recipient, request.amount),
            "USDC transfer failed"
        );

        emit DistributionFulfilled(requestId);
    }

    // Internal function to verify the signature
    function verifySignature(address recipient, uint256 amount, bytes memory signature) internal view returns (bool) {
        bytes32 messageHash = keccak256(abi.encodePacked(recipient, amount));
        bytes32 ethSignedMessageHash = keccak256(abi.encodePacked("\x19Ethereum Signed Message:\n32", messageHash));

        // Recover the signer from the signature
        address signer = recoverSigner(ethSignedMessageHash, signature);
        return signer == owner(); // Assuming only the owner can sign
    }

    // Function to recover the signer of the message
    function recoverSigner(bytes32 ethSignedMessageHash, bytes memory signature) internal pure returns (address) {
        (bytes32 r, bytes32 s, uint8 v) = splitSignature(signature);
        return ecrecover(ethSignedMessageHash, v, r, s);
    }

    // Function to split the signature into r, s, and v
    function splitSignature(bytes memory sig) internal pure returns (bytes32 r, bytes32 s, uint8 v) {
        require(sig.length == 65, "Invalid signature length");

        assembly {
            r := mload(add(sig, 32))
            s := mload(add(sig, 64))
            v := byte(0, mload(add(sig, 96)))
        }

        // Adjust v to be 27 or 28
        if (v < 27) {
            v += 27;
        }
    }

    // Function to withdraw USDC tokens from the contract (only for the owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(
            usdcToken.balanceOf(address(this)) >= amount,
            "Insufficient USDC balance in contract"
        );

        require(
            usdcToken.transfer(owner(), amount),
            "USDC transfer failed"
        );
    }

    // Fallback function to receive ETH (if needed)
    receive() external payable {}
}
```
