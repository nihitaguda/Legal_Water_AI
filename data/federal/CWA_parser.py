#open file
#read line
#see if like if in list of sections. add to file
# if so, pull the contents from that point to editorial notes
# run data cleaner 
# add to new file
# output file

with open('CleanWaterAct.txt') as f:
    print(f.read())
    lines = f.readlines()
    for i in range(len(lines) - 1):
        if lines[i+1].strip().lower() == "section 1267":
            i+=i
            print(i)
            if lines[i].strip().lower() == "Editorial Notes"


