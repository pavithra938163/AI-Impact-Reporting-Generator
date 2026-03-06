def calculate_plastic_saved(order):
    return order.quantity * order.plastic_per_unit_grams


def calculate_carbon_avoided(order):

    carbon_per_km = 0.00012  # tons CO2 per km

    imported = order.import_distance_km * carbon_per_km
    local = order.local_distance_km * carbon_per_km

    avoided = imported - local

    return round(avoided * 1000, 2)
