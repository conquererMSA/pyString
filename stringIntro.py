'''
String: a string is a sequence of unicode charecter.
a=>unicode value assign in computer memmory=> integer value for
unicode=> computer understood binary.
a=>unicode=>integer=>binary
ord('char') method char er unicode return kore.
chr(integer) method unicode value niye charecter return kore

'''
info="MSA is will be a conquerer"
details="""
MSA is a software engineer. He got HSC certificate from GSC.
He currently studied on NSTU.
"""
# print(details)
valueInt=ord('A') # 65 is a unicode value for capital A, 97 for
# small a
valueChar=chr(97) # a, chr method unicode niye char return kore
print(valueChar)
