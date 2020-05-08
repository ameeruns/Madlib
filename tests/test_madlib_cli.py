from madlib_cli.madlib_cli import read_content_file, split_content,merge,close_content_file,write_content_file

def test_file_initial_read():
    actual = read_content_file('madlib_cli/assets/contents.txt')
    expected = "The {Adjective} is {Noun}"
    assert actual == expected

def test_split_content():
    actual = split_content('The {Adjective} is {Noun}')
    expected = ['Adjective', 'Noun'],"The {} is {}"
    assert actual == expected

def test_merge():
    actual = merge(['Sun', 'Bright'],'The {} is {}')
    expected = "The Sun is Bright"
    assert actual == expected

def test_write_content_file():
    actual = write_content_file('madlib_cli/assets/contents.txt','The Sun is Bright')
    expected = "The Sun is Bright"
    assert actual == expected

def test_file_initial_read_new():
    actual = read_content_file('madlib_cli/assets/contents_new.txt')
    expected = "A {Adjective} is {Noun}"
    assert actual == expected

def test_split_content_new():
    actual = split_content('A {Adjective} is {Noun}')
    expected = ['Adjective', 'Noun'],"A {} is {}"
    assert actual == expected

def test_merge_new():
    actual = merge(['Home', 'life'],'A {} is {}')
    expected = "A Home is life"
    assert actual == expected