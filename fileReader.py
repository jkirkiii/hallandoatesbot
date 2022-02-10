import logging

logger = logging.getLogger()

def get_lines():
    lines = []
    logger.info('Opening file')
    try:
        with open('youmakemydreams.txt', 'r') as file:
            lines = file.readlines()
    except Exception as e:
            logger.error("Error opening file", exc_info=True)
            raise e
    logger.info('File opened')
    return lines