from pydantic import BaseModel

class Order(BaseModel):
    order_id: str
    product_name: str
    quantity: int
    plastic_per_unit_grams: float
    local_distance_km: float
    import_distance_km: float
    supplier_type: str
