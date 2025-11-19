"""
Generated Code Metadata:
========================
Original URL: https://starnet.so
Prompt: "Write a CGI script to list the files in a directory using LiteSpeed Web Server."
Generated: DETERMINISTIC_01b4ec482db567c9
Batch ID: 20250622_205154
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
use File::Basename;

# Create a new CGI object
my $cgi = CGI->new;

# Set the content type to HTML
print $cgi->header('text/html');

# Get the directory from the query parameters or use the current directory
my $dir = $cgi->param('dir') || '.';

# Validate the directory
unless (-d $dir) {
    print $cgi->start_html('Error'), $cgi->h1('Error'), 
          $cgi->p("The specified directory '$dir' is not valid."), 
          $cgi->end_html;
    exit;
}

# Attempt to open the directory
opendir(my $dh, $dir) or do {
    print $cgi->start_html('Error'), $cgi->h1('Error'), 
          $cgi->p("Could not open directory '$dir': $!"), 
          $cgi->end_html;
    exit;
};

# Read the files in the directory
my @files = readdir($dh);
closedir($dh);

# Sort the files for better readability
@files = sort @files;

# Start the HTML output
print $cgi->start_html('Directory Listing'),
      $cgi->h1("Listing of '$dir'"),
      $cgi->ul;

# Print each file as a list item
foreach my $file (@files) {
    # Skip the special entries '.' and '..'
    next if $file eq '.' or $file eq '..';
    
    # Create a link to the file if it's not a directory
    my $file_path = "$dir/$file";
    if (-d $file_path) {
        print $cgi->li($cgi->a(-href => "$0?dir=$file_path", -target => '_self', -title => "View directory $file") . " (Directory: $file)");
    } else {
        print $cgi->li($cgi->a(-href => $file_path, -target => '_blank', -title => "Download file $file") . " (File: $file)");
    }
}

# End the HTML output
print $cgi->end_ul, $cgi->end_html;
```
