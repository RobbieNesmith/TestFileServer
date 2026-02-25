## Setup

You will need python >3.9 to run this.

1. Create a virtual environment with [venv](https://docs.python.org/3/library/venv.html)
   - `python -m venv env`
2. Activate the environment
   - `. env/bin/activate`
3. Install dependencies from requirements.txt
   - `pip install -r requirements.txt`

## How to run

While your virtual environment is active, run with `python app.py [your file that you want to serve]`

The host and port can be configured with `--host` and `--port` but default to localhost and 5000.

The response status code can be configured with `--code` but will default to 200. See [http.cat](https://http.cat) for more information on status codes.