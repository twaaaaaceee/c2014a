class BuildingError(Exception):
    def __str__(self):
        return f" Матеріалів дуже мало, так нічого не вийде!"
def check_material(amount_of_material, limit_value):
    if amount_of_material<limit_value:
        return " матеріалу достатньо"
    else:
        raise BuildingError(amount_of_material)
materials=300
check_material(materials,123)

class BuildingError(Exception):
    def __str__(self):
        return f"Матеріалу трохи більше лимиту, так ми працювати не зможемо"
def check_material(amount_of_material, limit_value):
    if amount_of_material>limit_value:
        return " матеріалу достатньо"
    else:
        raise BuildingError(amount_of_material)
materials=123
check_material(materials,150)

class BuildingError(Exception):
    def __str__(self):
        return f"Матеріалу трохи недостатньо!"
def check_material(amount_of_material, limit_value):
    if amount_of_material<limit_value:
        return " матеріалу достатньо"
    else:
        raise BuildingError(amount_of_material)
materials=350
check_material(materials,300)

