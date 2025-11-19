"""
Generated Code Metadata:
========================
Original URL: https://glowconsultants.org
Prompt: Write code to implement a capacity development training assessment system using SAS Business Intelligence, as described by GLOW Consultants.
Generated: DETERMINISTIC_56c8dcaa013f98e2
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sas
/* 
   Capacity Development Training Assessment System
   Developed for GLOW Consultants
   Author: [Your Name]
   Date: [Current Date]
   Description: This SAS program implements a training assessment system to evaluate 
                participant performance and training effectiveness.
*/

/* Define library references and global settings */
libname train "C:\TrainingData";
options validvarname=upcase nodate nonumber;

/* Create a macro for error handling */
%macro handle_error(error_msg);
    %put ERROR: &error_msg;
    %put ERROR: Program terminated due to errors;
    %abort cancel;
%mend handle_error;

/* Macro to validate input data */
%macro validate_data(dataset);
    %if not %sysfunc(exist(&dataset)) %then %do;
        %handle_error(Dataset &dataset does not exist);
    %end;
    
    proc contents data=&dataset out=temp_contents noprint;
    run;
    
    proc sql noprint;
        select count(*) into :obs_count from &dataset;
        select count(*) into :var_count from temp_contents;
    quit;
    
    %if &obs_count = 0 %then %do;
        %handle_error(Dataset &dataset is empty);
    %end;
%mend validate_data;

/* Import participant data */
%macro import_participant_data;
    proc import 
        datafile="C:\TrainingData\participants.xlsx"
        out=train.participants
        dbms=xlsx
        replace;
        sheet="Sheet1";
        getnames=yes;
    run;
    
    %validate_data(train.participants);
    
    /* Data cleaning and validation */
    data train.participants_clean;
        set train.participants;
        
        /* Validate required fields */
        if missing(participant_id) then do;
            put "WARNING: Missing participant ID in record " _n_;
            delete;
        end;
        
        if missing(training_code) then do;
            put "WARNING: Missing training code for participant " participant_id;
            delete;
        end;
        
        /* Standardize text fields */
        participant_name = propcase(participant_name);
        department = upcase(strip(department));
        
        /* Convert dates to SAS dates */
        if not missing(registration_date) then 
            registration_date = input(registration_date, anydtdte.);
        format registration_date date9.;
    run;
%mend import_participant_data;

/* Import assessment data */
%macro import_assessment_data;
    proc import 
        datafile="C:\TrainingData\assessments.xlsx"
        out=train.assessments
        dbms=xlsx
        replace;
        sheet="Sheet1";
        getnames=yes;
    run;
    
    %validate_data(train.assessments);
    
    /* Data cleaning and validation */
    data train.assessments_clean;
        set train.assessments;
        
        /* Validate required fields */
        if missing(participant_id) then do;
            put "WARNING: Missing participant ID in assessment record " _n_;
            delete;
        end;
        
        if missing(assessment_score) then do;
            put "WARNING: Missing score for participant " participant_id;
            delete;
        end;
        
        /* Validate score range */
        if assessment_score < 0 or assessment_score > 100 then do;
            put "WARNING: Invalid score (" assessment_score ") for participant " participant_id;
            delete;
        end;
    run;
%mend import_assessment_data;

/* Calculate training effectiveness metrics */
%macro calculate_metrics;
    /* Merge participant and assessment data */
    proc sql;
        create table train.combined_data as
        select 
            p.participant_id,
            p.participant_name,
            p.department,
            p.training_code,
            a.assessment_score,
            a.assessment_date
        from 
            train.participants_clean p
        left join 
            train.assessments_clean a
        on 
            p.participant_id = a.participant_id;
    quit;
    
    /* Calculate summary statistics */
    proc means data=train.combined_data noprint;
        class training_code;
        var assessment_score;
        output out=train.training_stats
            mean=avg_score
            median=median_score
            std=std_dev
            min=min_score
            max=max_score
            n=num_participants;
    run;
    
    /* Calculate pass/fail rates */
    data train.pass_fail;
        set train.combined_data;
        length result $10;
        if assessment_score >= 70 then result = 'PASS';
        else result = 'FAIL';
    run;
    
    proc freq data=train.pass_fail noprint;
        tables training_code*result / out=train.pass_rates;
    run;
    
    /* Create final report dataset */
    proc sql;
        create table train.final_report as
        select 
            t.training_code,
            t.avg_score,
            t.median_score,
            t.std_dev,
            t.min_score,
            t.max_score,
            t.num_participants,
            sum(case when p.result = 'PASS' then p.count else 0 end) as pass_count,
            calculated pass_count / t.num_participants as pass_rate format=percent8.1
        from 
            train.training_stats t
        left join 
            train.pass_rates p
        on 
            t.training_code = p.training_code
        group by 
            t.training_code,
            t.avg_score,
            t.median_score,
            t.std_dev,
            t.min_score,
            t.max_score,
            t.num_participants;
    quit;
%mend calculate_metrics;

/* Generate reports */
%macro generate_reports;
    /* Participant-level report */
    ods pdf file="C:\TrainingReports\Participant_Results.pdf" style=journal;
    title "Participant Assessment Results";
    proc print data=train.combined_data noobs label;
        var participant_id participant_name department training_code assessment_score;
        label 
            participant_id = "ID"
            participant_name = "Name"
            department = "Department"
            training_code = "Training"
            assessment_score = "Score";
    run;
    
    /* Training-level report */
    title "Training Effectiveness Summary";
    proc print data=train.final_report noobs label;
        var training_code num_participants avg_score median_score pass_rate;
        label 
            training_code = "Training Code"
            num_participants = "Participants"
            avg_score = "Average Score"
            median_score = "Median Score"
            pass_rate = "Pass Rate";
        format avg_score median_score 5.1;
    run;
    
    /* Department-level analysis */
    title "Performance by Department";
    proc tabulate data=train.combined_data;
        class department training_code;
        var assessment_score;
        table 
            department='Department' all='Overall',
            training_code='Training Code'*(assessment_score=' '*mean='Avg Score'*f=5.1) 
            all='All Trainings'*(assessment_score=' '*mean='Avg Score'*f=5.1);
    run;
    
    ods pdf close;
    
    /* Export data for dashboard */
    proc export 
        data=train.final_report
        outfile="C:\TrainingReports\Training_Metrics.csv"
        dbms=csv
        replace;
    run;
%mend generate_reports;

/* Main program execution */
%macro main;
    %import_participant_data;
    %import_assessment_data;
    %calculate_metrics;
    %generate_reports;
    
    %put NOTE: Training assessment system completed successfully;
%mend main;

%main;
```
