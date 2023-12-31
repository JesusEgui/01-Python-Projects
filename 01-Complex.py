This is the final name generator

import random
import string

print('''

  $$$$$$\                                               $$$$$$$$\                    $$\       
   \__$$ |                                              $$  _____|                   \__|      
      $$ | $$$$$$\   $$$$$$$\ $$\   $$\  $$$$$$$\       $$ |      $$$$$$\  $$\   $$\ $$\       
      $$ |$$  __$$\ $$  _____|$$ |  $$ |$$  _____|      $$$$$\   $$  __$$\ $$ |  $$ |$$ |      
$$\   $$ |$$$$$$$$ |\$$$$$$\  $$ |  $$ |\$$$$$$\        $$  __|  $$ /  $$ |$$ |  $$ |$$ |      
$$ |  $$ |$$   ____| \____$$\ $$ |  $$ | \____$$\       $$ |     $$ |  $$ |$$ |  $$ |$$ |      
\$$$$$$  |\$$$$$$$\ $$$$$$$  |\$$$$$$  |$$$$$$$  |      $$$$$$$$\\$$$$$$$ |\$$$$$$  |$$ |      
 \______/  \_______|\_______/  \______/ \_______/       \________|\____$$ | \______/ \__|      
                                                                 $$\   $$ |                    
                                                                 \$$$$$$  |                    
                                                                  \______/                                                                                                                          
      ''')

allowed_departments = ["Marketing", "Accounting", "FinOps"]

def generate_ec2_names(num_instances, department):
    department = department.title()
    
    if department not in allowed_departments:
        print("This Name Generator is only available for Marketing, Accounting, and FinOps departments.")
        return None

    ec2_names = []

    for _ in range(num_instances):
        random_chars = ''.join(random.choices(string.ascii_letters, k=3))
        random_numbers = ''.join(random.choices(string.digits, k=3))
        ec2_name = f"{department}-{random_chars}-{random_numbers}"
        ec2_names.append(ec2_name)

    return ec2_names

def execute_complex_generator():
    print("COMPLEX EC2 Random Name Generator")
    num_instances = int(input("How many EC2 instances do you want to name? "))
    department = input("Enter your department name (Marketing, Accounting, or FinOps): ")

    generated_names = generate_ec2_names(num_instances, department)

    if generated_names:
        print("Generated EC2 names:")
        for name in generated_names:
            print(name)

execute_complex_generator()
------------------------------------------------------------------------------------------------------------------------------
import random
import string

# Define the allowed departments
allowed_departments = ["Marketing", "Accounting", "FinOps"]

# Function to generate unique EC2 names
def generate_ec2_names(num_instances, department):
    # Convert the department input to title case for validation
    department = department.title()

    # Advanced department validation
    if department not in allowed_departments:
        print("This Name Generator is only available for Marketing, Accounting, and FinOps departments.")
        return None

    ec2_names = []

    for _ in range(num_instances):
        # Generate random characters and numbers for the unique name
        random_chars = ''.join(random.choices(string.ascii_letters, k=3))
        random_numbers = ''.join(random.choices(string.digits, k=3))

        # Combine department, random characters, and numbers for the name
        ec2_name = f"{department}-{random_chars}-{random_numbers}"

        ec2_names.append(ec2_name)

    return ec2_names

# Function to execute the complex EC2 Name Generator
def execute_complex_generator():
    print("COMPLEX EC2 Random Name Generator")
    num_instances = int(input("How many EC2 instances do you want to name? "))
    department = input("Enter your department name (Marketing, Accounting, or FinOps): ")

    generated_names = generate_ec2_names(num_instances, department)

    if generated_names:
        print("Generated EC2 names:")
        for name in generated_names:
            print(name)

# Execute the complex generator
execute_complex_generator()
