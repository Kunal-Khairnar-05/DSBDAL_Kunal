# ===== Problem Statement 1 =====

#------
import pandas as pd
import numpy as np
#------
df = pd.read_csv("Titanic.csv")
df.head()
#------
df.tail()
#------
df.info()
#------
df.describe()
#------
df.isnull().sum()
#------
df['PClass'] = df['PClass'].fillna(df['PClass'].mode()[0])
df['Age'] = df['Age'].fillna(df['Age'].mean())
#------
df.isnull().sum()
#------
df.describe()
#------
df.shape
#------
df.size
#------
df.dtypes
#------
df = pd.get_dummies(df, columns=["Sex"], dtype=int)
#------
df.head()
#------
#------

















# ===== Problem Statement 2 =====


import pandas as pd
import numpy as np

# 1 & 2. Load Dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# 3. Data Preprocessing & Initial Stats
print("Dimensions:", df.shape)
print("\nInitial Statistics:\n", df.describe())
print("\nMissing Values:\n", df.isnull().sum())

# Handling Missing Values
df['Age'] = df['Age'].fillna(df['Age'].mean())

# 4. Data Formatting (Type Conversion)
print("\nData Types Before Conversion:\n", df.dtypes)

# Example: Converting 'Survived' to boolean (logical) and 'Pclass' to factor/category
df['Survived'] = df['Survived'].astype(bool)
df['Pclass'] = df['Pclass'].astype('category')

print("\nData Types After Conversion:\n", df.dtypes)

# 5. Data Normalization (Min-Max Scaling)
# Normalizing 'Age' and 'Fare' to a range of [0, 1]
def normalize(column):
    return (column - column.min()) / (column.max() - column.min())

df['Age'] = normalize(df['Age'])
df['Fare'] = normalize(df['Fare'])

print("\nNormalized Data (First 5 rows):\n", df[['Age', 'Fare']].head())












# ===== Problem Statement 3 =====

import pandas as pd
import matplotlib.pyplot as plt
#------
df = pd.read_csv("StudentsPerformance.csv")
df.head()
#------
df.isnull().sum()
#------
df['mathscore'] = df['mathscore'].fillna(df['mathscore'].mean())
#------
df.isnull().sum()
#------
df.shape
#------
df.info
#------
df.boxplot(column="mathscore")
plt.show()
#------
Q1 = df['mathscore'].quantile(0.25)
Q3 = df['mathscore'].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5*IQR
higher = Q3 + 1.5*IQR

print(Q1, Q3, lower, higher)

df_math = df[(df['mathscore'] >= lower) & (df['mathscore'] <= higher)]
#------
df_math.boxplot(column='mathscore')
plt.show()
#------
df['mathscore'].describe()
#------




df.boxplot(column="readingscore")
plt.show()
#------
Q1 = df['readingscore'].quantile(0.25)
Q3 = df['readingscore'].quantile(0.75)

IQR = Q3-Q1

lower = Q1 - 1.5*IQR
higher = Q3 + 1.5*IQR

print(Q1, Q3, lower, higher)
df_new = df[(df['readingscore'] >= lower) & (df['readingscore'] <= higher)]
#------
df_new.boxplot(column="readingscore")
plt.show()
#------
df['readingscore'].describe()
#------
#------



















# ===== Problem Statement 4 =====

import pandas as pd
import numpy as np

df = pd.read_csv('StudentsPerformance.csv')

# Scan for missing values
print(df.isnull().sum())

# Fill missing values with the average (Mean Imputation)
df['mathscore'] = df['mathscore'].fillna(df['mathscore'].mean())

# Identify initial skewness
initial_skew = df['mathscore'].skew()
print(f"Original Skewness: {initial_skew:.2f}")

# Transformation: log1p handles 0 values safely (log of 1 + x)
df['math_log'] = np.log1p(df['mathscore'])

# Check new skewness
print(f"New Skewness: {df['math_log'].skew():.2f}")

# Create a comparison of the original and transformed distributions
plt.figure(figsize=(12, 5))

# Graph 1: Original Distribution
plt.subplot(1, 2, 1)
sns.histplot(df['mathscore'], kde=True, color='royalblue', bins=20)
plt.title(f"Original Math Score\n(Skewness: {initial_skew:.2f})")
plt.xlabel("Score")
plt.ylabel("Frequency")

# Graph 2: Transformed Distribution
plt.subplot(1, 2, 2)
sns.histplot(df['math_log'], kde=True, color='darkorange', bins=20)
plt.title(f"Log Transformed Math Score\n(Skewness: {final_skew:.2f})")
plt.xlabel("Log(Score + 1)")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()

















# ===== Problem Statement 5 =====

import pandas as pd

df = pd.read_csv("13adult.csv")
#------
df.head()
#------
df.info()
#------
df.groupby("education")['age'].mean()
#------
df.groupby("education")['age'].median()
#------
df.groupby("education")['age'].std()
#------
df.groupby("education")['age'].describe()
#------
list_data = df.groupby("education")["age"].mean().tolist()
#------
print(list_data)



df = pd.read_csv("13Iris.csv")
#------
df.head()
#------
df.drop('Id', axis=1)
#------
df.columns
#------
df['species'].unique()
#------
df.groupby("species").describe()
#------
setosa = df[(df['species'] == 'Iris-setosa')]
#------
print("Mean of setosa : ", setosa.mean(numeric_only=True))
print("Median of setosa : ", setosa.median(numeric_only=True))
print("Standard Deviation of setosa : ", setosa.std(numeric_only=True))
print("Percentiles of setosa : ", setosa.quantile([0.25, 0.5, 0.75], numeric_only=True))
#------
versicolor = df[(df['species'] == 'Iris-versicolor')]

print("Mean of versicolor: ", versicolor.mean(numeric_only=True))
print("Median of versicolor: ", versicolor.median(numeric_only=True))
print("Standard Deviation of versicolor: ", versicolor.std(numeric_only=True))
print("Percentiles of versicolor: ", versicolor.quantile([0.25, 0.5, 0.75], numeric_only=True))
#------
virginica = df[(df['species'] == 'Iris-virginica')]

print("Mean of virginica: ", virginica.mean(numeric_only=True))
print("Median of virginica: ", virginica.median(numeric_only=True))
print("Standard Deviation of virginica: ", virginica.std(numeric_only=True))
print("Percentiles of virginica: ", virginica.quantile([0.25, 0.5, 0.75], numeric_only=True))






















# ==== Problem Statement 6 =====

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
#------
df = pd.read_csv("HousingData.csv")
df.head()
#------
df.columns
#------
print("Missing Values: ")
df.isnull().sum()
#------
df.fillna(df.mean(), inplace=True)
#------
df.isnull().sum()
#------
X = df.drop("MEDV", axis=1)
y = df["MEDV"]
#------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=43)
#------
print("Train Shape:", X_train.shape)
print("Test Shape:", X_test.shape)
#------
model = LinearRegression()
model.fit(X_train, y_train)
#------
y_pred = model.predict(X_test)
#------
print("Predicted values: ", y_pred[:5])
print("Actual values: ", y_test[:5].values)
#------
from sklearn.metrics import mean_squared_error
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = model.score(X_test, y_test)
print("RMSE: ", rmse)
print("R2 Score: ", r2)
#------
import matplotlib.pyplot as plt
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Actual vs Predicted Values")
plt.show()
#------
new_Data = pd.DataFrame([{
"CRIM": 0.06,
"ZN":	0.3,
"INDUS"	:0.1,
"CHAS"	:0.4,
"NOX"	:0.6,
"RM"	:0.1,
"AGE"	:0.8,
"DIS"	:0.9,
"RAD"	:0.1,
"TAX"	:10,
"PTRATIO"	:0.2,
"B"	:30,
"LSTAT":0.3
}])
#------
prediction = model.predict(new_Data)
#------
print("Predicted Price : ", prediction[0])
































# ===== Problem Statement 7 =====

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
#------
df = pd.read_csv("Social_Network_Ads.csv")
df.head()
#------
df.shape
#------
df.drop("User ID", axis=1)
#------
print("Purchased Count : ", df['Purchased'].value_counts())
#------
import seaborn as sns

# Converting gender to numeric value
df['Gender'] = df['Gender'].map({0:"Male", 1:"Female"})

# select numeric column
df_numeric = df.select_dtypes(include=["int64", "float64"])

corr = df_numeric.corr()

plt.figure(figsize=(10,10))
sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap")
plt.show()
#------
df.groupby('Purchased')[["Age","EstimatedSalary"]].mean()
#------
df['Gender_Label'] = df['Gender'].map({'Male':0, 'Female':1})

df['Gender_Label'].value_counts().plot(kind='bar')

plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()
#------
X = df[['Age','EstimatedSalary']]
y = df['Purchased']
#------
from sklearn.preprocessing import StandardScaler

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Scale the data
sc = StandardScaler()
X = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
#------
model = LogisticRegression()
model.fit(X_train, y_train)
print("Model Trained")
#------
# Predictions
y_pred = model.predict(X_test)
print("Training Accuracy :  {:.2f}%".format(model.score(X_train, y_train)))
print("Testing Accuracy : {:.2f}%".format(model.score(X_test, y_test)))
#------
# Confusion matrix

cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix : ",cm)
#------
TN = cm[0][0]
FP = cm[0][1]
FN = cm[1][0]
TP = cm[1][1]

print("True Negative : ", TN)
print("False Positive : ", FP)
print("False Negative : ", FN)
print("True Positive : ", TP)
#------
accuracy = (TP + TN) / (TP + TN + FP + FN)
precision = TP / (TP + FP)
recall = TP / (TP + FN)
error_rate = 1 - accuracy
f1_score = 2* (precision*recall)/(precision+recall)

print("Accuracy : ", accuracy)
print("Precision : ", precision)
print("Recall : ", recall)
print("Error Rate : ", error_rate)
print("F1 Score : ", f1_score)
#------
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))























# ==== Problem Statement 8 =====

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#------
df = pd.read_csv("Iris.csv")
df.head()
#------
df = df.drop('Id', axis=1)
#------
X = df.iloc[:,:4].values
y = df['species'].values
#------
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=8)
#------
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)
#------
y_pred = classifier.predict(X_test)
print(y_pred)
#------
y_compare = np.vstack((y_test, y_pred)).T
y_compare[:5,:]
#------
# Confusion matrix

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
sns.heatmap(cm, annot=True)

plt.xlabel("Predicted values")
plt.ylabel("Actual values")
plt.title("Confusion Matrix")
plt.show()
#------
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

print(confusion_matrix(y_test, y_pred))
print(accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
print("Error rate: ", 1-accuracy_score(y_test, y_pred))























# ==== Problem Statement 9 =====

import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
#------
from nltk import word_tokenize, sent_tokenize
#------
sent = "Hello, I am Kunal. I am the 3rd year student of the CSE branch at DYPIEMR"

print("Word tokenize : ", word_tokenize(sent))
print("Sent tokenize : ", sent_tokenize(sent))
#------
from nltk.corpus import stopwords

nltk.download('stopwords')
#------
stop_words = stopwords.words('english')
print("Stop words : ", stop_words)
#------
token = word_tokenize(sent)
cleaned_token = []

for word in token:
  if word.lower() not in stop_words:
    cleaned_token.append(word)

print("Original tokens :", token)
print("CLeaned toekn:", cleaned_token)
#------
words = [word.lower() for word in cleaned_token if word.isalpha()]
print("Cleaned token : ", words)
#------
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

stemmed_words = [stemmer.stem(word) for word in words]
print("Stemmed Words:" , stemmed_words)
#------
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')
#------
lemmatizer = WordNetLemmatizer()

lem_words = [lemmatizer.lemmatize(word) for word in words]

print("Lemmatized words : ", lem_words)
#------
from nltk import pos_tag
nltk.download("averaged_perceptron_tagger_eng")
#------
tagged = pos_tag(words)
print("POS tagged words : ", tagged)
#------
from sklearn.feature_extraction.text import TfidfVectorizer

docs = [
    "Data science is an important field",
    "Machine learning is a part of data science",
    "Deep learning is used in machine learning",
    "Artificial intelligence is related to data science"
    ]
#------
vectorizer = TfidfVectorizer(analyzer="word", norm=None, use_idf=True, smooth_idf=False)
vectorizer.fit(docs)
print("Vocabulary : ", vectorizer.vocabulary_)
#------
tfidf_matrix = vectorizer.fit_transform(docs)
print("TF-IDF Matrix : \n", tfidf_matrix)




















# ==== Problem Statement 10 =====
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the inbuilt titanic dataset
titanic = sns.load_dataset('titanic')

# Pattern 1: Correlation Heatmap to see relationships between numeric variables
plt.figure(figsize=(8, 5))
sns.heatmap(titanic.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Pattern in Titanic Data")
plt.show()

# Pattern 2: Survival rate by Gender and Class
sns.barplot(x='pclass', y='survived', hue='sex', data=titanic)
plt.title("Survival Pattern: Class vs Gender")
plt.show()



# Create a figure to hold multiple subplots for better visualization
plt.figure(figsize=(15, 12))

# A. Histogram
plt.subplot(3, 2, 1)
sns.histplot(titanic['fare'], kde=False, bins=30, color='blue')
plt.title("Fare Histogram")

# B. Histplot (with KDE)
plt.subplot(3, 2, 2)
sns.histplot(titanic['fare'], kde=True, color='green')
plt.title("Fare Histplot with KDE")

# C. Distplot (Note: distplot is deprecated, using displot or histplot(kde=True))
# To strictly satisfy the prompt requirement:
plt.subplot(3, 2, 3)
sns.histplot(titanic['fare'], kde=True, stat="density", color='orange')
plt.title("Fare Distplot (via Histplot Density)")

# D. Rug Plot (Shows individual data points as sticks)
plt.subplot(3, 2, 4)
sns.rugplot(titanic['fare'], color='red')
sns.histplot(titanic['fare'], alpha=0.3) # Adding hist for context
plt.title("Fare Rug Plot")

# E. Bar Plot (Fare distributed by Class)
plt.subplot(3, 2, 5)
sns.barplot(x='pclass', y='fare', data=titanic, palette='magma')
plt.title("Mean Fare by Class (Bar Plot)")

plt.tight_layout()
plt.show()

# F. Joint Plot (Needs two variables - Fare vs Age)
# Jointplot creates its own figure, so we call it separately
sns.jointplot(x='age', y='fare', data=titanic, kind='reg', color='purple')
plt.suptitle("Fare vs Age Joint Plot", y=1.02)
plt.show()



























# ==== Problem Statement 11 =====
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
titanic = sns.load_dataset('titanic')

# Set figure size
plt.figure(figsize=(10, 6))

# Creating the box plot
# x: gender, y: age, hue: survival status
sns.boxplot(x='sex', y='age', hue='survived', data=titanic, palette='Set1')

plt.title("Age Distribution by Gender and Survival (Box Plot)")
plt.xlabel("Gender")
plt.ylabel("Age")
plt.legend(title="Survived", loc='upper right', labels=['No', 'Yes'])
plt.show()



plt.figure(figsize=(10, 6))

# Creating the violin plot
# split=True merges the two survival categories into one 'violin' for easier comparison
sns.violinplot(x='sex', y='age', hue='survived', data=titanic, palette='Set2', split=True)

plt.title("Age Distribution by Gender and Survival (Violin Plot)")
plt.xlabel("Gender")
plt.ylabel("Age")
plt.legend(title="Survived", loc='upper right')
plt.show()


























# ==== Problem Statement 12 =====

import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = sns.load_dataset('iris')

# List of numeric features to plot
features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

# --- Histograms with Subplots ---
plt.figure(figsize=(10, 8))
for i, col in enumerate(features):
    plt.subplot(2, 2, i + 1) # 2 rows, 2 columns, index i+1
    sns.histplot(df[col], kde=True)
    plt.title(f'Distribution of {col}')

plt.tight_layout()
plt.show()

# --- Boxplots with Subplots ---
plt.figure(figsize=(10, 8))
for i, col in enumerate(features):
    plt.subplot(2, 2, i + 1)
    sns.boxplot(x='species', y=col, data=df)
    plt.title(f'Boxplot of {col}')

plt.tight_layout()
plt.show()
























# ==== Problem Statement 13 =====


import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = sns.load_dataset('iris')

# List of numeric features to plot
features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

# --- Histograms with Subplots ---
plt.figure(figsize=(10, 8))
for i, col in enumerate(features):
    plt.subplot(2, 2, i + 1) # 2 rows, 2 columns, index i+1
    sns.histplot(df[col], kde=True)
    plt.title(f'Distribution of {col}')

plt.tight_layout()
plt.show()

# --- Histograms: Comparing Distributions ---
plt.figure(figsize=(10, 8))
for i, col in enumerate(features):
    plt.subplot(2, 2, i + 1)
    sns.histplot(df, x=col, hue='species', kde=True, element="step")
    plt.title(f'Distribution Comparison: {col}')

plt.tight_layout()
plt.show()

# --- Boxplots: Identifying Outliers ---
plt.figure(figsize=(10, 8))
for i, col in enumerate(features):
    plt.subplot(2, 2, i + 1)
    sns.boxplot(x='species', y=col, data=df)
    plt.title(f'Outlier Detection: {col}')

plt.tight_layout()
plt.show()

























# ==== Problem Statement 14 =====
import pandas as pd

# 1. Load the dataset
# If your txt file uses spaces or tabs, use sep='\s+' 
df = pd.read_csv('sample_weather.txt')

# 2. Convert date column to datetime objects
df['date'] = pd.to_datetime(df['date'])

# 3. Extract Year and Month for grouping
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month

# 4. Calculate Year-wise Averages
year_wise = df.groupby('year')[['temperature', 'dewpoint', 'windspeed']].mean()

# 5. Calculate Month-wise Averages
month_wise = df.groupby(['year', 'month'])[['temperature', 'dewpoint', 'windspeed']].mean()

print("--- Year-wise Averages ---")
print(year_wise)

print("\n--- Month-wise Averages ---")
print(month_wise)





























# ==== Problem Statement 15 =====
# import org.apache.spark.{SparkConf, SparkContext}

# object WordCount {
#   def main(args: Array[String]): Unit = {
#     // 1. Setup Spark
#     val conf = new SparkConf().setAppName("WordCount").setMaster("local")
#     val sc = new SparkContext(conf)

#     // 2. Process Data
#     val input = sc.textFile("input.txt")
#     val counts = input.flatMap(line => line.split(" "))
#                       .map(word => (word, 1))
#                       .reduceByKey(_ + _)

#     // 3. Print result and Stop
#     counts.foreach(println)
#     sc.stop()
#   }
# }