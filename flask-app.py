from flask import Flask, render_template, request
import  os
import pickle
app = Flask(__name__,template_folder='templateFiles', static_folder='staticFiles')
filename = 'model-files/finalized_model.pkl'
loaded_model = pickle.load(open(filename, 'rb'))
port = int(os.environ.get("PORT", 5000))


y_map = {0: 'Bream',
 1: 'Parkki',
 2: 'Perch',
 3: 'Pike',
 4: 'Roach',
 5: 'Smelt',
 6: 'Whitefish'}

@app.route('/')
def index():
    return render_template(r'index.html')

@app.route('/results', methods=['POST'])
def results():
    form = request.form.values()
    if request.method == 'POST':
        vals = [float(i) for i in list(form)]
        print([vals])
        predicted_Species = loaded_model.predict([vals])
        species = y_map.get(predicted_Species[0])
        print(predicted_Species)
        print(species)
        return render_template('resultsform.html', Species=species)


if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True,port=port)