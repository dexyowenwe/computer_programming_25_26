

# Session 2 continuity variables (Rule settings). Do not change these.
THRESHOLD = 2.0
FEATURE_NAME = "petal_length"
POSITIVE_LABEL = "setosa"
NEGATIVE_LABEL = "not_setosa"
LABEL_KEY = "species"



correct = 0      # Count of correct predictions
wrong = 0        # Count of wrong predictions
total = 0        # Total samples processed
y_pred_list = []  # List of all predictions made


flower1 = {
    "id": "flower1",
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2,
    "species": "setosa"
}

# Task 1: Create A dictionary for second flower

flower2 = { 
"id": "flower2",
"sepal_length": 4.9,
"sepal_width" : 3.0,
"petal_length" : 1.4,
"petal_width" : 0.2,
"species": "setosa" 
}
# <your code here> remember to close me for a dict


# Task 2: Create list of dictionaries
dataset= [flower1, flower2]

# Task 3: Create a for loop to process the dataset
for flower in dataset:
print(flower["id"], flower["petal_length"], flower["species"])

# Task 4: Use an if-else statement to classify each sample
for flower in dataset:
if flower["petal_length"] < threshold:
    y_pred = positive_label
else:
    y_pred = negative_label
print(flower["id"],"Pred:",)