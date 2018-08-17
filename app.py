from flask import Flask, url_for
from flask import render_template
application = Flask(__name__)

@application.route("/")
def home_page():
	return render_template('/index.html')


#application.add_url_rule('/', 'index', (lambda x: home_page()))

if __name__ == "__main__":
	application.debug = False
	application.run()
