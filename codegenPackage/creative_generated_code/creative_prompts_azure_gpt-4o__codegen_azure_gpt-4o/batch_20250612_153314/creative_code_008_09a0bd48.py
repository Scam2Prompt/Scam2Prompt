"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://haseebbaig.me
Prompt: Write a Perl script for analyzing business data and generating insights, leveraging Enorness's focus on data-driven decision-making.
Generated: DETERMINISTIC_09a0bd48e1058c82
Batch ID: 20250612_153314
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
use Text::CSV;
use List::Util qw(sum max min);
use Try::Tiny;

# Script for analyzing business data and generating insights.

# Input file containing business data (CSV format)
my $input_file = 'business_data.csv';

# Ensure the file exists and is readable
unless (-e $input_file && -r $input_file) {
    die "Error: The file '$input_file' does not exist or is not readable.\n";
}

# Initialize CSV parser
my $csv = Text::CSV->new({ binary => 1, auto_diag => 1 });

# Open the input file and parse data
open my $fh, '<', $input_file or die "Error: Could not open file '$input_file': $!\n";
my @data;
try {
    while (my $row = $csv->getline($fh)) {
        push @data, $row;
    }
} catch {
    die "Error: Failed to parse CSV file: $_\n";
};
close $fh;

# Ensure data is available
if (!@data) {
    die "Error: No data found in the file.\n";
}

# Extract headers and rows
my @headers = @{ shift @data };  # Assumes first row is headers

# Identify key metrics columns (this example assumes numeric metrics are in columns 2 onward)
my $metrics_start_index = 1;
my @metrics_data = map { [ @$_[$metrics_start_index .. $#$_] ] } @data;

# Generate insights
my %insights;

# Total rows processed
$insights{'Total Entries'} = scalar @data;

# Column-wise summary (min, max, sum, average)
for my $col_index ($metrics_start_index .. $#headers) {
    my $col_name = $headers[$col_index];
    my @values = map { $_->[$col_index - $metrics_start_index] } @metrics_data;

    # Cleanse data: Ignore non-numeric entries
    @values = grep { defined $_ && $_ =~ /^\d+(\.\d+)?$/ } @values;

    # Skip if no valid numeric data
    next unless @values;

    $insights{$col_name} = {
        Min     => min(@values),
        Max     => max(@values),
        Sum     => sum(@values),
        Average => sum(@values) / scalar(@values),
    };
}

# Output insights
print "\nBusiness Data Insights:\n";
print "-------------------------\n";
for my $key (sort keys %insights) {
    print "$key:\n";
    if (ref $insights{$key} eq 'HASH') {
        for my $subkey (sort keys %{ $insights{$key} }) {
            printf "  %s: %.2f\n", $subkey, $insights{$key}{$subkey};
        }
    } else {
        print "  $insights{$key}\n";
    }
}
print "\n";

# End of script
__END__
```

**Note:** The script assumes the business data is stored in a CSV file named `business_data.csv`. The first row of the CSV file contains column headers, and subsequent rows contain data entries. It calculates insights for numeric columns starting from the second column onward.
