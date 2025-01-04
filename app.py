from flask import Flask, render_template, request

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def index():
    # Render the index.html template
    return render_template('index.html')

# Define the route for the calculation
@app.route('/calculate', methods=['POST'])

def calculate():
    # Get the form data from the request
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']
    
    # Perform the requested operation
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        result = num1 / num2
    else:
        result = 'Invalid operation'
    
    # Render the index.html template with the result
    return render_template('index.html', result=result)

# Run the application in debug mode
if __name__ == '__main__':
    app.run(debug=True)
