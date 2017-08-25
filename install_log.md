http://methane.github.io/flask-handson/start.html

```sh
$ bash -l
$ python -V
Python 3.6.1
$ pip -V
pip 9.0.1 from /home/mint/.pyenv/versions/3.6.1/lib/python3.6/site-packages (python 3.6)
$ python -m venv /media/mint/85f78c06-a96e-4020-ac36-9419b7e456db/mint/root/tools/pyenv/3.6.1/venv/webapp/
$ source /media/mint/85f78c06-a96e-4020-ac36-9419b7e456db/mint/root/tools/pyenv/3.6.1/venv/webapp/bin/activate
(webapp) $ pip install Flask
Collecting Flask
  Downloading Flask-0.12.2-py2.py3-none-any.whl (83kB)
    100% |████████████████████████████████| 92kB 860kB/s 
Collecting click>=2.0 (from Flask)
  Downloading click-6.7-py2.py3-none-any.whl (71kB)
    100% |████████████████████████████████| 71kB 1.5MB/s 
Collecting Werkzeug>=0.7 (from Flask)
  Downloading Werkzeug-0.12.2-py2.py3-none-any.whl (312kB)
    100% |████████████████████████████████| 317kB 836kB/s 
Collecting Jinja2>=2.4 (from Flask)
  Using cached Jinja2-2.9.6-py2.py3-none-any.whl
Collecting itsdangerous>=0.21 (from Flask)
  Downloading itsdangerous-0.24.tar.gz (46kB)
    100% |████████████████████████████████| 51kB 2.2MB/s 
Collecting MarkupSafe>=0.23 (from Jinja2>=2.4->Flask)
  Using cached MarkupSafe-1.0.tar.gz
Installing collected packages: click, Werkzeug, MarkupSafe, Jinja2, itsdangerous, Flask
  Running setup.py install for MarkupSafe ... done
  Running setup.py install for itsdangerous ... done
Successfully installed Flask-0.12.2 Jinja2-2.9.6 MarkupSafe-1.0 Werkzeug-0.12.2 click-6.7 itsdangerous-0.24
```


