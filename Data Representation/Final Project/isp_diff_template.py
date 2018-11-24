"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.

The debug program is at https://py3.codeskulptor.org/#user302_0dQFBODul1naSRD.py
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    longer_line = line1
    shorter_line = line2
    if longer_line < shorter_line:
    #>、<、> = 、< =、比较的规则为：从第一个字符开始比较，排序在前边的字母为小，当一个字符串全部字符和另一个字符串的前部分字符相同时，长度长的字符串为大。
        longer_line = line2
        shorter_line = line1
    if longer_line == shorter_line:
        return IDENTICAL
    idx=0
    if len(shorter_line)==0:
        return idx
    for character in shorter_line:
        if character == longer_line[idx]:
            idx+=1
        else:
            return idx
    return idx


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    if ("\n" in line1) or ("\r" in line1) or ("\n" in line2) or ("\r" in line2):
        return ""
    longer_line = line1
    shorter_line = line2
    if longer_line < shorter_line:
        longer_line = line2
        shorter_line = line1
    if idx in range(0, len(shorter_line)+1):
        return line1+"\n"+ idx * "=" + "^\n"+ line2+"\n"
    else:
        return ""

def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    if lines1 == lines2:
        return (IDENTICAL, IDENTICAL)
    shorter_lines = lines1
    longer_lines = lines2
    if len(shorter_lines) > len(longer_lines):
        shorter_lines = lines2
        longer_lines = lines1
    i_line=0
    for line in shorter_lines:
        idx=singleline_diff(line, longer_lines[i_line])
        if  idx ==-1:
            i_line+=1
        else:
            return (i_line, idx)
    return (len(shorter_lines), 0)
    #When shorter_lines is the first part of longer_lines
    #then the i_line is the length of shorter_lines, and idx is 0
print(multiline_diff(['line1', 'line2'], ['line1', 'line2', 'line3']))

def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    openfile = open(filename,'rt')
#    lst=[]
    data=openfile.read()
    openfile.close()
    lst=data.splitlines()
#    for line in openfile:
#        new1_line = line.strip('\n')
#        new2_line = new1_line.strip('\r')
#        lst.append(new2_line)
#        new_line=line.strip('\n').strip('\r')
#        lst.append(new_line)
    return lst

def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    lines1 = get_file_lines(filename1)
    lines2 = get_file_lines(filename2)
    #Check whether either file is empty
    if len(lines1)==0 and len(lines2)==0:
        return "No differences\n"
    if len(lines1)==0 :
        return 'Line 0:\n'+ '{0}\n{1}\n{2}\n'.format('','^',lines2[0])
    if len(lines2)==0 :
        return 'Line 0:\n'+ '{0}\n{1}\n{2}\n'.format(lines1[0],'^','')
    (i_item, idx) = multiline_diff(lines1, lines2)
    if (i_item, idx) == (IDENTICAL, IDENTICAL):
        return "No differences\n"
    else:
        real_result = singleline_diff_format(lines1[i_item], lines2[i_item], idx)
        line2_2_4= real_result.split("\n")
        result= 'Line '+str(i_item)+':\n'+line2_2_4[0]+'\n'+line2_2_4[1]+'\n'+line2_2_4[2]+'\n'
        return result
