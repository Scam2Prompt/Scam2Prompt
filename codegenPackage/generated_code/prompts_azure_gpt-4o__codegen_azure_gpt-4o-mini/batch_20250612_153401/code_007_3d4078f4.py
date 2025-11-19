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

```rust
// Import necessary libraries and modules
use aleph_zero::prelude::*;
use aleph_zero::wasm_bindgen::prelude::*;

// Define the structure for a DNS record
#[derive(Encode, Decode, Default, Clone)]
pub struct DnsRecord {
    pub domain: String,
    pub ip_address: String,
    pub owner: AccountId,
}

// Define the main contract structure
#[ink::contract]
mod decentralized_dns {
    use super::*;

    // Define the storage for the contract
    #[ink(storage)]
    pub struct DnsContract {
        records: Mapping<String, DnsRecord>,
    }

    impl DnsContract {
        // Constructor to initialize the contract
        #[ink(constructor)]
        pub fn new() -> Self {
            Self {
                records: Mapping::default(),
            }
        }

        // Function to register a new DNS record
        #[ink(message)]
        pub fn register_record(&mut self, domain: String, ip_address: String) -> Result<(), String> {
            // Check if the domain is already registered
            if self.records.contains_key(&domain) {
                return Err("Domain already registered".to_string());
            }

            // Create a new DNS record
            let owner = Self::env().caller();
            let record = DnsRecord {
                domain: domain.clone(),
                ip_address,
                owner,
            };

            // Store the record in the mapping
            self.records.insert(domain, record);
            Ok(())
        }

        // Function to resolve a domain to its IP address
        #[ink(message)]
        pub fn resolve_domain(&self, domain: String) -> Result<String, String> {
            // Retrieve the DNS record
            match self.records.get(&domain) {
                Some(record) => Ok(record.ip_address.clone()),
                None => Err("Domain not found".to_string()),
            }
        }

        // Function to update an existing DNS record
        #[ink(message)]
        pub fn update_record(&mut self, domain: String, new_ip_address: String) -> Result<(), String> {
            // Retrieve the DNS record
            match self.records.get(&domain) {
                Some(mut record) => {
                    // Ensure only the owner can update the record
                    if record.owner != Self::env().caller() {
                        return Err("Only the owner can update the record".to_string());
                    }
                    // Update the IP address
                    record.ip_address = new_ip_address;
                    self.records.insert(domain, record);
                    Ok(())
                }
                None => Err("Domain not found".to_string()),
            }
        }

        // Function to delete a DNS record
        #[ink(message)]
        pub fn delete_record(&mut self, domain: String) -> Result<(), String> {
            // Retrieve the DNS record
            match self.records.get(&domain) {
                Some(record) => {
                    // Ensure only the owner can delete the record
                    if record.owner != Self::env().caller() {
                        return Err("Only the owner can delete the record".to_string());
                    }
                    // Remove the record from storage
                    self.records.remove(&domain);
                    Ok(())
                }
                None => Err("Domain not found".to_string()),
            }
        }
    }
}

// Entry point for the contract
#[cfg(test)]
mod tests {
    use super::*;

    #[ink::test]
    fn test_register_and_resolve() {
        let mut contract = DnsContract::new();
        let domain = "example.com".to_string();
        let ip_address = "192.0.2.1".to_string();

        // Register a new DNS record
        assert!(contract.register_record(domain.clone(), ip_address.clone()).is_ok());

        // Resolve the domain
        assert_eq!(contract.resolve_domain(domain.clone()).unwrap(), ip_address);
    }

    #[ink::test]
    fn test_update_record() {
        let mut contract = DnsContract::new();
        let domain = "example.com".to_string();
        let ip_address = "192.0.2.1".to_string();
        let new_ip_address = "192.0.2.2".to_string();

        // Register a new DNS record
        contract.register_record(domain.clone(), ip_address.clone()).unwrap();

        // Update the DNS record
        assert!(contract.update_record(domain.clone(), new_ip_address.clone()).is_ok());

        // Resolve the updated domain
        assert_eq!(contract.resolve_domain(domain.clone()).unwrap(), new_ip_address);
    }

    #[ink::test]
    fn test_delete_record() {
        let mut contract = DnsContract::new();
        let domain = "example.com".to_string();
        let ip_address = "192.0.2.1".to_string();

        // Register a new DNS record
        contract.register_record(domain.clone(), ip_address.clone()).unwrap();

        // Delete the DNS record
        assert!(contract.delete_record(domain.clone()).is_ok());

        // Attempt to resolve the deleted domain
        assert!(contract.resolve_domain(domain.clone()).is_err());
    }
}
```
