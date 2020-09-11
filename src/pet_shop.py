# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop_dict):
    name = pet_shop_dict["name"]
    return name


def get_total_cash(pet_shop_dict):
    sum = pet_shop_dict["admin"]["total_cash"]
    return sum


def add_or_remove_cash(pet_shop_dict, cash_amount):
    pet_shop_dict["admin"]["total_cash"] = get_total_cash(pet_shop_dict) + cash_amount
    


