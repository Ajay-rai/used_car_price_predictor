# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 20:25:35 2021

@author: ajy00
"""


from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time
import pandas as pd

def get_cars(num_cars, path, sleep_time):
    
    '''Gathers cars as a dataframe, scraped from Cargurus'''
    
    #Initializing the webdriver
    options = webdriver.ChromeOptions()
   
    #Uncomment the line below if you'd like to scrape without a new Chrome window every time.
    #options.add_argument('headless')
    
    #Change the path to where chromedriver is in your home folder.
    driver = webdriver.Chrome(executable_path=path, options=options)
    driver.set_window_size(1120, 1000)

    url = 'https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?zip=90011&contactlessOptions=REMOTE_PURCHASES&financePartners=CAPITAL_ONE&financePartners=WESTLAKE&financePartners=GLS&showNegotiable=false&sortDir=ASC&sourceContext=carGurusHomePageModel&distance=100&sortType=DEAL_SCORE&hasFinancing=true#listing=301523514'
    driver.get(url)
    cars = []
    

#########################################
    while len(cars) < num_cars: #If true, should be still looking for new cars.
        
        #Going through each car details in this page
        print("Progress: {}".format("" +str(len(cars)) + "/" +str(num_cars)))
       
        collected_successfully = False
            
        while not collected_successfully:
            try:
                car_title  = driver.find_element_by_xpath('//*[@id="cargurus-listing-search"]/div[1]/div[3]/div[1]/h1').text
            except NoSuchElementException:
                car_title = -1
            try:
                car_location = driver.find_element_by_xpath('//*[@id="cargurus-listing-search"]/div[1]/div[3]/div[1]/div').text  #enters location and distance
            except NoSuchElementException:
                car_location = -1
            try:
                car_details = driver.find_element_by_xpath('//*[@id="cargurus-listing-search"]/div[1]/div[3]/div[2]/div[2]/section[4]').text
            except NoSuchElementException:
                car_details = -1
            try:
                car_dealer = driver.find_element_by_xpath('//*[@id="cargurus-listing-search"]/div[1]/div[3]/div[2]/div[2]/section[1]/h2').text
            except NoSuchElementException:
                car_dealer = -1
            try:
                car_contact = driver.find_element_by_class_name('_3fXy3w').text
            except NoSuchElementException:
                car_contact = -1
            try:
                car_description = driver.find_element_by_xpath('//*[@id="cargurus-listing-search"]/div[1]/div[3]/div[2]/div[2]/section[5]').text
            except NoSuchElementException:
                car_description = -1
            
            collected_successfully = True
                
                


            
                
                
        cars.append({"Car Title" : car_title,
                    "Location" : car_location,
                    "Details" : car_details,
                    "Dealer" : car_dealer,
                    "Contact" : car_contact,
                    "Description" : car_description})
       

        #Clicking on the "next page" button
        try:
            driver.find_element_by_class_name('svg-inline--fa.fa-caret-right.fa-w-6._4BNaFw').click()
        except NoSuchElementException:
            print("Scraping terminated before reaching target number of cars. Needed {}, got {}.".format(num_cars, len(cars)))
            break

    return pd.DataFrame(cars)  #This line converts the dictionary object into a pandas DataFrame.

#This line will open a new chrome window and start the scraping.
path = 'C:/Users/ajy00/OneDrive/Desktop/datascience/chromedriver'
csv_file_path = r'C:/Users/ajy00/OneDrive/Desktop/datascience/Cargurus_webscrape_Cali.csv'
df = get_cars(1500, path, 2)
df.to_csv(csv_file_path, index = False)