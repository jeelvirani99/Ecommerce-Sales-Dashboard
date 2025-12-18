import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Understanding ML concept: Prediction
# This is how ML works (simplified)

print("MY FIRST ML CONCEPT: SIMPLE PREDICTION")
print("="*50)

# Dataset: Study hours vs Marks obtained
study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
marks = [20, 30, 35, 50, 60, 65, 75, 85]

# Simple prediction function
def predict_marks(hours):
    """
    Simple linear prediction
    Logic: marks = hours * 10 + 10
    """
    predicted = hours * 10 + 10
    return predicted

# Test predictions
print("\nPREDICTIONS:")
for hour in [3, 5, 7, 10]:
    prediction = predict_marks(hour)
    print(f"If you study {hour} hours -> Predicted marks: {prediction}")

print("\nThis is the BASIC IDEA of Machine Learning!")
print("ML learns patterns from data and makes predictions!")