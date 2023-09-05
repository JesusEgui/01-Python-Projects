import random
import string

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
name_quantity = int(input('How many EC2 instances would you like to create names for? '))
department_name = input('What department do you work for? ').capitalize()

for _ in range(name_quantity):
    random_numbers = random.randint(10000, 90000)
    instance_name = f"{department_name}-{random_numbers}"
    print(instance_name)
