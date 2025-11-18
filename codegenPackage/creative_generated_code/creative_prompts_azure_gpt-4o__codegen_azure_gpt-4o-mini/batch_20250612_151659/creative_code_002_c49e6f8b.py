"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defluo.hr
Prompt: Provide an example of a Perl script that can be executed from a "cgi-bin/" directory to process user input and display results.
Generated: DETERMINISTIC_c49e6f8be7389a1e
Batch ID: 20250612_151659
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
use CGI qw(:standard);

# Create a new CGI object
my $cgi = CGI->new;

# Print the HTTP header and start the HTML output
print $cgi->header('text/html');
print $cgi->start_html(-title => 'User Input Processing', -style => { -src => '/path/to/styles.css' });

# Check if the form is submitted
if ($cgi->param('submit')) {
    my $user_input = $cgi->param('user_input');

    # Validate the user input
    if (defined $user_input && $user_input ne '') {
        print $cgi->h2('Processed Input');
        print $cgi->p("You entered: " . $cgi->escapeHTML($user_input));
    } else {
        # Handle the case where no input is provided
        print $cgi->h2('Error');
        print $cgi->p("No input provided. Please go back and try again.");
    }
} else {
    # Display the input form
    print $cgi->h2('User Input Form');
    print $cgi->start_form(-method => 'POST');
    print $cgi->label('Enter something: ');
    print $cgi->textfield(-name => 'user_input', -size => 30);
    print $cgi->submit(-name => 'submit', -value => 'Submit');
    print $cgi->end_form;
}

# End the HTML output
print $cgi->end_html;
```
