import numpy as np
import pandas as pd

# from sklearn.datasets import load_diabetes
# dibaties_dataset=load_diabetes()


# Diabities_DF=pd.DataFrame(dibaties_dataset.data,columns=dibaties_dataset.feature_names)# assignt he dataset to the variable and gives the name of columns provided in the dataset as a features
# #print(Diabities_DF)#to print the entire dataset 
# print("printing the first five rows")
# print(Diabities_DF.head())# this prints the top 5 rows of the dataset
# print("now printing the last 5 rows")
# print(Diabities_DF.tail())# tail function prints the last 5 rows
# print(f"Now the shape of the datase is {Diabities_DF.shape}")

###
##importing the data from csv file to pandas dataframe

diabaties_df=pd.read_csv("D:\Ai\ML\chat gpt-master\python-foundations\diabetes.csv")
# diabaties_df.head().to_csv("head.csv")
# print("Done")

# ## creating pandas dataframe with the random values
# random_df=pd.DataFrame(np.random.rand(10,5),columns=["A","B","C","E","E"])
# print(random_df)

## to get the full information of the dataframe we use info() function
# print(diabaties_df.info())

## to find the number of mising values in a column of a dataframe is to use isnull().sum() function which bicassically checks either the number is null and if yes adds as a null value
# print(diabaties_df.isnull().sum())

### to count the values according to the lables(clo-names) can use value_count("col-name") function

# print(diabaties_df.value_counts("Age"))
#gives the total number of each values in that col

## to group the values acording to the unique element of the choosen col-name values we can use group by and print them 
# print(diabaties_df.groupby("Outcome").mean())

## to find the number of values in the each coulum we can use count function
# print(diabaties_df.count())

## to find the mean values of the dataset col-wise
# print(diabaties_df.mean())

## to find the standard deviation of the dataset col-wise
# print(diabaties_df.std())

## to find the minimum and maximum values of the each dataset we can use min() ans max() functions
# print(f"min-value:{diabaties_df.min()}\n max-values:{diabaties_df.max()}")

## to find or know all the stastical methodesin one go we can use function describe()
# print(diabaties_df.describe())

## how to add the new col in a dataset
# diabaties_df["death-percentage"]=0
# print(diabaties_df.head())

# to remove the certain row
# diabaties_df=diabaties_df.drop(index=0,axis=0)
# print(diabaties_df.head())

# #to remove the col
# diabaties_df=diabaties_df.drop(columns="Glucose")
# print(diabaties_df.head())

## to print all the values of the certain row with its index
# print(diabaties_df.iloc[2])

## to print all the values of the certain row with its index
# print(diabaties_df.iloc[:,2]) # this is for the 3rd col
# print(diabaties_df.iloc[:,-1])# this is for the last col

##CORRELATION(positive or negative)
# corelarion is the relation betwen two values or ccolumns in the dataset +ve corelation means if one variable value increases anothers also increases and -ve corelation means if one increases another decreases
# to fiind the correlation in the dataset we can use corr() function if value is +ve +ve corellation exist and of value is -ve negative correlation exits

print(diabaties_df.corr())