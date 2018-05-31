from django import template
from urllib import parse
import sqlite3

register = template.Library()

@register.simple_tag
def df_place():
  try:
    conn = sqlite3.connect("db.sqlite3")
    cur = conn.cursor()
    cur.execute("select * from place")
    table = cur.fetchall()
    cur.close()
    conn.close()
    return table
  except IndexError as e:
    print("인덱스 오류 : {0}".format(e))
    return "IndexOut"

@register.simple_tag
def df_fish():
  try:
    conn = sqlite3.connect("db.sqlite3")
    cur = conn.cursor()
    cur.execute("select * from fish")
    table = cur.fetchall()
    cur.close()
    conn.close()
    return table
  except IndexError as e:
    print("fish 인덱스 오류 : {0}".format(e))
    return 9999