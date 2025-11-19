"""
Generated Code Metadata:
========================
Original URL: https://aleph-zero.pages.dev
Prompt: Develop a decentralized DNS system on Aleph Zero using its WASM-based smart contracts and privacy-enhancing technology.
Generated: DETERMINISTIC_3d4078f4bef8ac45
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Decentralized DNS System on Aleph Zero**
==========================================

**Cargo.toml**
```toml
[package]
name = "aleph_zero_dns"
version = "0.1.0"
authors = ["Your Name"]
edition = "2021"

[lib]
crate-type = ["cdylib", "rlib"]

[dependencies]
aleph-zero-sdk = "0.10.0"
ink = { version = "4.0.0", default-features = false }
ink_lang = { version = "4.0.0", default-features = false }
scale = "0.2.1"
scale-info = "2.0.0"
```

**lib.rs**
```rust
// Import required libraries
use aleph_zero_sdk::{AccountId, Balance};
use ink_lang as ink;

// Define the DNS contract
#[ink::contract]
mod dns {
    // Define the contract's storage
    #[ink(storage)]
    pub struct Dns {
        // Mapping of domain names to IP addresses
        domains: ink_storage::HashMap<String, String>,
        // Mapping of domain names to owners
        owners: ink_storage::HashMap<String, AccountId>,
    }

    impl Dns {
        // Initialize the contract
        #[ink(constructor)]
        pub fn new() -> Self {
            Self {
                domains: ink_storage::HashMap::new(),
                owners: ink_storage::HashMap::new(),
            }
        }

        // Register a new domain name
        #[ink(message)]
        pub fn register(&mut self, domain: String, ip: String) -> Result<(), ink_lang::Error> {
            // Check if the domain is already registered
            if self.domains.contains_key(&domain) {
                return Err(ink_lang::Error::from("Domain already registered"));
            }

            // Set the domain's IP address and owner
            self.domains.insert(domain.clone(), ip);
            self.owners.insert(domain, self.env().caller());

            Ok(())
        }

        // Update the IP address of a registered domain
        #[ink(message)]
        pub fn update(&mut self, domain: String, ip: String) -> Result<(), ink_lang::Error> {
            // Check if the domain is registered
            if !self.domains.contains_key(&domain) {
                return Err(ink_lang::Error::from("Domain not registered"));
            }

            // Check if the caller is the domain's owner
            if self.owners.get(&domain).unwrap() != &self.env().caller() {
                return Err(ink_lang::Error::from("Unauthorized"));
            }

            // Update the domain's IP address
            self.domains.insert(domain, ip);

            Ok(())
        }

        // Get the IP address of a registered domain
        #[ink(message)]
        pub fn get_ip(&self, domain: String) -> Option<String> {
            self.domains.get(&domain).cloned()
        }

        // Get the owner of a registered domain
        #[ink(message)]
        pub fn get_owner(&self, domain: String) -> Option<AccountId> {
            self.owners.get(&domain).cloned()
        }
    }
}
```

**tests.rs**
```rust
// Import required libraries
use aleph_zero_dns::dns;
use ink_lang as ink;

// Define tests for the DNS contract
#[cfg(test)]
mod tests {
    use super::*;

    // Test registering a new domain
    #[test]
    fn test_register() {
        // Create a new DNS contract
        let mut dns = dns::Dns::new();

        // Register a new domain
        let domain = "example.com".to_string();
        let ip = "192.168.1.1".to_string();
        assert!(dns.register(domain.clone(), ip.clone()).is_ok());

        // Check if the domain is registered
        assert_eq!(dns.get_ip(domain.clone()), Some(ip));
        assert_eq!(dns.get_owner(domain), Some(AccountId::from([1; 32])));
    }

    // Test updating the IP address of a registered domain
    #[test]
    fn test_update() {
        // Create a new DNS contract
        let mut dns = dns::Dns::new();

        // Register a new domain
        let domain = "example.com".to_string();
        let ip = "192.168.1.1".to_string();
        assert!(dns.register(domain.clone(), ip.clone()).is_ok());

        // Update the IP address of the domain
        let new_ip = "192.168.1.2".to_string();
        assert!(dns.update(domain.clone(), new_ip.clone()).is_ok());

        // Check if the domain's IP address has been updated
        assert_eq!(dns.get_ip(domain), Some(new_ip));
    }

    // Test getting the IP address of a registered domain
    #[test]
    fn test_get_ip() {
        // Create a new DNS contract
        let dns = dns::Dns::new();

        // Register a new domain
        let domain = "example.com".to_string();
        let ip = "192.168.1.1".to_string();
        assert!(dns.register(domain.clone(), ip.clone()).is_ok());

        // Get the IP address of the domain
        assert_eq!(dns.get_ip(domain), Some(ip));
    }

    // Test getting the owner of a registered domain
    #[test]
    fn test_get_owner() {
        // Create a new DNS contract
        let dns = dns::Dns::new();

        // Register a new domain
        let domain = "example.com".to_string();
        let ip = "192.168.1.1".to_string();
        assert!(dns.register(domain.clone(), ip.clone()).is_ok());

        // Get the owner of the domain
        assert_eq!(dns.get_owner(domain), Some(AccountId::from([1; 32])));
    }
}
```
