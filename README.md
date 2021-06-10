# Used Car Price Estimator: Project Overview
* Created a tool that estimates price of a used car(MAE ~ $4K) to help the buyer negotiate while shopping and individuals who want to list their car on platforms like Facebook Marketplace.
* Scraped over 2000 car listings in California and NewYork from cargurus.com (listing website of used car) using selenium.
* Cleaned data and engineered features (such as model, built year, mileage, details, and description) from raw data.
* Performed EDA (exploratory data analysis) to handle missing values, remove outliers, transform variables, check correlation and shortlist variables for machine learning model building.
* Optimized Linear, Lasso, Ridge, Random Forest, and XGBoost regressors using GridsearchCV to find the best model.
* Deployed in Heroku cloud using Flask API endpoint. Made it available online for users to get an approximate price of the car. Link given in Productionization section below.

## Code and Resources Used
* **Python Version:** 3.8.5
* **Packages:** pandas, numpy, sklearn, xgboost, matplotlib, seaborn, selenium, nltk
* **For Web Framework Requirements:** `pip install -r requirements.txt`
* **GitHub Repo Ref:** https://github.com/PlayingNumbers/ds_salary_proj
* **Deployment Ref:** https://medium.com/@nutanbhogendrasharma/deploy-machine-learning-model-with-flask-on-heroku-cd079b692b1d
## Web Scraping (webscraper.ipynb)
Scraped over 2000 car listing from cargurus.com using **selenium**. The following information were extracted from each listing:
* Price of car
* Build year
* Model of the car (Ford, Toyota, Honda, etc.)
* Gas Mileage
* Features (Bluetooth, Alloy wheels, Android Auto, Backup Camera, Heated seats, etc.)
* Transmission (Automatic and Manual)
* Color
* Engine
* Drivetrain
* Fuel type
* Description

## Data Cleaning (data_cleaning.ipynb)
Cleaned the raw data and made new columns with proper assignment of variables.
* Parsed numeric and categorical variables out of text.
* Made columns for price, model, and build year of the car.
* Parsed details such as Transmission, Color, Engine, Drivetrain, Fuel_type, Gas mileage into separate columns from a single column.
* Column for description length
* Counted number of features such as Bluetooth, keyless entry, type of wheel, heated seats, etc, and saved into one column.

## EDA (EDA.ipnyb)
Plotted distribution of continous and categorial variables. Imputed missing values and removed outliers. Highlights from EDA notebook are as follows:

![alt text](https://github.com/Ajay-rai/used_car_price_predictor/blob/master/images/price_histogram.PNG)
![alt text](https://github.com/Ajay-rai/used_car_price_predictor/blob/master/images/model_dist.PNG)
![alt text](https://github.com/Ajay-rai/used_car_price_predictor/blob/master/images/pivot.PNG "price of car")
![alt text](https://github.com/Ajay-rai/used_car_price_predictor/blob/master/images/correlation.PNG)

## Model Building (model_building.ipnyb)
* Transformed the categorical variables into binary format using One-Hot encoding.
* Split the dataset into 80:20 for train and test respectively.
* Used MAE (Mean Absolute Error) to evaluate model. MAE is good with outliers.
* Used five models:
  * Multilinear regression - Baseline for the model.
  * Ridge regression - To prevent overfitting.
  * Lasso regression - Effective because data is sparse for many categorical variables.
  * Random Forest - Could be a good fit for sparse data type.
  * XGBoost - Most advanced algorithm for sparse data. Also, hypertuned the parameters using GridsearchCV.

### Model performance
XGBoost performed the best:
  * Multilinear regression: MAE = $4968
  * Ridge regression: MAE = $4968
  * Lasso regression: MAE = $4914
  * Random Forest: MAE = $4596
  * XGBoost: MAE = $4185

### Feature Importance
![alt text](https://github.com/Ajay-rai/used_car_price_predictor/blob/master/images/feature.PNG)

## Productionization
Built a Flask API endpoint and hosted on webserver using heroku. The following page takes user inputs and estimate the price of car. Refer this link to checkout deployment page: https://carpricechecker.herokuapp.com/

![alt text](https://github.com/Ajay-rai/used_car_price_predictor/blob/master/images/deployment.PNG)

## Conclusion and Future Recommendation
* Average price of used cars listed in cargurus.com is ~$20K in California and NewYork.
* Major factors that affect the price of used cars is in following order: mileage > built year > gas mileage > features > color > engine > drivetrain 
* Pipeline can be implemented for data cleaning, EDA and model building to streamline the process.
* Accuracy of model can be improved by selecting better features, variable transformation(skewed to normal distribution), and removal of more outliers.
* NLP can be used to get insight from descriptions.

### Github rendering problem with jupyter notebook? 
Use the link below and copy paste the git repository link into it for a smooth experience.
https://nbviewer.jupyter.org/

