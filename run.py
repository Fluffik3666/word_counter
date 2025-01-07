import logging
import os
from datetime import datetime
from internal.counter import Counter
import argparse

os.makedirs('logs', exist_ok=True)

logger = logging.getLogger('word_counter')
file_handler = logging.FileHandler(f'logs/word_counter_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')
console_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def main():
    parser = argparse.ArgumentParser(description="Count the number of words in a string")
    parser.add_argument("string", help="The string to count the number of words in")
    parser.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"])
    args = parser.parse_args()
    
    logger.setLevel(getattr(logging, args.log_level))
    logger.info(f"Processing string: {args.string}")
    
    try:
        counter = Counter(args.string)
        result = counter.count()
        logger.info(f"Count result: {result}")
        print(f"The number of words in the string is {result}")
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise

if __name__ == "__main__":
    main()