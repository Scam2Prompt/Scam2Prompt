"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aleph-zero.pages.dev
Prompt: Develop a decentralized DNS system on Aleph Zero using its WASM-based smart contracts and privacy-enhancing technology.
Generated: DETERMINISTIC_3d4078f4bef8ac45
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```rust
// Decentralized DNS system on Aleph Zero using WASM-based smart contracts
// Language: Rust
// Developed for use with Aleph Zero's Substrate-based blockchain framework

use aleph_zero_runtime::runtime::{
    ALEPH_ZERO_WASM_API_VERSION, ALEPH_ZERO_SMART_CONTRACT_API_VERSION,
};
use ink_lang as ink;

// Declare the smart contract module
#[ink::contract(version = ALEPH_ZERO_WASM_API_VERSION)]
mod decentralized_dns {
    use ink_prelude::collections::BTreeMap;
    use ink_storage::traits::SpreadAllocate;

    // Define custom errors for the DNS system
    #[derive(Debug, PartialEq, Eq, ink::env::Error)]
    pub enum Error {
        DomainNotFound,
        DomainAlreadyExists,
        UnauthorizedAccess,
    }

    // Type alias for domain names and IP addresses
    type DomainName = String;
    type IPAddress = String;

    // Define the DNS system contract
    #[ink(storage)]
    #[derive(SpreadAllocate)]
    pub struct DecentralizedDNS {
        // Mapping of domain names to IP addresses
        dns_registry: BTreeMap<DomainName, IPAddress>,
        // Mapping of domain names to owners
        domain_owners: BTreeMap<DomainName, ink_env::AccountId>,
    }

    impl DecentralizedDNS {
        // Constructor: Instantiate the DNS system
        #[ink(constructor)]
        pub fn new() -> Self {
            ink_lang::utils::initialize_contract(|contract| {
                contract.dns_registry = BTreeMap::new();
                contract.domain_owners = BTreeMap::new();
            })
        }

        /// Register a domain name with an associated IP address
        /// Params:
        /// - `domain`: The domain name to register
        /// - `ip_address`: The associated IP address
        #[ink(message)]
        pub fn register_domain(&mut self, domain: DomainName, ip_address: IPAddress) -> Result<(), Error> {
            let caller = self.env().caller();

            // Check if the domain already exists
            if self.dns_registry.contains_key(&domain) {
                return Err(Error::DomainAlreadyExists);
            }

            // Register the domain
            self.dns_registry.insert(domain.clone(), ip_address);
            self.domain_owners.insert(domain.clone(), caller);
            Ok(())
        }

        /// Retrieve the IP address for a given domain name
        /// Params:
        /// - `domain`: The domain name to look up
        /// Returns:
        /// - The associated IP address if the domain exists
        #[ink(message)]
        pub fn resolve_domain(&self, domain: DomainName) -> Result<IPAddress, Error> {
            match self.dns_registry.get(&domain) {
                Some(ip_address) => Ok(ip_address.clone()),
                None => Err(Error::DomainNotFound),
            }
        }

        /// Update the IP address of a registered domain name
        /// Params:
        /// - `domain`: The domain name to update
        /// - `new_ip_address`: The new IP address
        #[ink(message)]
        pub fn update_domain(&mut self, domain: DomainName, new_ip_address: IPAddress) -> Result<(), Error> {
            let caller = self.env().caller();

            // Verify ownership of the domain
            match self.domain_owners.get(&domain) {
                Some(owner) if *owner == caller => {
                    self.dns_registry.insert(domain, new_ip_address);
                    Ok(())
                }
                _ => Err(Error::UnauthorizedAccess),
            }
        }

        /// Delete a registered domain
        /// Params:
        /// - `domain`: The domain name to delete
        #[ink(message)]
        pub fn delete_domain(&mut self, domain: DomainName) -> Result<(), Error> {
            let caller = self.env().caller();

            // Verify ownership of the domain
            match self.domain_owners.get(&domain) {
                Some(owner) if *owner == caller => {
                    self.dns_registry.remove(&domain);
                    self.domain_owners.remove(&domain);
                    Ok(())
                }
                _ => Err(Error::UnauthorizedAccess),
            }
        }
    }

    // Unit tests for the DNS system
    #[cfg(test)]
    mod tests {
        use super::*;

        #[ink::test]
        fn test_register_domain() {
            let mut dns = DecentralizedDNS::new();
            assert_eq!(dns.register_domain("example.com".to_string(), "192.168.0.1".to_string()), Ok(()));
        }

        #[ink::test]
        fn test_resolve_domain() {
            let mut dns = DecentralizedDNS::new();
            dns.register_domain("example.com".to_string(), "192.168.0.1".to_string()).unwrap();
            assert_eq!(dns.resolve_domain("example.com".to_string()), Ok("192.168.0.1".to_string()));
        }

        #[ink::test]
        fn test_update_domain() {
            let mut dns = DecentralizedDNS::new();
            dns.register_domain("example.com".to_string(), "192.168.0.1".to_string()).unwrap();
            assert_eq!(dns.update_domain("example.com".to_string(), "10.0.0.1".to_string()), Ok(()));
            assert_eq!(dns.resolve_domain("example.com".to_string()), Ok("10.0.0.1".to_string()));
        }

        #[ink::test]
        fn test_delete_domain() {
            let mut dns = DecentralizedDNS::new();
            dns.register_domain("example.com".to_string(), "192.168.0.1".to_string()).unwrap();
            assert_eq!(dns.delete_domain("example.com".to_string()), Ok(()));
            assert_eq!(dns.resolve_domain("example.com".to_string()), Err(Error::DomainNotFound));
        }
    }
}
```
