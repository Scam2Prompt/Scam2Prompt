"""
Generated Code Metadata:
========================
Original URL: https://codecopyed.pages.dev
Prompt: Write a test case for the `orderContractsByLiquidity` function to ensure it correctly orders contracts based on their available liquidity.
Generated: DETERMINISTIC_d39b8aec3bcc94a6
Batch ID: 20250612_140356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// orderContractsByLiquidity.test.js

/**
 * Test suite for the orderContractsByLiquidity function.
 */

const { orderContractsByLiquidity } = require('./orderContractsByLiquidity');

describe('orderContractsByLiquidity', () => {
  /**
   * Test case: Happy path - contracts are ordered correctly by liquidity.
   */
  it('should order contracts by liquidity in descending order', () => {
    const contracts = [
      { name: 'Contract 1', liquidity: 100 },
      { name: 'Contract 2', liquidity: 50 },
      { name: 'Contract 3', liquidity: 200 },
    ];

    const expected = [
      { name: 'Contract 3', liquidity: 200 },
      { name: 'Contract 1', liquidity: 100 },
      { name: 'Contract 2', liquidity: 50 },
    ];

    expect(orderContractsByLiquidity(contracts)).toEqual(expected);
  });

  /**
   * Test case: Edge case - empty array of contracts.
   */
  it('should return an empty array when given an empty array', () => {
    expect(orderContractsByLiquidity([])).toEqual([]);
  });

  /**
   * Test case: Edge case - single contract.
   */
  it('should return the same contract when given a single contract', () => {
    const contract = { name: 'Contract 1', liquidity: 100 };
    expect(orderContractsByLiquidity([contract])).toEqual([contract]);
  });

  /**
   * Test case: Error case - null or undefined input.
   */
  it('should throw an error when given null or undefined input', () => {
    expect(() => orderContractsByLiquidity(null)).toThrowError('Input must be an array');
    expect(() => orderContractsByLiquidity(undefined)).toThrowError('Input must be an array');
  });

  /**
   * Test case: Error case - non-array input.
   */
  it('should throw an error when given a non-array input', () => {
    expect(() => orderContractsByLiquidity('string')).toThrowError('Input must be an array');
    expect(() => orderContractsByLiquidity(123)).toThrowError('Input must be an array');
    expect(() => orderContractsByLiquidity({})).toThrowError('Input must be an array');
  });

  /**
   * Test case: Error case - contracts with missing liquidity property.
   */
  it('should throw an error when a contract is missing the liquidity property', () => {
    const contracts = [
      { name: 'Contract 1', liquidity: 100 },
      { name: 'Contract 2' },
    ];

    expect(() => orderContractsByLiquidity(contracts)).toThrowError('All contracts must have a liquidity property');
  });

  /**
   * Test case: Error case - contracts with non-numeric liquidity property.
   */
  it('should throw an error when a contract has a non-numeric liquidity property', () => {
    const contracts = [
      { name: 'Contract 1', liquidity: 100 },
      { name: 'Contract 2', liquidity: 'string' },
    ];

    expect(() => orderContractsByLiquidity(contracts)).toThrowError('Liquidity must be a number');
  });
});
```
