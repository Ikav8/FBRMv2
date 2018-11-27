from flask import Flask
from FBRMv2 import resultados_y_proximos_partidos_HTML

app = Flask(__name__)


@app.route('/')
def home():
	return 'Hello'
	#return resultados_y_proximos_partidos_HTML()


if __name__ == "__main__":
	app.run()