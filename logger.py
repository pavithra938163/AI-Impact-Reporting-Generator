import logging

logging.basicConfig(
    filename="ai_logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_prompt(prompt):
    logging.info(f"PROMPT: {prompt}")

def log_response(response):
    logging.info(f"RESPONSE: {response}")
