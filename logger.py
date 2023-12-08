import logging
import logging.handlers

# LOG_FILENAME = "text_generator.log"
LOG_NAME = "postadmission-genai-pack"

def get_logger(name: str = LOG_NAME, file_level: int = logging.INFO, console_level: int = logging.INFO) -> logging.Logger:
    """
    Returns a configured logger.

    :param name: Name of the logger.
    :param file_level: Logging level for the file handler.
    :param console_level: Logging level for the console handler.
    :return: Configured logger.
    """
    
    logger = logging.getLogger(name)
    
    # This checks if the logger is already configured.
    # If it is, it simply returns the logger to avoid adding duplicate handlers.
    if logger.hasHandlers():
        return logger
    
    logger.setLevel(logging.DEBUG)  # Set logger level to the lowest possible.

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Create a file handler
    # file_handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=10*1024*1024, backupCount=5)  # 10 MB file size limit with 5 backup files
    # file_handler.setLevel(file_level)
    # file_handler.setFormatter(formatter)
    # logger.addHandler(file_handler)

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger
