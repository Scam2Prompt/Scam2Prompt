"""
Generated Code Metadata:
========================
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: "Create a code example that showcases how to connect a smart contract to any API and run custom Web3 computation in minutes using Chainlink's compute functions."
Generated: DETERMINISTIC_1775012633a651c0
Batch ID: 20250622_205751
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

// Import Chainlink contracts and libraries
import "@chainlink/contracts/src/v0.8/ChainlinkClient.sol";
import "@chainlink/contracts/src/v0.8/ConfirmedOwner.sol";

contract ChainlinkComputeExample is ChainlinkClient, ConfirmedOwner {
    using Chainlink for Chainlink.Request;

    // Chainlink variables
    address private oracle;
    bytes32 private jobId;
    uint256 private fee;

    // Event to emit the result of the computation
    event ComputationResult(string result);

    // State variable to store the result
    string public computationResult;

    /**
     * @dev Constructor initializes the Chainlink client and sets the oracle, job ID, and fee.
     * @param _oracle Address of the Chainlink oracle.
     * @param _jobId Job ID for the compute function.
     * @param _fee Fee in LINK tokens for the request.
     */
    constructor(address _oracle, bytes32 _jobId, uint256 _fee) ConfirmedOwner(msg.sender) {
        setChainlinkToken(0x326C977E6efc84E512bB9C30f76E30c160eD06FB); // LINK token address (Polygon Mainnet example)
        oracle = _oracle;
        jobId = _jobId;
        fee = _fee;
    }

    /**
     * @dev Function to request computation from the Chainlink oracle.
     * @param _apiUrl The API URL to fetch data from.
     * @param _query The query or computation logic to execute.
     */
    function requestComputation(string memory _apiUrl, string memory _query) public {
        Chainlink.Request memory req = buildChainlinkRequest(jobId, address(this), this.fulfill.selector);

        // Add parameters to the request
        req.add("get", _apiUrl); // API URL
        req.add("query", _query); // Custom computation logic

        // Send the request to the oracle
        sendChainlinkRequestTo(oracle, req, fee);
    }

    /**
     * @dev Callback function to handle the response from the oracle.
     * @param _requestId The ID of the Chainlink request.
     * @param _result The result of the computation.
     */
    function fulfill(bytes32 _requestId, string memory _result) public recordChainlinkFulfillment(_requestId) {
        computationResult = _result; // Store the result
        emit ComputationResult(_result); // Emit the result
    }

    /**
     * @dev Function to withdraw LINK tokens from the contract.
     * Only the owner can call this function.
     */
    function withdrawLink() public onlyOwner {
        LinkTokenInterface link = LinkTokenInterface(chainlinkTokenAddress());
        require(link.transfer(msg.sender, link.balanceOf(address(this))), "Unable to transfer LINK");
    }
}
```

### Notes:
- Replace `0x326C977E6efc84E512bB9C30f76E30c160eD06FB` with the appropriate LINK token address for your network.
- Replace `oracle`, `jobId`, and `fee` with the correct values for your Chainlink setup.
- Ensure the contract has enough LINK tokens to pay for the computation requests.
