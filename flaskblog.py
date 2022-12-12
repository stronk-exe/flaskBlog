from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
	{
		'author': 'stronk',
		'title': 'Blog Post test 1',
		'content': 'First post content',
		'date_posted': 'December 12, 2022'
	}
]
@app.route("/")

@app.route("/home")
def home():
    return render_template('home.html', title='About')

@app.route("/about")
def about():
    return render_template('about.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)