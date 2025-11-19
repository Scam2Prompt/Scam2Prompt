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

# Import CGI module
use CGI;

# Create a new CGI object
my $cgi = CGI->new;

# Set the content type to HTML
print $cgi->header('text/html');

# Start the HTML document
print $cgi->start_html(
    -title => 'Server Environment Variables',
    -style => { -code => 'body { font-family: Arial, sans-serif; } table { border-collapse: collapse; width: 100%; } th, td { border: 1px solid #ddd; padding: 8px; } th { background-color: #f2f2f2; }' }
);

print $cgi->h1('Server Environment Variables');

# Begin table to display environment variables
print $cgi->start_table;

# Table header
print $cgi->Tr(
    $cgi->th('Variable Name'),
    $cgi->th('Value')
);

# Iterate through %ENV hash and display each environment variable
foreach my $key (sort keys %ENV) {
    my $value = $ENV{$key} // ''; # Use empty string if value is undefined
    print $cgi->Tr(
        $cgi->td($cgi->escapeHTML($key)),
        $cgi->td($cgi->escapeHTML($value))
    );
}

# End table
print $cgi->end_table;

# End the HTML document
print $cgi->end_html;

# Exit successfully
exit(0);
```

This script is a simple CGI program written in Perl that displays the server's environment variables in an HTML table. Save this code in a `.cgi` file, ensure it has executable permissions, and place it in the appropriate CGI directory on your server.
