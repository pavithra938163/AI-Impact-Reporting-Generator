from openai import OpenAI
from config import Config
from utils.logger import log_prompt, log_response

client = OpenAI(api_key=Config.OPENAI_API_KEY)

def generate_impact_statement(data):

    prompt = f"""
    Generate a sustainability impact summary.

    Plastic Saved: {data['plastic']} grams
    Carbon Avoided: {data['carbon']} kg
    Supplier Type: {data['supplier']}

    Write a short customer-friendly sustainability statement.
    """

    log_prompt(prompt)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    text = response.choices[0].message.content

    log_response(text)

    return text
