from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_activity = request.form['activity']
        return f"You selected: {selected_activity}"
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)