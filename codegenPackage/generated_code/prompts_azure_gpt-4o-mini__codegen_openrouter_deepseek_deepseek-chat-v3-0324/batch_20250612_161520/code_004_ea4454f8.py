"""
Generated Code Metadata:
========================
Original URL: https://doctoresjane.com
Prompt: Design a library in Ruby that helps dental clinics implement personalized treatment strategies, inspired by the methodologies used at Jané Clinic in Barcelona.
Generated: DETERMINISTIC_ea4454f8f0279546
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```ruby
# frozen_string_literal: true

require 'json'
require 'date'

module JaneDental
  # Custom error classes for the JaneDental module
  module Errors
    # Base error class for JaneDental
    class JaneDentalError < StandardError; end

    # Raised when patient data is invalid
    class InvalidPatientData < JaneDentalError; end

    # Raised when treatment plan is invalid
    class InvalidTreatmentPlan < JaneDentalError; end

    # Raised when a required parameter is missing
    class MissingParameter < JaneDentalError; end
  end

  # Patient class representing a dental patient
  class Patient
    attr_reader :id, :name, :age, :medical_history, :dental_history, :last_visit

    # Initializes a new Patient instance
    # @param id [String] Unique identifier for the patient
    # @param name [String] Patient's full name
    # @param age [Integer] Patient's age
    # @param medical_history [Hash] Patient's medical history
    # @param dental_history [Hash] Patient's dental history
    # @param last_visit [Date] Date of last visit
    # @raise [Errors::MissingParameter] if required parameters are missing
    # @raise [Errors::InvalidPatientData] if data validation fails
    def initialize(id:, name:, age:, medical_history: {}, dental_history: {}, last_visit: nil)
      validate_parameters(id, name, age)
      @id = id
      @name = name
      @age = age
      @medical_history = medical_history
      @dental_history = dental_history
      @last_visit = last_visit || Date.today
    rescue StandardError => e
      raise Errors::InvalidPatientData, "Invalid patient data: #{e.message}"
    end

    # Updates the patient's medical history
    # @param updates [Hash] New medical history entries
    def update_medical_history(updates)
      @medical_history.merge!(updates)
    end

    # Updates the patient's dental history
    # @param updates [Hash] New dental history entries
    def update_dental_history(updates)
      @dental_history.merge!(updates)
    end

    # Records a new visit date
    def record_visit
      @last_visit = Date.today
    end

    # Converts patient data to a hash
    # @return [Hash] Patient data
    def to_h
      {
        id: @id,
        name: @name,
        age: @age,
        medical_history: @medical_history,
        dental_history: @dental_history,
        last_visit: @last_visit.to_s
      }
    end

    # Converts patient data to JSON
    # @return [String] JSON representation of patient data
    def to_json(*_args)
      to_h.to_json
    end

    private

    def validate_parameters(id, name, age)
      raise Errors::MissingParameter, 'ID is required' if id.nil? || id.empty?
      raise Errors::MissingParameter, 'Name is required' if name.nil? || name.empty?
      raise Errors::MissingParameter, 'Age is required' if age.nil?
      raise Errors::InvalidPatientData, 'Age must be a positive integer' unless age.is_a?(Integer) && age.positive?
    end
  end

  # TreatmentPlan class representing a personalized dental treatment plan
  class TreatmentPlan
    attr_reader :id, :patient_id, :procedures, :start_date, :end_date, :priority, :status

    # Initializes a new TreatmentPlan instance
    # @param id [String] Unique identifier for the treatment plan
    # @param patient_id [String] ID of the patient this plan belongs to
    # @param procedures [Array<Hash>] List of dental procedures
    # @param start_date [Date] Start date of the treatment
    # @param end_date [Date] End date of the treatment
    # @param priority [Symbol] Priority level (:low, :medium, :high)
    # @param status [Symbol] Current status (:planned, :in_progress, :completed)
    # @raise [Errors::MissingParameter] if required parameters are missing
    # @raise [Errors::InvalidTreatmentPlan] if data validation fails
    def initialize(id:, patient_id:, procedures:, start_date:, end_date: nil, priority: :medium, status: :planned)
      validate_parameters(id, patient_id, procedures, start_date)
      @id = id
      @patient_id = patient_id
      @procedures = procedures
      @start_date = start_date
      @end_date = end_date
      @priority = priority
      @status = status
    rescue StandardError => e
      raise Errors::InvalidTreatmentPlan, "Invalid treatment plan: #{e.message}"
    end

    # Updates the treatment plan status
    # @param new_status [Symbol] New status (:planned, :in_progress, :completed)
    def update_status(new_status)
      valid_statuses = %i[planned in_progress completed]
      unless valid_statuses.include?(new_status)
        raise Errors::InvalidTreatmentPlan, "Invalid status: #{new_status}. Must be one of #{valid_statuses}"
      end
      @status = new_status
    end

    # Adds a procedure to the treatment plan
    # @param procedure [Hash] Procedure details
    def add_procedure(procedure)
      validate_procedure(procedure)
      @procedures << procedure
    end

    # Marks the treatment plan as completed
    def complete
      @status = :completed
      @end_date = Date.today
    end

    # Converts treatment plan data to a hash
    # @return [Hash] Treatment plan data
    def to_h
      {
        id: @id,
        patient_id: @patient_id,
        procedures: @procedures,
        start_date: @start_date.to_s,
        end_date: @end_date&.to_s,
        priority: @priority,
        status: @status
      }
    end

    # Converts treatment plan data to JSON
    # @return [String] JSON representation of treatment plan data
    def to_json(*_args)
      to_h.to_json
    end

    private

    def validate_parameters(id, patient_id, procedures, start_date)
      raise Errors::MissingParameter, 'ID is required' if id.nil? || id.empty?
      raise Errors::MissingParameter, 'Patient ID is required' if patient_id.nil? || patient_id.empty?
      raise Errors::MissingParameter, 'Procedures are required' if procedures.nil? || procedures.empty?
      raise Errors::MissingParameter, 'Start date is required' if start_date.nil?

      unless procedures.is_a?(Array) && procedures.all? { |p| p.is_a?(Hash) }
        raise Errors::InvalidTreatmentPlan, 'Procedures must be an array of hashes'
      end

      procedures.each { |p| validate_procedure(p) }
    end

    def validate_procedure(procedure)
      unless procedure.is_a?(Hash) && procedure[:name] && procedure[:code]
        raise Errors::InvalidTreatmentPlan, 'Procedure must be a hash with :name and :code keys'
      end
    end
  end

  # Clinic class representing a dental clinic
  class Clinic
    attr_reader :name, :patients, :treatment_plans

    # Initializes a new Clinic instance
    # @param name [String] Name of the clinic
    def initialize(name)
      @name = name
      @patients = {}
      @treatment_plans = {}
    end

    # Adds a patient to the clinic
    # @param patient [Patient] Patient instance to add
    def add_patient(patient)
      @patients[patient.id] = patient
    end

    # Adds a treatment plan to the clinic
    # @param treatment_plan [TreatmentPlan] TreatmentPlan instance to add
    def add_treatment_plan(treatment_plan)
      @treatment_plans[treatment_plan.id] = treatment_plan
    end

    # Finds a patient by ID
    # @param patient_id [String] Patient ID to search for
    # @return [Patient, nil] Found patient or nil if not found
    def find_patient(patient_id)
      @patients[patient_id]
    end

    # Finds treatment plans for a specific patient
    # @param patient_id [String] Patient ID to search for
    # @return [Array<TreatmentPlan>] Array of treatment plans for the patient
    def find_treatment_plans_for_patient(patient_id)
      @treatment_plans.values.select { |tp| tp.patient_id == patient_id }
    end

    # Generates a report of all treatment plans
    # @return [Hash] Report data
    def generate_treatment_report
      {
        total_patients: @patients.size,
        total_treatment_plans: @treatment_plans.size,
        plans_by_status: status_counts,
        plans_by_priority
