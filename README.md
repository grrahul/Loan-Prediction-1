# Loan Prediction
We have developed a machine learning model to predict the loan approval status. We have used different regression models and compared them. Based on mean squared error, absolute mean error, r2 score we have decided the best model for the dataset. We have used streamlit library for wepage and streamlit share for deployment.
</br>

## Module Description
Model | Description | 
:-------------: | :---------: |
Linear Regressor | Simple linear regression is an approach for predicting a response using a single feature.It is assumed that the two variables are linearly related. Hence, we try to find a linear function that predicts the response value(y) as accurately as possible as a function of the feature or independent variable(x). | 
Multi Linear Regressor | Multiple linear regression (MLR), also known simply as multiple regression, is a statistical technique that uses several explanatory variables to predict the outcome of a response variable. Multiple regression is an extension of linear (OLS) regression that uses just one explanatory variable. | 
Random Forest Regressor | The random forest combines hundreds or thousands of decision trees, trains each one on a slightly different set of the observations, splitting nodes in each tree considering a limited number of the features. The final predictions of the random forest are made by averaging the predictions of each individual tree. |
Decission Tree Regressor | Decision Tree is a decision-making tool that uses a flowchart-like tree structure or is a model of decisions and all of their possible results, including outcomes, input costs, and utility.Decision-tree algorithm falls under the category of supervised learning algorithms. It works for both continuous as well as categorical output variables. |

## Data Sets
The data set was collected from Kaggle, It contains variables like Gender, Marrital status, Income, Loan Amount, Loan Amount Term, Credit History, etc. We have first determined the training and testing data and then we have cleaned the data and processed it.

## Quick Start
To use the repo and run inferences, please follow the guidelines below
</br>
- Cloning the Repository: 

        $ git clone https://github.com/Harish-2001/loan-prediction2.git
        
- Entering the directory: 

        $ cd loan-prediction2/
        
- Setting up the Python Environment with dependencies:

        $ pip install -r requirements.txt

- Running the file for inference:

        $ streamlit run main.py
## Deployment

Linear | Random Forest | 
:-------------: | :---------: |
![rf-op](https://user-images.githubusercontent.com/72653126/143570203-c298ffbd-7705-44b1-b9ba-42d7a7561fc1.png) | ![gru-op](https://user-images.githubusercontent.com/72653126/143570278-3623e0ff-3f3b-4836-a54f-9c48722ad589.png)|

## Conclusion
We have concluded the following -

- Random Forest performs the best among the regression and it has the lowest mean square error, mean absolute error, r2 score.
- Decision Tress has the highest mean square error, mean absolute error, r2 score. It is the worest regressor for loan prediction.

## Webpage link
[https://share.streamlit.io/harish-2001/loan-prediction2/main/app.py](url)
Copy the link and open in new tab..
