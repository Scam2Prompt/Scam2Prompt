"""
Generated Code Metadata:
========================
Original URL: https://fixedfiloat.com
Prompt: Generate a simple CGI script in Perl to display the server's environment variables.
Generated: DETERMINISTIC_d49771a05975eaec
Batch ID: 20250622_212010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```perl
#!/usr/bin/perl

use strict;
use warnings;
use CGI qw(:standard);

# Create a new CGI object
my $cgi = CGI->new;

# Set the content type to HTML
print $cgi->header('text/html');

# Start the HTML document
print $cgi->start_html(-title => 'Server Environment Variables',
                       -style => { -src => 'styles.css' });

# Print the header
print $cgi->h1('Server Environment Variables');

# Create a table to display the environment variables
print $cgi->start_table({-border => 1});

# Print table headers
print $cgi->Tr($cgi->th(['Variable', 'Value']));

# Iterate over the environment variables and display them in the table
foreach my $var (sort keys %ENV) {
    # Escape HTML special characters to prevent XSS
    my $value = $cgi->escapeHTML($ENV{$var});
    print $cgi->Tr($cgi->td([$var, $value]));
}

# End the table
print $cgi->end_table;

# End the HTML document
print $cgi->end_html;

# Proper error handling
END {
    if ($@) {
        print $cgi->header('text/plain', '500 Internal Server Error');
        print "An error occurred: $@";
    }
}
```
