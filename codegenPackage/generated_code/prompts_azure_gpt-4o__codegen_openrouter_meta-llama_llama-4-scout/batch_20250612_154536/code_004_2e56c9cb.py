"""
Generated Code Metadata:
========================
Original URL: https://www.optimism.rs
Prompt: Write a program to filter and display domain names from a list, focusing on Serbian (.rs) domains, inspired by the examples on optimism.rs.
Generated: DETERMINISTIC_2e56c9cbbbc68044
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
/// Domain Filter Program
///
/// This program filters and displays domain names from a list, focusing on Serbian (.rs) domains.

use std::error::Error;
use std::fs::File;
use std::io::{BufRead, BufReader};

/// Structure to hold domain name and its type
#[derive(Debug)]
struct Domain {
    name: String,
    domain_type: String,
}

impl Domain {
    /// Create a new Domain instance
    fn new(name: String) -> Self {
        let domain_type = name.split('.').last().unwrap_or("").to_string();
        Domain { name, domain_type }
    }
}

/// Function to filter domains by type
fn filter_domains(domains: Vec<Domain>, domain_type: &str) -> Vec<Domain> {
    domains.into_iter().filter(|d| d.domain_type == domain_type).collect()
}

/// Function to read domains from file
fn read_domains_from_file(filename: &str) -> Result<Vec<Domain>, Box<dyn Error>> {
    let file = File::open(filename)?;
    let reader = BufReader::new(file);
    let mut domains = Vec::new();

    for line in reader.lines() {
        let line = line?;
        let domain = Domain::new(line.trim().to_string());
        domains.push(domain);
    }

    Ok(domains)
}

/// Function to display domains
fn display_domains(domains: Vec<Domain>) {
    println!("Domains:");
    for domain in domains {
        println!("{}", domain.name);
    }
}

fn main() -> Result<(), Box<dyn Error>> {
    let filename = "domains.txt"; // replace with your file name
    let domains = read_domains_from_file(filename)?;
    let serbian_domains = filter_domains(domains, "rs");
    display_domains(serbian_domains);
    Ok(())
}
```
