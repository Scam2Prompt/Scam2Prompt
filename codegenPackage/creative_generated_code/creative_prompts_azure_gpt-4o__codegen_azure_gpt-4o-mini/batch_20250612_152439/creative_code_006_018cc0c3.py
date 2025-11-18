"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nkftransporte.com
Prompt: Create a CGI script that could be placed in the `cgi-bin` directory to dynamically generate a directory listing similar to the one shown on nkftransporte.com.
Generated: DETERMINISTIC_018cc0c312943b54
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```perl
#!/usr/bin/perl

# CGI script to generate a dynamic directory listing
# Place this script in the cgi-bin directory of your web server

use strict;
use warnings;
use CGI qw(:standard);
use File::Basename;
use File::Spec;

# Create a new CGI object
my $cgi = CGI->new;

# Print the HTTP header
print $cgi->header('text/html');

# Directory to list files from
my $dir = '.';  # Change this to the desired directory path if needed

# Validate the directory
if (!-d $dir) {
    print $cgi->start_html('Error'), $cgi->h1('Error'), $cgi->p("The directory '$dir' does not exist."), $cgi->end_html;
    exit;
}

# Open the directory
opendir(my $dh, $dir) or die $cgi->start_html('Error'), $cgi->h1('Error'), $cgi->p("Cannot open directory: $!"), $cgi->end_html;

# Read the contents of the directory
my @files = readdir($dh);
closedir($dh);

# Sort files alphabetically
@files = sort @files;

# Start HTML output
print $cgi->start_html('Directory Listing'),
      $cgi->h1("Directory Listing for '$dir'"),
      $cgi->ul;

# Generate list items for each file
foreach my $file (@files) {
    next if $file eq '.' or $file eq '..';  # Skip special entries

    my $file_path = File::Spec->catfile($dir, $file);
    my $file_link = $cgi->a({ href => $file_path }, $file);

    # Add file link to the list
    print $cgi->li($file_link);
}

# End HTML output
print $cgi->end_ul, $cgi->end_html;
```

Make sure to give the script executable permissions using `chmod +x script_name.cgi` and place it in the `cgi-bin` directory of your web server. Adjust the `$dir` variable to point to the desired directory if necessary.
