"""
Week 4 practice project template for Python Data Representation
Update syntax for print in CodeSkulptor Docs
from "print ..." syntax in Python 2 to "print(...)" syntax for Python 3
"""

# HTML tags that bounds example code
PREFIX = "<pre class='cm'>"
POSTFIX = "</pre>"
PRINT = "print"


def update_line(line):
    """
    Takes a string line representing a single line of code
    and returns a string with print updated
    """
    # Strip left white space using built-in string method lstrip()
    new_line = line.lstrip()
    # If line is print statement,  use the format() method to add insert parentheses
    if "print" in new_line:
        original_space = ' ' * line.find(PRINT) #in order to insert Space preceeding print
        #Actually line.find("print") only find the "p"
        return "{}print({})".format(original_space,new_line[6:]) #keep in mind that string is indexed by character. 6 is len(print) plus len(" ")
    # Note that solution does not handle white space/comments after print statememt
    return line

# Some simple tests
print(update_line(""))
print(update_line("foobar()"))  
print(update_line("print 1 + 1"))      
print(update_line("    print 2, 3, 4"))

# Expect output
##
##foobar()
##print(1 + 1)
##    print(2, 3, 4)


def update_pre_block(pre_block):
    """
    Take a string that correspond to a <pre> block in html and parses it into lines.  
    Returns string corresponding to updated <pre> block with each line
    updated via process_line()
    """
    new_block=pre_block.split("\n")
    updated_block=""
    for line in new_block[:-1]:
        updated_block=updated_block+update_line(line)+"\n"
    updated_block=updated_block+update_line(new_block[-1]) #The last line does not need another "\n"
    return updated_block

# Some simple tests
print(update_pre_block(""))
print(update_pre_block("foobar()"))
print(update_pre_block("if foo():\n    bar()"))
print(update_pre_block("print\nprint 1+1\nprint 2, 3, 4"))
print(update_pre_block("    print a + b\n    print 23 * 34\n        print 1234"))

# Expected output
##
##foobar()
##if foo():
##    bar()
##print()
##print(1+1)
##print(2, 3, 4)
##    print(a + b)
##    print(23 * 34)
##        print(1234)

def update_file(input_file_name, output_file_name):
    """
    Open and read the file specified by the string input_file_name
    Proces the <pre> blocks in the loaded text to update print syntax)
    Write the update text to the file specified by the string output_file_name
    """
    #My debug code is at https://py3.codeskulptor.org/#user302_eZhmkVvJzm7W6OK_4.py  
    # open file and read text in file as a string
    opened_file=open(input_file_name,'rt')
    whole_file=opened_file.read()
    opened_file.close()
    updated_text=""
    # split text in <pre> blocks and update using update_pre_block()  
    content_split_PREFIX=whole_file.split(PREFIX)
    updated_text=updated_text+content_split_PREFIX[0]  #The content before PREFIX is unchangedly inserted into output file
    for content in content_split_PREFIX[1:]:
        updated_text+=PREFIX
        [pre_block,post_block]=content.split(POSTFIX,1) #Specify the maxsplit will only return maxsplit+1 elements. In this case, only first POSTFIX will be considered
        updated_text+=update_pre_block(pre_block)+POSTFIX+post_block

    # Write the answer in the specified output file
    new_file=open(output_file_name,"wt")
    new_file.write(updated_text)
    new_file.close()
# A couple of test files
update_file("table.html", "table_updated.html")
update_file("docs.html", "docs_updated.html")

# Import some code to check whether the computed files are correct
import examples3_file_diff as file_diff
file_diff.compare_files("table_updated.html", "table_updated_solution.html")
file_diff.compare_files("docs_updated.html", "docs_updated_solution.html")

# Expected output
##table_updated.html and table_updated_solution.html are the same
##docs_updated.html and docs_updated_solution.html are the same

