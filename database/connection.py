import sqlite3

CONN = sqlite3.connect('supermarket.db')
CURSOR = CONN.cursor()