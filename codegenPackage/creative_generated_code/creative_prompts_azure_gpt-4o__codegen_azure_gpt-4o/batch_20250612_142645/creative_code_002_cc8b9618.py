"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syr-whistler.com
Prompt: Provide an example of a Perl CGI script that could be placed in the "cgi-bin" directory to handle form submissions.
Generated: DETERMINISTIC_cc8b9618651329b6
Batch ID: 20250612_142645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```perl
#!/usr/bin/perl

# Enforce strict and warnings for good programming practice
use strict;
use warnings;

# Use CGI module to handle HTTP request and response
use CGI;
my $cgi = CGI->new;

# Set content type to HTML for the response
print $cgi->header('text/html');

# Begin HTML response
print $cgi->start_html(-title => "Form Submission Handler");

# Check if the request method is POST (form submission)
if ($cgi->request_method() eq 'POST') {
    # Retrieve form parameters
    my $name  = $cgi->param('name')  || '';
    my $email = $cgi->param('email') || '';
    my $message = $cgi->param('message') || '';

    # Validate input (basic example)
    if ($name eq '' || $email eq '' || $message eq '') {
        print $cgi->h1("Error: All fields are required.");
    } else {
        # Escape HTML entities to prevent XSS
        $name    = $cgi->escapeHTML($name);
        $email   = $cgi->escapeHTML($email);
        $message = $cgi->escapeHTML($message);

        # Display the submitted data
        print $cgi->h1("Form Submission Successful");
        print $cgi->p("Name: $name");
        print $cgi->p("Email: $email");
        print $cgi->p("Message: $message");

        # Here you can add logic to save this data to a database or send it via email.
    }
} else {
    # If request method is not POST, show a message
    print $cgi->h1("Error: Invalid request method");
    print $cgi->p("Please submit the form using the POST method.");
}

# End HTML response
print $cgi->end_html;

# Exit script successfully
exit 0;
```

Make sure this script is placed in the `cgi-bin` directory, and the server has permissions to execute it.
