# Circuit Frontend API

### python3 -m venv env
### source enc/bin/activate
### deactivate

### pip3 install falcon
### pip3 install falcon-cors
### pip3 install requests
### pip3 install pyjwt
### pip3 install gunicorn

### gunicorn -b localhost:3100 app:api
### gunicorn -b localhost:3100 app:api --reload
### gunicorn -b localhost:3100 app:api --daemon
### gunicorn -b localhost:3100 app:api --daemon --reload