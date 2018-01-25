people = {
    'man0':{
        'phone':'0000',
        'addr':'aaaa'
    },
    'man1':{
        'phone':'0000',
        'addr':'aaaa'
    },
    'man2':{
        'phone':'0000',
        'addr':'aaaa'
    }
}

labels = {
    'phone':'phone number',
    'addr':'address'
}

name = input('name:')
request = input('phone number(p) or address(a)?')

if  request == 'p':
    key = 'phone'
if request == 'a':
    key = 'addr'

if name in people:
    print("%s's %s is %s."%(name,labels[key],people[name][key]))