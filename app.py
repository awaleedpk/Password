from flask import Flask, request
import random
import string

app = Flask(__name__)

@app.route('/password')
def generate_password():
    length = int(request.args.get('length', 8)) 
    digits = request.args.get('digits', '').lower() in ('true', '1', 't')
    special_chars = request.args.get('special_chars', '').lower() in ('true', '1', 't')
    
    chars = string.ascii_letters
    if digits:
        chars += string.digits
    if special_chars:
        chars += string.punctuation
        
    password = ''.join(random.choice(chars) for i in range(length))
    
    return {'password': password}

if __name__ == '__main__':
    app.run()