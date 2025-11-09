import logging

logging.basicConfig(filename='file_info.log', filemode='w', level=logging.INFO)

logging.debug('info') # використайте інший рівень логування після logging (error, info, debug, exception, critical)
logging.info('info2')
logging.debug('info3')