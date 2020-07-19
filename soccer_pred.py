import numpy
import pandas
import xlrd

from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, classification_report, confusion_matrix, recall_score


# retrieving the data from the spreadsheet TR
training_file = r"MLS_soccer_data (1).xlsx"
training_extract = pandas.read_excel(training_file)
training_df = pandas.DataFrame(training_extract)

# prep the test set TR
test_file = r'soccer_test.xlsx'
test_extract = pandas.read_excel(test_file)
test_df = pandas.DataFrame(test_extract)


def clean_data(dataframe):
    # print(dataframe.head())

    reduced_df = dataframe.iloc[:, 3:]
    del reduced_df['Season']
    del reduced_df['Score']

    # print(reduced_df.head())
    return reduced_df


def run_tree_model(reduced_dataframe):
    X = reduced_dataframe.iloc[:, 0: -1]
    y = reduced_dataframe.iloc[:, -1]
    X_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=39)

    rd_tree_model = tree.DecisionTreeClassifier().fit(X_train, y_train)

    y_pred = rd_tree_model.predict(x_test)
    tree_score = rd_tree_model.score(x_test, y_test)
    print(tree_score)

    return rd_tree_model


def random_forest_model(reduced_dataframe):
    X = reduced_dataframe.iloc[:, 0: -1]
    y = reduced_dataframe.iloc[:, -1]
    X_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=33)

    forest_model = RandomForestClassifier(n_estimators=1000, random_state=33)
    forest_model.fit(X_train, y_train)
    forest_model.predict(x_test)

    forest_score = forest_model.score(x_test, y_test)
    print(forest_score)
    return forest_model


def test_model(model, dataframe):
    X = dataframe.iloc[:, 0: -1]
    y = dataframe.iloc[:, -1]

    pred_y = model.predict(X)

    print("Model predicts: ", pred_y)
    print("Actual Results: ", y)


def clean_data_2(dataframe):
    reduced_df = dataframe.iloc[:, 3:]

    reduced_df.drop(['Fouls', 'Offsides', 'Red Cards'], axis=1)
    del reduced_df['Season']
    del reduced_df['Score']

    # print(reduced_df.head())
    return reduced_df


reduced_train_df = clean_data(training_df)
rt_tree_model = run_tree_model(reduced_train_df)
random_forest = random_forest_model(reduced_train_df)

reduced_test_df = clean_data(test_df)
test_model(random_forest, reduced_test_df)

''' Model predicts:  ['Win' 'Win' 'Win' 'Tie' 'Tie' 'Win']
    Actual Results:    Win   Loss  Loss  Tie   Loss   Loss'''

# removed some categories in an attempt to see if there would be more accuracy
reduced_2 = clean_data_2(training_df)
random_forest_alt = random_forest_model(reduced_2)

reduced_test_2 = clean_data_2(test_df)
test_model(random_forest_alt, reduced_test_2)

'''model made the same predictions, and performed the same overall
 Model predicts:  ['Win' 'Win' 'Win' 'Tie' 'Tie' 'Win']
    Actual Results:    Win   Loss  Loss  Tie   Loss   Loss'''
