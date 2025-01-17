# Patient Insurance Cost Estimator

This project defines a `Patient` class in Python to represent patient medical information and estimate their insurance costs based on a simplified formula. It's a basic example demonstrating object-oriented programming concepts and can be used as a starting point for more complex healthcare-related applications.

## Features

*   **Patient Class:** Represents a patient with attributes like name, age, sex, BMI, number of children, and smoker status.
*   **Insurance Cost Estimation:** Calculates an estimated insurance cost using a predefined formula (note that this is a simplified estimation and not based on real-world insurance calculations).
*   **Data Update:** Allows updating a patient's age and number of children.
*   **Patient Profile:** Generates a dictionary containing the patient's information.

## Getting Started

### Prerequisites

*   Python 3.x installed on your system.

### Usage

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    ```

    (Replace `<repository_url>` with the actual URL of your GitHub repository).

2.  **Navigate to the project directory:**

    ```bash
    cd patient-insurance-cost-estimator 
    ```
    (Replace `patient-insurance-cost-estimator` with your directory name)

3.  **Run the Python script:**
    ```bash
    python patient_insurance.py
    ```
    (replace `patient_insurance.py` with the name of your python file)

    This will create a `Patient` object, update its number of children, estimate the insurance cost, and print the patient's profile.

## Code Structure

*   **`patient_insurance.py`:** (Or the name you gave to your python file) Contains the `Patient` class definition and the example usage code.

### `Patient` Class

#### Attributes

*   `name` (str): Patient's full name.
*   `age` (int): Patient's age in years.
*   `sex` (int): Patient's sex (0 for female, 1 for male).
*   `bmi` (float): Patient's body mass index.
*   `num_of_children` (int): Number of children the patient has.
*   `smoker` (int): Smoker status (0 for non-smoker, 1 for smoker).

#### Methods

*   `__init__(self, name, age, sex, bmi, num_of_children, smoker)`: Constructor to initialize a `Patient` object.
*   `__str__(self)`: Returns a string representation of the `Patient` object.
*   `estimated_insurance_cost(self)`: Estimates the insurance cost and prints it.
*   `update_age(self, new_age)`: Updates the patient's age.
*   `update_num_children(self, new_num_children)`: Updates the number of children.
*   `patient_profile(self)`: Returns a dictionary with the patient's information.

## Example Usage

```python
# Create a patient object
patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)

# Update the number of children
patient1.update_num_children(2)

# Estimate the insurance cost
patient1.estimated_insurance_cost()

# Print the patient's profile
print(patient1.patient_profile())
