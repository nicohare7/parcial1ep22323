import mariadb
config = {
    'host' : 'localhost',
    'port' : 3806,
    'user' : 'root',
    'password' : '12345',
    'database' : 'flask_mvc',
}
DB = mariadb.connect(**config)
DB.autocommit = True

