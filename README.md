# Inventory-tracking
A web application that tracks the current inventory. Users can create, edit, delete, and view inventory items. They can also export inventory data to a CSV.  
## Set up instructions
In the terminal, check if Python is installed:
```
~$ python --version
Python 3.7.4
````
If you don't have Python, you can download it [here.](https://www.python.org/downloads/)

Next, create a virtual environment for our Flask web application.
```
~$ python -m venv virtenv
~$ source virtenv/bin/activate
(virtenv) ~$ 
```
Now we will clone our Git repository. 
Alternatively, you can download the zip file and unzip it.
```
(virtenv) ~$ git clone https://github.com/nimra200/Inventory-tracking.git
Cloning into 'Inventory-tracking'...
remote: Enumerating objects: 18, done.
remote: Counting objects: 100% (18/18), done.
remote: Compressing objects: 100% (14/14), done.
remote: Total 18 (delta 1), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (18/18), done.
```
We need to navigate to our repository and install the project dependencies with Pip. If you don't have pip, you can install it [here:]( https://pip.pypa.io/en/stable/installation/)
```
(virtenv)~$ cd Inventory-tracking/
(virtenv)~$ pip install -r requirements.txt 
```
Run the server with:
```
(virtenv) (base) ~/Inventory-tracking$ python app.py 
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://localhost:5000/ (Press CTRL+C to quit)
```
In your web browswer, navigate to *http://localhost:5000/*. 



![Screen Shot 2022-01-09 at 8 11 20 PM](https://user-images.githubusercontent.com/56455442/148708773-af05d16b-abf3-4563-94a1-c74e77ebd95f.png)
