"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bpearlegy.com
Prompt: Write a Perl CGI script to process user input and return a dynamically generated HTML response.
Generated: DETERMINISTIC_9ef1fad404c92666
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```perl
#!/usr/bin/perl

use strict;
use warnings;
use CGI qw(:standard);  # Import CGI module
use CGI::Carp qw(fatalsToBrowser);  # Enable error reporting in the browser

# Create a new CGI object
my $cgi = CGI->new;

# Print out the HTTP header
print $cgi->header('text/html');

# Get user input from the form
my $name = $cgi->param('name') // '';  # Use // to provide a default value if not set
my $age = $cgi->param('age') // '';

# Validate user input
my $error_msg = '';
if ($name eq '') {
    $error_msg .= "Name is required.<br>";
}
if ($age !~ /^\d+$/) {
    $error_msg .= "Age must be a number.<br>";
}

# Start generating HTML response
print $cgi->start_html(-title => 'User Input Response', -style => { -src => 'styles.css' });

# Check for errors in user input
if ($error_msg) {
    print $cgi->h1("Input Error");
    print $cgi->p($error_msg);
    print $cgi->p("Please go back and correct your input.");
    print $cgi->a({ -href => $cgi->url(-relative => 1) }, "Go Back");
} else {
    # If no errors, display the greeting
    print $cgi->h1("Hello, $name!");
    print $cgi->p("You are $age years old.");
}

# End HTML response
print $cgi->end_html;

# Notes:
# Make sure to have a form that posts name and age to this script.
# Example form:
# <form action="script.cgi" method="post">
#     Name: <input type="text" name="name"><br>
#     Age: <input type="text" name="age"><br>
#     <input type="submit" value="Submit">
# </form>
```
