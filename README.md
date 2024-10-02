|Project Title|Car Dheko - Used Car Price Prediction
| :--- | :--- |
|**Skills take away From This Project**| 1.	Data Cleaning and Preprocessing 2.	Exploratory Data Analysis 3.	Machine Learning Model Development 4.	Price Prediction Techniques 5.	Model Evaluation and Optimization6.	Model Deployment 7.	Streamlit Application Development 8.	Documentation and Reporting
|**Domain**|Automotive Industry , Data Science, Machine Learning|

-   <ins>**Project Description:**</ins>
This project mainly focuses on cleaning the dataset and converting unstructured data given for 6 different cities to structured data using pandas and eliminate null values as part of data pre- processing, analysing different features of car data to come up with feature selection based on EDA and develop ML model to predict price comparing different models based on MSE, RMSE, MAE for accuracy and streamling pricing for used cars and visualizing the same on Streamlit app for better customer interface.

-  <ins>**Data cleaning and Preprocessing steps:**</ins>
- Step 1: Extracting the data set from the excel files to pandas dataframe for Bangalore, Chennai, Hyderabad, Jaipur, Delhi and Kolkata
- Step 2: Conversion of unstructured data to structured data by splitting data in new car detail, new car overview, new car specs and new car feature column into different columns to get required the data in pandas dataframe
- Step 3: Concatenate all the data columns to single dataframe for each city car data 
- Step 4: Load the data to a csv file for further data cleansing.
- Step 5: Check for null values in each dataset and data type conversions and 
- Step 6: Renaming column names as part of standardization by removing space in the column names.


- <ins>**Exploratory Data Analysis:**</ins>
- Step1:Drop the missing values from data columns since the overall missing value was very low 9 records
- Step 2: Check for statistical summary of data -Mean, Standard deviation, Min, Max, Count of unique records 
- Step3: Check for categorical variables and convert the data types to numeric by One hot encoding 
- Step 4:Understand the correlation between data through scatter plot and box violin plot, histogram  to analyse distribution of numerical  variables for each city data respectively

![cityyt](https://github.com/user-attachments/assets/0f735afb-81eb-4a88-addd-f924e4d956ff)

![outpu467](https://github.com/user-attachments/assets/822d13b2-1bca-49cd-b354-2370b22bf77b)


![out](https://github.com/user-attachments/assets/8a29c4d5-f5ae-44eb-9064-4ffdb89cc87d)

![output 45](https://github.com/user-attachments/assets/49dff9e7-50c5-46f7-8343-90ff3d709137)

![output46](https://github.com/user-attachments/assets/ce744a55-f1a4-43b2-b220-592043b9c790)

![sct](https://github.com/user-attachments/assets/1382cbe2-9602-4581-a38b-7c70ca481329)

![c](https://github.com/user-attachments/assets/374ec0f4-e955-40fa-900e-00045cd56edd)

![cityd](https://github.com/user-attachments/assets/4072bea9-7699-4739-9eaf-d2d24272c108)


-  <ins>**Feature Engineering:**</ins>
  Calculated Vehicle age from Model year and Vehicle age to calculate car pricing

 <ins>**Feature Selection:**</ins>
- Dropping the unnecessary columns from the cleaned car data based on lower correlation like colour of the body, model and car name 

- Load the Car dataset <ins>**Overall.csv**<ins>
-   This dataset contains information about used cars listed on website This data can be used for a lot of purposes such as price prediction to exemplify the use of linear regression in Machine Learning. The columns in the given dataset are as follows:

<img src="https://github.com/user-attachments/assets/a57d112f-d120-463e-8a36-bc779d28f2aa" width="600">
 
- Plotted a graph to check for feature importance to understand importance of features selected to increase the accuracy of the model.
  
![image](https://github.com/user-attachments/assets/65673791-6383-4b05-bbed-a2f5b2acaa2c)


 <ins>**Feature observation:**</ins>
Heatmaps and pair plot to analyse the correlation of the overall data combined for all the cities car data to understand overall data correlation of different columns of pandas dataframe.

![output2](https://github.com/user-attachments/assets/d23be7dc-9409-4f5b-a627-2f6a789136b1)

![heatmap](https://github.com/user-attachments/assets/0dbda1fa-1b52-407d-aed3-1d36307939a9)


**<ins>Target variable:**</ins> To understand the distribution and spread of car price by visualizing the data to understand data spread.

![output](https://github.com/user-attachments/assets/1a03b1bd-de8f-4c06-b87b-981a18046a29)


**<ins>Model Development :**</ins>
 - Create Target and feature variables from final dataframe and splitting the train and test ratio to 80:20

**<ins>Model Evaluation:**</ins>
- Calculated Mean squared error,Mean absolute error and root mean squared error to compare different models 

**<ins>Model Selection:**</ins>
- Random Forest Regressor have minimum 'RMSE' and high accuracy compared to other models. So, I decided to use Random Forest Regressor as Machine Learning Model.

**<ins>Predicting Test Data by visualizing:**</ins>
- Now that I've fit and trained the model, I need to evaluate its performance by predicting the test values and visualize the results

![Testpredict](https://github.com/user-attachments/assets/7eb3480d-eea2-499d-ad30-58f15084f6e6)

![predict](https://github.com/user-attachments/assets/c41c52a1-0e28-492c-8b35-7b8d1fe33118)


**<ins>Model Deployment:**</ins>
- Step 1: Generating a pickle file to dump the trained model 
- Step 2: Saving the trained model to be loaded to Streamlit for visualization model11.pkl

**<ins>Streamlit Visualization:**</ins>
- Step 1: load the pickled file to get the model data for prediction of car price
- Step 2: Define the user input fields as fitted in the training model
- Step 3: Create a input data with column names as saved in the trained model 
- Step 4: Make prediction from the model and display the estimated value of predicted car price 

![image](https://github.com/user-attachments/assets/6b6dbd32-9c15-4765-9d88-a0b13af01da5)




