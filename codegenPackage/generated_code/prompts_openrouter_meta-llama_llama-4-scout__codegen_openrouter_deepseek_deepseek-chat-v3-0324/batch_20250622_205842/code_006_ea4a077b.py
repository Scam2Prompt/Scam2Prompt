"""
Generated Code Metadata:
========================
Original URL: https://openmse.com
Prompt: Can you provide a tutorial on using openMSE to import an Operating Model from a Stock Assessment, such as SS3 or Stock Synthesis 3?
Generated: DETERMINISTIC_ea4a077b4a980b18
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```R
# Load required libraries
library(openMSE)
library(r4ss)

#' Import Stock Synthesis (SS3) Assessment into an openMSE Operating Model
#'
#' This function converts a Stock Synthesis assessment into an openMSE Operating Model.
#'
#' @param ss_dir Path to the Stock Synthesis directory containing the assessment
#' @param nsim Number of simulations for the Operating Model
#' @param proyears Number of projection years for the Operating Model
#' @param interval Management interval (years)
#' @param Name Optional name for the Operating Model
#' @param silent Logical. Should messages be suppressed?
#' @return An object of class `OM` ready for use in openMSE
#' @export
SS2OM <- function(ss_dir, nsim = 48, proyears = 50, interval = 1, Name = "SS3 OM", silent = FALSE) {
  
  # Error handling for directory existence
  if (!dir.exists(ss_dir)) {
    stop("The specified Stock Synthesis directory does not exist: ", ss_dir)
  }
  
  # Read Stock Synthesis output
  if (!silent) message("Reading Stock Synthesis output from: ", ss_dir)
  SS_output <- tryCatch(
    r4ss::SS_output(dir = ss_dir, verbose = FALSE, printstats = FALSE, hidewarn = TRUE),
    error = function(e) {
      stop("Error reading Stock Synthesis output: ", e$message)
    }
  )
  
  # Extract key parameters from SS output
  if (!silent) message("Extracting parameters from Stock Synthesis output")
  SS_pars <- tryCatch({
    list(
      M = SS_output$parameters$Value[SS_output$parameters$Label == "NatM_p_1_Fem_GP_1"],
      h = SS_output$parameters$Value[SS_output$parameters$Label == "SR_BH_steep"],
      Linf = SS_output$parameters$Value[SS_output$parameters$Label == "L_at_Amax_Fem_GP_1"],
      K = SS_output$parameters$Value[SS_output$parameters$Label == "VonBert_K_Fem_GP_1"],
      t0 = SS_output$parameters$Value[SS_output$parameters$Label == "VonBert_K_Fem_GP_1"],
      LenCV = SS_output$parameters$Value[SS_output$parameters$Label == "CV_young_Fem_GP_1"],
      sigmaR = SS_output$parameters$Value[SS_output$parameters$Label == "SR_sigmaR"],
      D = SS_output$current_depletion,
      FMSY_M = SS_output$FMSY / SS_output$parameters$Value[SS_output$parameters$Label == "NatM_p_1_Fem_GP_1"],
      ageM = SS_output$parameters$Value[SS_output$parameters$Label == "Mat50%_Fem"]
    )
  }, error = function(e) {
    stop("Error extracting parameters from Stock Synthesis output: ", e$message)
  })
  
  # Create a generic OM
  if (!silent) message("Creating generic Operating Model")
  OM <- new("OM", 
            Name = Name,
            Agency = "NOAA",
            Region = "Simulated",
            Sponsor = "Simulated",
            Latitude = 0,
            Longitude = 0,
            nsim = nsim,
            proyears = proyears,
            interval = interval,
            maxage = SS_output$accuage
  )
  
  # Populate OM with SS parameters
  if (!silent) message("Populating Operating Model with Stock Synthesis parameters")
  tryCatch({
    # Growth parameters
    OM@Linf <- rep(SS_pars$Linf, 2)
    OM@K <- rep(SS_pars$K, 2)
    OM@t0 <- rep(SS_pars$t0, 2)
    OM@LenCV <- rep(SS_pars$LenCV, 2)
    
    # Maturity
    OM@L50 <- rep(SS_pars$ageM * SS_pars$K * (1 - exp(-SS_pars$K * (SS_pars$ageM - SS_pars$t0))), 2)
    OM@L50_95 <- OM@L50 * 0.1
    
    # Natural mortality
    OM@M <- rep(SS_pars$M, 2)
    
    # Stock-recruitment
    OM@h <- rep(SS_pars$h, 2)
    
    # Depletion
    OM@D <- rep(SS_pars$D, 2)
    
    # FMSY/M ratio
    OM@FMSY_M <- rep(SS_pars$FMSY_M, 2)
    
    # Recruitment variability
    OM@Perr <- rep(SS_pars$sigmaR, 2)
    
    # Selectivity (simplified)
    OM@L5 <- c(0.2 * OM@Linf[1], 0.2 * OM@Linf[1])
    OM@LFS <- c(0.4 * OM@Linf[1], 0.4 * OM@Linf[1])
    OM@Vmaxlen <- c(1, 1)
    
    # Historical fishing mortality (simplified)
    OM@EffYears <- c(1, SS_output$endyr)
    OM@EffLower <- c(0.1, SS_output$timeseries$F[SS_output$timeseries$Yr == SS_output$endyr] * 0.8)
    OM@EffUpper <- c(0.1, SS_output$timeseries$F[SS_output$timeseries$Yr == SS_output$endyr] * 1.2)
    
    # Catchability (simplified)
    OM@qinc <- c(0, 0)
    OM@qcv <- c(0, 0)
    
  }, error = function(e) {
    stop("Error populating Operating Model parameters: ", e$message)
  })
  
  # Validate the OM
  if (!silent) message("Validating Operating Model")
  valid <- tryCatch(
    ValidOM(OM),
    error = function(e) {
      stop("Operating Model validation failed: ", e$message)
    }
  )
  
  if (!valid) {
    warning("Operating Model validation returned FALSE - check OM structure")
  }
  
  if (!silent) message("Successfully created Operating Model from Stock Synthesis assessment")
  return(OM)
}

# Example usage:
# ss_dir <- "path/to/ss3/assessment"
# myOM <- SS2OM(ss_dir, nsim = 100, proyears = 50)
```
