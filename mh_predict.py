import pandas as pd

# Load the cleaned CSV
df = pd.read_csv("smmh_clean.csv")

# Take a quick look
print(df.head())

# Numeric features
numeric_features = ['Stress_Level(1-10)', 'Sleep_Quality(1-10)', 'Daily_Screen_Time(hrs)', 'Exercise_Frequency(week)']

# Categorical features to encode
categorical_features = ['Gender', 'Social_Media_Platform']

# One-hot encode categorical features
df_encoded = pd.get_dummies(df, columns=categorical_features)

# Target variable
y = df_encoded['mh_score']

# Features (drop target and User_ID)
X = df_encoded.drop(['mh_score', 'User_ID', 'high_risk'], axis=1, errors='ignore')

print("X columns:", X.columns.tolist())
print("y name:", y.name)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(
    n_estimators=300,     # number of trees
    random_state=42,      # ensures reproducibility
    n_jobs=-1             # uses all CPU cores (faster)
)

model.fit(X_train, y_train)

# Make predictions
preds = model.predict(X_test)

# Evaluate the model
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

mae = mean_absolute_error(y_test, preds)
rmse = np.sqrt(mean_squared_error(y_test, preds))
r2 = r2_score(y_test, preds)

print("Model Performance:")
print("MAE:", mae)
print("RMSE:", rmse)
print("R²:", r2)

# Feature importance
importances = model.feature_importances_
feature_names = X.columns

print("\nFeature Importances:")
for name, score in sorted(zip(feature_names, importances), key=lambda x: x[1], reverse=True):
    print(f"{name}: {score:.4f}")

# Save the model using joblib
import joblib
joblib.dump(model, "mh_model.pkl")
print("\nModel saved as mh_model.pkl")

df_encoded["predicted_mh_score"] = model.predict(df_encoded[X.columns])

# Save enriched dataset
df_encoded.to_csv("mh_with_predictions.csv", index=False)
print("Saved mh_with_predictions.csv")