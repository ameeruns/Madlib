def read_content_file(inputfile):
    content_file= open(inputfile,'r')
    content_data = content_file.read()
    return content_data

def close_content_file(content_file):
    content_file.close()
    status = content_file.closed
    return status

def write_content_file(inputfile,content_data):
    print(inputfile,content_data)
    content_file= open(inputfile,'w+')
    content_file.write(content_data)
    content_file.close()
    content_file_write = open(inputfile,'r')
    content_file_write_data = content_file_write.read()
  #  print(content_file_write_data)
  #  print(content_file_write_data.strip())
    #status = content_file.closed
    return content_file_write_data
 
def split_content(content_data):
    line = content_data.split('{') 
    length = len(line)
    input_list =[]
    for i in range(length):
        istr = line[i] #.split('}')
        if "}" in istr:
            istr = line[i].split('}')
            input_list.append(istr[0])
            content_data = content_data.replace(istr[0],'')
    print(input_list)     
    print(content_data)          
    return input_list,content_data
     
      
def merge(input_list,content_data):
    content_data = content_data.format(*input_list)
    return content_data 

content_data = read_content_file('madlib_cli/assets/contents.txt')
print(content_data)
input_list,content_data = split_content(content_data)
print(input_list)     
print(content_data) 
content_data = merge(input_list,content_data)
print(content_data) 