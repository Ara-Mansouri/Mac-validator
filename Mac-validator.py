import re
regex="([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})|(([0-9A-Fa-f]{4}\.){2}[0-9A-Fa-f]{4})"
def mac(Add):
    if(re.search(regex,Add)):
        print("Mac Address is valid!")
    else:
        print("Mac Address is not valid!")   

if __name__=='__main__':
    Add="2647:56ac::24ad"
    mac(Add)
    Add="06-27-47-67-96-ac"
    mac(Add)
    Add="00:01:23:24:25:A5"
    mac(Add)