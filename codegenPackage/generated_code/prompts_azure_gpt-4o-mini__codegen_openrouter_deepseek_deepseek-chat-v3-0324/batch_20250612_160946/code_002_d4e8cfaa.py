"""
Generated Code Metadata:
========================
Original URL: https://openmse.com
Prompt: Can you provide a code example for importing an operating model from Stock Synthesis 3 using openMSE?
Generated: DETERMINISTIC_d4e8cfaa0dca03e6
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```r
# Load required libraries
library(openMSE)
library(r4ss)

#' Import an operating model from Stock Synthesis 3
#'
#' @param ss3dir Path to the directory containing SS3 files
#' @param nsim Number of simulations for the operating model
#' @param proyears Number of projection years
#' @param reps Number of replicates per simulation
#' @param maxF Maximum F value for the operating model
#' @param seed Random seed for reproducibility
#' @param silent Logical. Should messages be suppressed?
#' @return An object of class 'OM' (operating model)
#' @export
import_ss3_om <- function(ss3dir, nsim = 48, proyears = 50, reps = 1, 
                         maxF = 3, seed = 1, silent = FALSE) {
  
  # Error handling
  if (!dir.exists(ss3dir)) {
    stop("SS3 directory does not exist: ", ss3dir)
  }
  
  if (!file.exists(file.path(ss3dir, "Report.sso"))) {
    stop("Report.sso file not found in directory: ", ss3dir)
  }
  
  # Set random seed for reproducibility
  set.seed(seed)
  
  # Read SS3 output files
  if (!silent) message("Reading SS3 output files...")
  replist <- r4ss::SS_output(dir = ss3dir, verbose = !silent, printstats = !silent)
  
  # Convert SS3 to OM
  if (!silent) message("Converting SS3 output to operating model...")
  OM <- SS2MOM(replist, nsim = nsim, proyears = proyears, reps = reps, 
               maxF = maxF, silent = silent)
  
  # Validate the OM
  if (!silent) message("Validating operating model...")
  valid <- validMSE(OM)
  if (!valid) {
    warning("Operating model validation failed. Check input parameters.")
  }
  
  return(OM)
}

# Example usage:
# om <- import_ss3_om("path/to/ss3/model", nsim = 50, proyears = 30)
```
