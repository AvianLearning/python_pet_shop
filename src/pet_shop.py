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


def get_stock_count(pet_shop_dict):
    count = len(pet_shop_dict["pets"])
    return count


def get_pets_by_breed(pet_shop_dict, breed):
    breeds_found = []
    pets = pet_shop_dict['pets']
    for pet in pets:
        if pet['breed'] == breed:
            breeds_found.append(pet['breed'])

    return breeds_found
    

def find_pet_by_name(pet_shop_dict, name):
    p



        




