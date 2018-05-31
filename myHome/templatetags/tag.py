from urllib import parse
from django import template
import calendar

register = template.Library()


@register.filter()
def range_fuc(end_day):
  try:
    return range(1,int(end_day))
  except ValueError as e:
    return ""
@register.simple_tag
def day(URL):
  try:
    URL = parse.unquote(URL)
    URL_var = URL.split("?")[1].split("&")
    select_month = URL_var[2].split("month=")[1]
    end_day = calendar.monthrange(2018, int(select_month))[1]
    return end_day
  except IndexError as e:
    print("day 인덱스 오류 : {0}".format(e))
    return "IndexOut"


@register.simple_tag
def day2(month):
  end_day = calendar.monthrange(2018, int(month))[1]
  return end_day

@register.simple_tag
def select_day(URL):
  try:
    URL = parse.unquote(URL)
    URL_var = URL.split("?")[1].split("&")
    select_day = URL_var[3].split("day=")[1]
    return int(select_day)
  except IndexError as e:
    print("select_day 인덱스 오류 : {0}".format(e))
    return "IndexOut"

@register.simple_tag
def month(URL):
  try:
    URL = parse.unquote(URL)
    URL_var = URL.split("?")[1].split("&")
    select_month = URL_var[2].split("month=")[1]
    return int(select_month)
  except IndexError as e:
    print("month 인덱스 오류 : {0}".format(e))
    return "IndexOut"

@register.simple_tag
def all_month():
  month=[0]*7
  for i in range(7):
    month[i]=i+6
  return month

@register.simple_tag
def fish_kind(URL):
  try:
    URL = parse.unquote(URL)
    URL_var = URL.split("?")[1].split("&")
    fish_index= URL_var[0].split("species=")[1]
    print("fish 인덱스 : {0}".format(fish_index))
    return int(fish_index)
  except IndexError as e:
    print("fish 인덱스 오류 : {0}".format(e))
    return 999

@register.simple_tag
def fish_compare(fish, fish2):
  if fish==fish2:
    return 1
  else:
    return 0
