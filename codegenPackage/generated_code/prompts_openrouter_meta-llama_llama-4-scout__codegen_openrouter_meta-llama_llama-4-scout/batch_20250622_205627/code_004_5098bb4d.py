"""
Generated Code Metadata:
========================
Original URL: https://refconegypt.net
Prompt: "Create a simple web interface using CGI and Perl to interact with the file system, inspired by the directory listing at https://refconegypt.net."
Generated: DETERMINISTIC_5098bb4d0ae6c1cf
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
use CGI qw(:standard);

# Check if the current directory is set, otherwise use the current working directory
my $directory = param('directory') || '.';

# Check if the directory exists
if (! -d $directory) {
    print header("text/html"), start_html("Error"), h1("Error"), p("The specified directory does not exist."), end_html();
    exit;
}

# Open the directory
opendir(my $dh, $directory) || do {
    print header("text/html"), start_html("Error"), h1("Error"), p("Failed to open the directory: $!"), end_html();
    exit;
};

# Read the directory contents
my @files;
my @dirs;
while (readdir($dh)) {
    next if /^\./; # Skip . and ..
    my $item = "$directory/$_";
    if (-f $item) {
        push @files, $_;
    } elsif (-d $item) {
        push @dirs, $_;
    }
}
closedir($dh);

# Sort the directory and file lists
@dirs = sort @dirs;
@files = sort @files;

# HTML header
print header("text/html"), start_html("Directory Listing");

# HTML body
print h1("Directory Listing for $directory");

# List directories
print h2("Directories:");
print ul();
foreach my $dir (@dirs) {
    print li(a($dir, href => "?directory=$directory/$dir"));
}
print end_ul();

# List files
print h2("Files:");
print ul();
foreach my $file (@files) {
    print li($file);
}
print end_ul();

# Link to parent directory
if ($directory ne '.') {
    my $parent_dir = $directory;
    $parent_dir =~ s/[^\/]+$//;
    $parent_dir ||= '/';
    print p(a("Parent Directory", href => "?directory=$parent_dir"));
}

print end_html();
```
