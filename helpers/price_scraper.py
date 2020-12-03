#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 18:07:34 2020

@author: nastory
"""
try:
    import pandas as pd
    from selenium import webdriver
except ImportError as error:
    print(error.__class__.__name__ + ":" + error.message)


def scrape_data(observations=1):
    """Web scraping function. Uses Chrome driver to source generated data
    from http://turnip-price.now.sh

    Args:
        observations (int): Number of randomly generated observations to source from http://turnip-price.now.sh.

    Outputs:
        out (pandas.DataFrame): Weekly turnip price data
    """
    
    URL = "http://turnip-price.now.sh"
    DRIVER_PATH = '/Users/nastory/chromedriver'
    RAND_BUTTON_ID = 'generate-seed'
    
    data = {
            "buying-price": [],
            "selling-price-0": [],
            "selling-price-1": [],
            "selling-price-2": [],
            "selling-price-3": [],
            "selling-price-4": [],
            "selling-price-5": [],
            "selling-price-6": [],
            "selling-price-7": [],
            "selling-price-8": [],
            "selling-price-9": [],
            "selling-price-10": [],
            "selling-price-11": []
            }
    
    data_elem_ids = [
            "buying-price",
            "selling-price-0",
            "selling-price-1",
            "selling-price-2",
            "selling-price-3",
            "selling-price-4",
            "selling-price-5",
            "selling-price-6",
            "selling-price-7",
            "selling-price-8",
            "selling-price-9",
            "selling-price-10",
            "selling-price-11"
            ]
    
    with webdriver.Chrome(executable_path=DRIVER_PATH) as driver:
        driver.get(URL)
        for i in range(0, observations):
            rand_button = driver.find_element_by_id(RAND_BUTTON_ID)
            rand_button.click()
            for elem in data_elem_ids:
                data[elem].append(driver.find_element_by_id(elem).text)
    
    
    out = pd.DataFrame(data)
    out.columns = ['Purchase', 'Mon-AM', 'Mon-PM', 'Tues-AM', 'Tues-PM', 
                   'Wed-AM', 'Wed-PM', 'Thurs-AM', 'Thurs-PM', 'Fri-AM', 
                   'Fri-PM', 'Sat-AM', 'Sat-PM']
    
    return out.astype(float)
