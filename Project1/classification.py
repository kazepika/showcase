# List for Nature (use the label below)
product_classification =  {
            "Item 1": 'Stock 1',
            "Item 2": 'Stock 2'
            }

# Checking zone
key_to_check = "Item 1"

# Check if the key exists
if key_to_check.strip() in product_classification:
    print(f"The key '{key_to_check.strip()}' exists in the dictionary.")
else:
    print("False") # f"The key '{key_to_check}' does not exist in the dictionary."


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
(Please update the label to avoid errors)
Exisiting Labels for nature:
- Stock 1
- Stock 2



Unknown:


'''
