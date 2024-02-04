import os
import sys
import logging

# defining logging string
# %(asctime)s ---> for current time and date
# %(levelname)s ---> from which level you are running the code. Ex: if you are running code
# from root folder then the levelname is root.
# %(module)s ---> module name (which module you are running)
# %(message)s ---> what kind of log message you want to save.

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Creating Log folder

log_dir = "logs"

# creating log file (name: running_log.log) inside Log folder

log_filepath = os.path.join(log_dir, "running_log.log")

# Now we have to create a directory
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level = logging.INFO,
    format = logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]

)
# StreamHandler: sends logging output to streams such as sys.stdout, sys.stderr or any file-like object (or, more precisely, any object which supports write() and flush() methods)
# FileHandler: sends logging output to a disk file. It inherits the output functionality from StreamHandler.

# defining logger object

logger = logging.getLogger("mlProjectLogger")