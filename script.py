import pandas as pd
import numpy as np
import csv

with open("pdf_location", "r") as csv_file: 
    csv_reader = csv.reader(csv_file) # some of these functions can also be replaced by pandas library functions
    header = next(csv_reader) # skips header as most of the times its not much of use
    for row in csv_reader: # now just add which columns you want in the markdown fiel
        with open(f"{row[0]}.md", "w") as md_file:
            md_file.write("# " + row[0] + "\n")
            md_file.write("**Subtype** " + row[1] + "\n")
            md_file.write("**Tags:** " + row[2] + "\n")
            md_file.write("**Summary:**"+ row[3] + "\n")
            md_file.write("**Deployment Status:**" + row[4] + "\n")
            md_file.write("**Description:**" + row[5] + "\n")
            md_file.write("**URL:**" + row[6] + "\n")
            md_file.write("**Image:**" + row[7] + "\n")
            md_file.write("**Ecosystem/chain:**" + row[8] + "\n")
            md_file.write("**Twitter**" + row[9] + "\n")
            md_file.write("**Community**" + row[10]+"\n")
            md_file.write("**Whitepaper**" + row[11] + "\n")
# here you cn do all sorts of fancy things with md.
