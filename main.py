from flask import Flask, render_template, url_for, request, redirect
import csv


app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name=None):
    if page_name=='works':
        return render_template('works.html')
    elif page_name=='work':
        return render_template('work.html')
    elif page_name=='about':
        return render_template('about.html')
    elif page_name=='contact':
        return render_template('contact.html')
    elif page_name=='components':
        return render_template('componets.html')
    elif page_name =='ThankYou.html':
        return render_template('ThankYou.html')
    else:
        return render_template('error.html', name=page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            with open('./static/database.csv', 'a') as my_data:
                csv.writer(my_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL).writerow([str(data['email']), str(data['subject']), str(data['message'])])
            return redirect('/ThankYou.html')
        else:
            return 'somthing went wrong'
        except:
            return 'Your message did not save to our database please try again'
