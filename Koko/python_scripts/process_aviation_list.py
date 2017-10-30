def represent_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

with open('aviation_list_prepro.txt', 'r') as ifile, \
     open('aviation_lists_cleaned.txt', 'w') as ofile:
    year = 0
    for line in ifile:
        if line == '\n':
            # The line is an blank line        
            continue
        proc_line = line.rstrip()
        if represent_int(proc_line):
            # The line represents a year
            year = int(proc_line)
            continue
        else:
            # The line specifies an event
            old_substr = " - "
            new_substr = ", " + str(year) + ", "
            line = line.replace(old_substr, new_substr)
            newline = "On " + line
            ofile.write(newline)



