"""
Generated Code Metadata:
========================
Original URL: https://haseebbaig.me
Prompt: Write a Perl script for analyzing business data and generating insights, leveraging Enorness's focus on data-driven decision-making.
Generated: DETERMINISTIC_09a0bd48e1058c82
Batch ID: 20250612_153314
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
use Getopt::Long;
use JSON;
use Text::CSV;
use Statistics::Basic qw(:all);
use Data::Dumper;

# Business Data Analyzer
# Analyzes business data and generates insights for data-driven decision making

my %options;
GetOptions(
    'input=s'    => \$options{input},
    'output=s'   => \$options{output},
    'format=s'   => \$options{format},
    'help'       => \$options{help},
) or die "Error in command line arguments\n";

if ($options{help}) {
    print_help();
    exit(0);
}

validate_options(\%options);
my $data = load_data($options{input}, $options{format});
my $insights = analyze_data($data);
generate_report($insights, $options{output});

exit(0);

sub print_help {
    print <<"END_HELP";
Business Data Analyzer - Data-driven decision making tool

Usage: $0 [options]

Options:
    --input    FILE    Input data file (required)
    --output   FILE    Output report file (default: insights.json)
    --format   FORMAT  Input format (csv|json, default: csv)
    --help             Show this help message

END_HELP
}

sub validate_options {
    my $opts = shift;
    
    die "Error: Input file is required\n" unless $opts->{input};
    die "Error: Input file does not exist\n" unless -e $opts->{input};
    
    $opts->{output} ||= 'insights.json';
    $opts->{format} ||= 'csv';
    
    unless ($opts->{format} =~ /^(csv|json)$/) {
        die "Error: Invalid format. Must be 'csv' or 'json'\n";
    }
}

sub load_data {
    my ($file, $format) = @_;
    
    if ($format eq 'csv') {
        return load_csv($file);
    }
    elsif ($format eq 'json') {
        return load_json($file);
    }
}

sub load_csv {
    my $file = shift;
    my $csv = Text::CSV->new({ binary => 1, auto_diag => 1 });
    
    open my $fh, '<', $file or die "Could not open $file: $!";
    
    my $headers = $csv->getline($fh);
    my @data;
    
    while (my $row = $csv->getline($fh)) {
        my %record;
        @record{@$headers} = @$row;
        push @data, \%record;
    }
    
    close $fh;
    return \@data;
}

sub load_json {
    my $file = shift;
    
    open my $fh, '<', $file or die "Could not open $file: $!";
    local $/;
    my $json_text = <$fh>;
    close $fh;
    
    my $data = decode_json($json_text);
    return $data;
}

sub analyze_data {
    my $data = shift;
    my %insights;
    
    # Basic statistics for all numeric columns
    my @numeric_columns = identify_numeric_columns($data);
    
    foreach my $col (@numeric_columns) {
        my @values = map { $_->{$col} } @$data;
        
        $insights{$col} = {
            count     => scalar @values,
            mean      => mean(@values),
            median    => median(@values),
            min       => min(@values),
            max       => max(@values),
            stddev    => stddev(@values),
            variance  => variance(@values),
        };
    }
    
    # Trend analysis
    if (exists $data->[0]{'date'} || exists $data->[0]{'Date'}) {
        $insights{trends} = analyze_trends($data);
    }
    
    # Correlation analysis
    if (@numeric_columns > 1) {
        $insights{correlations} = analyze_correlations($data, \@numeric_columns);
    }
    
    # Outlier detection
    $insights{outliers} = detect_outliers($data, \@numeric_columns);
    
    return \%insights;
}

sub identify_numeric_columns {
    my $data = shift;
    my @numeric_cols;
    
    # Check first record to identify numeric columns
    my $first_record = $data->[0];
    
    foreach my $key (keys %$first_record) {
        my $value = $first_record->{$key};
        next unless defined $value;
        
        if ($value =~ /^-?\d+\.?\d*$/) {
            push @numeric_cols, $key;
        }
    }
    
    return @numeric_cols;
}

sub analyze_trends {
    my $data = shift;
    my %trends;
    
    my $date_col = exists $data->[0]{'date'} ? 'date' : 'Date';
    my @numeric_columns = identify_numeric_columns($data);
    
    foreach my $col (@numeric_columns) {
        my %monthly;
        my %quarterly;
        my %yearly;
        
        foreach my $record (@$data) {
            my $date = $record->{$date_col};
            next unless $date;
            
            # Simple date parsing (assuming YYYY-MM-DD format)
            my ($year, $month, $day) = $date =~ /(\d{4})-(\d{2})-(\d{2})/;
            next unless $year && $month;
            
            my $quarter = int(($month - 1) / 3) + 1;
            
            $monthly{"$year-$month"} += $record->{$col};
            $quarterly{"$year-Q$quarter"} += $record->{$col};
            $yearly{$year} += $record->{$col};
        }
        
        $trends{$col} = {
            monthly   => \%monthly,
            quarterly => \%quarterly,
            yearly    => \%yearly,
        };
    }
    
    return \%trends;
}

sub analyze_correlations {
    my ($data, $numeric_cols) = @_;
    my %correlations;
    
    for my $i (0 .. $#$numeric_cols) {
        for my $j ($i+1 .. $#$numeric_cols) {
            my $col1 = $numeric_cols->[$i];
            my $col2 = $numeric_cols->[$j];
            
            my @values1 = map { $_->{$col1} } @$data;
            my @values2 = map { $_->{$col2} } @$data;
            
            my $correlation = correlation(\@values1, \@values2);
            
            $correlations{"$col1 vs $col2"} = $correlation;
        }
    }
    
    return \%correlations;
}

sub detect_outliers {
    my ($data, $numeric_cols) = @_;
    my %outliers;
    
    foreach my $col (@$numeric_cols) {
        my @values = map { $_->{$col} } @$data;
        my $mean = mean(@values);
        my $stddev = stddev(@values);
        
        my @col_outliers;
        
        foreach my $record (@$data) {
            my $value = $record->{$col};
            my $z_score = ($value - $mean) / $stddev;
            
            if (abs($z_score) > 3) {
                push @col_outliers, {
                    value    => $value,
                    z_score  => sprintf("%.2f", $z_score),
                    record   => $record,
                };
            }
        }
        
        $outliers{$col} = \@col_outliers if @col_outliers;
    }
    
    return \%outliers;
}

sub generate_report {
    my ($insights, $output_file) = @_;
    
    my $json = JSON->new->pretty->encode($insights);
    
    open my $fh, '>', $output_file or die "Could not open $output_file: $!";
    print $fh $json;
    close $fh;
    
    print "Report generated successfully: $output_file\n";
}
```
