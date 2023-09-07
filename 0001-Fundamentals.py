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

def generate_ec2_names(num_instances, department):
    ec2_names = []

    for _ in range(num_instances):
        random_chars = ''.join(random.choices(string.ascii_letters, k=3))
        random_numbers = ''.join(random.choices(string.digits, k=3))
        ec2_name = f"{department}-{random_chars}-{random_numbers}"
        ec2_names.append(ec2_name)

    return ec2_names

def main():
    print("FOUNDATIONAL EC2 Random Name Generator")
    num_instances = int(input("How many EC2 instances do you want to name? "))
    department = input("Enter your department name: ")

    generated_names = generate_ec2_names(num_instances, department)

    if generated_names:
        print("Generated EC2 names:")
        for name in generated_names:
            print(name)

if __name__ == "__main__":
    main()

-------------------------------------------------------------------------------------------------------------
import random
import string

# Function to generate unique EC2 names
def generate_ec2_names(num_instances, department):
    ec2_names = []

    for _ in range(num_instances):
        # Generate random characters and numbers for the unique name
        random_chars = ''.join(random.choices(string.ascii_letters, k=3))
        random_numbers = ''.join(random.choices(string.digits, k=3))

        # Combine department, random characters, and numbers for the name
        ec2_name = f"{department}-{random_chars}-{random_numbers}"

        ec2_names.append(ec2_name)

    return ec2_names

# Main program
def main():
    print("FOUNDATIONAL EC2 Random Name Generator")
    num_instances = int(input("How many EC2 instances do you want to name? "))
    department = input("Enter your department name: ")

    generated_names = generate_ec2_names(num_instances, department)

    if generated_names:
        print("Generated EC2 names:")
        for name in generated_names:
            print(name)

if __name__ == "__main__":
    main()
