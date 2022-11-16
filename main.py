import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)

###  Shows first 5 rows in our dataframe (in Google Cobal or Anaconda)  ###
# print(df.head())


###  Shows last 5 rows in our dataframe (in Google Cobal or Anaconda)  ###
# print(df.tail())

###  Shows how many row and columns we have in our dataframe  ###
# print(df.shape)

###  Counts the number of entries in each column in our dataframe  ###
# print(df.count())

###  Calculates the total posts in each programming language  ###
# print(df.groupby('TAG').sum())

###  We can take data with '[]' or ' . '
# print(df['DATE'][1])
###  or  ##
# print(df.DATE[1])
###  The result is the same as we can see  ###

# print(type(df.DATE[1]))
###  As we can see the result is 'str'
###  To work easily we can convert our str to date type using: ' .to_datetime '

pd.to_datetime(df.DATE[1])
# print(type(pd.to_datetime(df.DATE[1])))
### As we can see '<class 'pandas._libs.tslibs.timestamps.Timestamp'>'

###  If you didn't see the differences
### uncomment line 25 and see the differences

### To convert all 'DATE' column to timestamp we can write
df.DATE = pd.to_datetime(df.DATE)
### To check uncomment bellow
# print(df.head())


###  Using pivot table
### Let's reshape our tabel
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')

# print(reshaped_df.shape)
### to see how we changed our dataframe uncomment bellow
# print(reshaped_df)


### Using count() we can see the number of entries per language
# print(reshaped_df.count())

### By using 'fillna()' we can replace none value numbers
# print(reshaped_df.head()) ### Here you can see NaN values

reshaped_df.fillna(0, inplace=True)

# print(reshaped_df.head()) ### Here we can see that we have changed NaN values to '0'


### To check is there any NaN value
# print(reshaped_df.isna().values.any())  ### Here we got 'False'


####################        Matplotlib          #############################

### Make plot ###
# plt.plot(reshaped_df.index, reshaped_df['java'])
### to show it ###
# plt.show()


plt.figure(figsize=(16,10)) # make chart larger
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)


### If you want to add more programming value chart you just add
# plt.plot(reshaped_df.index, reshaped_df['java'])
# plt.plot(reshaped_df.index, reshaped_df['c'])
# plt.plot(reshaped_df.index, reshaped_df['python'])
# plt.show()

### To make for all languages we have to use for loop   #####

# for column in reshaped_df.columns:
#     plt.plot(reshaped_df.index, reshaped_df[column])
#
# plt.show()


### To add tha names of programms we have to add...
roll_df = reshaped_df.rolling(window=12).mean()
for column in reshaped_df.columns:
    plt.plot(reshaped_df.index, reshaped_df[column],
             linewidth=3, label=roll_df[column].name)

plt.legend(fontsize=16)
plt.show()




