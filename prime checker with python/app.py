from flask import Flask, render_template, request

app = Flask(__name__)

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_prime', methods=['POST'])
def check_prime():
    number = int(request.form['number'])
    prime = is_prime(number)
    return render_template('result.html', number=number, prime=prime)

if __name__ == '__main__':
    app.run(debug=True)
