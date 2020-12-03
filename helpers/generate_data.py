#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 11:07:34 2020

@author: nastory
"""

import pandas as pd 

from price_scraper import scrape_data
from db_connection import DBConnect


def main(observations=1):
	"""Extract turnip price data from the web and upload it into the `turnips` database.

	Args:
		observations (int): Number of randomly generated observations to source from http://turnip-price.now.sh.
	
	Returns:
		None.
	"""
	
	df = scrape_data(observations)

	with DBConnect(db='turnips', autocommit=True) as cnx:
		df.to_sql(name='generated_tunip_prices', con=cnx.engine, if_exists='replace',
				  index=False, chunksize=1000)

	print(f"\n ** {observations} observations successfully uploaded.\n")

if(__name__ == '__main__'):
	observations = int(sys.argv[1])
	main(observations)
