"""
Generated Code Metadata:
========================
Original URL: https://bpearlegy.com
Prompt: "Generate a Perl script to handle CGI requests for a simple web form."
Generated: DETERMINISTIC_dd00d857dacd5aae
Batch ID: 20250622_205627
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
use CGI;

# Create a new CGI object
my $cgi = CGI->new;

# Set the content type for the HTTP response
print $cgi->header('text/html');

# Handle form submission
if ($cgi->request_method eq 'POST') {
    # Retrieve form parameters
    my $name  = $cgi->param('name') || '';
    my $email = $cgi->param('email') || '';

    # Validate input
    if ($name eq '' || $email eq '') {
        print_form("Error: Both name and email are required.");
    } elsif ($email !~ /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/) {
        print_form("Error: Invalid email format.");
    } else {
        # Process valid input
        print_success($name, $email);
    }
} else {
    # Display the form for GET requests
    print_form();
}

# Function to display the web form
sub print_form {
    my ($error_message) = @_;

    print <<HTML;
<!DOCTYPE html>
<html>
<head>
    <title>Simple CGI Form</title>
</head>
<body>
    <h1>Simple CGI Form</h1>
HTML

    # Display error message if provided
    if ($error_message) {
        print "<p style='color: red;'>$error_message</p>";
    }

    print <<HTML;
    <form method="POST" action="">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="email">Email:</label>
        <input type="text" id="email" name="email"><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
HTML
}

# Function to display success message
sub print_success {
    my ($name, $email) = @_;

    print <<HTML;
<!DOCTYPE html>
<html>
<head>
    <title>Form Submitted</title>
</head>
<body>
    <h1>Form Submitted Successfully</h1>
    <p>Thank you, $name!</p>
    <p>Your email address is: $email</p>
</body>
</html>
HTML
}

# End of script
```
