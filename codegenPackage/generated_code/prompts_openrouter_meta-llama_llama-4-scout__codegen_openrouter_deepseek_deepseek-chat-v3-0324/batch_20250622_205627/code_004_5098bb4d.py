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
use File::Basename;
use File::Spec::Functions;
use Cwd 'abs_path';

# Configuration
my $BASE_DIR = '/var/www/html/files';  # Change this to your desired base directory
my $TITLE = 'File Browser';

# Security check to prevent directory traversal
sub is_safe_path {
    my $path = shift;
    my $abs_base = abs_path($BASE_DIR);
    my $abs_path = abs_path($path);
    return $abs_path =~ /^\Q$abs_base\E/;
}

# Main CGI handler
print header(-charset => 'utf-8');
print start_html(-title => $TITLE, -style => { -code => get_css() });

my $current_dir = param('dir') || $BASE_DIR;
$current_dir = catdir($BASE_DIR, $current_dir) unless $current_dir eq $BASE_DIR;

unless (is_safe_path($current_dir)) {
    print h1('Access Denied'), p('Invalid directory path');
    print end_html;
    exit;
}

unless (-d $current_dir) {
    print h1('Error'), p('Directory does not exist');
    print end_html;
    exit;
}

display_directory($current_dir);
print end_html;

# Display directory contents
sub display_directory {
    my $dir = shift;
    my $parent_dir = dirname($dir);
    
    print h1('Directory: ', $dir);
    
    # Navigation breadcrumbs
    print p(a({-href => "?dir=$BASE_DIR"}, 'Root'), ' / ');
    my @parts = File::Spec->splitdir($dir);
    shift @parts;  # Remove base dir
    my $path = $BASE_DIR;
    foreach my $part (@parts) {
        $path = catdir($path, $part);
        print a({-href => "?dir=$path"}, $part), ' / ';
    }
    print br;
    
    # Parent directory link
    if ($dir ne $BASE_DIR) {
        print p(a({-href => "?dir=$parent_dir"}, '.. (Parent Directory)'));
    }
    
    # Directory listing
    print start_table({-border => 1, -cellspacing => 0, -cellpadding => 5});
    print Tr(
        th('Name'),
        th('Size'),
        th('Type'),
        th('Modified'),
        th('Actions')
    );
    
    opendir(my $dh, $dir) or die "Can't open directory: $!";
    my @entries = readdir($dh);
    closedir($dh);
    
    foreach my $entry (sort @entries) {
        next if $entry eq '.';
        my $full_path = catfile($dir, $entry);
        next unless is_safe_path($full_path);
        
        my $is_dir = -d $full_path;
        my $size = $is_dir ? '-' : format_size(-s $full_path);
        my $type = $is_dir ? 'Directory' : 'File';
        my $mtime = localtime((stat($full_path))[9]);
        
        my $link = $is_dir 
            ? a({-href => "?dir=$full_path"}, $entry)
            : a({-href => $full_path, -target => '_blank'}, $entry);
            
        print Tr(
            td($link),
            td($size),
            td($type),
            td($mtime),
            td($is_dir ? '' : a({-href => "?download=1&file=$full_path"}, 'Download'))
        );
    }
    print end_table;
}

# Format file size in human-readable format
sub format_size {
    my $bytes = shift;
    return '0 B' if $bytes == 0;
    
    my @units = ('B', 'KB', 'MB', 'GB', 'TB');
    my $unit = 0;
    
    while ($bytes >= 1024 && $unit < $#units) {
        $bytes /= 1024;
        $unit++;
    }
    
    return sprintf('%.2f %s', $bytes, $units[$unit]);
}

# Handle file downloads
if (param('download')) {
    my $file = param('file');
    if ($file && is_safe_path($file) && -f $file) {
        my $basename = basename($file);
        print header(
            -type => 'application/octet-stream',
            -attachment => $basename,
            -Content_Length => -s $file
        );
        
        open(my $fh, '<', $file) or die "Can't open file: $!";
        binmode($fh);
        print while <$fh>;
        close($fh);
        exit;
    }
}

# CSS styles
sub get_css {
    return <<'END_CSS';
body {
    font-family: Arial, sans-serif;
    margin: 20px;
    line-height: 1.6;
}
h1 {
    color: #333;
}
table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
}
th {
    background-color: #f2f2f2;
    text-align: left;
    padding: 8px;
}
td {
    border: 1px solid #ddd;
    padding: 8px;
}
tr:nth-child(even) {
    background-color: #f9f9f9;
}
a {
    color: #0066cc;
    text-decoration: none;
}
a:hover {
    text-decoration: underline;
}
END_CSS
}
```
