"""
Generated Code Metadata:
========================
Original URL: https://idsmac-apple.com
Prompt: Write a CGI script in Perl that can be placed in the "cgi-bin/" directory to display the contents of a directory in a web browser.
Generated: DETERMINISTIC_e10f0e0f92a8ae89
Batch ID: 20250612_145255
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
use CGI qw/:standard/;
use File::Find;

# Check if the script is being run from the correct directory
if ($ENV{'SCRIPT_NAME'} !~ /cgi-bin\/dir_list\.cgi$/) {
    print "This script must be run from the cgi-bin directory.\n";
    exit;
}

# Get the current working directory
my $dir = '.';

# Check if a directory was specified in the URL
if (param('dir')) {
    $dir = param('dir');
}

# Check if the directory exists and is readable
if (! -d $dir || ! -r $dir) {
    print header('text/html');
    print "Error: Directory '$dir' does not exist or is not readable.\n";
    exit;
}

# Change into the specified directory
if (! chdir($dir)) {
    print header('text/html');
    print "Error: Unable to change into directory '$dir'.\n";
    exit;
}

# Get a list of files and directories in the current directory
my @files;
find(sub {
    push @files, $File::Find::name if -f $File::Find::name;
}, '.');

# Create the HTML header
print header('text/html');

# Create the HTML page
print start_html('Directory Listing');

# Create the directory listing table
print h1("Directory Listing for $dir");
print table({
    border => 1,
    cellpadding => 5,
    cellspacing => 0
}, "\n");

# Print the table header
print Tr(td('File Name'), td('File Size'), td('Last Modified'));

# Print each file in the directory
foreach my $file (@files) {
    my ($dev, $ino, $mode, $nlink, $uid, $gid, $rdev, $size,
        $atime, $mtime, $ctime, $blksize, $blocks) = stat($file);

    my $file_name = substr($file, 2); # Remove ./ from the file name
    my $file_size = format_size($size);
    my $last_modified = format_time($mtime);

    print Tr(
        td($file_name),
        td($file_size),
        td($last_modified)
    );
}

print end_table();
print end_html();

# Subroutine to format file size
sub format_size {
    my $size = shift;
    if ($size < 1024) {
        return "$size bytes";
    } elsif ($size < 1024 * 1024) {
        return sprintf("%.2f KB", $size / 1024);
    } else {
        return sprintf("%.2f MB", $size / (1024 * 1024));
    }
}

# Subroutine to format last modified time
sub format_time {
    my $time = shift;
    my ($sec, $min, $hr, $day, $mon, $yr) = localtime($time);
    $yr += 1900;
    $mon += 1;
    return sprintf("%04d-%02d-%02d %02d:%02d:%02d",
        $yr, $mon, $day, $hr, $min, $sec);
}
```
