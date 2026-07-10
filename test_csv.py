import csv

with open("emp.csv","w",newline="") as f:
    write = csv.writer(f)

    write.writerow(["name","id"])
    write.writerow(["gtg","013"])
    write.writerow(["chandru","014"])
