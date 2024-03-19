from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/welcome', methods=['POST'])
def welcome():
   name = request.form['name']
   email = request.form['email']
   
   # создание cookie-файла с данными пользователя
   response = make_response(redirect(url_for('greet')))
   response.set_cookie('user', '{}:{}'.format(name, email))
   
   return response

@app.route('/greet')
def greet():
   user_data = request.cookies.get('user')
   if user_data:
       name, _ = user_data.split(':')
       return render_template('welcome.html', name=name)
   else:
       return redirect(url_for('index'))

@app.route('/logout')
def logout():
   # удаление cookie-файла с данными пользователя
   response = make_response(redirect(url_for('index')))
   response.set_cookie('user', '', expires=0)
   return response

if __name__ == '__main__':
   app.run(debug=True)
