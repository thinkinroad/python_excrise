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

person = people.get(name,{})
label = labels.get(key,key)
result = person.get(key,'not available')

print("%s's %s is %s."%(name,label,result))