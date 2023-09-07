import random
import string

def ec2_name_generator():
    allowed_departments = ('Marketing', 'marketing', 'Accounting', 'accounting', 'FinOps', 'finops', 'Finops')
    department_name = input('What department do you work for? ').capitalize()

    if department_name not in allowed_departments:
        print("Sorry, you are not allowed to use this EC2 name generator. Please contact I.T. for further info")
    else:
        name_quantity = int(input('How many EC2 instances would you like to create names for? '))

        for _ in range(name_quantity):
            random_numbers = random.randint(100000, 900000)
            instance_name = f"{department_name}-{random_numbers}"
            print(instance_name)
print('''

 $$$$$\                                               $$$$$$$$\                    $$\       
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
ec2_name_generator()
