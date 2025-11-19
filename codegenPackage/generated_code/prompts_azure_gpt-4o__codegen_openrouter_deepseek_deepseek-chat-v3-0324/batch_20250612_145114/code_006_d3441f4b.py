"""
Generated Code Metadata:
========================
Original URL: https://app-2v.xyz
Prompt: Create a step-by-step guide for resolving a domain name using Google Public DNS in a Node.js application.
Generated: DETERMINISTIC_d3441f4bdf3a92fa
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const dns = require('dns');
const { promisify } = require('util');

// Promisify the DNS resolve functions for async/await usage
const resolve4Async = promisify(dns.resolve4);
const resolve6Async = promisify(dns.resolve6);
const resolveAnyAsync = promisify(dns.resolveAny);
const resolveMxAsync = promisify(dns.resolveMx);
const resolveTxtAsync = promisify(dns.resolveTxt);
const resolveSrvAsync = promisify(dns.resolveSrv);
const resolveNsAsync = promisify(dns.resolveNs);
const resolveCnameAsync = promisify(dns.resolveCname);
const resolveSoaAsync = promisify(dns.resolveSoa);
const resolvePtrAsync = promisify(dns.resolvePtr);
const resolveNaptrAsync = promisify(dns.resolveNaptr);

// Set Google Public DNS servers
dns.setServers(['8.8.8.8', '8.8.4.4']);

/**
 * Resolves a domain name to its IPv4 addresses
 * @param {string} domain - The domain name to resolve
 * @returns {Promise<string[]>} - Array of IPv4 addresses
 */
async function resolveIPv4(domain) {
    try {
        return await resolve4Async(domain);
    } catch (err) {
        throw new Error(`IPv4 resolution failed: ${err.message}`);
    }
}

/**
 * Resolves a domain name to its IPv6 addresses
 * @param {string} domain - The domain name to resolve
 * @returns {Promise<string[]>} - Array of IPv6 addresses
 */
async function resolveIPv6(domain) {
    try {
        return await resolve6Async(domain);
    } catch (err) {
        throw new Error(`IPv6 resolution failed: ${err.message}`);
    }
}

/**
 * Resolves all available DNS records for a domain
 * @param {string} domain - The domain name to resolve
 * @returns {Promise<Object[]>} - Array of DNS records
 */
async function resolveAny(domain) {
    try {
        return await resolveAnyAsync(domain);
    } catch (err) {
        throw new Error(`DNS resolution failed: ${err.message}`);
    }
}

/**
 * Resolves MX records for a domain
 * @param {string} domain - The domain name to resolve
 * @returns {Promise<Object[]>} - Array of MX records
 */
async function resolveMX(domain) {
    try {
        return await resolveMxAsync(domain);
    } catch (err) {
        throw new Error(`MX record resolution failed: ${err.message}`);
    }
}

/**
 * Resolves TXT records for a domain
 * @param {string} domain - The domain name to resolve
 * @returns {Promise<string[][]>} - Array of TXT records
 */
async function resolveTXT(domain) {
    try {
        return await resolveTxtAsync(domain);
    } catch (err) {
        throw new Error(`TXT record resolution failed: ${err.message}`);
    }
}

/**
 * Example usage of the DNS resolver functions
 */
async function exampleUsage() {
    const domain = 'example.com';
    
    try {
        console.log(`Resolving ${domain} using Google Public DNS...`);
        
        const ipv4 = await resolveIPv4(domain);
        console.log('IPv4 addresses:', ipv4);
        
        const ipv6 = await resolveIPv6(domain);
        console.log('IPv6 addresses:', ipv6);
        
        const mxRecords = await resolveMX(domain);
        console.log('MX records:', mxRecords);
        
        const txtRecords = await resolveTXT(domain);
        console.log('TXT records:', txtRecords);
        
        const allRecords = await resolveAny(domain);
        console.log('All records:', allRecords);
    } catch (err) {
        console.error('Error:', err.message);
    }
}

// Uncomment to run the example
// exampleUsage();

module.exports = {
    resolveIPv4,
    resolveIPv6,
    resolveAny,
    resolveMX,
    resolveTXT,
    resolveSrv: resolveSrvAsync,
    resolveNs: resolveNsAsync,
    resolveCname: resolveCnameAsync,
    resolveSoa: resolveSoaAsync,
    resolvePtr: resolvePtrAsync,
    resolveNaptr: resolveNaptrAsync
};
```
