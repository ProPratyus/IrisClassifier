# IrisClassifier
This project is a web application built using Django and Machine Learning to classify Iris flower species based on their features. The model was trained using the popular Iris Dataset and is deployed as a web service where users can input flower measurements to get predictions.

Key Features:
Web Interface: Simple and user-friendly form for inputting flower features such as sepal length, sepal width, petal length, and petal width.
Machine Learning Model: Uses a trained Logistic Regression model to predict the flower species: Setosa, Versicolor, or Virginica.
Real-Time Prediction: Users can input the flower’s measurements and instantly get predictions for the species.

Tech Stack:
Backend: Python (Django), Scikit-learn (for the ML model)
Frontend: HTML, CSS (Bootstrap 5)
Model: Logistic Regression trained on the Iris Dataset, saved using Joblib for prediction.

How to Run:
Clone the repository to your local machine:  git clone https://github.com/ProPratyus/IrisClassifier.git

Navigate into the project folder: cd IrisClassifier

Install dependencies: pip install -r requirements.txt

Run the Django server: python manage.py runserver

Visit http://127.0.0.1:8000 in your browser to start classifying Iris flowers!
