from flask import Flask, render_template

app = Flask(__name__)

# Базовый шаблон
@app.route('/')
def base_template():
    return render_template('base.html')

# Дочерний шаблон для страницы категории "Одежда"
@app.route('/clothing')
def clothing_template():
    return render_template('clothing.html')

# Дочерний шаблон для страницы категории "Обувь"
@app.route('/shoes')
def shoes_template():
    return render_template('shoes.html')

# Дочерний шаблон для страницы товара "Куртка"
@app.route('/jacket')
def jacket_template():
    return render_template('jacket.html')

if __name__ == '__main__':
    app.run(debug=True)
