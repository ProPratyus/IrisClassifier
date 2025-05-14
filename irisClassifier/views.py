from django.shortcuts import render
from joblib import load
import pandas as pd

model = load('./savedModels/model.joblib')

species_map = {
    0: "setosa",
    1: "versicolor",
    2: "virginica"
}

def predictor(request):
    if request.method == 'POST':
        sepal_length = float(request.POST['sepal_length'])
        sepal_width = float(request.POST['sepal_width'])
        petal_length = float(request.POST['petal_length'])
        petal_width = float(request.POST['petal_width'])

        input_df = pd.DataFrame([{
            'sepal length (cm)': sepal_length,
            'sepal width (cm)': sepal_width,
            'petal length (cm)': petal_length,
            'petal width (cm)': petal_width
        }])

        prediction = model.predict(input_df)[0]
        y_pred = species_map[prediction]     

        return render(request, 'index.html', {'result': y_pred})
    return render(request, 'index.html')
