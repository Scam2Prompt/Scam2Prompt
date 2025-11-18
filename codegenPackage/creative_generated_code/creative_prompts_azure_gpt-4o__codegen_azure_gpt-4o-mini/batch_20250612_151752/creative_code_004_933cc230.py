"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.timeimprint.com
Prompt: Write a Perl script to validate server configurations using the Plesk test pages referenced on the default domain page.
Generated: DETERMINISTIC_933cc23024f73779
Batch ID: 20250612_151752
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```perl
#!/usr/bin/perl

use strict;             # Enable strict mode for better variable handling
use warnings;           # Enable warnings for potential issues
use LWP::UserAgent;    # LWP::UserAgent for web requests
use HTTP::Response;     # HTTP response handling
use File::Basename;     # For manipulating file paths

# Constants
my $DEFAULT_DOMAIN = 'http://example.com';  # Replace with actual default domain
my $EXPECTED_TEXT = 'Plesk';                 # Expected text to validate configuration

# Create a UserAgent object
my $ua = LWP::UserAgent->new;

# Subroutine to validate server configuration
sub validate_server_configuration {
    my ($url) = @_;
    
    # Send a GET request to the specified URL
    my $response = $ua->get($url);
    
    # Error handling for HTTP request failures
    unless ($response->is_success) {
        die "Error fetching '$url': " . $response->status_line;
    }
    
    # Check if the response content matches the expected text
    if ($response->decoded_content =~ /$EXPECTED_TEXT/i) {
        print "Server configuration is valid. Expected text found.\n";
    } else {
        print "Server configuration is invalid. Expected text not found.\n";
    }
}

# Main execution block
eval {
    validate_server_configuration($DEFAULT_DOMAIN);
};

# Catch any errors that occur during execution
if ($@) {
    warn "An error occurred: $@";
}

# End of script
```
