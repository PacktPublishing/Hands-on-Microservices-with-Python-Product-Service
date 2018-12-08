from flask import Flask, send_from_directory
from product_api import product_api_blueprint
from flask_swagger_ui import get_swaggerui_blueprint
import models

app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key",
    SQLALCHEMY_DATABASE_URI='mysql+mysqlconnector://root:test@product_db/product',
))

models.init_app(app)
models.create_tables(app)

app.register_blueprint(product_api_blueprint)
SWAGGER_URL = '/api/docs'
API_URL = '/api/product/docs.json' # Our API url (can of course be a local resource)
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={ # Swagger UI config overrides
        'app_name': "Test application"
    },
    # oauth_config={ # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    # 'clientId': "your-client-id",
    # 'clientSecret': "your-client-secret-if-required",
    # 'realm': "your-realms",
    # 'appName': "your-app-name",
    # 'scopeSeparator': " ",
    # 'additionalQueryStringParams': {'test': "hello"}
    # }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
