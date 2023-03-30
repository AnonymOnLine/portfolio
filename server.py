from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        try:
            id1 = data['id1']
        except KeyError:
            id1 = 'nem'
        try:
            id2 = data['id2']
        except KeyError:
            id2 = 'nem'
        try:
            id3 = data['id3']
        except KeyError:
            id3 = 'nem'
        try:
            id4 = data['id4']
        except KeyError:
            id4 = 'nem'
        try:
            id5 = data['id5']
        except KeyError:
            id5 = 'nem'
        try:
            id6 = data['id6']
        except KeyError:
            id6 = 'nem'
        name = data['name']
        email = data['email']

        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([id1, id2, id3, id4, id5, id6, name, email])


@app.route('/submit_form.html', methods=['POST', 'GET'])
def summit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not saved to database'
    else:
        return 'something went wrong'
