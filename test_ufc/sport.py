import pandas as pd
import numpy as np

# Loading the dataset
df1 = pd.read_csv("part4_2012-01-20.csv")
df = pd.read_csv("2012-01-20.csv")


df['Winner Name']=df1['Winner First Name'] + ' ' + df1['Winner Last Name']

df['fighter_x_win'] = (df['fighter_x_name'].str.upper() == df['Winner Name'].str.upper()).astype(int)


# print(df.head())


from lightgbm import LGBMClassifier
from sklearn.metrics import accuracy_score, classification_report
from joblib import dump
import warnings
warnings.filterwarnings("ignore")

drop_cols = ["fight_id", "Fight ID_x", "Fight ID_y", "date",
             "fighter_x_name", "fighter_y_name", "Winner Name","Stance_x", "Stance_y"]

X = df.drop(drop_cols + ["fighter_x_win"], axis=1, errors='ignore')
y = df["fighter_x_win"]




model_trained = 0
print("Training LightGBM model...")
model = LGBMClassifier(random_state=42)


if model_trained == 0:
    model.fit(X, y)
    print("Model trained.")

    # Evaluation function
    def evaluate_model(y_true, y_pred, set_name=""):
        acc = accuracy_score(y_true, y_pred)
        print(f"Accuracy ({set_name}): {acc:.4f}")
        print(f"Classification Report ({set_name}):\n{classification_report(y_true, y_pred)}")
        return acc

    # Evaluate on training data
    print("\n--- Training Performance ---")
    train_preds = model.predict(X)
    evaluate_model(y, train_preds, "Train")

    model_trained = 1


# --------------------------
# Save model to .pkl file
# --------------------------
dump(model, "lgbm_fighter_prediction.pkl")
print("\nModel saved as 'lgbm_fighter_prediction.pkl'")