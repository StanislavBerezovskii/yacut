# Project Yacut

## Description:

This project was completed as part of the Python developer + Yandex-Practicum online course.

**Yacut** is a link shortening service that associates long user links with short ones. The short link can be suggested by the user, or it will be generated automatically.

Thus, this service allows to turn a long and inconvenient link like “https://flask.palletsprojects.com/en/2.2.x/changes/#version-2-0-0” into a short and simple one like “http ://localhost/ver2".
After creating a short link, user can be redirected to the original address by following the new link.

In addition to working in a browser with a graphical interface, the service also provides an API that duplicates its functionality.

## Key technologies and libraries:
- [Python](https://www.python.org/);
- [Flask](https://pypi.org/project/Flask/);
- [SQLAlchemy](https://pypi.org/project/SQLAlchemy/);

## Installation:
1. Clone the repository:
```
git clone https://github.com/StanislavBerezovskii/yacut.git
```
2. Activate the venv virtual environment and install the project dependencies:
```
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```
3. Create an .env file in the root directory of the project with the following content:
```
FLASK_APP=yacut
FLASK_ENV=development или production
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=<your_secret_key>
```
4. The project is ready for launch.

## Usage:
To start the service locally, run the command:
```
flask run
```
The service will be launched and available via the following addresses:
- http://localhost/ - main page of the service;

    * If the short link field is not filled, it will be generated automatically.
    * A short link must be no longer than 16 characters (numbers and Latin letters in any case).

- http://localhost/api/id/ - API endpoint that accepts POST requests;

    * POST request scheme:
        ```json
        {
        "url": "string",
        "custom_id": "string" * (optional field)
        }
        ```
    * Scheme of the response to a POST request:
        ```json
        {
        "url": "string",
        "short_link": "string"
        }
        ```

- http://localhost/api/id/short_id/ - endpoint that accepts GET requests.
    
    The address must contain the created or generated short link instead of <short_id>.

    * Scheme of response to a GET request:
        ```json
        {
        "url": "string"
        }
        ```

    The full API specification is available in the repository - see openapi.yml file
  
## License:
- ### **MIT License**

### Author:
Stanislav Berezovskii

berezovskii.stas@gmail.com
