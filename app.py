# import sys

# def main():
#     if len(sys.argv) != 2:
#         print("Usage: python app.py <name>")
#         sys.exit(1)

#     name = sys.argv[1]
#     print(f"Hello, {name}!")

# if __name__ == "__main__":
#     main()
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)