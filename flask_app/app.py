from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        if not name or not age or not age.isdigit():
            return "Invalid input. Please enter a valid name and numeric age."
        return f"Hello, {name}! You are {age} years old."
    return '''
        <form method="post">
            Name: <input type="text" name="name"><br>
            Age: <input type="text" name="age"><br>
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
