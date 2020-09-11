# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop_dict):
    name = pet_shop_dict["name"]
    return name


def get_total_cash(pet_shop_dict):
    sum = pet_shop_dict["admin"]["total_cash"]
    return sum


def add_or_remove_cash(pet_shop_dict, cash_amount):
    new_total = get_total_cash(pet_shop_dict) + cash_amount
    pet_shop_dict["admin"]["total_cash"] = new_total
    

def get_pets_sold(pet_shop_dict):
    sold = pet_shop_dict["admin"]["pets_sold"]
    return sold


def increase_pets_sold(pet_shop_dict, num_sold):
    sold = get_pets_sold(pet_shop_dict) + num_sold
    pet_shop_dict["admin"]["pets_sold"] = sold



