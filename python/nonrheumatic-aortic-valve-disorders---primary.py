# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"G541600","system":"readv2"},{"code":"G541700","system":"readv2"},{"code":"Gyu5A00","system":"readv2"},{"code":"1005.0","system":"med"},{"code":"1007.0","system":"med"},{"code":"10187.0","system":"med"},{"code":"10964.0","system":"med"},{"code":"14998.0","system":"med"},{"code":"19019.0","system":"med"},{"code":"2343.0","system":"med"},{"code":"30610.0","system":"med"},{"code":"4548.0","system":"med"},{"code":"47887.0","system":"med"},{"code":"49185.0","system":"med"},{"code":"49272.0","system":"med"},{"code":"58810.0","system":"med"},{"code":"71004.0","system":"med"},{"code":"94521.0","system":"med"},{"code":"9591.0","system":"med"},{"code":"999.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('nonrheumatic-aortic-valve-disorders-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["nonrheumatic-aortic-valve-disorders---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["nonrheumatic-aortic-valve-disorders---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["nonrheumatic-aortic-valve-disorders---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
