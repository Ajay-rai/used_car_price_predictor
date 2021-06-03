# Used Car Price Estimator: Project Overview
* Created a tool that estimates price of a used car(MAE ~ $4K) to help buyer negotiate while shopping and individuals who want to list their car on platforms like Facebook Marketplace.
* Scraped over 2000 car listings from cargurus.com (listing website of used car) using python and selenium.
* Cleaned data and engineered features (such as model, built year, mileage, details and description) from raw data.
* Performed EDA (exploratory data analysis) to handle missing values, remove outliers, transform variables, check correlation and shortlist variables for machine learning model building.
* Optimized Linear, Lasso, Ridge, Random Forest, and XGBoost regressors using GridsearchCV to find the best model.

## Code and Resources Used
* **Python Version:** 3.8.5
* **Packages:** pandas, numpy, sklearn, xgboost, matplotlib, seaborn, selenium, nltk
* **GitHub Repo Ref:** https://github.com/PlayingNumbers/ds_salary_proj

## Web Scraping (webscraper.ipynb)
Scraped over 2000 car listing from cargurus.com using **selenium**. Following informations were exctracted from each listing:
* Price of car
* Bulid year
* Model of the car (Ford, Toyota, Honda, etc.)
* Gas Mileage
* Transmission (Automatic and Manual)
* Color
* Engine
* Drivetrain
* Fuel type
* Description

## Data Cleaning (data_cleaning.ipynb)
Cleaned the raw data and made new columns with proper assignment of variables.
* Parsed numeric and categorial variables out of text.
* Made columns for price, model and build year of the car.
* Parsed details such as Transmission, Color, Engine, Drivetrain, Fuel_type, Gas mileage into seperate columns from a single column.
* Column for description length
* Counted number of features such as Bluetooth, keyless entry, type of wheel, heated seats etc and saved into one column.

## EDA (EDA.ipnyb)
Plotted distribution of continous and categorial variables. Imputed missing values and removed outliers. Highlights from EDA notebook area as folows:
![alt text](https://github.com/Ajay-rai/used_car_price_predictor/blob/master/images/price_histogram.PNG)
![alt text](https://github.com/Ajay-rai/used_car_price_predictor/blob/master/images/model_dist.PNG)
![alt text](https://github.com/Ajay-rai/used_car_price_predictor/blob/master/images/pivot.PNG)
![alt text](https://github.com/Ajay-rai/used_car_price_predictor/blob/master/images/correlation.PNG)

## Model Building
* Transformed the categorial variables into binary format using One-Hot encoding.
* Split the dataset into 80:20 for train and test respectively.
* Used MAE (Mean Absolute Error) to evaluate model. MAE is good with outliers.
* Used five models:
  * Multilinear regression - Baseline for the model.
  * Ridge regression - To prevent overfitting.
  * Lasso regression - Effective because data is parse for many categorial variables.
  * Random Forest - Could be a good fit for sparse data type.
  * XGBoost - Most advanced algorithm for sparse data

### Model performance
XGBoost performed the best:
  * Multilinear regression: MAE = $4968
  * Ridge regression: MAE = $4968
  * Lasso regression: MAE = $4914
  * Random Forest: MAE = $4596
  * XGBoost: MAE = $4185

### Feature Importance
![alt text](https://github.com/Ajay-rai/used_car_price_predictor/blob/master/images/feature.PNG)

## Future Work
* To build flask API endpoint and host on a webserver. 

### Github rendering problem with jupyter notebook? 
Use the link below and copy paste the git repositry link into it for smooth experience.
https://nbviewer.jupyter.org/

