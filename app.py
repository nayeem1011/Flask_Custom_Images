from flask import Flask, render_template, request

app = Flask(__name__)

# Sample data
items = []

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/add_item', methods=['POST'])
def add_item():
    item = request.form.get('item')
    if item:
        items.append(item)
    return render_template('index.html', items=items)

if __name__ == '__main__':
   app.run(debug==True)



