import logging
import os

def get_logger():
    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("framework")

    if not logger.handlers:
        logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler("logs/test.log")
        console_handler = logging.StreamHandler()

        formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger