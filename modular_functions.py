import pandas as pd
from bs4 import BeautifulSoup
import requests
import numpy as np
from datetime import datetime

#all the functions required for the project are recorded here
#they will be imported in the main file.

def log_progress(message):
    """this function's intent is to maintain a log of the progress of etl at each step. for security, i used append mode to write the logs, so that the previous logs are not overwritten."""
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second
    now = datetime.now() 
    timestamp = now.strftime(timestamp_format) 
    with open("./etl_log.txt","a") as f: 
        f.write(timestamp + ' : ' + message + '\n')

#Now data extraction functions
def extract_data(url):
    pass

def transform_data(file):
    pass

def write_to_db(dataframe):
    pass

