class Patient:
    """
    Represents a patient with their medical information and provides methods
    to estimate insurance costs, update patient data, and create a patient profile.
    """

    def __init__(self, name, age, sex, bmi, num_of_children, smoker):
        """
        Initializes a new Patient object.

        Args:
            name (str): The patient's full name.
            age (int): The patient's age in years.
            sex (int): The patient's sex (0 for female, 1 for male).
            bmi (float): The patient's body mass index.
            num_of_children (int): The number of children the patient has.
            smoker (int): Whether the patient is a smoker (0 for non-smoker, 1 for smoker).
        """
        self.name = name
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.num_of_children = num_of_children
        self.smoker = smoker

    def __str__(self):
        """
        Returns a string representation of the Patient object.

        Returns:
            str: A string describing the patient's information.
        """
        return f"Patient: {self.name}, Age: {self.age}, Sex: {self.sex}, BMI: {self.bmi}, Children: {self.num_of_children}, Smoker: {self.smoker}"

    def estimated_insurance_cost(self):
        """
        Estimates the insurance cost for the patient based on their attributes.

        The formula used is a simplified estimation and may not reflect actual insurance costs.
        """
        estimated_cost = 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 12500
        print("{name}’s estimated insurance costs is {cost} dollars.".format(name=self.name, cost=estimated_cost))

    def update_age(self, new_age):
        """
        Updates the patient's age.

        Args:
            new_age (int): The patient's new age in years.
        """
        self.age = new_age
        print("{name} is now {age} years old.".format(name=self.name, age=new_age))

    def update_num_children(self, new_num_children):
        """
        Updates the number of children the patient has.

        Args:
            new_num_children (int): The new number of children.
        """
        self.num_of_children = new_num_children
        if self.num_of_children > 1:
            print("{name} has {children} children.".format(name=self.name, children=new_num_children))
        else:
            print("{name} has {children} child.".format(name=self.name, children=new_num_children))

    def patient_profile(self):
        """
        Creates a dictionary containing the patient's profile information.

        Returns:
            dict: A dictionary with the patient's name, age, sex, BMI, number of children, and smoker status.
        """
        patient_information = {}
        patient_information["Name"] = self.name
        patient_information["Age"] = self.age
        patient_information["Sex"] = self.sex
        patient_information["BMI"] = self.bmi
        patient_information["Number of Children"] = self.num_of_children
        patient_information["Smoker"] = self.smoker
        return patient_information


# Example usage:
patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)
patient1.update_num_children(20)
patient1.estimated_insurance_cost()
print(patient1.patient_profile())
