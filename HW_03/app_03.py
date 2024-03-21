from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

# Создание экземпляра приложения Flask
app = Flask(__name__)

# Настройки подключения к базе данных (SQLite в данном примере)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# Модель пользователя
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(255))

# Маршрут для отображения и обработки формы регистрации
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']

        # Хеширование пароля
        hashed_password = generate_password_hash(password)

        # Создание нового пользователя
        new_user = User(first_name=first_name, last_name=last_name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return 'Пользователь зарегистрирован успешно!'
    
    return render_template('register.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
