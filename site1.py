from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def menu():
    # read menu.txt
    with open('menu.txt', 'r', encoding='utf-8') as file:
        menu_items = [line.strip() for line in file.readlines()]

    # render template html
    return render_template('menu.html', menu_items=menu_items)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
