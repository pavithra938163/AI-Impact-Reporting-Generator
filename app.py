from fastapi import FastAPI
from utils.validator import Order
from services.impact_calculator import calculate_plastic_saved, calculate_carbon_avoided
from ai.impact_ai import generate_impact_statement
import json

app = FastAPI()


@app.post("/generate-impact")

def generate_report(order: Order):

    try:

        plastic_saved = calculate_plastic_saved(order)

        carbon_avoided = calculate_carbon_avoided(order)

        impact_statement = generate_impact_statement({
            "plastic": plastic_saved,
            "carbon": carbon_avoided,
            "supplier": order.supplier_type
        })

        report = {
            "order_id": order.order_id,
            "plastic_saved_grams": plastic_saved,
            "carbon_avoided_kg": carbon_avoided,
            "local_sourcing_summary":
                "Local sourcing reduces transportation emissions"
                if order.supplier_type == "local"
                else "Imported product has higher transportation emissions",

            "impact_statement": impact_statement
        }

        with open("reports/impact_reports.json", "a") as f:
            f.write(json.dumps(report) + "\n")

        return report

    except Exception as e:
        return {"error": str(e)}
