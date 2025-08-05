from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/rounit.html')

@app.route('/1')
def page1():
    return render_template('login.html')

@app.route('/index.html')
def page2():
    return render_template('index.html')


@app.route('/C&H.html')
def page6():
    return render_template('C&H.html')


@app.route('/food.html')
def page7():
    return render_template('food.html')


@app.route('/aart.html')
def page8():
    return render_template('aart.html')

@app.route('/hotel.html')
def page9():
    return render_template('hotel.html')

@app.route('/gallery.html')
def page5():
    return render_template('gallery.html')

@app.route('/contact.html')
def page3():
    return render_template('contact.html')

@app.route('/about.html')
def page4():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()

