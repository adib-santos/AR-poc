from flask import Flask 
import routes.routes as routes


app = Flask(__name__)
app.config.from_object('config')


if __name__ == '__main__':
  app.run()