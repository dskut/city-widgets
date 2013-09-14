#! /usr/bin/env python

import csv
import json

def get_year_indices(line):
    cells = line.strip().split(";")
    ind = 0
    for cell in cells:
        if cell == '"2010"':
            ind2010 = ind
        elif cell == '"2011"':
            ind2011 = ind
        elif cell == '"2012"':
            ind2012 = ind
        elif cell == '"2013"':
            ind2013 = ind
        ind += 1
    return ind2010, ind2011, ind2012, ind2013

def get_month_titles(line):
    return ""

def get_months(data):
    res = data[:]
    for i in xrange(1, len(data)):
        if res[i] >= data[i-1]:
            res[i] -= data[i-1]
    return res

def parse_csv(path):
    f = open(path)
    line_count = 0
    res = []
    for line in f:
        line_count += 1
        if line_count == 3:
            year_indices = get_year_indices(line)
        if line_count == 4:
            month_titles = get_month_titles(line)
        if line_count < 5:
            continue
        data = line.strip().split(';')
        subject = data[0]
        months_data = data[1:]
        months_data_int = map(lambda x: int(float(x[1:-1])), months_data)
        months = get_months(months_data_int)
        res.append(months)
    return res

data = parse_csv('data/data-36232-full.csv')
print data
