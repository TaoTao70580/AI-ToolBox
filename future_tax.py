# Simple machine learning model to predict future tax based on previous year
from sklearn.linear_model import LinearRegression

def predict_future_tax(previous_year_income, previous_year_deductions):
    # Assume we have historical data on income and deductions
    X = [[50000, 12000], [60000, 14000], [70000, 15000]]  # Example data: [income, deductions]
    y = [8000, 8500, 10000]  # Example tax owed for each case

    model = LinearRegression()
    model.fit(X, y)

    # Predict tax for the next year based on current income and deductions
    prediction = model.predict([[previous_year_income, previous_year_deductions]])
    return prediction[0]

predicted_tax = predict_future_tax(65000, 14500)
print(f"Predicted tax for next year: ${predicted_tax:.2f}")
