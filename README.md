# SQL Lite
SQLite is a serverless, transactional database engine that allows users to work with python with the sqlite3 module. SQLite is light in terms of setup and resources. It does not require a server to run, and the databses created are local with files stored on your disk. This is a great tool for databse prototyping, praticing, and more. 

# SQL Alchemy
SQLAlchemy is an ORM - Object Relational Mapping - tool that allows us to work with python (or any language) instead of SQL to query and manipulate the database. SQLAlchemy integates with SQLite, MySQL, Postgres.

# Install PIP 
PIP is pythons package manager used to install and update packages. To install PIP:
1. Download python 2.79+
2. Save the following as a py file to a folder in your directory: [get-pip.py](https://bootstrap.pypa.io/get-pip.py?force_isolation=true) 
3. Open the command prompt and navigate to the folder:
4. Use dir to check what is in your directory
  You will see the folder you want to select. Run cd foldername
  Verify your folder is there by using dir again
  When you have  navigated to the correct folder, run python get-pip.py:
```
    C:\Users\janet\OneDrive\Documents>python get-pip.py
```

# Install SQLAlchemy:
Once you have Python and PIP installed, you are ready to install SQLAlchemy. 
 ```
     C:\Users\janet\OneDrive\Documents>pip install sqlalchemy 
```

# Create VirtualEnviroment for your SQLAlchemy workspace
Once pip and SQLAlchemy is installed, you are ready to install and create yout virtual enviroment. 
Run the following command to install:
```
     C:\Users\janet\OneDrive\Documents>pip install virtualenv
 ``` 
Check the version:
```
     C:\Users\janet\python39\Scripts> virtualenv --version
```

Create workspace, give it a name! I will name my workspace sqlalchemy_workspace:
     C:\Users\janet\python39\Scripts> virtualenv sqlalchemy_workspace

